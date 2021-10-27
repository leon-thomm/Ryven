
from NENV import *

import reprlib


class NodeBase(Node):
    pass


class _Possibly_Sorted_Node(NodeBase):
    """
    """
    
    title = '_possibly_sorted'
    type_ = 'reprlib'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, reprlib._possibly_sorted(self.input(0)))
        

class Recursive_Repr_Node(NodeBase):
    """
    Decorator to make a repr function return fillvalue for a recursive call"""
    
    title = 'recursive_repr'
    type_ = 'reprlib'
    init_inputs = [
        NodeInputBP(label='fillvalue', dtype=dtypes.Data(default='...', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, reprlib.recursive_repr(self.input(0)))
        

class Repr_Node(NodeBase):
    """
    """
    
    title = 'repr'
    type_ = 'reprlib'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, reprlib.repr(self.input(0)))
        


export_nodes(
    _Possibly_Sorted_Node,
    Recursive_Repr_Node,
    Repr_Node,
)
