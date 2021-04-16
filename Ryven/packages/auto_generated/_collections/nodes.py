import ryvencore_qt as rc
import _collections


class AutoNode__collections__count_elements(rc.Node):
    title = '_count_elements'
    type_ = '_collections'
    doc = '''Count elements in the iterable, updating the mapping'''
    init_inputs = [
        rc.NodeInputBP(label='mapping'),
rc.NodeInputBP(label='iterable'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _collections._count_elements(self.input(0), self.input(1)))
        