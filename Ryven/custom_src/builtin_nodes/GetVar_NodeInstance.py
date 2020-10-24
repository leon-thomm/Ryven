from NIENV import *


class GetVar_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(GetVar_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = self.actionmethod ...
        self.var_name = ''

    def update_event(self, input_called=-1):
        vars_handler = self.flow.parent_script.variables_handler
        var = vars_handler.get_var(self.input(0))
        if var is not None:
            self.set_output_val(0, var.val)
        else:
            self.set_output_val(0, None)

    def get_current_var_name(self):
        return self.input(0)

    def get_data(self):
        return {}

    def set_data(self, data):
        pass

    def remove_event(self):
        pass