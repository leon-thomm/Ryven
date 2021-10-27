from NENV import *


class NodeBase(Node):

    def __init__(self, params):
        super().__init__(params)

        # here we could add some stuff for all nodes below...
        self.actions['asdf'] = {'method': self.asdf}

    def asdf(self):
        self.create_input_dt(dtype=dtypes.Integer(default=1, bounds=(1, 100)),
                             label='scale')


import random

class Rand_Node(NodeBase):
    """Generates random float in range"""

    title = 'random'
    init_inputs = [
        NodeInputBP(dtype=dtypes.Integer(default=1, bounds=(1, 100)), label='scale'),
    ]
    init_outputs = [
        NodeOutputBP(),
    ]
    color = '#aabb44'

    def update_event(self, inp=-1):
        self.set_output_val(0, round(random.random() * self.input(0), 3))


class Print_Node(NodeBase):
    """Prints your data"""

    title = 'print'
    init_inputs = [
        NodeInputBP(dtype=dtypes.Data(size='s')),
    ]
    color = '#3355dd'

    def update_event(self, inp=-1):
        print(self.input(0))


export_nodes(
    Rand_Node,
    Print_Node,
)
