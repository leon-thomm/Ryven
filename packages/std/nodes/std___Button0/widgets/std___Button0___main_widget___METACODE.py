from NIWENV import *

# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

from PySide2.QtWidgets import QPushButton


class %CLASS%(QPushButton, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QPushButton.__init__(self)

        
        self.setStyleSheet('''
        QPushButton {
            background-color: #36383B;
            padding-top: 5px;
            padding-bottom: 5px;
            padding-left: 22px;
            padding-right: 22px;
            border: 1px solid #666666;
            border-radius: 5px;
        }
        QPushButton:pressed {
            background-color: #bcbbf2;
        }
        ''')
        self.clicked.connect(M(self.parent_node_instance.button_clicked))

    def get_data(self):
        return {}

    def set_data(self, data):
        pass


    def remove_event(self):
        pass
