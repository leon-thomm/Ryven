
from ryven.NENV import *

import enum


class NodeBase(Node):
    pass


class _Decompose_Node(NodeBase):
    """
    
    Extract all members from the value.
    """
    
    title = '_decompose'
    type_ = 'enum'
    init_inputs = [
        NodeInputBP(label='flag'),
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, enum._decompose(self.input(0), self.input(1)))
        

class _High_Bit_Node(NodeBase):
    """
    
    returns index of highest bit, or -1 if value is zero or negative
    """
    
    title = '_high_bit'
    type_ = 'enum'
    init_inputs = [
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, enum._high_bit(self.input(0)))
        

class _Is_Descriptor_Node(NodeBase):
    """
    
    Returns True if obj is a descriptor, False otherwise.
    """
    
    title = '_is_descriptor'
    type_ = 'enum'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, enum._is_descriptor(self.input(0)))
        

class _Is_Dunder_Node(NodeBase):
    """
    
    Returns True if a __dunder__ name, False otherwise.
    """
    
    title = '_is_dunder'
    type_ = 'enum'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, enum._is_dunder(self.input(0)))
        

class _Is_Private_Node(NodeBase):
    """
    """
    
    title = '_is_private'
    type_ = 'enum'
    init_inputs = [
        NodeInputBP(label='cls_name'),
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, enum._is_private(self.input(0), self.input(1)))
        

class _Is_Sunder_Node(NodeBase):
    """
    
    Returns True if a _sunder_ name, False otherwise.
    """
    
    title = '_is_sunder'
    type_ = 'enum'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, enum._is_sunder(self.input(0)))
        

class _Make_Class_Unpicklable_Node(NodeBase):
    """
    
    Make the given class un-picklable.
    """
    
    title = '_make_class_unpicklable'
    type_ = 'enum'
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, enum._make_class_unpicklable(self.input(0)))
        

class _Reduce_Ex_By_Name_Node(NodeBase):
    """
    """
    
    title = '_reduce_ex_by_name'
    type_ = 'enum'
    init_inputs = [
        NodeInputBP(label='proto'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, enum._reduce_ex_by_name(self.input(0)))
        

class Unique_Node(NodeBase):
    """
    
    Class decorator for enumerations ensuring unique member values.
    """
    
    title = 'unique'
    type_ = 'enum'
    init_inputs = [
        NodeInputBP(label='enumeration'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, enum.unique(self.input(0)))
        


export_nodes(
    _Decompose_Node,
    _High_Bit_Node,
    _Is_Descriptor_Node,
    _Is_Dunder_Node,
    _Is_Private_Node,
    _Is_Sunder_Node,
    _Make_Class_Unpicklable_Node,
    _Reduce_Ex_By_Name_Node,
    Unique_Node,
)
