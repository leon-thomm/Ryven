
from NENV import *

import _sha1


class NodeBase(Node):
    pass


class AutoNode__sha1_sha1(NodeBase):
    title = 'sha1'
    type_ = '_sha1'
    doc = """Return a new SHA1 hash object; optionally initialized with a string."""
    init_inputs = [
        NodeInputBP(label='string'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sha1.sha1(self.input(0)))
        


export_nodes(
    AutoNode__sha1_sha1,
)
