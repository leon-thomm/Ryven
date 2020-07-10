from PySide2.QtCore import QTimer

from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node
from custom_src.retain import M


# GENERAL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output

# EDITING
# self.create_new_input(type_, label, widget_type='', widget_name='', widget_pos='under', pos=-1)
# self.delete_input(input or index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(output or index)


# LOGGING
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')


class Clock_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(Clock_NodeInstance, self).__init__(parent_node, flow, configuration)

        self.special_actions['start'] = {'method': M(self.action_start)}
        self.special_actions['stop'] = {'method': M(self.action_stop)}

        self.timer = QTimer()
        self.timer.timeout.connect(M(self.timeouted))

        self.initialized()


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

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass



    # optional - important for threading - stop everything here
    def removing(self):
        self.timer.stop()
