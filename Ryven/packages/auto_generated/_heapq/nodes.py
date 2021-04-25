
from NENV import *

import _heapq


class NodeBase(Node):
    pass


class AutoNode__heapq__heapify_max(NodeBase):
    title = '_heapify_max'
    type_ = '_heapq'
    doc = """Maxheap variant of heapify."""
    init_inputs = [
        NodeInputBP(label='heap'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq._heapify_max(self.input(0)))
        

class AutoNode__heapq__heappop_max(NodeBase):
    title = '_heappop_max'
    type_ = '_heapq'
    doc = """Maxheap variant of heappop."""
    init_inputs = [
        NodeInputBP(label='heap'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq._heappop_max(self.input(0)))
        

class AutoNode__heapq__heapreplace_max(NodeBase):
    title = '_heapreplace_max'
    type_ = '_heapq'
    doc = """Maxheap variant of heapreplace."""
    init_inputs = [
        NodeInputBP(label='heap'),
        NodeInputBP(label='item'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq._heapreplace_max(self.input(0), self.input(1)))
        

class AutoNode__heapq_heapify(NodeBase):
    title = 'heapify'
    type_ = '_heapq'
    doc = """Transform list into a heap, in-place, in O(len(heap)) time."""
    init_inputs = [
        NodeInputBP(label='heap'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq.heapify(self.input(0)))
        

class AutoNode__heapq_heappop(NodeBase):
    title = 'heappop'
    type_ = '_heapq'
    doc = """Pop the smallest item off the heap, maintaining the heap invariant."""
    init_inputs = [
        NodeInputBP(label='heap'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq.heappop(self.input(0)))
        

class AutoNode__heapq_heappush(NodeBase):
    title = 'heappush'
    type_ = '_heapq'
    doc = """Push item onto heap, maintaining the heap invariant."""
    init_inputs = [
        NodeInputBP(label='heap'),
        NodeInputBP(label='item'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq.heappush(self.input(0), self.input(1)))
        

class AutoNode__heapq_heappushpop(NodeBase):
    title = 'heappushpop'
    type_ = '_heapq'
    doc = """Push item on the heap, then pop and return the smallest item from the heap.

The combined action runs more efficiently than heappush() followed by
a separate call to heappop()."""
    init_inputs = [
        NodeInputBP(label='heap'),
        NodeInputBP(label='item'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq.heappushpop(self.input(0), self.input(1)))
        

class AutoNode__heapq_heapreplace(NodeBase):
    title = 'heapreplace'
    type_ = '_heapq'
    doc = """Pop and return the current smallest value, and add the new item.

This is more efficient than heappop() followed by heappush(), and can be
more appropriate when using a fixed-size heap.  Note that the value
returned may be larger than item!  That constrains reasonable uses of
this routine unless written as part of a conditional replacement:

    if item > heap[0]:
        item = heapreplace(heap, item)"""
    init_inputs = [
        NodeInputBP(label='heap'),
        NodeInputBP(label='item'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq.heapreplace(self.input(0), self.input(1)))
        


export_nodes(
    AutoNode__heapq__heapify_max,
    AutoNode__heapq__heappop_max,
    AutoNode__heapq__heapreplace_max,
    AutoNode__heapq_heapify,
    AutoNode__heapq_heappop,
    AutoNode__heapq_heappush,
    AutoNode__heapq_heappushpop,
    AutoNode__heapq_heapreplace,
)
