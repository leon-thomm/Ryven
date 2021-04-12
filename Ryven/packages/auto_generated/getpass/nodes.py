import ryvencore_qt as rc
import getpass


class AutoNode_getpass__raw_input(rc.Node):
    title = '_raw_input'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='prompt'),
rc.NodeInputBP(label='stream'),
rc.NodeInputBP(label='input'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, getpass._raw_input(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_getpass_fallback_getpass(rc.Node):
    title = 'fallback_getpass'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='prompt'),
rc.NodeInputBP(label='stream'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, getpass.fallback_getpass(self.input(0), self.input(1)))
        


class AutoNode_getpass_getpass(rc.Node):
    title = 'getpass'
    description = '''Prompt for password with echo off, using Windows getch().'''
    init_inputs = [
        rc.NodeInputBP(label='prompt'),
rc.NodeInputBP(label='stream'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, getpass.getpass(self.input(0), self.input(1)))
        


class AutoNode_getpass_getuser(rc.Node):
    title = 'getuser'
    description = '''Get the username from the environment or password database.

    First try various environment variables, then the password
    database.  This works on Windows as long as USERNAME is set.

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, getpass.getuser())
        


class AutoNode_getpass_unix_getpass(rc.Node):
    title = 'unix_getpass'
    description = '''Prompt for a password, with echo turned off.

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
    '''
    init_inputs = [
        rc.NodeInputBP(label='prompt'),
rc.NodeInputBP(label='stream'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, getpass.unix_getpass(self.input(0), self.input(1)))
        


class AutoNode_getpass_win_getpass(rc.Node):
    title = 'win_getpass'
    description = '''Prompt for password with echo off, using Windows getch().'''
    init_inputs = [
        rc.NodeInputBP(label='prompt'),
rc.NodeInputBP(label='stream'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, getpass.win_getpass(self.input(0), self.input(1)))
        