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

        # self.special_actions['action name'] = self.actionmethod ...
        # ...

        if configuration:
            self.set_data(configuration['state data'])


    def update_event(self, input_called=-1):
        if input_called == 0:
            arr = self.input(1)
            val = self.input(2)
            arr.append(val)
            self.outputs[1].set_val(arr)
            self.exec_output(0)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass



    # optional - important for threading - stop everything here
    def removing(self):
        pass
