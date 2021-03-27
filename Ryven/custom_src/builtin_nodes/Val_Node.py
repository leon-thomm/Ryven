import os

from PySide2.QtWidgets import QLineEdit

from NENV import *
from NWENV import *
from ryvencore_qt import *


class ValNode_MainWidget(MWB, QLineEdit):

    value_changed = Signal(object)

    def __init__(self, params):
        MWB.__init__(self, params)
        QLineEdit.__init__(self)

        self.setStyleSheet('''
            QLineEdit{
                border-radius: 10px;
                background-color: transparent;
                border: 1px solid #404040;
                color: #aaaaaa;
                padding: 3px;
            }
        ''')

        self.setFixedWidth(80)
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

    def get_data(self):
        data = {'text': self.text()}
        return data

    def set_data(self, data):
        self.setText(data['text'])

    def remove_event(self):
        pass


class Val_Node(Node):

    title = 'val'
    description = 'returns the evaluated value that is typed into the input field'
    init_outputs = [
        NodeInputBP(type_='data')
    ]
    main_widget_class = ValNode_MainWidget
    main_widget_pos = 'between ports'
    style = 'extended'
    color = '#c69a15'

    def __init__(self, params):
        super(Val_Node, self).__init__(params)

        self.special_actions['edit val via dialog'] = {'method': self.action_edit_via_dialog}
        self.val = None

    def place_event(self):
        self.main_widget().value_changed.connect(self.main_widget_val_changed)

    def main_widget_val_changed(self, val):
        self.val = val
        self.update()

    def update_event(self, input_called=-1):
        self.set_output_val(0, self.val)

    def action_edit_via_dialog(self):
        from ..EditVal_Dialog import EditVal_Dialog

        val_dialog = EditVal_Dialog(parent=None, init_val=self.val)
        accepted = val_dialog.exec_()
        if accepted:
            self.main_widget().setText(str(val_dialog.get_val()))
            self.update()

    def get_current_var_name(self):
        return self.input(0)

    def get_data(self):
        return {
            'val': self.main_widget().get_val()
        }

    def set_data(self, data):
        self.val = data['val']

    def remove_event(self):
        pass
