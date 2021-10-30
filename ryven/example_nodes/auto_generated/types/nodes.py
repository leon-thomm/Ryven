
from ryven.NENV import *

import types


class NodeBase(Node):
    pass


class _Calculate_Meta_Node(NodeBase):
    """
    Calculate the most derived metaclass."""
    
    title = '_calculate_meta'
    type_ = 'types'
    init_inputs = [
        NodeInputBP(label='meta'),
        NodeInputBP(label='bases'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, types._calculate_meta(self.input(0), self.input(1)))
        

class _Cell_Factory_Node(NodeBase):
    """
    """
    
    title = '_cell_factory'
    type_ = 'types'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, types._cell_factory())
        

class Coroutine_Node(NodeBase):
    """
    Convert regular generator function to a coroutine."""
    
    title = 'coroutine'
    type_ = 'types'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, types.coroutine(self.input(0)))
        

class New_Class_Node(NodeBase):
    """
    Create a class object dynamically using the appropriate metaclass."""
    
    title = 'new_class'
    type_ = 'types'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='bases', dtype=dtypes.Data(default=(), size='s')),
        NodeInputBP(label='kwds', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='exec_body', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, types.new_class(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Prepare_Class_Node(NodeBase):
    """
    Call the __prepare__ method of the appropriate metaclass.

    Returns (metaclass, namespace, kwds) as a 3-tuple

    *metaclass* is the appropriate metaclass
    *namespace* is the prepared class namespace
    *kwds* is an updated copy of the passed in kwds argument with any
    'metaclass' entry removed. If no kwds argument is passed in, this will
    be an empty dict.
    """
    
    title = 'prepare_class'
    type_ = 'types'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='bases', dtype=dtypes.Data(default=(), size='s')),
        NodeInputBP(label='kwds', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, types.prepare_class(self.input(0), self.input(1), self.input(2)))
        

class Resolve_Bases_Node(NodeBase):
    """
    Resolve MRO entries dynamically as specified by PEP 560."""
    
    title = 'resolve_bases'
    type_ = 'types'
    init_inputs = [
        NodeInputBP(label='bases'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, types.resolve_bases(self.input(0)))
        


export_nodes(
    _Calculate_Meta_Node,
    _Cell_Factory_Node,
    Coroutine_Node,
    New_Class_Node,
    Prepare_Class_Node,
    Resolve_Bases_Node,
)
