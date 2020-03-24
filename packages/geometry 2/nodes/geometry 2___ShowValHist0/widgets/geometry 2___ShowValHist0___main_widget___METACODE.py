# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

from PySide2.QtWidgets import QLineEdit


class %NODE_TITLE%_NodeInstance_MainWidget(QLineEdit):
    def __init__(self, parent_node_instance):
        super(%NODE_TITLE%_NodeInstance_MainWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        # ...

    def deleted(self):
        pass

    def get_data(self):
        return self.text()

    def set_data(self, data):
        self.setText(data)
