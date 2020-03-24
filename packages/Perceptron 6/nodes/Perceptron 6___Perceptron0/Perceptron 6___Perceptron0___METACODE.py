from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node

import random

# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output
# self.create_new_input(type_, label, append=True, widget_type='', widget_name='', widget_pos='under')
# self.delete_input(input or index)
# self.create_new_output(type_, label, append=True)
# self.delete_output(output or index)
# self.update_shape()


class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        self.special_actions['reset'] = self.action_reset
        self.weights = [random.uniform(-1, 1), random.uniform(-1, 1)]

        if configuration:
            self.set_data(configuration['state data'])


    def action_reset(self):
        self.weights = [random.uniform(-1, 1), random.uniform(-1, 1)]

    def guess(self, x1, x2):
        return x1*self.weights[0]+x2*self.weights[1]

    def sign(self, val):
        return -1 if val < 0 else +1

    def updating(self, token, input_called=-1):
        if input_called == 0:  # guess
            x1 = self.input(1)
            x2 = self.input(2)
            guess = self.guess(x1, x2)
            signed_guess = self.sign(guess)
            print('setting val of perceptron output to', signed_guess)
            self.outputs[1].set_val(signed_guess)
            self.exec_output(0)

        elif input_called == 3:  # correct
            print('a')
            fix_factor = self.input(5)
            print('b')
            x1 = self.input(1)
            print('c')
            x2 = self.input(2)
            print('calling input 4 for error')
            err = self.input(4)
            print(x1)
            print(err)
            print('fix_factor:', fix_factor)
            d_w1 = x1*err*fix_factor
            self.weights[0] += d_w1
            d_w2 = x2*err*fix_factor
            self.weights[1] += d_w2

    def deleted(self):
        pass

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...
