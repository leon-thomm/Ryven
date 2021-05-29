from NWENV import *

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QLineEdit


class Result_Node_MainWidget(MWB, QLineEdit):
    def __init__(self, params):
        MWB.__init__(self, params)
        QLineEdit.__init__(self)

        self.setReadOnly(True)
        self.setFixedWidth(120)


    def show_val(self, new_val):
        self.setText(str(new_val))
        self.setCursorPosition(0)


class ValNode_MainWidget(MWB, QLineEdit):

    value_changed = Signal(object)

    def __init__(self, params):
        MWB.__init__(self, params)
        QLineEdit.__init__(self)

        # self.setFixedWidth(80)
        # self.setMinimumWidth(80)
        self.resize(120, 31)
        self.editingFinished.connect(self.editing_finished)

    def editing_finished(self):
        # self.node.update()
        self.value_changed.emit(self.get_val())

    def get_val(self):
        val = None
        try:
            val = eval(self.text())
        except Exception as e:
            val = self.text()
        return val

    def get_state(self):
        data = {'text': self.text()}
        return data

    def set_state(self, data):
        self.setText(data['text'])


export_widgets(
    Result_Node_MainWidget,
    ValNode_MainWidget,
)