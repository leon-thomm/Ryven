
from NENV import *

import pstats


class NodeBase(Node):
    pass


class Add_Callers_Node(NodeBase):
    title = 'add_callers'
    type_ = 'pstats'
    doc = """Combine two caller lists in a single list."""
    init_inputs = [
        NodeInputBP(label='target'),
        NodeInputBP(label='source'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.add_callers(self.input(0), self.input(1)))
        

class Add_Func_Stats_Node(NodeBase):
    title = 'add_func_stats'
    type_ = 'pstats'
    doc = """Add together all the stats for two profile entries."""
    init_inputs = [
        NodeInputBP(label='target'),
        NodeInputBP(label='source'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.add_func_stats(self.input(0), self.input(1)))
        

class Count_Calls_Node(NodeBase):
    title = 'count_calls'
    type_ = 'pstats'
    doc = """Sum the caller statistics to get total number of calls received."""
    init_inputs = [
        NodeInputBP(label='callers'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.count_calls(self.input(0)))
        

class F8_Node(NodeBase):
    title = 'f8'
    type_ = 'pstats'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.f8(self.input(0)))
        

class Func_Get_Function_Name_Node(NodeBase):
    title = 'func_get_function_name'
    type_ = 'pstats'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.func_get_function_name(self.input(0)))
        

class Func_Std_String_Node(NodeBase):
    title = 'func_std_string'
    type_ = 'pstats'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='func_name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.func_std_string(self.input(0)))
        

class Func_Strip_Path_Node(NodeBase):
    title = 'func_strip_path'
    type_ = 'pstats'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='func_name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.func_strip_path(self.input(0)))
        


export_nodes(
    Add_Callers_Node,
    Add_Func_Stats_Node,
    Count_Calls_Node,
    F8_Node,
    Func_Get_Function_Name_Node,
    Func_Std_String_Node,
    Func_Strip_Path_Node,
)
