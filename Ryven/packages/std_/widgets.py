from NWENV import *
from PySide2.QtWidgets import QPushButton


class ButtonNode_MainWidget(QPushButton, MWB):

    def __init__(self, params):
        MWB.__init__(self, params)
        QPushButton.__init__(self)

        self.clicked.connect(self.update_node)


export_widgets(
    ButtonNode_MainWidget,
)
