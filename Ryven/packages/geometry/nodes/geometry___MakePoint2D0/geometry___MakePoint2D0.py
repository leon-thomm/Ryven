from NENV import *


# GENERAL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget()                    <- access to main widget
# self.exec_output(index)             <- executes an execution output

# EDITING
# self.create_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(input or index)
# self.create_output(type_, label, pos=-1)
# self.delete_output(output or index)


# LOGGING
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')


class MakePoint2D_Node(Node):
    def __init__(self, params):
        super(MakePoint2D_Node, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...


    def update_event(self, input_called=-1):
        self.outputs[0].set_val([self.input(0), self.input(1)])

    def get_state(self):
        data = {}
        # ...
        return data

    def set_state(self, data):
        pass


    def remove_event(self):
        pass
