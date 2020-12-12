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
        self.points = []


    def update_event(self, input_called=-1):
        if input_called == 0:
            self.points = self.input(1)
            self.main_widget.show_points(self.points)
            self.exec_output(0)

    def get_data(self):
        data = {'points': self.points}
        return data

    def set_data(self, data):
        self.points = data['points']
        self.main_widget.show_points(self.points)


    def remove_event(self):
        pass
