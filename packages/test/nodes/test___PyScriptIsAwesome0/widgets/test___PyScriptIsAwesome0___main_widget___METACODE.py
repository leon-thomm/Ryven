from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

import os


class %NODE_TITLE%_NodeInstance_MainWidget(...):
    def __init__(self, parent_node_instance):
        super(%NODE_TITLE%_NodeInstance_MainWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        self.package_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../')
        # ------------------------------------------------

        self.setStyleSheet('''

        ''')

        # ...


    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass



    # optional - important for threading - stop everything here
    def removing(self):
        pass
