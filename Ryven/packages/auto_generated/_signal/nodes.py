import ryvencore_qt as rc
import _signal


class AutoNode__signal_getsignal(rc.Node):
    title = 'getsignal'
    type_ = '_signal'
    description = '''Return the current action for the given signal.

The return value can be:
  SIG_IGN -- if the signal is being ignored
  SIG_DFL -- if the default action for the signal is in effect
  None    -- if an unknown handler is in effect
  anything else -- the callable Python object used as a handler'''
    init_inputs = [
        rc.NodeInputBP(label='signalnum'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _signal.getsignal(self.input(0)))
        


class AutoNode__signal_raise_signal(rc.Node):
    title = 'raise_signal'
    type_ = '_signal'
    description = '''Send a signal to the executing process.'''
    init_inputs = [
        rc.NodeInputBP(label='signalnum'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _signal.raise_signal(self.input(0)))
        


class AutoNode__signal_signal(rc.Node):
    title = 'signal'
    type_ = '_signal'
    description = '''Set the action for the given signal.

The action can be SIG_DFL, SIG_IGN, or a callable Python object.
The previous action is returned.  See getsignal() for possible return values.

*** IMPORTANT NOTICE ***
A signal handler function is called with two arguments:
the first is the signal number, the second is the interrupted stack frame.'''
    init_inputs = [
        rc.NodeInputBP(label='signalnum'),
rc.NodeInputBP(label='handler'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _signal.signal(self.input(0), self.input(1)))
        


class AutoNode__signal_strsignal(rc.Node):
    title = 'strsignal'
    type_ = '_signal'
    description = '''Return the system description of the given signal.

The return values can be such as "Interrupt", "Segmentation fault", etc.
Returns None if the signal is not recognized.'''
    init_inputs = [
        rc.NodeInputBP(label='signalnum'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _signal.strsignal(self.input(0)))
        


class AutoNode__signal_valid_signals(rc.Node):
    title = 'valid_signals'
    type_ = '_signal'
    description = '''Return a set of valid signal numbers on this platform.

The signal numbers returned by this function can be safely passed to
functions like `pthread_sigmask`.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _signal.valid_signals())
        