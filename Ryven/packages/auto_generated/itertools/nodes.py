import ryvencore_qt as rc
import itertools


class AutoNode_itertools_tee(rc.Node):
    title = 'tee'
    type_ = 'itertools'
    doc = '''Returns a tuple of n independent iterators.'''
    init_inputs = [
        rc.NodeInputBP(label='iterable'),
rc.NodeInputBP(label='n'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, itertools.tee(self.input(0), self.input(1)))
        