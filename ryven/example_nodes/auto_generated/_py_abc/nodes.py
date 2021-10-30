
from ryven.NENV import *

import _py_abc


class NodeBase(Node):
    pass


class Get_Cache_Token_Node(NodeBase):
    """
    Returns the current ABC cache token.

    The token is an opaque object (supporting equality testing) identifying the
    current version of the ABC cache for virtual subclasses. The token changes
    with every call to ``register()`` on any ABC.
    """
    
    title = 'get_cache_token'
    type_ = '_py_abc'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _py_abc.get_cache_token())
        


export_nodes(
    Get_Cache_Token_Node,
)
