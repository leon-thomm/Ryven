
from NENV import *

import sre_constants


class NodeBase(Node):
    pass


class _Makecodes_Node(NodeBase):
    """
    """
    
    title = '_makecodes'
    type_ = 'sre_constants'
    init_inputs = [
        NodeInputBP(label='names'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_constants._makecodes(self.input(0)))
        


export_nodes(
    _Makecodes_Node,
)
