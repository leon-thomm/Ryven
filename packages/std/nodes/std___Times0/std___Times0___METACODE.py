from NIENV import *


# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output
# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(input or index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(output or index)



class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        self.special_actions['add input'] = {'method': M(self.action_add_input)}
        self.num_inputs = 2


    def update_event(self, input_called=-1):
        sum_val = self.input(0)
        for i in range(1, len(self.inputs)):
            sum_val *= self.input(i)
        self.outputs[0].set_val(sum_val)

    def action_add_input(self):
        self.create_new_input('data', '', widget_name='std line edit s r nb', widget_pos='besides')
        self.num_inputs += 1
        self.special_actions['remove input'] = {'method': M(self.action_remove_input)}

    def action_remove_input(self):
        self.delete_input(self.inputs[-1])
        self.num_inputs -= 1
        if self.num_inputs == 2:
            del self.special_actions['remove input']

    def get_data(self):
        data = {'num inputs': self.num_inputs}
        return data

    def set_data(self, data):
        self.num_inputs = data['num inputs']


    def remove_event(self):
        pass
