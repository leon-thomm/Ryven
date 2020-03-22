from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node


# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        self.special_actions['print something 1'] = {'method': self.print_something,
                                                     'data': 'hello!!'}
        self.special_actions['print something 2'] = {'method': self.print_something,
                                                     'data': 'HELLOO!?!?!?'}

        if configuration:
            self.set_data(configuration['state data'])


    def updating(self, token, input_called=-1):
        if input_called == 0:
            print(self.input(1))
            self.exec_output(0)

    def print_something(self, data):
        print(data)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...



    # optional - important for threading - stop everything here
    def removing(self):
        pass
