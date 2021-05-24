
from NENV import *

import token


class NodeBase(Node):
    pass


class Iseof_Node(NodeBase):
    """
    """
    
    title = 'ISEOF'
    type_ = 'token'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, token.ISEOF(self.input(0)))
        

class Isnonterminal_Node(NodeBase):
    """
    """
    
    title = 'ISNONTERMINAL'
    type_ = 'token'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, token.ISNONTERMINAL(self.input(0)))
        

class Isterminal_Node(NodeBase):
    """
    """
    
    title = 'ISTERMINAL'
    type_ = 'token'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, token.ISTERMINAL(self.input(0)))
        


export_nodes(
    Iseof_Node,
    Isnonterminal_Node,
    Isterminal_Node,
)
