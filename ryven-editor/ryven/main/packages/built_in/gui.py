from ryvencore import Data

from ryven.gui_env import *
from .nodes import *
from qtpy.QtGui import QKeySequence
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QLineEdit, QDialog, QDialogButtonBox, QMessageBox, QPlainTextEdit, QShortcut, QVBoxLayout


class Result_Node_MainWidget(NodeMainWidget, QLineEdit):
    def __init__(self, params):
        NodeMainWidget.__init__(self, params)
        QLineEdit.__init__(self)

        self.setReadOnly(True)
        self.setFixedWidth(120)


    def show_val(self, new_val):
        self.setText(str(new_val))
        self.setCursorPosition(0)

@node_gui(Result_Node)
class ResultGui(NodeGUI):
    main_widget_class = Result_Node_MainWidget
    main_widget_pos = 'between ports'
    color = '#c69a15'


class ValNode_MainWidget(NodeMainWidget, QLineEdit):

    value_changed = Signal(object)

    def __init__(self, params):
        NodeMainWidget.__init__(self, params)
        QLineEdit.__init__(self)

        # self.setFixedWidth(80)
        # self.setMinimumWidth(80)
        self.resize(120, 31)
        self.editingFinished.connect(self.editing_finished)

    def editing_finished(self):
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



class EditVal_Dialog(QDialog):
    def __init__(self, parent, init_val):
        super(EditVal_Dialog, self).__init__(parent)

        # shortcut
        save_shortcut = QShortcut(QKeySequence.Save, self)
        save_shortcut.activated.connect(self.save_triggered)

        main_layout = QVBoxLayout()

        self.val_text_edit = QPlainTextEdit()
        val_str = ''
        try:
            val_str = str(init_val)
        except Exception as e:
            msg_box = QMessageBox(QMessageBox.Warning, 'Value parsing failed',
                                  'Couldn\'t stringify value', QMessageBox.Ok, self)
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec_()
            self.reject()

        self.val_text_edit.setPlainText(val_str)

        main_layout.addWidget(self.val_text_edit)

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout.addWidget(button_box)

        self.setLayout(main_layout)
        self.resize(450, 300)

        self.setWindowTitle('edit val')

    def save_triggered(self):
        self.accept()

    def get_val(self):
        val = self.val_text_edit.toPlainText()
        try:
            val = eval(val)
        except Exception as e:
            pass
        return val

@node_gui(Val_Node)
class ValGui(NodeGUI):
    main_widget_class = ValNode_MainWidget
    style = 'small'
    color = '#c69a15'

    def initialized(self):
        self.main_widget().value_changed.connect(self.widget_val_updated)
        self.actions['edit val via dialog'] = {'method': self.action_edit_via_dialog}

    def widget_val_updated(self):
        self.node.val = Data(self.main_widget().get_val())
        self.node.update()

    def action_edit_via_dialog(self):
        val_dialog = EditVal_Dialog(parent=None, init_val=self.node.val)
        accepted = val_dialog.exec_()
        if accepted:
            self.main_widget().setText(str(val_dialog.get_val()))
            self.update()

@node_gui(SetVarsPassive_Node)
class SetVarsGui(NodeGUI):
    style = 'normal'
    color = '#c69a15'

    def initialized(self):
        self.actions['add var input'] = {'method': self.add_var}
        self.actions['remove var input'] = {}
        self.rebuild_remove_actions()

    def add_var(self):
        self.node.add_var_input()

    def remove_var(self, i):
        self.node.remove_var_input(i)

    def rebuild_remove_actions(self):

        # remove_keys = []
        # for k, v in self.actions['remove var input'].items():
        #     if k.startswith('remove var'):
        #         remove_keys.append(k)
        # for k in remove_keys:
        #     del self.gui.actions['remove var input'][k]
        self.actions['remove var input'] = {}

        for i in range(self.node.num_vars):
            self.actions[f'remove var input'][f'{i+1}'] = {
                'method': self.remove_var,
                'data': i+1
            }


@node_gui(SetVar_Node)
class SetVarGui(NodeGUI):
    input_widget_classes = {
        'varname': inp_widgets.Builder.str_line_edit(),
        'val': inp_widgets.Builder.str_line_edit(),
    }
    # init_input_widgets = {
    #     1: {'name': 'varname', 'pos': 'besides'},
    #     2: {'name': 'val', 'pos': 'besides'}
    # }
    style = 'normal'
    color = '#c69a15'

    def __init__(self, params):
        super().__init__(params)

        self.input_widgets[self.node.inputs[-2]] = {'name': 'varname', 'pos': 'besides'}
        self.input_widgets[self.node.inputs[-1]] = {'name': 'val', 'pos': 'besides'}

@node_gui(GetVar_Node)
class GetVarGui(NodeGUI):
    input_widget_classes = {
        'varname': inp_widgets.Builder.str_line_edit(),
    }
    init_input_widgets = {
        0: {'name': 'varname', 'pos': 'besides'}
    }
    color = '#c69a15'
