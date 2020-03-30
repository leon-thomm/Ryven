from PySide2.QtWidgets import QLineEdit
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

import os


class %NODE_TITLE%_NodeInstance_MainWidget(QLineEdit):
    def __init__(self, parent_node_instance):
        super(%NODE_TITLE%_NodeInstance_MainWidget, self).__init__()

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



    # optional - important for threading - stop everything here
    def removing(self):
        pass
