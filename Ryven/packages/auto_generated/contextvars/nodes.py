
from NENV import *

import contextvars


class NodeBase(Node):
    pass


class Copy_Context_Node(NodeBase):
    """
    """
    
    title = 'copy_context'
    type_ = 'contextvars'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, contextvars.copy_context())
        


export_nodes(
    Copy_Context_Node,
)
