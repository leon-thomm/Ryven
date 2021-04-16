from ryvencore_qt import *


class And_Node(Node):

    title = '&&'
    description = 'logical AND'
    init_inputs = [
        NodeInputBP(type_='data', label='', add_config={'widget name': 'std line edit', 'widget pos': 'besides'}),
        NodeInputBP(type_='data', label='', add_config={'widget name': 'std line edit', 'widget pos': 'besides'}),
    ]
    init_outputs = [
        NodeInputBP(type_='data', label='')
    ]
    style = 'small'
    color = '#aa4444'
    icon = 'custom_src/built_in/test.svg'


    def __init__(self, params):
        super().__init__(params)

        self.special_actions['add input'] = {'method': self.action_add_input}
        self.enlargement_state = 0


    def action_add_input(self):
        self.create_input('data', '', {'widget name': 'std line edit s r nb', 'widget pos': 'besides'})
        self.enlargement_state += 1
        self.special_actions['remove input'] = {'method': self.action_remove_input}

    def action_remove_input(self):
        self.delete_input(self.inputs[-1])
        self.enlargement_state -= 1
        if self.enlargement_state == 0:
            del self.special_actions['remove input']

    def update_event(self, input_called=-1):
        result = True
        for i in range(1+self.enlargement_state):
            result = result and self.input(i) and self.input(i+1)
        self.outputs[0].set_val(result)

    def get_state(self):
        data = {'enlargement state': self.enlargement_state}
        return data

    def set_state(self, data):
        self.enlargement_state = data['enlargement state']