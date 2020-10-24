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

        self.special_actions['add else if'] = {'method': M(self.action_add_else_if)}
        self.else_if_enlargement_state = 0


    def action_add_else_if(self):
        self.create_new_input('data', 'condition '+str(self.else_if_enlargement_state+1), widget_name='std line edit m', widget_pos='under')
        self.create_new_output('exec', 'elif '+str(self.else_if_enlargement_state+1), pos=len(self.outputs)-1)
        self.else_if_enlargement_state += 1
        self.special_actions['remove else if'] = {'method': M(self.action_remove_else_if)}


    def action_remove_else_if(self):
        self.delete_input(self.inputs[-1])
        self.delete_output(self.outputs[-2])
        self.else_if_enlargement_state -= 1
        if self.else_if_enlargement_state == 0:
            del self.special_actions['remove else if']


    def update_event(self, input_called=-1):
        if input_called == 0:
            self.do_if(0, self.else_if_enlargement_state)

    def do_if(self, if_cnt, current_enlarment_state):
        if self.input(1+if_cnt):
            self.exec_output(if_cnt)
        elif if_cnt < current_enlarment_state:
            self.do_if(if_cnt+1, current_enlarment_state)
        else:
            self.exec_output(len(self.outputs)-1)

    def get_data(self):
        data = {'else if enlargment state': self.else_if_enlargement_state}
        return data

    def set_data(self, data):
        self.else_if_enlargement_state = data['else if enlargment state']


    def remove_event(self):
        pass
