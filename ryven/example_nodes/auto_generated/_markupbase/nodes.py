
from ryven.NENV import *

import _markupbase


class NodeBase(Node):
    pass


class _Declname_Match_Node(NodeBase):
    """
    Matches zero or more characters at the beginning of the string."""
    
    title = '_declname_match'
    type_ = '_markupbase'
    init_inputs = [
        NodeInputBP(label='string'),
        NodeInputBP(label='pos', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='endpos', dtype=dtypes.Data(default=9223372036854775807, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _markupbase._declname_match(self.input(0), self.input(1), self.input(2)))
        

class _Declstringlit_Match_Node(NodeBase):
    """
    Matches zero or more characters at the beginning of the string."""
    
    title = '_declstringlit_match'
    type_ = '_markupbase'
    init_inputs = [
        NodeInputBP(label='string'),
        NodeInputBP(label='pos', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='endpos', dtype=dtypes.Data(default=9223372036854775807, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _markupbase._declstringlit_match(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _Declname_Match_Node,
    _Declstringlit_Match_Node,
)
