from NIENV import *


# GENERAL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
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


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        self.special_actions['add exec input'] = {'method': M(self.action_add_exec_input)}
        self.special_actions['add data input'] = {'method': M(self.action_add_data_input)}

        self.num_scripts = 1
        self.num_data_inputs = 0


    def action_add_exec_input(self):
        self.num_scripts += 1
        self.create_new_input('exec', '', pos=self.num_scripts-1)
        self.create_new_output('exec', '')
        print('node before:', self.main_widget.height())
        self.main_widget.add_new_script()  # shape gets updated in main_widget
        print('node after:', self.main_widget.height())
        self.special_actions['remove exec input'] = {'method': M(self.action_remove_exec_input)}

    def action_remove_exec_input(self):
        self.delete_input(self.num_scripts-1)
        self.delete_output(-1)
        self.num_scripts -= 1
        self.main_widget.delete_script()  # shape gets updated in main_widget
        if self.num_scripts == 1:
            del self.special_actions['remove exec input']

    def action_add_data_input(self):
        self.num_data_inputs += 1
        self.create_new_input('data', '')
        self.special_actions['remove data input'] = {'method': M(self.action_remove_data_input)}

    def action_remove_data_input(self):
        self.delete_input(-1)
        self.num_data_inputs -= 1
        if self.num_data_inputs == 0:
            del self.special_actions['remove data input']

    def update_event(self, input_called=-1):
        if input_called > -1 < self.num_scripts:
            try:
                exec(self.main_widget.get_code(input_called))
                self.exec_output(input_called)
            except Exception as e:
                self.log_message('couldn\'t execute script number '+str(input_called+1)+'\n    '+str(e), 'error')

    def get_data(self):
        codes = []
        for i in range(self.num_scripts):
            code = self.main_widget.get_code(i)
            codes.append(code)
        data = {'num scripts': self.num_scripts,
                'num data inputs': self.num_data_inputs,
                'codes': codes}
        return data

    def set_data(self, data):
        for i in range(data['num scripts']):
            self.action_add_exec_input()

        for i in range(data['num data inputs']):
            self.action_add_data_input()

        for i in range(len(data['codes'])):
            c = data['codes'][i]
            self.main_widget.set_code(i, c)


    def remove_event(self):
        pass
