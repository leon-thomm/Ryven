from NENV import *


ButtonWidget, \
 = load_from_file(file='widgets.py', caller_file=__file__, components_list=[
        'ButtonWidget', 
    ], gui=True)





import numpy as np

class SuperNode(Node):

    init_inputs = [
        NodeInputBP()
    ]
    init_outputs = [
        NodeOutputBP()
    ]
    main_widget_class = ButtonWidget
    main_widget_pos = 'below ports'

    def __init__(self, params):
        super().__init__(params)
        self.val = 42

    def get_state(self):
        return {'val': self.val}
    
    def set_state(self, data):
        self.val = data['val']


class Node1(SuperNode):
    title = 'Node 1'
    description = 'My first node!'

    def update_event(self, input_called=-1):
        print('I got something! look:', self.input(0))





nodes = [
    Node1,
]
