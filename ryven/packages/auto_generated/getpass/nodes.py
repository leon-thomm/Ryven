
from NENV import *

import getpass


class NodeBase(Node):
    pass


class _Raw_Input_Node(NodeBase):
    """
    """
    
    title = '_raw_input'
    type_ = 'getpass'
    init_inputs = [
        NodeInputBP(label='prompt', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='stream', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='input', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, getpass._raw_input(self.input(0), self.input(1), self.input(2)))
        

class Fallback_Getpass_Node(NodeBase):
    """
    """
    
    title = 'fallback_getpass'
    type_ = 'getpass'
    init_inputs = [
        NodeInputBP(label='prompt', dtype=dtypes.Data(default='Password: ', size='s')),
        NodeInputBP(label='stream', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, getpass.fallback_getpass(self.input(0), self.input(1)))
        

class Getpass_Node(NodeBase):
    """
    Prompt for password with echo off, using Windows getch()."""
    
    title = 'getpass'
    type_ = 'getpass'
    init_inputs = [
        NodeInputBP(label='prompt', dtype=dtypes.Data(default='Password: ', size='s')),
        NodeInputBP(label='stream', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, getpass.getpass(self.input(0), self.input(1)))
        

class Getuser_Node(NodeBase):
    """
    Get the username from the environment or password database.

    First try various environment variables, then the password
    database.  This works on Windows as long as USERNAME is set.

    """
    
    title = 'getuser'
    type_ = 'getpass'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, getpass.getuser())
        

class Unix_Getpass_Node(NodeBase):
    """
    Prompt for a password, with echo turned off.

    Args:
      prompt: Written on stream to ask for the input.  Default: 'Password: '
      stream: A writable file object to display the prompt.  Defaults to
              the tty.  If no tty is available defaults to sys.stderr.
    Returns:
      The seKr3t input.
    Raises:
      EOFError: If our input tty or stdin was closed.
      GetPassWarning: When we were unable to turn echo off on the input.

    Always restores terminal settings before returning.
    """
    
    title = 'unix_getpass'
    type_ = 'getpass'
    init_inputs = [
        NodeInputBP(label='prompt', dtype=dtypes.Data(default='Password: ', size='s')),
        NodeInputBP(label='stream', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, getpass.unix_getpass(self.input(0), self.input(1)))
        

class Win_Getpass_Node(NodeBase):
    """
    Prompt for password with echo off, using Windows getch()."""
    
    title = 'win_getpass'
    type_ = 'getpass'
    init_inputs = [
        NodeInputBP(label='prompt', dtype=dtypes.Data(default='Password: ', size='s')),
        NodeInputBP(label='stream', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, getpass.win_getpass(self.input(0), self.input(1)))
        


export_nodes(
    _Raw_Input_Node,
    Fallback_Getpass_Node,
    Getpass_Node,
    Getuser_Node,
    Unix_Getpass_Node,
    Win_Getpass_Node,
)
