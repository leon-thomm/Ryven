import ryvencore_qt as rc
import asynchat


class AutoNode_asynchat_find_prefix_at_end(rc.Node):
    title = 'find_prefix_at_end'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='haystack'),
rc.NodeInputBP(label='needle'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asynchat.find_prefix_at_end(self.input(0), self.input(1)))
        