# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

from PySide2.QtWidgets import QPushButton


class Button_NodeInstance_MainWidget(QPushButton):
    def __init__(self, parent_node_instance):
        super(Button_NodeInstance_MainWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------
        self.setStyleSheet('''
            background-color: #36383B;
            padding-top: 5px;
            padding-bottom: 5px;
            padding-left: 22px;
            padding-right: 22px;
            border: 1px solid #666666;
            border-radius: 5px;
        ''')

    def get_data(self):
        return {}

    def set_data(self, data):
        pass



    # optional - important for threading - stop everything here
    def removing(self):
        pass
