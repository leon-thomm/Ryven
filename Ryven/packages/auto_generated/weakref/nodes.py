
from NENV import *

import weakref


class NodeBase(Node):
    pass


class _Remove_Dead_Weakref_Node(NodeBase):
    title = '_remove_dead_weakref'
    type_ = 'weakref'
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
        self.set_output_val(0, weakref._remove_dead_weakref(self.input(0), self.input(1)))
        

class Getweakrefcount_Node(NodeBase):
    title = 'getweakrefcount'
    type_ = 'weakref'
    doc = """Return the number of weak references to 'object'."""
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, weakref.getweakrefcount(self.input(0)))
        


export_nodes(
    _Remove_Dead_Weakref_Node,
    Getweakrefcount_Node,
)
