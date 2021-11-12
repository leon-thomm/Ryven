
from ryven.NENV import *

import codeop


class NodeBase(Node):
    pass


class _Compile_Node(NodeBase):
    """
    """
    
    title = '_compile'
    type_ = 'codeop'
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='filename'),
        NodeInputBP(label='symbol'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codeop._compile(self.input(0), self.input(1), self.input(2)))
        

class _Maybe_Compile_Node(NodeBase):
    """
    """
    
    title = '_maybe_compile'
    type_ = 'codeop'
    init_inputs = [
        NodeInputBP(label='compiler'),
        NodeInputBP(label='source'),
        NodeInputBP(label='filename'),
        NodeInputBP(label='symbol'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codeop._maybe_compile(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Compile_Command_Node(NodeBase):
    """
    Compile a command and determine whether it is incomplete.

    Arguments:

    source -- the source string; may contain \n characters
    filename -- optional filename from which source was read; default
                "<input>"
    symbol -- optional grammar start symbol; "single" (default), "exec"
              or "eval"

    Return value / exceptions raised:

    - Return a code object if the command is complete and valid
    - Return None if the command is incomplete
    - Raise SyntaxError, ValueError or OverflowError if the command is a
      syntax error (OverflowError and ValueError can be produced by
      malformed literals).
    """
    
    title = 'compile_command'
    type_ = 'codeop'
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='filename', dtype=dtypes.Data(default='<input>', size='s')),
        NodeInputBP(label='symbol', dtype=dtypes.Data(default='single', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codeop.compile_command(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _Compile_Node,
    _Maybe_Compile_Node,
    Compile_Command_Node,
)
