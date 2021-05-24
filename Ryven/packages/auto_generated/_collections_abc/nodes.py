
from NENV import *

import _collections_abc


class NodeBase(Node):
    pass


class _Check_Methods_Node(NodeBase):
    """
    """
    
    title = '_check_methods'
    type_ = '_collections_abc'
    init_inputs = [
        NodeInputBP(label='C'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _collections_abc._check_methods(self.input(0)))
        

class _Type_Repr_Node(NodeBase):
    """
    Return the repr() of an object, special-casing types (internal helper).

    Copied from :mod:`typing` since collections.abc
    shouldn't depend on that module.
    """
    
    title = '_type_repr'
    type_ = '_collections_abc'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _collections_abc._type_repr(self.input(0)))
        

class Abstractmethod_Node(NodeBase):
    """
    A decorator indicating abstract methods.

    Requires that the metaclass is ABCMeta or derived from it.  A
    class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods are overridden.
    The abstract methods can be called using any of the normal
    'super' call mechanisms.  abstractmethod() may be used to declare
    abstract methods for properties and descriptors.

    Usage:

        class C(metaclass=ABCMeta):
            @abstractmethod
            def my_abstract_method(self, ...):
                ...
    """
    
    title = 'abstractmethod'
    type_ = '_collections_abc'
    init_inputs = [
        NodeInputBP(label='funcobj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _collections_abc.abstractmethod(self.input(0)))
        


export_nodes(
    _Check_Methods_Node,
    _Type_Repr_Node,
    Abstractmethod_Node,
)
