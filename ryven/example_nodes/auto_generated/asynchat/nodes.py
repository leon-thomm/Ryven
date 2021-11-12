
from ryven.NENV import *

import asynchat


class NodeBase(Node):
    pass


class Find_Prefix_At_End_Node(NodeBase):
    """
    """
    
    title = 'find_prefix_at_end'
    type_ = 'asynchat'
    init_inputs = [
        NodeInputBP(label='haystack'),
        NodeInputBP(label='needle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, asynchat.find_prefix_at_end(self.input(0), self.input(1)))
        


export_nodes(
    Find_Prefix_At_End_Node,
)
