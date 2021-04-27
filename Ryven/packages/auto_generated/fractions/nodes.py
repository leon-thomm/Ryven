
from NENV import *

import fractions


class NodeBase(Node):
    pass


class _Gcd_Node(NodeBase):
    title = '_gcd'
    type_ = 'fractions'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fractions._gcd(self.input(0), self.input(1)))
        

class Gcd_Node(NodeBase):
    title = 'gcd'
    type_ = 'fractions'
    doc = """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fractions.gcd(self.input(0), self.input(1)))
        


export_nodes(
    _Gcd_Node,
    Gcd_Node,
)
