
from NENV import *

import bdb


class NodeBase(Node):
    pass


class Bar_Node(NodeBase):
    """
    """
    
    title = 'bar'
    type_ = 'bdb'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, bdb.bar(self.input(0)))
        

class Checkfuncname_Node(NodeBase):
    """
    Return True if break should happen here.

    Whether a break should happen depends on the way that b (the breakpoint)
    was set.  If it was set via line number, check if b.line is the same as
    the one in the frame.  If it was set via function name, check if this is
    the right function and if it is on the first executable line.
    """
    
    title = 'checkfuncname'
    type_ = 'bdb'
    init_inputs = [
        NodeInputBP(label='b'),
        NodeInputBP(label='frame'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, bdb.checkfuncname(self.input(0), self.input(1)))
        

class Effective_Node(NodeBase):
    """
    Determine which breakpoint for this file:line is to be acted upon.

    Called only if we know there is a breakpoint at this location.  Return
    the breakpoint that was triggered and a boolean that indicates if it is
    ok to delete a temporary breakpoint.  Return (None, None) if there is no
    matching breakpoint.
    """
    
    title = 'effective'
    type_ = 'bdb'
    init_inputs = [
        NodeInputBP(label='file'),
        NodeInputBP(label='line'),
        NodeInputBP(label='frame'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, bdb.effective(self.input(0), self.input(1), self.input(2)))
        

class Foo_Node(NodeBase):
    """
    """
    
    title = 'foo'
    type_ = 'bdb'
    init_inputs = [
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, bdb.foo(self.input(0)))
        

class Set_Trace_Node(NodeBase):
    """
    Start debugging with a Bdb instance from the caller's frame."""
    
    title = 'set_trace'
    type_ = 'bdb'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, bdb.set_trace())
        

class Test_Node(NodeBase):
    """
    """
    
    title = 'test'
    type_ = 'bdb'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, bdb.test())
        


export_nodes(
    Bar_Node,
    Checkfuncname_Node,
    Effective_Node,
    Foo_Node,
    Set_Trace_Node,
    Test_Node,
)
