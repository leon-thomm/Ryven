import ryvencore_qt as rc
import _opcode


class AutoNode__opcode_stack_effect(rc.Node):
    title = 'stack_effect'
    type_ = '_opcode'
    doc = '''Compute the stack effect of the opcode.'''
    init_inputs = [
        rc.NodeInputBP(label='opcode'),
rc.NodeInputBP(label='oparg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _opcode.stack_effect(self.input(0), self.input(1)))
        