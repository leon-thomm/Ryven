from NIWENV import *

# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

from PySide2.QtWidgets import QLabel


class %CLASS%(QLabel, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QLabel.__init__(self)

        self.img_filepath = ''
        self.resize(140, 15)

        self.setStyleSheet('''
            color: #bbbbbb;
            background: transparent;
            border: none;
        ''')

    def set_path_text(self, path):
        self.img_filepath = path
        path_short = path if len(path) < 15 else '...' + path[-15:]
        self.setText('path: ' + path_short)

    def get_data(self):
        return {'image file path': self.img_filepath}

    def set_data(self, data):
        self.img_filepath = data['image file path']


    def remove_event(self):
        pass
