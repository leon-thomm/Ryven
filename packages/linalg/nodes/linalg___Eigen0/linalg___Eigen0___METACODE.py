from NIENV import *


# API METHODS

# self.main_widget        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# self.set_output_val(index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# ------------------------------------------------------------------------------
from numpy.linalg import eig


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        self.special_actions['add matrix input'] = {'method': M(self.action_add_matrix_input)}
        self.num_matrix_inputs = 1

    def action_add_matrix_input(self):
        self.create_new_input('data', '')
        self.num_matrix_input += 1
        self.special_actions['remove matrix input'] = {'method': M(self.action_rem_matrix_input)}

    def action_rem_matrix_input(self):
        self.delete_input(-1)
        self.num_matrix_input -= 1
        if self.num_matrix_input == 1:
            del self.special_actions['remove matrix input']

    def update_event(self, input_called=-1):
        w, v = eig(self.input(0))
        self.set_output_val(0, w)
        self.set_output_val(1, v)

    def get_data(self):
        data = {'number matrix inputs': self.num_matrix_inputs}
        return data

    def set_data(self, data):
        self.num_matrix_inputs = data['number matrix inputs']
        for i in range(self.num_matrix_inputs-1):
            self.action_add_matrix_input()

    def removing(self):
        pass
