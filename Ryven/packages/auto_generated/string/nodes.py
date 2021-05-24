
from NENV import *

import string


class NodeBase(Node):
    pass


class Capwords_Node(NodeBase):
    """
    capwords(s [,sep]) -> string

    Split the argument into words using split, capitalize each
    word using capitalize, and join the capitalized words using
    join.  If the optional second argument sep is absent or None,
    runs of whitespace characters are replaced by a single space
    and leading and trailing whitespace are removed, otherwise
    sep is used to split and join the words.

    """
    
    title = 'capwords'
    type_ = 'string'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='sep', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, string.capwords(self.input(0), self.input(1)))
        


export_nodes(
    Capwords_Node,
)
