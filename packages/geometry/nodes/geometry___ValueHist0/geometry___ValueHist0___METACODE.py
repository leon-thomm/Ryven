from NIENV import *


# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output
# self.create_new_input(type_, label, widget_name=None, widget_pos='under')
# self.delete_input(input or index)
# self.create_new_output(type_, label, append=True)
# self.delete_output(output or index)



class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        self.special_actions['reset'] = {'method': M(self.action_reset)}
        self.values = []

    def action_reset(self):
        self.reset()

    def reset(self):
        self.values.clear()
        self.main_widget.update(self.values)

    def update_event(self, input_called=-1):
        if input_called == 0:  # exec
            self.values.append(self.input(1))
            self.main_widget.update(self.values)
            self.exec_output(0)
        elif input_called == 2:
            self.reset()

    def get_data(self):
        data = {'values': self.values}
        return data

    def set_data(self, data):
        self.values = data['values']
        self.main_widget.update(self.values)


    def remove_event(self):
        pass
