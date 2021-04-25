
from NENV import *

import _statistics


class NodeBase(Node):
    pass


class AutoNode__statistics__normal_dist_inv_cdf(NodeBase):
    title = '_normal_dist_inv_cdf'
    type_ = '_statistics'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='p'),
        NodeInputBP(label='mu'),
        NodeInputBP(label='sigma'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _statistics._normal_dist_inv_cdf(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    AutoNode__statistics__normal_dist_inv_cdf,
)
