
from NENV import *

import timeit


class NodeBase(Node):
    pass


class _Globals_Node(NodeBase):
    title = '_globals'
    type_ = 'timeit'
    doc = """Return the dictionary containing the current scope's global variables.

NOTE: Updates to this dictionary *will* affect name lookups in the current
global scope and vice-versa."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, timeit._globals())
        

class Main_Node(NodeBase):
    title = 'main'
    type_ = 'timeit'
    doc = """Main program, used when run as a script.

    The optional 'args' argument specifies the command line to be parsed,
    defaulting to sys.argv[1:].

    The return value is an exit code to be passed to sys.exit(); it
    may be None to indicate success.

    When an exception happens during timing, a traceback is printed to
    stderr and the return value is 1.  Exceptions at other times
    (including the template compilation) are not caught.

    '_wrap_timer' is an internal interface used for unit testing.  If it
    is not None, it must be a callable that accepts a timer function
    and returns another timer function (used for unit testing).
    """
    init_inputs = [
        NodeInputBP(label='args', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, timeit.main(self.input(0)))
        

class Reindent_Node(NodeBase):
    title = 'reindent'
    type_ = 'timeit'
    doc = """Helper to reindent a multi-line statement."""
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='indent'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, timeit.reindent(self.input(0), self.input(1)))
        

class Repeat_Node(NodeBase):
    title = 'repeat'
    type_ = 'timeit'
    doc = """Convenience function to create Timer object and call repeat method."""
    init_inputs = [
        NodeInputBP(label='stmt', dtype=dtypes.Data(default='pass', size='s')),
        NodeInputBP(label='setup', dtype=dtypes.Data(default='pass', size='s')),
        NodeInputBP(label='timer', dtype=dtypes.Data(default=<built-in function perf_counter>, size='s')),
        NodeInputBP(label='repeat', dtype=dtypes.Data(default=5, size='s')),
        NodeInputBP(label='number', dtype=dtypes.Data(default=1000000, size='s')),
        NodeInputBP(label='globals', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, timeit.repeat(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class Timeit_Node(NodeBase):
    title = 'timeit'
    type_ = 'timeit'
    doc = """Convenience function to create Timer object and call timeit method."""
    init_inputs = [
        NodeInputBP(label='stmt', dtype=dtypes.Data(default='pass', size='s')),
        NodeInputBP(label='setup', dtype=dtypes.Data(default='pass', size='s')),
        NodeInputBP(label='timer', dtype=dtypes.Data(default=<built-in function perf_counter>, size='s')),
        NodeInputBP(label='number', dtype=dtypes.Data(default=1000000, size='s')),
        NodeInputBP(label='globals', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, timeit.timeit(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


export_nodes(
    _Globals_Node,
    Main_Node,
    Reindent_Node,
    Repeat_Node,
    Timeit_Node,
)
