import ryvencore_qt as rc
import _warnings


class AutoNode__warnings_warn(rc.Node):
    title = 'warn'
    type_ = '_warnings'
    description = '''Issue a warning, or maybe ignore it or raise an exception.'''
    init_inputs = [
        rc.NodeInputBP(label='message'),
rc.NodeInputBP(label='category'),
rc.NodeInputBP(label='stacklevel'),
rc.NodeInputBP(label='source'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _warnings.warn(self.input(0), self.input(1), self.input(2), self.input(3)))
        