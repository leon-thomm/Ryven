
from NENV import *

import _abc


class NodeBase(Node):
    pass


class AutoNode__abc__abc_init(NodeBase):
    title = '_abc_init'
    type_ = '_abc'
    doc = """Internal ABC helper for class set-up. Should be never used outside abc module."""
    init_inputs = [
        NodeInputBP(label='self'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _abc._abc_init(self.input(0)))
        

class AutoNode__abc__abc_instancecheck(NodeBase):
    title = '_abc_instancecheck'
    type_ = '_abc'
    doc = """Internal ABC helper for instance checks. Should be never used outside abc module."""
    init_inputs = [
        NodeInputBP(label='self'),
        NodeInputBP(label='instance'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _abc._abc_instancecheck(self.input(0), self.input(1)))
        

class AutoNode__abc__abc_register(NodeBase):
    title = '_abc_register'
    type_ = '_abc'
    doc = """Internal ABC helper for subclasss registration. Should be never used outside abc module."""
    init_inputs = [
        NodeInputBP(label='self'),
        NodeInputBP(label='subclass'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _abc._abc_register(self.input(0), self.input(1)))
        

class AutoNode__abc__abc_subclasscheck(NodeBase):
    title = '_abc_subclasscheck'
    type_ = '_abc'
    doc = """Internal ABC helper for subclasss checks. Should be never used outside abc module."""
    init_inputs = [
        NodeInputBP(label='self'),
        NodeInputBP(label='subclass'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _abc._abc_subclasscheck(self.input(0), self.input(1)))
        

class AutoNode__abc__get_dump(NodeBase):
    title = '_get_dump'
    type_ = '_abc'
    doc = """Internal ABC helper for cache and registry debugging.

Return shallow copies of registry, of both caches, and
negative cache version. Don't call this function directly,
instead use ABC._dump_registry() for a nice repr."""
    init_inputs = [
        NodeInputBP(label='self'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _abc._get_dump(self.input(0)))
        

class AutoNode__abc__reset_caches(NodeBase):
    title = '_reset_caches'
    type_ = '_abc'
    doc = """Internal ABC helper to reset both caches of a given class.

Should be only used by refleak.py"""
    init_inputs = [
        NodeInputBP(label='self'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _abc._reset_caches(self.input(0)))
        

class AutoNode__abc__reset_registry(NodeBase):
    title = '_reset_registry'
    type_ = '_abc'
    doc = """Internal ABC helper to reset registry of a given class.

Should be only used by refleak.py"""
    init_inputs = [
        NodeInputBP(label='self'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _abc._reset_registry(self.input(0)))
        

class AutoNode__abc_get_cache_token(NodeBase):
    title = 'get_cache_token'
    type_ = '_abc'
    doc = """Returns the current ABC cache token.

The token is an opaque object (supporting equality testing) identifying the
current version of the ABC cache for virtual subclasses. The token changes
with every call to register() on any ABC."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _abc.get_cache_token())
        


export_nodes(
    AutoNode__abc__abc_init,
    AutoNode__abc__abc_instancecheck,
    AutoNode__abc__abc_register,
    AutoNode__abc__abc_subclasscheck,
    AutoNode__abc__get_dump,
    AutoNode__abc__reset_caches,
    AutoNode__abc__reset_registry,
    AutoNode__abc_get_cache_token,
)
