
from ryven.NENV import *

import _bootlocale


class NodeBase(Node):
    pass


class Getpreferredencoding_Node(NodeBase):
    """
    """
    
    title = 'getpreferredencoding'
    type_ = '_bootlocale'
    init_inputs = [
        NodeInputBP(label='do_setlocale', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _bootlocale.getpreferredencoding(self.input(0)))
        


export_nodes(
    Getpreferredencoding_Node,
)
