import ryvencore_qt as rc
import codeop


class AutoNode_codeop__compile(rc.Node):
    title = '_compile'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='source'),
rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='symbol'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codeop._compile(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codeop__maybe_compile(rc.Node):
    title = '_maybe_compile'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='compiler'),
rc.NodeInputBP(label='source'),
rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='symbol'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codeop._maybe_compile(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_codeop_compile_command(rc.Node):
    title = 'compile_command'
    doc = '''Compile a command and determine whether it is incomplete.

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
    '''
    init_inputs = [
        rc.NodeInputBP(label='source'),
rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='symbol'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codeop.compile_command(self.input(0), self.input(1), self.input(2)))
        