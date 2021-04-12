import ryvencore_qt as rc
import _multibytecodec


class AutoNode__multibytecodec___create_codec(rc.Node):
    title = '__create_codec'
    type_ = '_multibytecodec'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='arg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _multibytecodec.__create_codec(self.input(0)))
        