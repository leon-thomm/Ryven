import os

from PySide2.QtWidgets import QLineEdit

from NIENV import *


class Result_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(Result_NodeInstance, self).__init__(params)

    def update_event(self, input_called=-1):
        self.main_widget.show_val(self.input(0))

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass


class Result_NodeInstance_MainWidget(QLineEdit):
    def __init__(self, parent_node_instance):
        super(Result_NodeInstance_MainWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        self.package_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../')
        # ------------------------------------------------

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