
from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class SetVar_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(SetVar_NodeInstance, self).__init__(parent_node, flow, configuration)

        self.special_actions['execute'] = {'method': self.action_execute}
        self.var_name = ''

        if configuration:
            self.set_data(configuration['state data'])

    def update_event(self, input_called=-1):
        if input_called == 0:
            self.var_name = self.input(1)
            vars_handler = self.flow.parent_script.variables_handler
            if vars_handler.set_var(self.input(1), self.input(2)):
                self.outputs[1].set_val(self.input(2))
            self.exec_output(0)

    def action_execute(self):
        self.update(0)

    def removed(self):
        pass

    def get_data(self):
        return {}

    def set_data(self, data):
        pass