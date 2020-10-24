from NIENV import *


# API METHODS

# self.main_widget        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# self.set_output_val(index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# ------------------------------------------------------------------------------
import random


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        
        self.special_actions['make executable'] = {'method': M(self.action_make_executable)}
        self.active = False

    def action_make_executable(self):
        del self.special_actions['make executable']
        self.special_actions['make passve'] = {'method': M(self.action_make_passive)}
        self.create_new_input('exec', '', pos=0)
        self.create_new_output('exec', '', pos=0)
        self.active = True
    
    def action_make_passive(self):
        del self.special_actions['make passve']
        self.special_actions['make executable'] = {'method': M(self.action_make_executable)}
        self.delete_input(0)
        self.delete_output(0)
        self.active = False

    def update_event(self, input_called=-1):
        if self.active and input_called==0:
            self.set_output_val(1, random.randint(self.input(1), self.input(2)))
            self.exec_output(0)
        else:
            self.set_output_val(0, random.randint(self.input(0), self.input(1)))

    def get_data(self):
        data = {'active': self.active}
        return data

    def set_data(self, data):
        self.active = data['active']

    def removing(self):
        pass
