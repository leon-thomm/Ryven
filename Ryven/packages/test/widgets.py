from NWENV import *
from PySide2.QtWidgets import QPushButton


class ButtonWidget(MWB, QPushButton):
    def __init__(self, params):
        MWB.__init__(self, params)
        QPushButton.__init__(self)

        self.setText('fancy button!')
        self.clicked.connect(self._clicked)
    
    def _clicked(self):
        print('clicked!')
