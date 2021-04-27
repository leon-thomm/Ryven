
from NENV import *

import tracemalloc


class NodeBase(Node):
    pass


class _Compare_Grouped_Stats_Node(NodeBase):
    title = '_compare_grouped_stats'
    type_ = 'tracemalloc'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='old_group'),
        NodeInputBP(label='new_group'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc._compare_grouped_stats(self.input(0), self.input(1)))
        

class _Format_Size_Node(NodeBase):
    title = '_format_size'
    type_ = 'tracemalloc'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='size'),
        NodeInputBP(label='sign'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc._format_size(self.input(0), self.input(1)))
        

class _Get_Object_Traceback_Node(NodeBase):
    title = '_get_object_traceback'
    type_ = 'tracemalloc'
    doc = """Get the traceback where the Python object obj was allocated.

Return a tuple of (filename: str, lineno: int) tuples.
Return None if the tracemalloc module is disabled or did not
trace the allocation of the object."""
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc._get_object_traceback(self.input(0)))
        

class _Get_Traces_Node(NodeBase):
    title = '_get_traces'
    type_ = 'tracemalloc'
    doc = """Get traces of all memory blocks allocated by Python.

Return a list of (size: int, traceback: tuple) tuples.
traceback is a tuple of (filename: str, lineno: int) tuples.

Return an empty list if the tracemalloc module is disabled."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc._get_traces())
        

class _Normalize_Filename_Node(NodeBase):
    title = '_normalize_filename'
    type_ = 'tracemalloc'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc._normalize_filename(self.input(0)))
        

class Clear_Traces_Node(NodeBase):
    title = 'clear_traces'
    type_ = 'tracemalloc'
    doc = """Clear traces of memory blocks allocated by Python."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc.clear_traces())
        

class Get_Object_Traceback_Node(NodeBase):
    title = 'get_object_traceback'
    type_ = 'tracemalloc'
    doc = """
    Get the traceback where the Python object *obj* was allocated.
    Return a Traceback instance.

    Return None if the tracemalloc module is not tracing memory allocations or
    did not trace the allocation of the object.
    """
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc.get_object_traceback(self.input(0)))
        

class Get_Traceback_Limit_Node(NodeBase):
    title = 'get_traceback_limit'
    type_ = 'tracemalloc'
    doc = """Get the maximum number of frames stored in the traceback of a trace.

By default, a trace of an allocated memory block only stores
the most recent frame: the limit is 1."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc.get_traceback_limit())
        

class Get_Traced_Memory_Node(NodeBase):
    title = 'get_traced_memory'
    type_ = 'tracemalloc'
    doc = """Get the current size and peak size of memory blocks traced by tracemalloc.

Returns a tuple: (current: int, peak: int)."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc.get_traced_memory())
        

class Get_Tracemalloc_Memory_Node(NodeBase):
    title = 'get_tracemalloc_memory'
    type_ = 'tracemalloc'
    doc = """Get the memory usage in bytes of the tracemalloc module.

This memory is used internally to trace memory allocations."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc.get_tracemalloc_memory())
        

class Is_Tracing_Node(NodeBase):
    title = 'is_tracing'
    type_ = 'tracemalloc'
    doc = """Return True if the tracemalloc module is tracing Python memory allocations."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc.is_tracing())
        

class Start_Node(NodeBase):
    title = 'start'
    type_ = 'tracemalloc'
    doc = """Start tracing Python memory allocations.

Also set the maximum number of frames stored in the traceback of a
trace to nframe."""
    init_inputs = [
        NodeInputBP(label='nframe', dtype=dtypes.Data(default=1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc.start(self.input(0)))
        

class Stop_Node(NodeBase):
    title = 'stop'
    type_ = 'tracemalloc'
    doc = """Stop tracing Python memory allocations.

Also clear traces of memory blocks allocated by Python."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc.stop())
        

class Take_Snapshot_Node(NodeBase):
    title = 'take_snapshot'
    type_ = 'tracemalloc'
    doc = """
    Take a snapshot of traces of memory blocks allocated by Python.
    """
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc.take_snapshot())
        

class Total_Ordering_Node(NodeBase):
    title = 'total_ordering'
    type_ = 'tracemalloc'
    doc = """Class decorator that fills in missing ordering methods"""
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, tracemalloc.total_ordering(self.input(0)))
        


export_nodes(
    _Compare_Grouped_Stats_Node,
    _Format_Size_Node,
    _Get_Object_Traceback_Node,
    _Get_Traces_Node,
    _Normalize_Filename_Node,
    Clear_Traces_Node,
    Get_Object_Traceback_Node,
    Get_Traceback_Limit_Node,
    Get_Traced_Memory_Node,
    Get_Tracemalloc_Memory_Node,
    Is_Tracing_Node,
    Start_Node,
    Stop_Node,
    Take_Snapshot_Node,
    Total_Ordering_Node,
)
