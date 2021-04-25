
from NENV import *

import array


class NodeBase(Node):
    pass


class AutoNode_array__array_reconstructor(NodeBase):
    title = '_array_reconstructor'
    type_ = 'array'
    doc = """Internal. Used for pickling support."""
    init_inputs = [
        NodeInputBP(label='arraytype'),
        NodeInputBP(label='typecode'),
        NodeInputBP(label='mformat_code'),
        NodeInputBP(label='items'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, array._array_reconstructor(self.input(0), self.input(1), self.input(2), self.input(3)))
        


export_nodes(
    AutoNode_array__array_reconstructor,
)
