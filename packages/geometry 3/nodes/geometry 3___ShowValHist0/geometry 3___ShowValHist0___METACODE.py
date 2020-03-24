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


class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        self.special_actions['reset'] = self.action_reset
        self.values = []

        if configuration:
            self.set_data(configuration['state data'])
    
    def action_reset(self):
        self.reset()

    def reset(self):
        self.values.clear()
        self.main_widget.update(self.values)

    def update(self, input_called=-1, token=None):
        self.handle_token(token)
        # ------------------------

        if input_called == 0:  # exec
            if self.input(1):
                self.values.append(self.input(1))
                self.main_widget.update(self.values)
            self.exec_output(0)
        elif input_called == 2:
            self.reset()

        # ------------------------
        self.data_outputs_updated()

    def deleted(self):
        pass

    def get_data(self):
        data = {'values': self.values}
        return data

    def set_data(self, data):
        self.values = data['values']
        self.main_widget.update(self.values)
