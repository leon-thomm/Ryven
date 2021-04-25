from NWENV import *

from qtpy.QtWidgets import QComboBox
# from qtpy.QtCore import ...
# from qtpy.QtGui import ...


class %CLASS%(QComboBox, IWB):
    def __init__(self, params):
        IWB.__init__(self, params)
        QComboBox.__init__(self)

        self.addItem('own')
        self.addItem('Global')
        self.addItem('Errors')

        self.currentTextChanged.connect(self.text_changed)
        self.setCurrentText('personal')

        self.setStyleSheet(self.parent_node_instance.session_stylesheet())


    def text_changed(self, t):
        self.parent_node_instance.target = t

    def get_val(self):
        return self.currentText()


    def get_state(self):
        data = {'text': self.currentText()}
        return data

    def set_state(self, data):
        self.setCurrentText(data['text'])


    # remove logs and stop threads and timers here
    def remove_event(self):
        pass # ...