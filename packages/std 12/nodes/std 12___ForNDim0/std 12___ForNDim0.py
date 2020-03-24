from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node


# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.create_new_input(type_, label, append=True, widget_type='', widget_name='', widget_pos='under')
# self.delete_input(input or index)
# self.create_new_output(type_, label, append=True)
# self.delete_output(output or index)
# self.update_shape()


class ForNDim_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(ForNDim_NodeInstance, self).__init__(parent_node, flow, configuration)

        self.special_actions['execute'] = self.action_exec_input_0
        self.special_actions['add dimension'] = self.action_add_dimension
        # self.special_actions['remove dimension'] = self.action_remove_dimension
        self.dimensions = 1

        if configuration:
            self.set_data(configuration['state data'])


    def update(self, input_called=-1, token=None):
        self.handle_token(token)
        # ------------------------

        if input_called == 0:
            self.iterate(1)

        # ------------------------
        self.data_outputs_updated()

    def iterate(self, current_dim):
        print('iterating through dimension', current_dim)
        from_input_index = 1 + (2*(current_dim-1))
        to_input_index = from_input_index+1
        exec_output_index = 2*(current_dim-1)
        counter_output_index = exec_output_index+1

        for i in range(self.input(from_input_index), self.input(to_input_index)):
            self.outputs[counter_output_index].set_val(i)
            print('calling exec_output')
            self.exec_output(exec_output_index)
            if current_dim < self.dimensions:
                print('calling new iteration')
                self.iterate(current_dim+1)

    def action_exec_input_0(self):
        self.update(0)

    def action_add_dimension(self):
        new_dim = self.dimensions+1
        self.create_new_input('data', 'i'+str(new_dim)+' from', widget_type='std spin box', widget_pos='besides')
        self.create_new_input('data', 'i'+str(new_dim)+' to', widget_type='std spin box', widget_pos='besides')
        self.create_new_output('exec', 'i'+str(new_dim)+' loop')
        self.create_new_output('data', 'i'+str(new_dim))
        self.dimensions += 1
        self.update_shape()

        self.special_actions['remove dimension'] = self.action_remove_dimension

    def action_remove_dimension(self):
        self.delete_input(self.inputs[-1])
        self.delete_input(self.inputs[-1])
        self.delete_output(self.outputs[-1])
        self.delete_output(self.outputs[-1])
        self.dimensions -= 1
        self.update_shape()

        if self.dimensions == 1:
            del self.special_actions['remove dimension']

    def deleted(self):
        pass

    def get_data(self):
        data = {'num dimensions': self.dimensions}
        return data

    def set_data(self, data):
        self.dimensions = data['num dimensions']
