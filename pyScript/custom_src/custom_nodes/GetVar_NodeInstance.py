from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class GetVar_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(GetVar_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        self.var_name = ''

        if configuration:
            self.set_data(configuration['state data'])

    def updating(self, token, input_called=-1):
        self.outputs[0].set_val(self.flow.parent_script.get_var(self.input(0)).val)

    def removed(self):
        pass

    def get_data(self):
        return {}

    def set_data(self, data):
        # self.var_name = data['variable name']
        pass