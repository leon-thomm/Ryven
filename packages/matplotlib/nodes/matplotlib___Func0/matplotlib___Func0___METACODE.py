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
import numpy as np


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        x = None
        if type(self.input(0)) == str:
            x = np.linspace(*eval(self.input(0)))
        else:
            x = self.input(0)
        # x = eval('np.linspace('+self.input(0)+')') if type(self.input(0)) == str else self.input(0)
        functions = {}
        for i in range(self.input(1).count('\n')+1):
            signature = self.input(1).splitlines()[i]
            if signature != '':
                functions[signature] = eval(signature)
        #function_signatures = self.input(1).splitlines()
        #functions = [eval(l) for l in function_signatures]
        self.main_widget.redraw(x, functions)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...

    def removing(self):
        pass
