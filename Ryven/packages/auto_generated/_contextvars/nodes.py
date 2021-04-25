
from NENV import *

import _contextvars


class NodeBase(Node):
    pass


class AutoNode__contextvars_copy_context(NodeBase):
    title = 'copy_context'
    type_ = '_contextvars'
    doc = """"""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _contextvars.copy_context())
        


export_nodes(
    AutoNode__contextvars_copy_context,
)
