
from ryven.NENV import *

import copy


class NodeBase(Node):
    pass


class _Copy_Immutable_Node(NodeBase):
    """
    """
    
    title = '_copy_immutable'
    type_ = 'copy'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copy._copy_immutable(self.input(0)))
        

class _Deepcopy_Atomic_Node(NodeBase):
    """
    """
    
    title = '_deepcopy_atomic'
    type_ = 'copy'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='memo'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copy._deepcopy_atomic(self.input(0), self.input(1)))
        

class _Deepcopy_Dict_Node(NodeBase):
    """
    """
    
    title = '_deepcopy_dict'
    type_ = 'copy'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='memo'),
        NodeInputBP(label='deepcopy', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copy._deepcopy_dict(self.input(0), self.input(1), self.input(2)))
        

class _Deepcopy_List_Node(NodeBase):
    """
    """
    
    title = '_deepcopy_list'
    type_ = 'copy'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='memo'),
        NodeInputBP(label='deepcopy', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copy._deepcopy_list(self.input(0), self.input(1), self.input(2)))
        

class _Deepcopy_Method_Node(NodeBase):
    """
    """
    
    title = '_deepcopy_method'
    type_ = 'copy'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='memo'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copy._deepcopy_method(self.input(0), self.input(1)))
        

class _Deepcopy_Tuple_Node(NodeBase):
    """
    """
    
    title = '_deepcopy_tuple'
    type_ = 'copy'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='memo'),
        NodeInputBP(label='deepcopy', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copy._deepcopy_tuple(self.input(0), self.input(1), self.input(2)))
        

class _Keep_Alive_Node(NodeBase):
    """
    Keeps a reference to the object x in the memo.

    Because we remember objects by their id, we have
    to assure that possibly temporary objects are kept
    alive by referencing them.
    We store a reference at the id of the memo, which should
    normally not be used unless someone tries to deepcopy
    the memo itself...
    """
    
    title = '_keep_alive'
    type_ = 'copy'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='memo'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copy._keep_alive(self.input(0), self.input(1)))
        

class _Reconstruct_Node(NodeBase):
    """
    """
    
    title = '_reconstruct'
    type_ = 'copy'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='memo'),
        NodeInputBP(label='func'),
        NodeInputBP(label='args'),
        NodeInputBP(label='state', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='listiter', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='dictiter', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='deepcopy', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copy._reconstruct(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        

class Copy_Node(NodeBase):
    """
    Shallow copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.
    """
    
    title = 'copy'
    type_ = 'copy'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copy.copy(self.input(0)))
        

class Deepcopy_Node(NodeBase):
    """
    Deep copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.
    """
    
    title = 'deepcopy'
    type_ = 'copy'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='memo', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copy.deepcopy(self.input(0), self.input(1)))
        


export_nodes(
    _Copy_Immutable_Node,
    _Deepcopy_Atomic_Node,
    _Deepcopy_Dict_Node,
    _Deepcopy_List_Node,
    _Deepcopy_Method_Node,
    _Deepcopy_Tuple_Node,
    _Keep_Alive_Node,
    _Reconstruct_Node,
    Copy_Node,
    Deepcopy_Node,
)
