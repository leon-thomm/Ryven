from NENV import *


# API METHODS --------------

# self.main_widget()
# self.update_shape()

# Ports
# self.input(index)
# self.set_output_val(index, val)
# self.exec_output(index)

# self.create_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_output(type_, label, pos=-1)
# self.delete_output(index)

# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# --------------------------


class MakeComplex_Node(Node):
    def __init__(self, params):
        super(MakeComplex_Node, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        self.set_output_val(0, complex(self.input(0), self.input(1)))

    def get_state(self):
        data = {}
        return data

    def set_state(self, data):
        pass

    def removing(self):
        pass
