
from ryven.NENV import *

import symtable


class NodeBase(Node):
    pass


class Symtable_Node(NodeBase):
    """
    """
    
    title = 'symtable'
    type_ = 'symtable'
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='filename'),
        NodeInputBP(label='compile_type'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, symtable.symtable(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    Symtable_Node,
)
