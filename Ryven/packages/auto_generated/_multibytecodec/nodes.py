
from NENV import *

import _multibytecodec


class NodeBase(Node):
    pass


class AutoNode__multibytecodec___create_codec(NodeBase):
    title = '__create_codec'
    type_ = '_multibytecodec'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='arg'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _multibytecodec.__create_codec(self.input(0)))
        


export_nodes(
    AutoNode__multibytecodec___create_codec,
)
