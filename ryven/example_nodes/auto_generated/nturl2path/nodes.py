
from ryven.NENV import *

import nturl2path


class NodeBase(Node):
    pass


class Pathname2Url_Node(NodeBase):
    """
    OS-specific conversion from a file system path to a relative URL
    of the 'file' scheme; not recommended for general use."""
    
    title = 'pathname2url'
    type_ = 'nturl2path'
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, nturl2path.pathname2url(self.input(0)))
        

class Url2Pathname_Node(NodeBase):
    """
    OS-specific conversion from a relative URL of the 'file' scheme
    to a file system path; not recommended for general use."""
    
    title = 'url2pathname'
    type_ = 'nturl2path'
    init_inputs = [
        NodeInputBP(label='url'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, nturl2path.url2pathname(self.input(0)))
        


export_nodes(
    Pathname2Url_Node,
    Url2Pathname_Node,
)
