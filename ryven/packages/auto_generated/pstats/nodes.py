
from NENV import *

import pstats


class NodeBase(Node):
    pass


class Add_Callers_Node(NodeBase):
    """
    Combine two caller lists in a single list."""
    
    title = 'add_callers'
    type_ = 'pstats'
    init_inputs = [
        NodeInputBP(label='target'),
        NodeInputBP(label='source'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pstats.add_callers(self.input(0), self.input(1)))
        

class Add_Func_Stats_Node(NodeBase):
    """
    Add together all the stats for two profile entries."""
    
    title = 'add_func_stats'
    type_ = 'pstats'
    init_inputs = [
        NodeInputBP(label='target'),
        NodeInputBP(label='source'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pstats.add_func_stats(self.input(0), self.input(1)))
        

class Count_Calls_Node(NodeBase):
    """
    Sum the caller statistics to get total number of calls received."""
    
    title = 'count_calls'
    type_ = 'pstats'
    init_inputs = [
        NodeInputBP(label='callers'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pstats.count_calls(self.input(0)))
        

class Dataclass_Node(NodeBase):
    """
    Returns the same class as was passed in, with dunder methods
    added based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If
    repr is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method function is added. If frozen is true, fields may
    not be assigned to after instance creation.
    """
    
    title = 'dataclass'
    type_ = 'pstats'
    init_inputs = [
        NodeInputBP(label='cls', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pstats.dataclass(self.input(0)))
        

class F8_Node(NodeBase):
    """
    """
    
    title = 'f8'
    type_ = 'pstats'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pstats.f8(self.input(0)))
        

class Func_Get_Function_Name_Node(NodeBase):
    """
    """
    
    title = 'func_get_function_name'
    type_ = 'pstats'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pstats.func_get_function_name(self.input(0)))
        

class Func_Std_String_Node(NodeBase):
    """
    """
    
    title = 'func_std_string'
    type_ = 'pstats'
    init_inputs = [
        NodeInputBP(label='func_name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pstats.func_std_string(self.input(0)))
        

class Func_Strip_Path_Node(NodeBase):
    """
    """
    
    title = 'func_strip_path'
    type_ = 'pstats'
    init_inputs = [
        NodeInputBP(label='func_name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pstats.func_strip_path(self.input(0)))
        


export_nodes(
    Add_Callers_Node,
    Add_Func_Stats_Node,
    Count_Calls_Node,
    Dataclass_Node,
    F8_Node,
    Func_Get_Function_Name_Node,
    Func_Std_String_Node,
    Func_Strip_Path_Node,
)
