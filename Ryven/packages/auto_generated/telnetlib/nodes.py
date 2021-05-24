
from NENV import *

import telnetlib


class NodeBase(Node):
    pass


class Test_Node(NodeBase):
    """
    Test program for telnetlib.

    Usage: python telnetlib.py [-d] ... [host [port]]

    Default host is localhost; default port is 23.

    """
    
    title = 'test'
    type_ = 'telnetlib'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, telnetlib.test())
        


export_nodes(
    Test_Node,
)
