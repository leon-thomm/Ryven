from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class Val_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(Val_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...

        self.initialized()

    def update_event(self, input_called=-1):
        self.set_output_val(0, self.main_widget.get_val())

    def get_current_var_name(self):
        return self.input(0)

    def removed(self):
        pass

    def get_data(self):
        return {}

    def set_data(self, data):
        pass