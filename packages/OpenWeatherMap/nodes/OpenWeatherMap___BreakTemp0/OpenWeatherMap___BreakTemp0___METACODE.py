from NIENV import *


# API METHODS

# self.main_widget        <- access to main widget


# Ports
# self.input(index)                   <- access to input data
# self.set_output_val(self, index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')

# ------------------------------------------------------------------------------

from pyowm.utils.measurables import kelvin_to_celsius, kelvin_to_fahrenheit


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    # don't call self.update_event() directly, use self.update() instead
    def update_event(self, input_called=-1):
        temp_dict = self.input(0)

        if self.input(1) != 'kelvin':
            for key in list(temp_dict.keys()):
                item = temp_dict[key]
                if item is not None:
                    if self.input(1) == 'celsius':
                        temp_dict[key] = kelvin_to_celsius(item)
                    elif self.input(1) == 'fahrenheit':
                        temp_dict[key] = kelvin_to_fahrenheit(item)
            # temp_dict = kelvin_dict_to(temp_dict, self.input(1)) doesn't work with NoneType values -.- which happen to persist
        
        temp = temp_dict['temp']
        temp_kf = temp_dict['temp_kf']
        temp_max = temp_dict['temp_max']
        temp_min = temp_dict['temp_min']
        feels_like = temp_dict['feels_like']
        
        self.set_output_val(0, temp)
        self.set_output_val(1, temp_kf)
        self.set_output_val(2, temp_min)
        self.set_output_val(3, temp_max)
        self.set_output_val(4, feels_like)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...


    def remove_event(self):
        pass
