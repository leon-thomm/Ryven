from NENV import *


# API METHODS

# self.main_widget()        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# self.set_output_val(index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_output(type_, label, pos=-1)
# self.delete_output(index)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# ------------------------------------------------------------------------------


class ArrRemove_Node(Node):
    def __init__(self, params):
        super(ArrRemove_Node, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        if input_called == 0:
            arr = self.input(1)
            arr.remove(self.input(2))
            self.set_output_val(1, arr)
            self.exec_output(0)

    def get_state(self):
        data = {}
        # ...
        return data

    def set_state(self, data):
        pass # ...

    def removing(self):
        pass
