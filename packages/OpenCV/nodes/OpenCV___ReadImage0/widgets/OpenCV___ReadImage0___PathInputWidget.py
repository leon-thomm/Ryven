from NIWENV import *

from PySide2.QtWidgets import QPushButton, QFileDialog
from PySide2.QtCore import QObject, Signal
# from PySide2.QtGui import ...
import os

class PathInputWidget_PortInstanceWidget(QPushButton, IWB):

    path_chosen = Signal(str)

    def __init__(self, params):
        IWB.__init__(self, params)
        QPushButton.__init__(self, "Select")
        self.setStyleSheet('''
            color: #cccccc;
            border-radius: 5px;
            border: 1px solid #aaaaaa;
            padding-top: 3px;
            padding-bottom: 3px;
            padding-left: 25px;
            padding-right: 25px;
            background: transparent;
        ''')

        self.clicked.connect(M(self.button_clicked))

    def button_clicked(self):
        file_path = QFileDialog.getOpenFileName(self, 'Select image')[0]
        try:
            file_path = os.path.relpath(file_path)
        except ValueError:
            pass  # keep absolute path
        # self.node.path_chosen(file_path)
        self.path_chosen.emit(file_path)

    def get_data(self):
        return self.text()

    def set_data(self, data):
        self.setText(data)

    def remove_event(self):
        pass
