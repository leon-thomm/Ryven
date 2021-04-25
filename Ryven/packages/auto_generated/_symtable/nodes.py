
from NENV import *

import _symtable


class NodeBase(Node):
    pass


class AutoNode__symtable_symtable(NodeBase):
    title = 'symtable'
    type_ = '_symtable'
    doc = """Return symbol and scope dictionaries used internally by compiler."""
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='filename'),
        NodeInputBP(label='startstr'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _symtable.symtable(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    AutoNode__symtable_symtable,
)
