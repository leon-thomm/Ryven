import ryvencore_qt as rc
import formatter


class AutoNode_formatter_test(rc.Node):
    title = 'test'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, formatter.test(self.input(0)))
        