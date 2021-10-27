
from NENV import *

import cProfile


class NodeBase(Node):
    pass


class Label_Node(NodeBase):
    """
    """
    
    title = 'label'
    type_ = 'cProfile'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cProfile.label(self.input(0)))
        

class Main_Node(NodeBase):
    """
    """
    
    title = 'main'
    type_ = 'cProfile'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cProfile.main())
        

class Run_Node(NodeBase):
    """
    Run statement under profiler optionally saving results in filename

    This function takes a single argument that can be passed to the
    "exec" statement, and an optional file name.  In all cases this
    routine attempts to "exec" its first argument and gather profiling
    statistics from the execution. If no file name is present, then this
    function automatically prints a simple profiling report, sorted by the
    standard name string (file/line/function-name) that is presented in
    each line.
    """
    
    title = 'run'
    type_ = 'cProfile'
    init_inputs = [
        NodeInputBP(label='statement'),
        NodeInputBP(label='filename', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='sort', dtype=dtypes.Data(default=-1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cProfile.run(self.input(0), self.input(1), self.input(2)))
        

class Runctx_Node(NodeBase):
    """
    Run statement under profiler, supplying your own globals and locals,
    optionally saving results in filename.

    statement and filename have the same semantics as profile.run
    """
    
    title = 'runctx'
    type_ = 'cProfile'
    init_inputs = [
        NodeInputBP(label='statement'),
        NodeInputBP(label='globals'),
        NodeInputBP(label='locals'),
        NodeInputBP(label='filename', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='sort', dtype=dtypes.Data(default=-1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cProfile.runctx(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


export_nodes(
    Label_Node,
    Main_Node,
    Run_Node,
    Runctx_Node,
)
