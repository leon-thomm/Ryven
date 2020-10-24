from NIENV import *


# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        self.special_actions['print something 1'] = {'method': M(self.print_something),
                                                     'data': 'hello!!'}
        self.special_actions['print something 2'] = {'method': M(self.print_something),
                                                     'data': 'HELLOO!?!?!?'}


    def update_event(self, input_called=-1):
        if input_called == 0:
            print(self.input(1))
            self.exec_output(0)

    def print_something(self, data):
        print(data)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
