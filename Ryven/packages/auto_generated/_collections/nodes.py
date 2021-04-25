
from NENV import *

import _collections


class NodeBase(Node):
    pass


class AutoNode__collections__count_elements(NodeBase):
    title = '_count_elements'
    type_ = '_collections'
    doc = """Count elements in the iterable, updating the mapping"""
    init_inputs = [
        NodeInputBP(label='mapping'),
        NodeInputBP(label='iterable'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _collections._count_elements(self.input(0), self.input(1)))
        


export_nodes(
    AutoNode__collections__count_elements,
)
