from custom_src.retain import M
from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node
from custom_src.EditVal_Dialog import EditVal_Dialog


class Val_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(Val_NodeInstance, self).__init__(parent_node, flow, configuration)

        self.special_actions['edit val via dialog'] = {'method': M(self.action_edit_via_dialog)}

        self.initialized()

    def update_event(self, input_called=-1):
        self.set_output_val(0, self.main_widget.get_val())

    def action_edit_via_dialog(self):
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