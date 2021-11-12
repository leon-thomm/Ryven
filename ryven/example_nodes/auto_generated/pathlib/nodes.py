
from ryven.NENV import *

import pathlib


class NodeBase(Node):
    pass


class _Getfinalpathname_Node(NodeBase):
    """
    A helper function for samepath on windows."""
    
    title = '_getfinalpathname'
    type_ = 'pathlib'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pathlib._getfinalpathname(self.input(0)))
        

class _Ignore_Error_Node(NodeBase):
    """
    """
    
    title = '_ignore_error'
    type_ = 'pathlib'
    init_inputs = [
        NodeInputBP(label='exception'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pathlib._ignore_error(self.input(0)))
        

class _Is_Wildcard_Pattern_Node(NodeBase):
    """
    """
    
    title = '_is_wildcard_pattern'
    type_ = 'pathlib'
    init_inputs = [
        NodeInputBP(label='pat'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pathlib._is_wildcard_pattern(self.input(0)))
        

class Urlquote_From_Bytes_Node(NodeBase):
    """
    Like quote(), but accepts a bytes object rather than a str, and does
    not perform string-to-bytes encoding.  It always returns an ASCII string.
    quote_from_bytes(b'abc def?') -> 'abc%20def%3f'
    """
    
    title = 'urlquote_from_bytes'
    type_ = 'pathlib'
    init_inputs = [
        NodeInputBP(label='bs'),
        NodeInputBP(label='safe', dtype=dtypes.Data(default='/', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pathlib.urlquote_from_bytes(self.input(0), self.input(1)))
        


export_nodes(
    _Getfinalpathname_Node,
    _Ignore_Error_Node,
    _Is_Wildcard_Pattern_Node,
    Urlquote_From_Bytes_Node,
)
