
from NENV import *

import _weakref


class NodeBase(Node):
    pass


class AutoNode__weakref__remove_dead_weakref(NodeBase):
    title = '_remove_dead_weakref'
    type_ = '_weakref'
    doc = """Atomically remove key from dict if it points to a dead weakref."""
    init_inputs = [
        NodeInputBP(label='dct'),
        NodeInputBP(label='key'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _weakref._remove_dead_weakref(self.input(0), self.input(1)))
        

class AutoNode__weakref_getweakrefcount(NodeBase):
    title = 'getweakrefcount'
    type_ = '_weakref'
    doc = """Return the number of weak references to 'object'."""
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _weakref.getweakrefcount(self.input(0)))
        


export_nodes(
    AutoNode__weakref__remove_dead_weakref,
    AutoNode__weakref_getweakrefcount,
)
