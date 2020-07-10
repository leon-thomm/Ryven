from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QMessageBox, QVBoxLayout

from NodesList_NodeWidget import NodesList_NodeWidget


class NodesListWidget(QWidget):
    def __init__(self, main_window):
        super(NodesListWidget, self).__init__()

        self.main_window = main_window
        self.widgets = []
        self.selected_widget_index = None

        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.main_layout)


    def add_node(self, node):
        w = NodesList_NodeWidget(node)
        self.main_layout.addWidget(w)
        w.del_node_triggered.connect(self.del_node)
        w.mouse_pressed.connect(self.widget_clicked)
        self.widgets.append(w)

    def set_current_index(self, index):
        if index == -1:
            index = len(self.widgets)-1
        if self.selected_widget_index is not None and self.selected_widget_index < len(self.widgets):
            self.widgets[self.selected_widget_index].set_selected(False)
        self.selected_widget_index = index
        self.widgets[index].set_selected(True)

    def node_renamed(self, index, name):
        w = self.widgets[index]
        w.set_name(name)

    def widget_clicked(self):
        index = self.widgets.index(self.sender())
        self.main_window.set_current_node(index=index)

    def del_node(self):
        msg_box = QMessageBox(QMessageBox.Warning, 'Deleting node',
                              'You are about to delete a node. All content will be lost. '
                              'Do you want to continue?', QMessageBox.Cancel | QMessageBox.Yes, self)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        ret = msg_box.exec_()
        if ret != QMessageBox.Yes:
            return

        w = self.sender()
        index = self.widgets.index(w)

        self.widgets.remove(w)
        w.setParent(None)
        self.main_window.delete_node(index)

    def clear_list(self):
        for w in self.widgets:
            w.setParent(None)
        self.widgets.clear()