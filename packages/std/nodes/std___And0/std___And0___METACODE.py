from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node
from custom_src.retain import M


class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        self.special_actions['add input'] = {'method': M(self.action_add_input)}
        self.enlargement_state = 0

        self.initialized() 


    def action_add_input(self):
        self.create_new_input('data', '', widget_type='std line edit', widget_pos='besides')
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
            result = result and self.input(i) and self.input(i+1)
        self.outputs[0].set_val(result)

    def get_data(self):
        data = {'enlargement state': self.enlargement_state}
        return data

    def set_data(self, data):
        self.enlargement_state = data['enlargement state']



    # optional - important for threading - stop everything here
    def removing(self):
        pass
