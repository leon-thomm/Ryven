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

        self.special_actions['add target option'] = {'method': M(self.action_add_target_option)}
        self.log = self.new_log('Log Node Log')
        self.default_target = 'personal'
        self.showing_target_option = False

        self.target = self.default_target


    def action_add_target_option(self):
        del self.special_actions['add target option']
        self.add_target_option()

    def add_target_option(self):
        self.special_actions['remove target option'] = {'method': M(self.action_remove_target_option)}
        self.create_new_input('data', 'target', widget_name='LogTargetComboBox', widget_pos='besides')
        self.showing_target_option = True

    def action_remove_target_option(self):
        del self.special_actions['remove target option']
        self.remove_target_option()

    def remove_target_option(self):
        self.special_actions['add target option'] = {'method': M(self.action_add_target_option)}
        self.delete_input(-1)
        self.target = self.default_target
        self.showing_target_option = False

    def update_event(self, input_called=-1):
        if input_called == 0:
            if self.target == 'personal':
                self.log.log(self.input(1))
            else:
                self.log_message(self.input(1), target=self.target)
            self.exec_output(0)

    def get_data(self):
        data = {'target': self.target,
                'showing target': self.showing_target_option}
        return data

    def set_data(self, data):
        self.target = data['target']
        self.showing_target_option =  data['showing target']


    def remove_event(self):
        pass
