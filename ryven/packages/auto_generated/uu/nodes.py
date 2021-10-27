
from NENV import *

import uu


class NodeBase(Node):
    pass


class Decode_Node(NodeBase):
    """
    Decode uuencoded file"""
    
    title = 'decode'
    type_ = 'uu'
    init_inputs = [
        NodeInputBP(label='in_file'),
        NodeInputBP(label='out_file', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='mode', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='quiet', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uu.decode(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Encode_Node(NodeBase):
    """
    Uuencode file"""
    
    title = 'encode'
    type_ = 'uu'
    init_inputs = [
        NodeInputBP(label='in_file'),
        NodeInputBP(label='out_file'),
        NodeInputBP(label='name', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='mode', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uu.encode(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Test_Node(NodeBase):
    """
    uuencode/uudecode main program"""
    
    title = 'test'
    type_ = 'uu'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uu.test())
        


export_nodes(
    Decode_Node,
    Encode_Node,
    Test_Node,
)
