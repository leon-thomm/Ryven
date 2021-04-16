import ryvencore_qt as rc
import _statistics


class AutoNode__statistics__normal_dist_inv_cdf(rc.Node):
    title = '_normal_dist_inv_cdf'
    type_ = '_statistics'
    doc = ''''''
    init_inputs = [
        rc.NodeInputBP(label='p'),
rc.NodeInputBP(label='mu'),
rc.NodeInputBP(label='sigma'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _statistics._normal_dist_inv_cdf(self.input(0), self.input(1), self.input(2)))
        