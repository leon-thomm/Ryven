# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

from PySide2.QtWidgets import QLabel


class %NODE_TITLE%_NodeInstance_MainWidget(QLabel):
    def __init__(self, parent_node_instance):
        super(%NODE_TITLE%_NodeInstance_MainWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------
        self.img_filepath = ''
        self.resize(140, 15)

        self.setStyleSheet('''
            color: #bbbbbb;
            background: transparent;
            border: none;
        ''')

    def set_path_text(self, path):
        self.img_filepath = path
        path_short = path if len(path) < 15 else '...' + path[-15:]
        self.setText('path: ' + path_short)

    def get_data(self):
        return {'image file path': self.img_filepath}

    def set_data(self, data):
        self.img_filepath = data['image file path']



    # optional - important for threading - stop everything here
    def removing(self):
        pass
