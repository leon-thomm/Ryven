from NWENV import *

# from PySide2.QtWidgets import ...
from PySide2.QtCore import Qt
# from PySide2.QtGui import ...

from PySide2.QtWidgets import QSlider


class %CLASS%(QSlider, IWB):

    val_changed = Signal(float)

    def __init__(self, params):
        IWB.__init__(self, params)
        QSlider.__init__(self, Qt.Horizontal)

        self.setStyleSheet('''
            background: transparent;
        ''')
        self.setFixedWidth(70)
        self.setMinimum(0)
        self.setMaximum(100000)
        self.setSingleStep(1)
        self.valueChanged.connect(self.slider_val_changed)


    def slider_val_changed(self, v):
        # self.node.update_timer_interval((v/self.maximum()))
        self.val_changed.emit(v/self.maximum())

    def get_val(self):
        return (self.value()/self.maximum())

    def get_state(self):
        data = {'val': self.value()}
        return data

    def set_state(self, data):
        self.setValue(data['val'])

    def remove_event(self):
        pass
