from NIENV import *


# GENERAL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output

# EDITING
# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(input or index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(output or index)


# LOGGING
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...


    def update_event(self, input_called=-1):
        if input_called == 0:
            file = self.input(1)
            data = str(self.input(2))
            file.write(data)
            self.exec_output(0)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        # ...
        pass


    def remove_event(self):
        pass
