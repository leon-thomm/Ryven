import ryvencore_qt as rc
import _sha1


class AutoNode__sha1_sha1(rc.Node):
    title = 'sha1'
    type_ = '_sha1'
    doc = '''Return a new SHA1 hash object; optionally initialized with a string.'''
    init_inputs = [
        rc.NodeInputBP(label='string'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sha1.sha1(self.input(0)))
        