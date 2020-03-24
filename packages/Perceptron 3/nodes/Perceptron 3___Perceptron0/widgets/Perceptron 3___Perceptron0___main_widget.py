from PySide2.QtWidgets import QLabel, QVBoxLayout, QPushButton
# from PySide2.QtCore import ...
from PySide2.QtGui import QPixmap

from PySide2.QtWidgets import QWidget


class Perceptron_NodeInstance_MainWidget(QWidget):
    def __init__(self, parent_node_instance):
        super(Perceptron_NodeInstance_MainWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        self.label = QLabel('asdf')
        self.label.setPixmap(QPixmap('../../perceptron.png'))
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.label)
        self.layout().addWidget(QPushButton())
        self.resize(300, 300)

    def deleted(self):
        pass

    def get_data(self):
        return {}

    def set_data(self, data):
        pass
