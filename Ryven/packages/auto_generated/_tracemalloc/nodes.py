
from NENV import *

import _tracemalloc


class NodeBase(Node):
    pass


class AutoNode__tracemalloc__get_object_traceback(NodeBase):
    title = '_get_object_traceback'
    type_ = '_tracemalloc'
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
        self.set_output_val(0, _tracemalloc._get_object_traceback(self.input(0)))
        

class AutoNode__tracemalloc__get_traces(NodeBase):
    title = '_get_traces'
    type_ = '_tracemalloc'
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
        self.set_output_val(0, _tracemalloc._get_traces())
        

class AutoNode__tracemalloc_clear_traces(NodeBase):
    title = 'clear_traces'
    type_ = '_tracemalloc'
    doc = """Clear traces of memory blocks allocated by Python."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _tracemalloc.clear_traces())
        

class AutoNode__tracemalloc_get_traceback_limit(NodeBase):
    title = 'get_traceback_limit'
    type_ = '_tracemalloc'
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
        self.set_output_val(0, _tracemalloc.get_traceback_limit())
        

class AutoNode__tracemalloc_get_traced_memory(NodeBase):
    title = 'get_traced_memory'
    type_ = '_tracemalloc'
    doc = """Get the current size and peak size of memory blocks traced by tracemalloc.

Returns a tuple: (current: int, peak: int)."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _tracemalloc.get_traced_memory())
        

class AutoNode__tracemalloc_get_tracemalloc_memory(NodeBase):
    title = 'get_tracemalloc_memory'
    type_ = '_tracemalloc'
    doc = """Get the memory usage in bytes of the tracemalloc module.

This memory is used internally to trace memory allocations."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _tracemalloc.get_tracemalloc_memory())
        

class AutoNode__tracemalloc_is_tracing(NodeBase):
    title = 'is_tracing'
    type_ = '_tracemalloc'
    doc = """Return True if the tracemalloc module is tracing Python memory allocations."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _tracemalloc.is_tracing())
        

class AutoNode__tracemalloc_start(NodeBase):
    title = 'start'
    type_ = '_tracemalloc'
    doc = """Start tracing Python memory allocations.

Also set the maximum number of frames stored in the traceback of a
trace to nframe."""
    init_inputs = [
        NodeInputBP(label='nframe'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _tracemalloc.start(self.input(0)))
        

class AutoNode__tracemalloc_stop(NodeBase):
    title = 'stop'
    type_ = '_tracemalloc'
    doc = """Stop tracing Python memory allocations.

Also clear traces of memory blocks allocated by Python."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _tracemalloc.stop())
        


export_nodes(
    AutoNode__tracemalloc__get_object_traceback,
    AutoNode__tracemalloc__get_traces,
    AutoNode__tracemalloc_clear_traces,
    AutoNode__tracemalloc_get_traceback_limit,
    AutoNode__tracemalloc_get_traced_memory,
    AutoNode__tracemalloc_get_tracemalloc_memory,
    AutoNode__tracemalloc_is_tracing,
    AutoNode__tracemalloc_start,
    AutoNode__tracemalloc_stop,
)
