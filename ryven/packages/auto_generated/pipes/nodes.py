
from NENV import *

import pipes


class NodeBase(Node):
    pass


class Makepipeline_Node(NodeBase):
    """
    """
    
    title = 'makepipeline'
    type_ = 'pipes'
    init_inputs = [
        NodeInputBP(label='infile'),
        NodeInputBP(label='steps'),
        NodeInputBP(label='outfile'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pipes.makepipeline(self.input(0), self.input(1), self.input(2)))
        

class Quote_Node(NodeBase):
    """
    Return a shell-escaped version of the string *s*."""
    
    title = 'quote'
    type_ = 'pipes'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pipes.quote(self.input(0)))
        


export_nodes(
    Makepipeline_Node,
    Quote_Node,
)
