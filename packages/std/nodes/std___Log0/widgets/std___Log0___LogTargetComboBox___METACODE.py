from NIWENV import *

from PySide2.QtWidgets import QComboBox
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...


class %CLASS%(QComboBox, IWB):
    def __init__(self, params):
        IWB.__init__(self, params)
        QComboBox.__init__(self)

        self.addItem('personal')
        self.addItem('global')
        self.addItem('error')

        self.currentTextChanged.connect(M(self.text_changed))
        self.setCurrentText('personal')

        self.setStyleSheet(self.parent_node_instance.session_stylesheet())


    def text_changed(self, t):
        self.parent_node_instance.target = t

    def get_val(self):
        return self.currentText()


    def get_data(self):
        data = {'text': self.currentText()}
        return data

    def set_data(self, data):
        self.setCurrentText(data['text'])


    # remove logs and stop threads and timers here
    def remove_event(self):
        pass # ...