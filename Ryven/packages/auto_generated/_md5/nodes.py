
from NENV import *

import _md5


class NodeBase(Node):
    pass


class AutoNode__md5_md5(NodeBase):
    title = 'md5'
    type_ = '_md5'
    doc = """Return a new MD5 hash object; optionally initialized with a string."""
    init_inputs = [
        NodeInputBP(label='string'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _md5.md5(self.input(0)))
        


export_nodes(
    AutoNode__md5_md5,
)
