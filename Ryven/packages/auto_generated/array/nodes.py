import ryvencore_qt as rc
import array


class AutoNode_array__array_reconstructor(rc.Node):
    title = '_array_reconstructor'
    type_ = 'array'
    description = '''Internal. Used for pickling support.'''
    init_inputs = [
        rc.NodeInputBP(label='arraytype'),
rc.NodeInputBP(label='typecode'),
rc.NodeInputBP(label='mformat_code'),
rc.NodeInputBP(label='items'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, array._array_reconstructor(self.input(0), self.input(1), self.input(2), self.input(3)))
        