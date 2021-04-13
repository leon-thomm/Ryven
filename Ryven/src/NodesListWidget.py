from PySide2.QtCore import QMimeData, QByteArray, Qt, QPoint
from PySide2.QtGui import QStandardItemModel, QStandardItem, QDrag
from PySide2.QtWidgets import QWidget, QTreeView, QVBoxLayout, QMenu, QAction


class NodesView(QTreeView):
    pass


class NodeItem(QStandardItem):
    def __init__(self, node):
        super().__init__(node.title)
        self.node = node

        self.setEditable(False)
        self.setDragEnabled(True)


class NodesListWidget(QWidget):
    def __init__(self, main_window, session):
        super().__init__()
        self.main_window = main_window
        self.session = session

        self.view = NodesView()
        self.model = QStandardItemModel()
        self.view.setModel(self.model)
        self.view.setHeaderHidden(True)
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.view.customContextMenuRequested.connect(self.on_context_menu_requested)
        self.custom_node_items = []

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.view)

    def update_list(self):
        self.model.clear()

        packages = {}  # {str: [Node]}
        for node, package_name in self.main_window.node_packages.items():
            if package_name in packages.keys():
                packages[package_name].append(node)
            else:
                packages[package_name] = [node]

        for package_name, nodes in packages.items():
            package_item = QStandardItem(package_name)
            package_item.setEditable(False)
            for n in nodes:
                node_item = NodeItem(n)
                # node_item.setEditable(False)
                # node_item.setDragEnabled(True)
                package_item.appendRow(node_item)
            self.model.appendRow(package_item)

        # custom nodes

        custom_nodes_item = QStandardItem('CUSTOM')
        for c_n in self.custom_node_items:
            custom_nodes_item.appendRow(c_n)
        self.model.appendRow(custom_nodes_item)

    def on_context_menu_requested(self, p: QPoint):
        menu = QMenu()

        index = self.view.indexAt(p)
        if index.isValid():
            w = self.model.itemFromIndex(index)
            if w.text() == 'CUSTOM':
                a = QAction('add new', self)
                a.triggered.connect(self.add_custom_node)
                menu.addAction(a)
        menu.exec_(self.view.viewport().mapToGlobal(p))
        # return menu

    def add_custom_node(self):
        print('adding custom node!')
