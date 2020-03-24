from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node


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


class Plus_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(Plus_NodeInstance, self).__init__(parent_node, flow, configuration)

        self.special_actions['add input'] = self.action_add_input
        self.num_inputs = 2

        if configuration:
            self.set_data(configuration['state data'])


    def updating(self, token, input_called=-1):
        try:
            sum_val = sum([self.input(i) for i in range(len(self.inputs))])
            self.outputs[0].set_val(sum_val)
        except Exception as e:
            sum_val = ''
            for i in range(len(self.inputs)):
                sum_val += str(self.input(i))
            self.outputs[0].set_val(sum_val)

    def action_add_input(self):
        self.create_new_input('data', '', widget_type='std line edit', widget_pos='besides')
        self.num_inputs += 1
        self.special_actions['remove input'] = self.action_remove_input

    def action_remove_input(self):
        self.delete_input(self.inputs[-1])
        self.num_inputs -= 1
        if self.num_inputs == 2:
            del self.special_actions['remove input']

    def get_data(self):
        data = {'num inputs': self.num_inputs}
        return data

    def set_data(self, data):
        self.num_inputs = data['num inputs']



    # optional - important for threading - stop everything here
    def removing(self):
        pass
