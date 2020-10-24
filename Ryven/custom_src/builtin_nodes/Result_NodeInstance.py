from NIENV import *


class Result_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(Result_NodeInstance, self).__init__(params)

    def update_event(self, input_called=-1):
        self.main_widget.show_val(self.input(0))

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass
