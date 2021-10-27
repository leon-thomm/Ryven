
from NENV import *

import code


class NodeBase(Node):
    pass


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
    type_ = 'code'
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
        self.set_output_val(0, code.compile_command(self.input(0), self.input(1), self.input(2)))
        

class Interact_Node(NodeBase):
    """
    Closely emulate the interactive Python interpreter.

    This is a backwards compatible interface to the InteractiveConsole
    class.  When readfunc is not specified, it attempts to import the
    readline module to enable GNU readline if it is available.

    Arguments (all optional, all default to None):

    banner -- passed to InteractiveConsole.interact()
    readfunc -- if not None, replaces InteractiveConsole.raw_input()
    local -- passed to InteractiveInterpreter.__init__()
    exitmsg -- passed to InteractiveConsole.interact()

    """
    
    title = 'interact'
    type_ = 'code'
    init_inputs = [
        NodeInputBP(label='banner', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='readfunc', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='local', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='exitmsg', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, code.interact(self.input(0), self.input(1), self.input(2), self.input(3)))
        


export_nodes(
    Compile_Command_Node,
    Interact_Node,
)
