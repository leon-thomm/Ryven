from NIENV import *


# API METHODS --------------

# self.main_widget
# self.update_shape()

# Ports
# self.input(index)
# self.set_output_val(index, val)
# self.exec_output(index)

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index)

# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# --------------------------


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        self.special_actions['use data instead'] = {'method': M(self.action_use_data)}
        self.using_function = True

    def action_use_data(self):
        del self.special_actions['use data instead']
        self.special_actions['use func instead'] = {'method': M(self.action_use_func)}
        
        self.delete_input(0)
        self.delete_input(0)
        self.delete_input(0)
        
        self.create_new_input('data', 'data', pos=0)

        self.using_function = False

    def action_use_func(self):
        del self.special_actions['use func instead']
        self.special_actions['use data instead'] = {'method': M(self.action_use_data)}
        
        self.delete_input(0)
        
        self.create_new_input('data', 'f', widget_name='FunctionInput', widget_pos='under', pos=0)
        self.create_new_input('data', 'noise range', widget_name='std line edit s r nb', widget_pos='besides', pos=1)
        self.create_new_input('data', 'm', widget_name='std line edit s r nb', widget_pos='besides', pos=2)

        self.using_function = True

    def update_event(self, input_called=-1):
        if self.using_function:
            f = self.input(0)
            noise_range = self.input(1)
            m = self.input(2)
            min_deg, max_deg = self.input(3) # should be a tuple (min, max)
            min_x, max_x = self.input(4)    # same, here: (min, max)
            self.main_widget.redraw_by_func(f, noise_range, m, min_deg, max_deg, min_x, max_x)
        else:
            data = self.input(0)
            min_deg, max_deg = self.input(1) # should be a tuple (min, max)
            min_x, max_x = self.input(2)    # same, here: (min, max)
            self.main_widget.redraw_by_data(data, min_deg, max_deg, min_x, max_x)
            

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
