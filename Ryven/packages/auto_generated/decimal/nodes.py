
from NENV import *

import decimal


class NodeBase(Node):
    pass


class Getcontext_Node(NodeBase):
    title = 'getcontext'
    type_ = 'decimal'
    doc = """Get the current default context.

"""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, decimal.getcontext())
        

class Localcontext_Node(NodeBase):
    title = 'localcontext'
    type_ = 'decimal'
    doc = """Return a context manager that will set the default context to a copy of ctx
on entry to the with-statement and restore the previous default context when
exiting the with-statement. If no context is specified, a copy of the current
default context is used.

"""
    init_inputs = [
        NodeInputBP(label='ctx', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, decimal.localcontext(self.input(0)))
        

class Setcontext_Node(NodeBase):
    title = 'setcontext'
    type_ = 'decimal'
    doc = """Set a new default context.

"""
    init_inputs = [
        NodeInputBP(label='context'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, decimal.setcontext(self.input(0)))
        


export_nodes(
    Getcontext_Node,
    Localcontext_Node,
    Setcontext_Node,
)
