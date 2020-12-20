import os

from PySide2.QtWidgets import QLineEdit

from NIENV import *


class Val_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(Val_NodeInstance, self).__init__(params)

        self.special_actions['edit val via dialog'] = {'method': M(self.action_edit_via_dialog)}

    def update_event(self, input_called=-1):
        self.set_output_val(0, self.main_widget.get_val())

    def action_edit_via_dialog(self):
        from custom_src.EditVal_Dialog import EditVal_Dialog

        val_dialog = EditVal_Dialog(self.flow, self.main_widget.get_val())
        accepted = val_dialog.exec_()
        if accepted:
            self.main_widget.setText(str(val_dialog.get_val()))
            self.update()

    def get_current_var_name(self):
        return self.input(0)

    def get_data(self):
        return {}

    def set_data(self, data):
        pass

    def remove_event(self):
        pass


class ValNode_Instance_MainWidget(QLineEdit):
    def __init__(self, parent_node_instance):
        super(ValNode_Instance_MainWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        self.package_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../')
        # ------------------------------------------------

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
        self.parent_node_instance.update()

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