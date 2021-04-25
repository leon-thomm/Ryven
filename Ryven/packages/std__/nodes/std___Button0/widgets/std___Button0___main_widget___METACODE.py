from NWENV import *

# from qtpy.QtWidgets import ...
# from qtpy.QtCore import ...
# from qtpy.QtGui import ...

from qtpy.QtWidgets import QPushButton


class %CLASS%(QPushButton, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QPushButton.__init__(self)

        
        # self.setStyleSheet('''
        # QPushButton {
        #     background-color: #36383B;
        #     padding-top: 5px;
        #     padding-bottom: 5px;
        #     padding-left: 22px;
        #     padding-right: 22px;
        #     border: 1px solid #666666;
        #     border-radius: 5px;
        # }
        # QPushButton:pressed {
        #     background-color: #bcbbf2;
        # }
        # ''')
        self.clicked.connect(self.parent_node_instance.button_clicked)

    def get_state(self):
        return {}

    def set_state(self, data):
        pass


    def remove_event(self):
        pass
