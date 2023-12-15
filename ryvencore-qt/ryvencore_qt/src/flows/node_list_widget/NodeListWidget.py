from qtpy.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QScrollArea,
    QTreeView,
    QSplitter,
    QAbstractItemView,
    QListView,
    QLabel,
)

from qtpy.QtCore import Qt, Signal, QModelIndex, QSortFilterProxyModel
from qtpy.QtGui import QStandardItemModel, QStandardItem, QFont

from ryvencore import Node
from .utils import search, sort_nodes, inc, dec
from ..node_list_widget.NodeWidget import NodeWidget
from statistics import median
from re import escape
from typing import Dict, Type, List

# from ryven import NodesPackage

class NodeStandardItemModel(QStandardItemModel):
    
    def mimeData(self, indexes):
        item = self.itemFromIndex(indexes[0])
        return item.mimeData()
    
class NodeStandardItem(QStandardItem):
    """A node item for use in a model. Helpful when creating a tree view"""
    def __init__(self, node, text = None):
        super().__init__(text)
        self.setDragEnabled(True)
        self.setFont(text_font())
        self.node = node
    
    def mimeData(self):
        return NodeWidget._create_mime_data(self.node) 
    
class NodeListWidget(QWidget):
    # SIGNALS
    escaped = Signal()
    node_chosen = Signal(object)

    def __init__(self, session, show_packages: bool = False):
        super().__init__()

        self.session = session
        self.nodes: List[Type[Node]] = []
        self.package_nodes: List[Type[Node]] = []

        self.current_nodes: List[Node] = []  # currently selectable nodes
        self.active_node_widget_index = -1  # index of focused node widget
        self.active_node_widget = None  # focused node widget
        self.node_widgets: Dict[Node, NodeWidget] = {}  # Node-NodeWidget assignments
        self._node_widget_index_counter = 0

        # holds the path to the tree item
        self.path_to_item: dict = {}
        self.tree_items: List[QStandardItem] = []
        self.show_packages: bool = show_packages
        self._setup_UI()

    def _setup_UI(self) -> None:
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.main_layout)

        # splitter between packages and nodes
        splitter = QSplitter(Qt.Vertical)
        self.layout().addWidget(splitter)

        # search for the tree
        self.search_line_tree = QLineEdit(self)
        self.search_line_tree.setPlaceholderText('search packages...')
        self.search_line_tree.textChanged.connect(self.search_pkg_tree)

        # tree view
        self.pack_proxy_model: QSortFilterProxyModel = QSortFilterProxyModel()
        self.pack_proxy_model.setRecursiveFilteringEnabled(True)
        # we need qt6 for not filtering out the children if they would be filtered
        # out otherwise
        self.pack_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pack_tree = QTreeView()
        self.pack_tree.setModel(self.pack_proxy_model)
        self.pack_tree.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.pack_tree.setDragEnabled(True)

        def on_select(index: QModelIndex):
            source_index = index.model().mapToSource(index)
            item: QStandardItem = index.model().sourceModel().itemFromIndex(source_index)
            func = item.data(Qt.UserRole + 1)
            if func != None:
                func()

        # pkg widget
        self.pkg_widget = QWidget()
        self.pkg_widget.setLayout(QVBoxLayout())
        self.pkg_widget.layout().addWidget(self.search_line_tree)
        self.pkg_widget.layout().addWidget(self.pack_tree)

        self.pack_tree.clicked.connect(on_select)

        if self.show_packages:
            splitter.addWidget(self.pkg_widget)
        
        splitter.setSizes([30])
        
        # nodes widget
        nodes_widget = QWidget()
        nodes_widget.setLayout(QVBoxLayout())
        splitter.addWidget(nodes_widget)

        # adding all stuff to the layout
        self.search_line_edit = QLineEdit(self)
        self.search_line_edit.setPlaceholderText('search for node...')
        self.search_line_edit.textChanged.connect(self._update_view)
        nodes_widget.layout().addWidget(self.search_line_edit)
        
        self.current_pack_label = QLabel('Package: None')
        self.current_pack_label.setFont(text_font())
        nodes_widget.layout().addWidget(self.current_pack_label)
        
        self.list_scroll_area = QScrollArea(self)
        self.list_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list_scroll_area.setWidgetResizable(True)
        self.list_scroll_area.setContentsMargins(0, 0, 0, 0)

        self.list_scroll_area_widget = QWidget()
        self.list_scroll_area_widget.setContentsMargins(15, 10, 15, 10)
        self.list_scroll_area.setWidget(self.list_scroll_area_widget)

        self.list_layout = QVBoxLayout()
        self.list_layout.setContentsMargins(0, 0, 0, 0)
        self.list_layout.setAlignment(Qt.AlignTop)
        self.list_scroll_area_widget.setLayout(self.list_layout)

        nodes_widget.layout().addWidget(self.list_scroll_area)

        self._update_view('')

        self.setStyleSheet(self.session.design.node_selection_stylesheet)

        self.search_line_edit.setFocus()

    def search_pkg_tree(self, search: str):
        if search and search != '':
            # removes whitespace and escapes all special regex chars
            new_search = escape(search.strip())
            # regex that enforces the text starts with <new_search>
            self.pack_proxy_model.setFilterRegularExpression(f'^{new_search}')
            self.pack_tree.expandAll()
        else:
            self.pack_proxy_model.setFilterRegularExpression('')
            self.pack_tree.collapseAll()

    def make_nodes_current(self, pack_nodes, pkg_name: str):
        def select_nodes():
            if not pack_nodes or self.package_nodes == pack_nodes:
                return
            self.package_nodes = pack_nodes
            self.current_pack_label.setText(f'Package: {pkg_name}')
            self._update_view()

        return select_nodes

    def make_pack_hier(self) -> None:
        """
        Creates a hierarchical view of the packages based on the nodes' identifier.
        """

        self.tree_items.clear()

        model = NodeStandardItemModel()
        model.setHorizontalHeaderLabels(["Packages"])
        root_item = model.invisibleRootItem()

        # should be dict[str, QStandardItem | (QStandardItem, list)] in 3.9+
        h_dict: dict = {"root_item": root_item}
        font = text_font()
        # A completely nestable tree-view
        for n in self.nodes:
            full_name = n.identifier
            comps = full_name.rsplit('.', 1)
            path = comps[0]
            # node_name = comps[1]

            # if the path isn't found, create all the nested items that are needed
            if not path in h_dict:
                split_path = path.split('.')
                current_path = split_path[0]
                current_root = root_item
                split_path_len = len(split_path)
                for i, s in enumerate(split_path):
                    if not current_path in h_dict:
                        item = QStandardItem(s)
                        item.setFont(font)
                        item.setDragEnabled(False)
                        self.tree_items.append(item)
                        item.setEditable(False)
                        node_list: List[Type[Node]] = []
                        h_dict[current_path] = (item, node_list)
                        item.setData(self.make_nodes_current(node_list, current_path), Qt.UserRole + 1)
                        current_root.appendRow(item)
                    current_root = h_dict[current_path][0]
                    if i != split_path_len - 1:
                        current_path = current_path + f'.{split_path[i+1]}'

            item, pack_nodes = h_dict[path]

            node_item = NodeStandardItem(n, n.title)

            node_item.setEditable(False)
            item.appendRow(node_item)
            pack_nodes.append(n)
            self.tree_items.append(node_item)
        
        self.pack_proxy_model.setSourceModel(model)

    def mousePressEvent(self, event):
        # need to accept the event, so the scene doesn't process it further
        QWidget.mousePressEvent(self, event)
        event.accept()

    def keyPressEvent(self, event):
        """key controls"""

        num_items = len(self.current_nodes)

        if event.key() == Qt.Key_Escape:
            self.escaped.emit()

        elif event.key() == Qt.Key_Down:
            self._set_active_node_widget_index(inc(self.active_node_widget_index, length=num_items))
        elif event.key() == Qt.Key_Up:
            self._set_active_node_widget_index(dec(self.active_node_widget_index, num_items))

        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if len(self.current_nodes) > 0:
                self._place_node(self.active_node_widget_index)
        else:
            event.setAccepted(False)

    def wheelEvent(self, event):
        # need to accept the event, so the scene doesn't process it further
        QWidget.wheelEvent(self, event)
        event.accept()

    def refocus(self):
        """focuses the search line edit and selects the text"""
        self.search_line_edit.setFocus()
        self.search_line_edit.selectAll()

    def update_list(self, nodes):
        """update the list of available nodes"""
        self.nodes = sort_nodes(nodes)
        self._update_view('')

    def _update_view(self, search_text=''):
        nodes = self.nodes if search_text is not None and search_text != '' else self.package_nodes

        if nodes == None or len(nodes) == 0:
            nodes = self.nodes

        if len(nodes) == 0:
            return

        search_text = search_text.lower()

        # remove all node widgets

        for i in reversed(range(self.list_layout.count())):
            self.list_layout.itemAt(i).widget().setParent(None)

        self.current_nodes.clear()

        self._node_widget_index_counter = 0

        # search
        sorted_distances = search(
            items={n: [n.title.lower()] + n.tags for n in nodes}, text=search_text
        )

        # create node widgets
        cutoff = median(sorted_distances.values())
        for n, dist in sorted_distances.items():
            if search_text != '' and dist > cutoff:
                continue

            self.current_nodes.append(n)

            if self.node_widgets.get(n) is None:
                self.node_widgets[n] = self._create_node_widget(n)

            self.list_layout.addWidget(self.node_widgets[n])

        # focus on first result
        if len(self.current_nodes) > 0:
            self._set_active_node_widget_index(0)

    def _create_node_widget(self, node):
        node_widget = NodeWidget(self, node)
        node_widget.custom_focused_from_inside.connect(self._node_widget_focused_from_inside)
        node_widget.setObjectName('node_widget_' + str(self._node_widget_index_counter))
        self._node_widget_index_counter += 1
        node_widget.chosen.connect(self._node_widget_chosen)

        return node_widget

    def _node_widget_focused_from_inside(self):
        index = self.list_layout.indexOf(self.sender())
        self._set_active_node_widget_index(index)

    def _set_active_node_widget_index(self, index):
        self.active_node_widget_index = index
        node_widget = self.list_layout.itemAt(index).widget()

        if self.active_node_widget:
            self.active_node_widget.set_custom_focus(False)

        node_widget.set_custom_focus(True)
        self.active_node_widget = node_widget
        self.list_scroll_area.ensureWidgetVisible(self.active_node_widget)

    def _node_widget_chosen(self):
        index = int(self.sender().objectName()[self.sender().objectName().rindex('_') + 1 :])
        self._place_node(index)

    def _place_node(self, index):
        node_index = index
        node = self.current_nodes[node_index]
        self.node_chosen.emit(node)
        self.escaped.emit()

def text_font():
    return QFont('Source Code Pro', 9)