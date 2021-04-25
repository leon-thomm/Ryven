
from NENV import *

import itertools


class NodeBase(Node):
    pass


class AutoNode_itertools_tee(NodeBase):
    title = 'tee'
    type_ = 'itertools'
    doc = """Returns a tuple of n independent iterators."""
    init_inputs = [
        NodeInputBP(label='iterable'),
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, itertools.tee(self.input(0), self.input(1)))
        


export_nodes(
    AutoNode_itertools_tee,
)
