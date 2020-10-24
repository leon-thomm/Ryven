from NIENV import *


class SetVar_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(SetVar_NodeInstance, self).__init__(params)

        self.var_name = ''

    def update_event(self, input_called=-1):
        if input_called == 0:
            self.var_name = self.input(1)
            vars_handler = self.flow.parent_script.variables_handler
            if vars_handler.set_var(self.input(1), self.input(2)):
                self.set_output_val(1, self.input(2))
            self.exec_output(0)

    def get_data(self):
        return {}

    def set_data(self, data):
        pass

    def remove_event(self):
        pass