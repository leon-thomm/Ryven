
from NENV import *

import signal


class NodeBase(Node):
    pass


class _Enum_To_Int_Node(NodeBase):
    title = '_enum_to_int'
    type_ = 'signal'
    doc = """Convert an IntEnum member to a numeric value.
    If it's not an IntEnum member return the value itself.
    """
    init_inputs = [
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, signal._enum_to_int(self.input(0)))
        

class _Int_To_Enum_Node(NodeBase):
    title = '_int_to_enum'
    type_ = 'signal'
    doc = """Convert a numeric value to an IntEnum member.
    If it's not a known member, return the numeric value itself.
    """
    init_inputs = [
        NodeInputBP(label='value'),
        NodeInputBP(label='enum_klass'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, signal._int_to_enum(self.input(0), self.input(1)))
        

class Getsignal_Node(NodeBase):
    title = 'getsignal'
    type_ = 'signal'
    doc = """Return the current action for the given signal.

The return value can be:
  SIG_IGN -- if the signal is being ignored
  SIG_DFL -- if the default action for the signal is in effect
  None    -- if an unknown handler is in effect
  anything else -- the callable Python object used as a handler"""
    init_inputs = [
        NodeInputBP(label='signalnum'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, signal.getsignal(self.input(0)))
        

class Raise_Signal_Node(NodeBase):
    title = 'raise_signal'
    type_ = 'signal'
    doc = """Send a signal to the executing process."""
    init_inputs = [
        NodeInputBP(label='signalnum'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, signal.raise_signal(self.input(0)))
        

class Signal_Node(NodeBase):
    title = 'signal'
    type_ = 'signal'
    doc = """Set the action for the given signal.

The action can be SIG_DFL, SIG_IGN, or a callable Python object.
The previous action is returned.  See getsignal() for possible return values.

*** IMPORTANT NOTICE ***
A signal handler function is called with two arguments:
the first is the signal number, the second is the interrupted stack frame."""
    init_inputs = [
        NodeInputBP(label='signalnum'),
        NodeInputBP(label='handler'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, signal.signal(self.input(0), self.input(1)))
        

class Strsignal_Node(NodeBase):
    title = 'strsignal'
    type_ = 'signal'
    doc = """Return the system description of the given signal.

The return values can be such as "Interrupt", "Segmentation fault", etc.
Returns None if the signal is not recognized."""
    init_inputs = [
        NodeInputBP(label='signalnum'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, signal.strsignal(self.input(0)))
        

class Valid_Signals_Node(NodeBase):
    title = 'valid_signals'
    type_ = 'signal'
    doc = """Return a set of valid signal numbers on this platform.

The signal numbers returned by this function can be safely passed to
functions like `pthread_sigmask`."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, signal.valid_signals())
        


export_nodes(
    _Enum_To_Int_Node,
    _Int_To_Enum_Node,
    Getsignal_Node,
    Raise_Signal_Node,
    Signal_Node,
    Strsignal_Node,
    Valid_Signals_Node,
)
