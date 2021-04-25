from qtpy.QtCore import QTimer

from NENV import *


# GENERAL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget()                    <- access to main widget
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


class %CLASS%(Node):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        self.special_actions['start'] = {'method': self.action_start}
        self.special_actions['stop'] = {'method': self.action_stop}

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeouted)  # TODO: use sth else than QTimer

    def view_place_event(self):
        self.input_widget(0).val_changed.connect(self.update_timer_interval)

    def update_event(self, input_called=-1):
        pass

    def action_start(self):
        self.update_timer_interval(self.input(0))
        self.timer.start()

    def action_stop(self):
        self.timer.stop()

    def update_timer_interval(self, new_val):
        self.timer.setInterval(new_val*1000)

    def timeouted(self):
        self.exec_output(0)

    def get_state(self):
        data = {}
        # ...
        return data

    def set_state(self, data):
        pass


    def remove_event(self):
        self.timer.stop()
