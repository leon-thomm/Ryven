
from ryven.NENV import *

import pprint


class NodeBase(Node):
    pass


class _Perfcheck_Node(NodeBase):
    """
    """
    
    title = '_perfcheck'
    type_ = 'pprint'
    init_inputs = [
        NodeInputBP(label='object', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pprint._perfcheck(self.input(0)))
        

class _Recursion_Node(NodeBase):
    """
    """
    
    title = '_recursion'
    type_ = 'pprint'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pprint._recursion(self.input(0)))
        

class _Safe_Repr_Node(NodeBase):
    """
    """
    
    title = '_safe_repr'
    type_ = 'pprint'
    init_inputs = [
        NodeInputBP(label='object'),
        NodeInputBP(label='context'),
        NodeInputBP(label='maxlevels'),
        NodeInputBP(label='level'),
        NodeInputBP(label='sort_dicts'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pprint._safe_repr(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class _Safe_Tuple_Node(NodeBase):
    """
    Helper function for comparing 2-tuples"""
    
    title = '_safe_tuple'
    type_ = 'pprint'
    init_inputs = [
        NodeInputBP(label='t'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pprint._safe_tuple(self.input(0)))
        

class _Wrap_Bytes_Repr_Node(NodeBase):
    """
    """
    
    title = '_wrap_bytes_repr'
    type_ = 'pprint'
    init_inputs = [
        NodeInputBP(label='object'),
        NodeInputBP(label='width'),
        NodeInputBP(label='allowance'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pprint._wrap_bytes_repr(self.input(0), self.input(1), self.input(2)))
        

class Isreadable_Node(NodeBase):
    """
    Determine if saferepr(object) is readable by eval()."""
    
    title = 'isreadable'
    type_ = 'pprint'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pprint.isreadable(self.input(0)))
        

class Isrecursive_Node(NodeBase):
    """
    Determine if object requires a recursive representation."""
    
    title = 'isrecursive'
    type_ = 'pprint'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pprint.isrecursive(self.input(0)))
        

class Pformat_Node(NodeBase):
    """
    Format a Python object into a pretty-printed representation."""
    
    title = 'pformat'
    type_ = 'pprint'
    init_inputs = [
        NodeInputBP(label='object'),
        NodeInputBP(label='indent', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='width', dtype=dtypes.Data(default=80, size='s')),
        NodeInputBP(label='depth', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pprint.pformat(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Pp_Node(NodeBase):
    """
    Pretty-print a Python object"""
    
    title = 'pp'
    type_ = 'pprint'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pprint.pp(self.input(0)))
        

class Pprint_Node(NodeBase):
    """
    Pretty-print a Python object to a stream [default is sys.stdout]."""
    
    title = 'pprint'
    type_ = 'pprint'
    init_inputs = [
        NodeInputBP(label='object'),
        NodeInputBP(label='stream', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='indent', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='width', dtype=dtypes.Data(default=80, size='s')),
        NodeInputBP(label='depth', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pprint.pprint(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Saferepr_Node(NodeBase):
    """
    Version of repr() which can handle recursive data structures."""
    
    title = 'saferepr'
    type_ = 'pprint'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pprint.saferepr(self.input(0)))
        


export_nodes(
    _Perfcheck_Node,
    _Recursion_Node,
    _Safe_Repr_Node,
    _Safe_Tuple_Node,
    _Wrap_Bytes_Repr_Node,
    Isreadable_Node,
    Isrecursive_Node,
    Pformat_Node,
    Pp_Node,
    Pprint_Node,
    Saferepr_Node,
)
