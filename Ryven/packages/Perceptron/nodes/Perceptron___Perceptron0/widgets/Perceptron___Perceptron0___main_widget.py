from NIWEVN import *
package_path = widget_pp(__file__)

from PySide2.QtWidgets import QLabel, QVBoxLayout, QPushButton
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap

from PySide2.QtWidgets import QWidget

class Perceptron_Node_MainWidget(QWidget, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QWidget.__init__()

        

        self.label = QLabel()
        pix = QPixmap(package_path+'perceptron.png')
        self.label.setPixmap(pix.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.label)
        self.setStyleSheet('background: transparent;')


    def get_state(self):
        data = {}
        # ...
        return data

    def set_state(self, data):
        pass


    def remove_event(self):
        pass
