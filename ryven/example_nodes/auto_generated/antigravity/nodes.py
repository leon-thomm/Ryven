
from ryven.NENV import *

import antigravity


class NodeBase(Node):
    pass


class Geohash_Node(NodeBase):
    """
    Compute geohash() using the Munroe algorithm.

    >>> geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
    37.857713 -122.544543

    """
    
    title = 'geohash'
    type_ = 'antigravity'
    init_inputs = [
        NodeInputBP(label='latitude'),
        NodeInputBP(label='longitude'),
        NodeInputBP(label='datedow'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, antigravity.geohash(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    Geohash_Node,
)
