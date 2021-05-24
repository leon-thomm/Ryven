
from NENV import *

import abc


class NodeBase(Node):
    pass


class _Abc_Init_Node(NodeBase):
    """
    Internal ABC helper for class set-up. Should be never used outside abc module."""
    
    title = '_abc_init'
    type_ = 'abc'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, abc._abc_init())
        

class _Abc_Instancecheck_Node(NodeBase):
    """
    Internal ABC helper for instance checks. Should be never used outside abc module."""
    
    title = '_abc_instancecheck'
    type_ = 'abc'
    init_inputs = [
        NodeInputBP(label='instance'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, abc._abc_instancecheck(self.input(0)))
        

class _Abc_Register_Node(NodeBase):
    """
    Internal ABC helper for subclasss registration. Should be never used outside abc module."""
    
    title = '_abc_register'
    type_ = 'abc'
    init_inputs = [
        NodeInputBP(label='subclass'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, abc._abc_register(self.input(0)))
        

class _Abc_Subclasscheck_Node(NodeBase):
    """
    Internal ABC helper for subclasss checks. Should be never used outside abc module."""
    
    title = '_abc_subclasscheck'
    type_ = 'abc'
    init_inputs = [
        NodeInputBP(label='subclass'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, abc._abc_subclasscheck(self.input(0)))
        

class _Get_Dump_Node(NodeBase):
    """
    Internal ABC helper for cache and registry debugging.

Return shallow copies of registry, of both caches, and
negative cache version. Don't call this function directly,
instead use ABC._dump_registry() for a nice repr."""
    
    title = '_get_dump'
    type_ = 'abc'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, abc._get_dump())
        

class _Reset_Caches_Node(NodeBase):
    """
    Internal ABC helper to reset both caches of a given class.

Should be only used by refleak.py"""
    
    title = '_reset_caches'
    type_ = 'abc'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, abc._reset_caches())
        

class _Reset_Registry_Node(NodeBase):
    """
    Internal ABC helper to reset registry of a given class.

Should be only used by refleak.py"""
    
    title = '_reset_registry'
    type_ = 'abc'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, abc._reset_registry())
        

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
    type_ = 'abc'
    init_inputs = [
        NodeInputBP(label='funcobj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, abc.abstractmethod(self.input(0)))
        

class Get_Cache_Token_Node(NodeBase):
    """
    Returns the current ABC cache token.

The token is an opaque object (supporting equality testing) identifying the
current version of the ABC cache for virtual subclasses. The token changes
with every call to register() on any ABC."""
    
    title = 'get_cache_token'
    type_ = 'abc'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, abc.get_cache_token())
        


export_nodes(
    _Abc_Init_Node,
    _Abc_Instancecheck_Node,
    _Abc_Register_Node,
    _Abc_Subclasscheck_Node,
    _Get_Dump_Node,
    _Reset_Caches_Node,
    _Reset_Registry_Node,
    Abstractmethod_Node,
    Get_Cache_Token_Node,
)
