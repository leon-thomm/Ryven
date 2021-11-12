
from ryven.NENV import *

import opcode


class NodeBase(Node):
    pass


class Stack_Effect_Node(NodeBase):
    """
    Compute the stack effect of the opcode."""
    
    title = 'stack_effect'
    type_ = 'opcode'
    init_inputs = [
        NodeInputBP(label='opcode'),
        NodeInputBP(label='oparg', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, opcode.stack_effect(self.input(0), self.input(1)))
        


export_nodes(
    Stack_Effect_Node,
)
