# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

from PySide2.QtWidgets import QLineEdit


class ShowValHist_NodeInstance_MainWidget(QLineEdit):
    def __init__(self, parent_node_instance):
        super(ShowValHist_NodeInstance_MainWidget, self).__init__()

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
