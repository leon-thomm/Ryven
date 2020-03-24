from PySide2.QtWidgets import QLabel, QVBoxLayout, QPushButton
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap

from PySide2.QtWidgets import QWidget
import os


class Perceptron_NodeInstance_MainWidget(QWidget):
    def __init__(self, parent_node_instance):
        super(Perceptron_NodeInstance_MainWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        self.custom_content_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../custom content')
        # ------------------------------------------------

        self.label = QLabel()
        pix = QPixmap(self.custom_content_path+'/perceptron.png')
        self.label.setPixmap(pix.scaled(100, 60, Qt.KeepAspectRatio))
        print(self.custom_content_path)
        print(self.custom_content_path+'/perceptron.png')
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.label)
        self.setStyleSheet('background: transparent;')
        self.setFixedSize(300, 300)

    def deleted(self):
        pass

    def get_data(self):
        return {}

    def set_data(self, data):
        pass
