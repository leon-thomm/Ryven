import os

from PySide2.QtWidgets import QLineEdit

from NIENV import *
from NIWENV import *
from ..ryvencore.src.NodePort import NodeInput, NodeOutput


class Result_Node_MainWidget(MWB, QLineEdit):
    def __init__(self, params):
        MWB.__init__(self, params)
        QLineEdit.__init__(self)

        self.setStyleSheet('''
            QLineEdit{
                border-radius: 10px;
                background-color: transparent;
                border: 1px solid #404040;
                color: #aaaaaa;
                padding: 3px;
            }
        ''')

        self.setReadOnly(True)
        self.setFixedWidth(120)


    def show_val(self, new_val):
        self.setText(str(new_val))
        self.setCursorPosition(0)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass


class Result_Node(Node):

    title = 'result'
    description = 'displays a value converted to string'
    init_inputs = [
        NodeInput(type_='data')
    ]
    main_widget_class = Result_Node_MainWidget
    main_widget_pos = 'between ports'
    style = 'extended'
    color = '#c69a15'

    def __init__(self, params):
        super(Result_Node, self).__init__(params)

    def update_event(self, input_called=-1):
        self.main_widget().show_val(self.input(0))

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass
