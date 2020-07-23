from custom_src.retain import M

from PySide2.QtWidgets import QLineEdit
# from PySide2.QtCore import ...
from PySide2.QtGui import QFont


class %INPUT_WIDGET_TITLE%_PortInstanceWidget(QLineEdit):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(%INPUT_WIDGET_TITLE%_PortInstanceWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
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

        self.setFont(QFont('Corbel', 10))
        self.setEchoMode(QLineEdit.Password)

        # print('self.height():', self.height())
        # self.resize(100, self.height())
        # print('self.height():', self.height())


    def get_val(self):
        return self.text()


    def get_data(self):
        data = {'text': self.text()}
        return data

    def set_data(self, data):
        self.setText(data['text'])

    def remove_event(self):
        pass # remove log here etc. ...
