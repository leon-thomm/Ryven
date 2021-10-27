
from NENV import *

import shlex


class NodeBase(Node):
    pass


class _Find_Unsafe_Node(NodeBase):
    """
    Scan through string looking for a match, and return a corresponding match object instance.

Return None if no position in the string matches."""
    
    title = '_find_unsafe'
    type_ = 'shlex'
    init_inputs = [
        NodeInputBP(label='string'),
        NodeInputBP(label='pos', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='endpos', dtype=dtypes.Data(default=9223372036854775807, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shlex._find_unsafe(self.input(0), self.input(1), self.input(2)))
        

class _Print_Tokens_Node(NodeBase):
    """
    """
    
    title = '_print_tokens'
    type_ = 'shlex'
    init_inputs = [
        NodeInputBP(label='lexer'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shlex._print_tokens(self.input(0)))
        

class Join_Node(NodeBase):
    """
    Return a shell-escaped string from *split_command*."""
    
    title = 'join'
    type_ = 'shlex'
    init_inputs = [
        NodeInputBP(label='split_command'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shlex.join(self.input(0)))
        

class Quote_Node(NodeBase):
    """
    Return a shell-escaped version of the string *s*."""
    
    title = 'quote'
    type_ = 'shlex'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shlex.quote(self.input(0)))
        

class Split_Node(NodeBase):
    """
    Split the string *s* using shell-like syntax."""
    
    title = 'split'
    type_ = 'shlex'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='comments', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='posix', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shlex.split(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _Find_Unsafe_Node,
    _Print_Tokens_Node,
    Join_Node,
    Quote_Node,
    Split_Node,
)
