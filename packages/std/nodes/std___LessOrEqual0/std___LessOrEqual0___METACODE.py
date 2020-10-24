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
        self.enlargement_state = 0


    def action_add_input(self):
        self.create_new_input('data', '', widget_name='std line edit s r nb', widget_pos='besides')
        self.enlargement_state += 1
        self.special_actions['remove input'] = {'method': M(self.action_remove_input)}


    def action_remove_input(self):
        self.delete_input(self.inputs[-1])
        self.enlargement_state -= 1
        if self.enlargement_state == 0:
            del self.special_actions['remove input']


    def update_event(self, input_called=-1):
        result = True
        for i in range(1+self.enlargement_state):
            result = result and self.input(i) <= self.input(i+1)
        self.outputs[0].set_val(result)

    def get_data(self):
        data = {'enlargement state': self.enlargement_state}
        return data

    def set_data(self, data):
        self.enlargement_state = data['enlargement state']


    def remove_event(self):
        pass
