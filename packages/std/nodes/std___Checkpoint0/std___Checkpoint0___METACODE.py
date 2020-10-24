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


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        self.special_actions['make exec'] = {'method': M(self.action_make_exec)}
        self.passive = True
        self.num_exec_outputs = 0

    def action_make_exec(self):
        self.passive = False
        self.delete_input(0)
        self.delete_output(0)
        self.create_new_input('exec', '')
        del self.special_actions['make exec']
        self.special_actions['make data'] = {'method': M(self.action_make_data)}
        self.special_actions['add sequence output'] = {'method': M(self.action_add_sequence_output)}
        self.action_add_sequence_output()
    
    def action_add_sequence_output(self):
        self.create_new_output('exec', '')
        self.num_exec_outputs += 1
        self.special_actions['remove output '+str(self.num_exec_outputs)] = {'method': M(self.action_remove_sequence_output),
                                                                             'data': self.num_exec_outputs-1}  # -1 because index
    def action_remove_sequence_output(self, index):
        self.delete_output(index)
        
        # rebuilding special actions
        for i in range(self.num_exec_outputs):        
            del self.special_actions['remove output '+str(i+1)]
        self.num_exec_outputs -= 1
        for i in range(self.num_exec_outputs):
            self.special_actions['remove output '+str(i+1)] = {'method': M(self.action_remove_sequence_output),
                                                               'data': i}
    
    def action_make_data(self):
        self.passive = True
        self.delete_input(0)
        for i in range(self.num_exec_outputs):
            self.delete_output(0)
            del self.special_actions['remove output '+str(i+1)]
        self.num_exec_outputs = 0
        self.create_new_input('data', '')
        self.create_new_output('data', '')
        del self.special_actions['make data']
        del self.special_actions['add sequence output']
        self.special_actions['make exec'] = {'method': M(self.action_make_exec)}

    def update_event(self, input_called=-1):
        if self.passive:
            self.set_output_val(0, self.input(0))
        else:
            if input_called==0:
                for i in range(self.num_exec_outputs):
                    self.exec_output(i)

    def get_data(self):
        data = {'passive': self.passive,
                'num exec outputs': self.num_exec_outputs}
        return data

    def set_data(self, data):
        self.passive = data['passive']
        self.num_exec_outputs = data['num exec outputs']

    def removing(self):
        pass
