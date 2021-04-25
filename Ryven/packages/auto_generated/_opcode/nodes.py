
from NENV import *

import _opcode


class NodeBase(Node):
    pass


class AutoNode__opcode_stack_effect(NodeBase):
    title = 'stack_effect'
    type_ = '_opcode'
    doc = """Compute the stack effect of the opcode."""
    init_inputs = [
        NodeInputBP(label='opcode'),
        NodeInputBP(label='oparg'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _opcode.stack_effect(self.input(0), self.input(1)))
        


export_nodes(
    AutoNode__opcode_stack_effect,
)
