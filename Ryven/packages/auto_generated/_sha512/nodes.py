
from NENV import *

import _sha512


class NodeBase(Node):
    pass


class AutoNode__sha512_sha384(NodeBase):
    title = 'sha384'
    type_ = '_sha512'
    doc = """Return a new SHA-384 hash object; optionally initialized with a string."""
    init_inputs = [
        NodeInputBP(label='string'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sha512.sha384(self.input(0)))
        

class AutoNode__sha512_sha512(NodeBase):
    title = 'sha512'
    type_ = '_sha512'
    doc = """Return a new SHA-512 hash object; optionally initialized with a string."""
    init_inputs = [
        NodeInputBP(label='string'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sha512.sha512(self.input(0)))
        


export_nodes(
    AutoNode__sha512_sha384,
    AutoNode__sha512_sha512,
)
