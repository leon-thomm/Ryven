
from NENV import *

import pdb


class NodeBase(Node):
    pass


class Find_Function_Node(NodeBase):
    """
    """
    
    title = 'find_function'
    type_ = 'pdb'
    init_inputs = [
        NodeInputBP(label='funcname'),
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pdb.find_function(self.input(0), self.input(1)))
        

class Getsourcelines_Node(NodeBase):
    """
    """
    
    title = 'getsourcelines'
    type_ = 'pdb'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pdb.getsourcelines(self.input(0)))
        

class Help_Node(NodeBase):
    """
    """
    
    title = 'help'
    type_ = 'pdb'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pdb.help())
        

class Lasti2Lineno_Node(NodeBase):
    """
    """
    
    title = 'lasti2lineno'
    type_ = 'pdb'
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='lasti'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pdb.lasti2lineno(self.input(0), self.input(1)))
        

class Main_Node(NodeBase):
    """
    """
    
    title = 'main'
    type_ = 'pdb'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pdb.main())
        

class Pm_Node(NodeBase):
    """
    """
    
    title = 'pm'
    type_ = 'pdb'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pdb.pm())
        

class Post_Mortem_Node(NodeBase):
    """
    """
    
    title = 'post_mortem'
    type_ = 'pdb'
    init_inputs = [
        NodeInputBP(label='t', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pdb.post_mortem(self.input(0)))
        

class Run_Node(NodeBase):
    """
    """
    
    title = 'run'
    type_ = 'pdb'
    init_inputs = [
        NodeInputBP(label='statement'),
        NodeInputBP(label='globals', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='locals', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pdb.run(self.input(0), self.input(1), self.input(2)))
        

class Runcall_Node(NodeBase):
    """
    """
    
    title = 'runcall'
    type_ = 'pdb'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pdb.runcall())
        

class Runctx_Node(NodeBase):
    """
    """
    
    title = 'runctx'
    type_ = 'pdb'
    init_inputs = [
        NodeInputBP(label='statement'),
        NodeInputBP(label='globals'),
        NodeInputBP(label='locals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pdb.runctx(self.input(0), self.input(1), self.input(2)))
        

class Runeval_Node(NodeBase):
    """
    """
    
    title = 'runeval'
    type_ = 'pdb'
    init_inputs = [
        NodeInputBP(label='expression'),
        NodeInputBP(label='globals', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='locals', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pdb.runeval(self.input(0), self.input(1), self.input(2)))
        

class Set_Trace_Node(NodeBase):
    """
    """
    
    title = 'set_trace'
    type_ = 'pdb'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pdb.set_trace())
        

class Test_Node(NodeBase):
    """
    """
    
    title = 'test'
    type_ = 'pdb'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pdb.test())
        


export_nodes(
    Find_Function_Node,
    Getsourcelines_Node,
    Help_Node,
    Lasti2Lineno_Node,
    Main_Node,
    Pm_Node,
    Post_Mortem_Node,
    Run_Node,
    Runcall_Node,
    Runctx_Node,
    Runeval_Node,
    Set_Trace_Node,
    Test_Node,
)
