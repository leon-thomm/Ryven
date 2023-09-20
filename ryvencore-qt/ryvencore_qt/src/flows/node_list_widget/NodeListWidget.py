from qtpy.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QScrollArea
from qtpy.QtCore import Qt, Signal

from ryvencore import Node
from .utils import search, sort_nodes, inc, dec
from ..node_list_widget.NodeWidget import NodeWidget

from statistics import median


class NodeListWidget(QWidget):

    # SIGNALS
    escaped = Signal()
    node_chosen = Signal(object)

    def __init__(self, session):
        super().__init__()

        self.session = session
        self.nodes: list[type[Node]] = []

        self.current_nodes = []             # currently selectable nodes
        self.active_node_widget_index = -1  # index of focused node widget
        self.active_node_widget = None      # focused node widget
        self.node_widgets = {}              # Node-NodeWidget assignments
        self._node_widget_index_counter = 0

        self._setup_UI()


    def _setup_UI(self):

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.main_layout)

        # adding all stuff to the layout
        self.search_line_edit = QLineEdit(self)
        self.search_line_edit.setPlaceholderText('search for node...')
        self.search_line_edit.textChanged.connect(self._update_view)
        self.layout().addWidget(self.search_line_edit)


        self.list_scroll_area = QScrollArea(self)
        self.list_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list_scroll_area.setWidgetResizable(True)
        self.list_scroll_area.setContentsMargins(0, 0, 0, 0)

        self.list_scroll_area_widget = QWidget()
        self.list_scroll_area_widget.setContentsMargins(0, 0, 0, 0)
        self.list_scroll_area.setWidget(self.list_scroll_area_widget)

        self.list_layout = QVBoxLayout()
        self.list_layout.setContentsMargins(0, 0, 0, 0)
        self.list_layout.setAlignment(Qt.AlignTop)
        self.list_scroll_area_widget.setLayout(self.list_layout)

        self.layout().addWidget(self.list_scroll_area)

        self._update_view('')

        self.setStyleSheet(self.session.design.node_selection_stylesheet)

        self.search_line_edit.setFocus()


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
            self._set_active_node_widget_index(
                inc(self.active_node_widget_index, length=num_items)
            )
        elif event.key() == Qt.Key_Up:
            self._set_active_node_widget_index(
                dec(self.active_node_widget_index, num_items)
            )

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
        if len(self.nodes) == 0:
            return

        search_text = search_text.lower()

        # remove all node widgets

        for i in reversed(range(self.list_layout.count())):
            self.list_layout.itemAt(i).widget().setParent(None)

        self.current_nodes.clear()

        self._node_widget_index_counter = 0

        # search
        sorted_distances = search(
            items={
                n: [n.title.lower()] + n.tags
                for n in self.nodes
            },
            text=search_text
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
        index = int(self.sender().objectName()[self.sender().objectName().rindex('_')+1:])
        self._place_node(index)


    def _place_node(self, index):
        node_index = index
        node = self.current_nodes[node_index]
        self.node_chosen.emit(node)
        self.escaped.emit()
