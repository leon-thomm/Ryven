from PySide2.QtWidgets import QLineEdit

from NENV import *
from NWENV import *


class Result_Node_MainWidget(MWB, QLineEdit):
    def __init__(self, params):
        MWB.__init__(self, params)
        QLineEdit.__init__(self)

        self.setReadOnly(True)
        self.setFixedWidth(120)


    def show_val(self, new_val):
        self.setText(str(new_val))
        self.setCursorPosition(0)


class Result_Node(Node):

    title = 'result'
    description = 'displays a value converted to string'
    init_inputs = [
        NodeInputBP(type_='data')
    ]
    main_widget_class = Result_Node_MainWidget
    main_widget_pos = 'between ports'
    style = 'extended'
    color = '#c69a15'

    def __init__(self, params):
        super(Result_Node, self).__init__(params)

    def place_event(self):
        if self.session.gui:
            self.main_widget().show_val(self.input(0))

    def update_event(self, input_called=-1):
        if self.session.gui:
            self.main_widget().show_val(self.input(0))
