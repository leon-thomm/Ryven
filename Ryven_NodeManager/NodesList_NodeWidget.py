from PySide2.QtWidgets import QWidget, QHBoxLayout, QMenu, QAction, QLineEdit
from PySide2.QtCore import Signal, Qt, QEvent


class NodesList_NodeWidget(QWidget):

    mouse_pressed = Signal()
    del_node_triggered = Signal()

    def __init__(self, node):
        super(NodesList_NodeWidget, self).__init__()

        self.node = node

        # UI
        layout = QHBoxLayout()

        self.name_line_edit = QLineEdit(node.title)
        self.name_line_edit.setEnabled(False)

        layout.addWidget(self.name_line_edit)

        self.setLayout(layout)

    def set_name(self, name):
        self.name_line_edit.setText(name)

    def set_selected(self, selected):
        if selected:
            self.name_line_edit.setStyleSheet('background: rgba(84, 169, 222, 200);')
        else:
            self.name_line_edit.setStyleSheet('')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed.emit()
        return


    def event(self, event):
        if event.type() == QEvent.ToolTip:
            self.setToolTip(self.node.content_widget.get_node_description())

        return QWidget.event(self, event)


    def contextMenuEvent(self, event):
        menu: QMenu = QMenu(self)

        delete_action = QAction('delete')
        delete_action.triggered.connect(self.action_delete_triggered)

        actions = [delete_action]
        for a in actions:
            menu.addAction(a)

        menu.exec_(event.globalPos())


    def action_delete_triggered(self):
        self.del_node_triggered.emit()