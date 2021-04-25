
from NENV import *

import _sha256


class NodeBase(Node):
    pass


class AutoNode__sha256_sha224(NodeBase):
    title = 'sha224'
    type_ = '_sha256'
    doc = """Return a new SHA-224 hash object; optionally initialized with a string."""
    init_inputs = [
        NodeInputBP(label='string'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sha256.sha224(self.input(0)))
        

class AutoNode__sha256_sha256(NodeBase):
    title = 'sha256'
    type_ = '_sha256'
    doc = """Return a new SHA-256 hash object; optionally initialized with a string."""
    init_inputs = [
        NodeInputBP(label='string'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sha256.sha256(self.input(0)))
        


export_nodes(
    AutoNode__sha256_sha224,
    AutoNode__sha256_sha256,
)
