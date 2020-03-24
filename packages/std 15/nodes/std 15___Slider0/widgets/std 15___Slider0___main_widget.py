# from PySide2.QtWidgets import ...
from PySide2.QtCore import Qt
# from PySide2.QtGui import ...

from PySide2.QtWidgets import QSlider


class Slider_NodeInstance_MainWidget(QSlider):
    def __init__(self, parent_node_instance):
        super(Slider_NodeInstance_MainWidget, self).__init__(Qt.Horizontal)

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------
        self.setStyleSheet('''
            background: transparent;
        ''')

        self.valueChanged.connect(self.val_changed)
        self.setMinimum(0)
        self.setMaximum(100)

    def val_changed(self):
        self.parent_node_instance.update()

    def get_val(self):
        return self.value()/100

    def get_data(self):
        return {'slider val': self.value()}

    def set_data(self, data):
        self.setValue(data['slider val'])



    # optional - important for threading - stop everything here
    def removed(self):
        pass
