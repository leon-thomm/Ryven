from PySide2.QtWidgets import QLineEdit
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

import os

from custom_src.Node import Node, NodePort


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


class Result_Node(Node):
    def __init__(self):
        super(Result_Node, self).__init__()


        self.title = 'result'
        self.type_ = 'result'
        self.description = 'displays any value'
        self.package = 'built in'
        self.has_main_widget = True
        self.main_widget_class = Result_NodeInstance_MainWidget
        self.main_widget_pos = 'between ports'
        self.design_style = 'extended'

        data_input_port = NodePort()
        data_input_port.type_ = 'data'
        data_input_port.label = ''
        data_input_port.widget_name = None
        self.inputs.append(data_input_port)