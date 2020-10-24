from NIENV import *


# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(input or index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(output or index)



class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        self.special_actions['add dimension'] = {'method': M(self.action_add_dimension)}

        self.dimensions = 1


    def update_event(self, input_called=-1):
        if input_called == 0:
            self.iterate(1)

    def iterate(self, current_dim):
        from_input_index = 1 + (2*(current_dim-1))
        to_input_index = from_input_index+1
        exec_output_index = 2*(current_dim-1)
        counter_output_index = exec_output_index+1

        for i in range(self.input(from_input_index), self.input(to_input_index)):
            self.outputs[counter_output_index].set_val(i)
            self.exec_output(exec_output_index)
            if current_dim < self.dimensions:
                self.iterate(current_dim+1)

    def action_add_dimension(self):
        new_dim = self.dimensions+1
        self.create_new_input('data', 'i'+str(new_dim)+' from', widget_name='std spin box', widget_pos='besides')
        self.create_new_input('data', 'i'+str(new_dim)+' to', widget_name='std spin box', widget_pos='besides')
        self.create_new_output('exec', 'i'+str(new_dim)+' loop')
        self.create_new_output('data', 'i'+str(new_dim))
        self.dimensions += 1


        self.special_actions['remove dimension'] = {'method': M(self.action_remove_dimension)}

    def action_remove_dimension(self):
        self.delete_input(-1)
        self.delete_input(-1)
        self.delete_output(-1)
        self.delete_output(-1)
        self.dimensions -= 1

        if self.dimensions == 1:
            del self.special_actions['remove dimension']

    def get_data(self):
        data = {'num dimensions': self.dimensions}
        return data

    def set_data(self, data):
        self.dimensions = data['num dimensions']


    def remove_event(self):
        pass
