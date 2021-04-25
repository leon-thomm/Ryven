
from NENV import *

import _warnings


class NodeBase(Node):
    pass


class AutoNode__warnings_warn(NodeBase):
    title = 'warn'
    type_ = '_warnings'
    doc = """Issue a warning, or maybe ignore it or raise an exception."""
    init_inputs = [
        NodeInputBP(label='message'),
        NodeInputBP(label='category'),
        NodeInputBP(label='stacklevel'),
        NodeInputBP(label='source'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _warnings.warn(self.input(0), self.input(1), self.input(2), self.input(3)))
        


export_nodes(
    AutoNode__warnings_warn,
)
