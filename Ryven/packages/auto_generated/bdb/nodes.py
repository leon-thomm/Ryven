import ryvencore_qt as rc
import bdb


class AutoNode_bdb_bar(rc.Node):
    title = 'bar'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, bdb.bar(self.input(0)))
        


class AutoNode_bdb_checkfuncname(rc.Node):
    title = 'checkfuncname'
    description = '''Return True if break should happen here.

    Whether a break should happen depends on the way that b (the breakpoint)
    was set.  If it was set via line number, check if b.line is the same as
    the one in the frame.  If it was set via function name, check if this is
    the right function and if it is on the first executable line.
    '''
    init_inputs = [
        rc.NodeInputBP(label='b'),
rc.NodeInputBP(label='frame'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, bdb.checkfuncname(self.input(0), self.input(1)))
        


class AutoNode_bdb_effective(rc.Node):
    title = 'effective'
    description = '''Determine which breakpoint for this file:line is to be acted upon.

    Called only if we know there is a breakpoint at this location.  Return
    the breakpoint that was triggered and a boolean that indicates if it is
    ok to delete a temporary breakpoint.  Return (None, None) if there is no
    matching breakpoint.
    '''
    init_inputs = [
        rc.NodeInputBP(label='file'),
rc.NodeInputBP(label='line'),
rc.NodeInputBP(label='frame'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, bdb.effective(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_bdb_foo(rc.Node):
    title = 'foo'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='n'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, bdb.foo(self.input(0)))
        


class AutoNode_bdb_set_trace(rc.Node):
    title = 'set_trace'
    description = '''Start debugging with a Bdb instance from the caller's frame.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, bdb.set_trace())
        


class AutoNode_bdb_test(rc.Node):
    title = 'test'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, bdb.test())
        