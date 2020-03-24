from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node


# GENERAL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output

# EDITING
# self.create_new_input(type_, label, append=True, widget_type='', widget_name='', widget_pos='under', pos=-1)
# self.delete_input(input or index)
# self.create_new_output(type_, label, append=True, pos=-1)
# self.delete_output(output or index)
# self.update_shape()                  <- recomputes the whole shape and content positions

# LOGGING
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')


class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        self.special_actions['add size input'] = {'method': self.action_add_size_input}
        self.size_input_shown = False

        if configuration:
            self.set_data(configuration['state data'])


    def updating(self, token, input_called=-1):
        if input_called == 0:
            file = self.input(1)
            if self.size_input_shown:
                size = self.input(2)
                self.outputs[1].set_val(file.read(size))
            else:
                self.outputs[1].set_val(file.read())
            self.exec_output(0)

    def action_add_size_input(self):
        self.create_new_input('data', 'size', append=True, widget_type='std spin box', widget_pos='besides')
        del self.special_actions['add size input']
        self.special_actions['remove size input'] = {'method': self.action_remove_size_input}
        self.size_input_shown = True
        self.update_shape()

    def action_remove_size_input(self):
        self.delete_input(-1)
        del self.special_actions['remove size input']
        self.special_actions['add size input'] = {'method': self.action_add_size_input}
        self.size_input_shown = False
        self.update_shape()

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...



    # optional - important for threading - stop everything here
    def removing(self):
        pass
