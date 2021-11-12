
from ryven.NENV import *

import formatter


class NodeBase(Node):
    pass


class Test_Node(NodeBase):
    """
    """
    
    title = 'test'
    type_ = 'formatter'
    init_inputs = [
        NodeInputBP(label='file', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, formatter.test(self.input(0)))
        


export_nodes(
    Test_Node,
)
