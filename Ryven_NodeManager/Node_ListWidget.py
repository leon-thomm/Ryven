from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel
from PySide2.QtCore import Signal

from Node import Node


class Node_ListWidget(QWidget):

    double_clicked = Signal(Node)

    def __init__(self, node):
        super(Node_ListWidget, self).__init__()
        self.setLayout(QHBoxLayout(self))
        self.label = QLabel(self)
        self.layout().addWidget(self.label)
        self.setFixedHeight(50)
        self.setStyleSheet('''
        border: 3px solid #303030;
        ''')

        self.node = node
        self.display_title = ''

        self.update_display_title()



    def mouseDoubleClickEvent(self, event):
        self.double_clicked.emit(self.node)



    def update_display_title(self):
        self.display_title = self.node.title
        self.label.setText(self.display_title)