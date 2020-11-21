from NIWENV import *

# from PySide2.QtWidgets import ...
from PySide2.QtCore import Qt
# from PySide2.QtGui import ...

from PySide2.QtWidgets import QSlider


class %CLASS%(QSlider, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QSlider.__init__(self, Qt.Horizontal)

        
        self.setStyleSheet('''
QSlider {
    background: transparent;
}

QSlider::groove:horizontal {
    border: 1px solid #6bbef2;
    background: rgba(59, 156, 217, 100);
    height: 8px;
    margin: 2px 0;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: rgba(59, 156, 217, 200);
    border: 2px solid #ffffff;
    width: 15px;
    height: 15px;
    margin: -4px 0;
    border-radius: 5px;
}
        ''')

        self.valueChanged.connect(M(self.val_changed))
        self.setMinimum(0)
        self.setMaximum(100)

    def val_changed(self, v):
        self.parent_node_instance.update()

    def get_val(self):
        return self.value()/100

    def get_data(self):
        return {'slider val': self.value()}

    def set_data(self, data):
        self.setValue(data['slider val'])


    def remove_event(self):
        pass
