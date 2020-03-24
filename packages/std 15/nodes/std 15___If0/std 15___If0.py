from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node


# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output
# self.create_new_input(type_, label, append=True, widget_type='', widget_name='', widget_pos='under', pos=-1)
# self.delete_input(input or index)
# self.create_new_output(type_, label, append=True, pos=-1)
# self.delete_output(output or index)
# self.update_shape()


class If_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(If_NodeInstance, self).__init__(parent_node, flow, configuration)

        self.special_actions['add else if'] = self.action_add_else_if
        self.special_actions['execute'] = self.action_execute
        self.else_if_enlargement_state = 0

        if configuration:
            self.set_data(configuration['state data'])


    def action_add_else_if(self):
        self.create_new_input('data', 'condition '+str(self.else_if_enlargement_state+1), widget_type='std line edit', widget_pos='under')
        self.create_new_output('exec', 'elif '+str(self.else_if_enlargement_state+1), append=False, pos=len(self.outputs)-1)
        self.else_if_enlargement_state += 1
        self.special_actions['remove else if'] = self.action_remove_else_if
        self.update_shape()

    def action_remove_else_if(self):
        self.delete_input(self.inputs[-1])
        self.delete_output(self.outputs[-2])
        self.else_if_enlargement_state -= 1
        if self.else_if_enlargement_state == 0:
            del self.special_actions['remove else if']
        self.update_shape()

    def action_execute(self):
        self.update(input_called=0)

    def updating(self, token, input_called=-1):
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



    # optional - important for threading - stop everything here
    def removed(self):
        pass
