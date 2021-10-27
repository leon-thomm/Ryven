
from NENV import *

import heapq


class NodeBase(Node):
    pass


class _Heapify_Max_Node(NodeBase):
    """
    Maxheap variant of heapify."""
    
    title = '_heapify_max'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='heap'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq._heapify_max(self.input(0)))
        

class _Heappop_Max_Node(NodeBase):
    """
    Maxheap variant of heappop."""
    
    title = '_heappop_max'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='heap'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq._heappop_max(self.input(0)))
        

class _Heapreplace_Max_Node(NodeBase):
    """
    Maxheap variant of heapreplace."""
    
    title = '_heapreplace_max'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='heap'),
        NodeInputBP(label='item'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq._heapreplace_max(self.input(0), self.input(1)))
        

class _Siftdown_Node(NodeBase):
    """
    """
    
    title = '_siftdown'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='heap'),
        NodeInputBP(label='startpos'),
        NodeInputBP(label='pos'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq._siftdown(self.input(0), self.input(1), self.input(2)))
        

class _Siftdown_Max_Node(NodeBase):
    """
    Maxheap variant of _siftdown"""
    
    title = '_siftdown_max'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='heap'),
        NodeInputBP(label='startpos'),
        NodeInputBP(label='pos'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq._siftdown_max(self.input(0), self.input(1), self.input(2)))
        

class _Siftup_Node(NodeBase):
    """
    """
    
    title = '_siftup'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='heap'),
        NodeInputBP(label='pos'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq._siftup(self.input(0), self.input(1)))
        

class _Siftup_Max_Node(NodeBase):
    """
    Maxheap variant of _siftup"""
    
    title = '_siftup_max'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='heap'),
        NodeInputBP(label='pos'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq._siftup_max(self.input(0), self.input(1)))
        

class Heapify_Node(NodeBase):
    """
    Transform list into a heap, in-place, in O(len(heap)) time."""
    
    title = 'heapify'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='heap'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq.heapify(self.input(0)))
        

class Heappop_Node(NodeBase):
    """
    Pop the smallest item off the heap, maintaining the heap invariant."""
    
    title = 'heappop'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='heap'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq.heappop(self.input(0)))
        

class Heappush_Node(NodeBase):
    """
    Push item onto heap, maintaining the heap invariant."""
    
    title = 'heappush'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='heap'),
        NodeInputBP(label='item'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq.heappush(self.input(0), self.input(1)))
        

class Heappushpop_Node(NodeBase):
    """
    Push item on the heap, then pop and return the smallest item from the heap.

The combined action runs more efficiently than heappush() followed by
a separate call to heappop()."""
    
    title = 'heappushpop'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='heap'),
        NodeInputBP(label='item'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq.heappushpop(self.input(0), self.input(1)))
        

class Heapreplace_Node(NodeBase):
    """
    Pop and return the current smallest value, and add the new item.

This is more efficient than heappop() followed by heappush(), and can be
more appropriate when using a fixed-size heap.  Note that the value
returned may be larger than item!  That constrains reasonable uses of
this routine unless written as part of a conditional replacement:

    if item > heap[0]:
        item = heapreplace(heap, item)"""
    
    title = 'heapreplace'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='heap'),
        NodeInputBP(label='item'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq.heapreplace(self.input(0), self.input(1)))
        

class Merge_Node(NodeBase):
    """
    Merge multiple sorted inputs into a single sorted output.

    Similar to sorted(itertools.chain(*iterables)) but returns a generator,
    does not pull the data into memory all at once, and assumes that each of
    the input streams is already sorted (smallest to largest).

    >>> list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
    [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]

    If *key* is not None, applies a key function to each element to determine
    its sort order.

    >>> list(merge(['dog', 'horse'], ['cat', 'fish', 'kangaroo'], key=len))
    ['dog', 'cat', 'fish', 'horse', 'kangaroo']

    """
    
    title = 'merge'
    type_ = 'heapq'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq.merge())
        

class Nlargest_Node(NodeBase):
    """
    Find the n largest elements in a dataset.

    Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]
    """
    
    title = 'nlargest'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='n'),
        NodeInputBP(label='iterable'),
        NodeInputBP(label='key', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq.nlargest(self.input(0), self.input(1), self.input(2)))
        

class Nsmallest_Node(NodeBase):
    """
    Find the n smallest elements in a dataset.

    Equivalent to:  sorted(iterable, key=key)[:n]
    """
    
    title = 'nsmallest'
    type_ = 'heapq'
    init_inputs = [
        NodeInputBP(label='n'),
        NodeInputBP(label='iterable'),
        NodeInputBP(label='key', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, heapq.nsmallest(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _Heapify_Max_Node,
    _Heappop_Max_Node,
    _Heapreplace_Max_Node,
    _Siftdown_Node,
    _Siftdown_Max_Node,
    _Siftup_Node,
    _Siftup_Max_Node,
    Heapify_Node,
    Heappop_Node,
    Heappush_Node,
    Heappushpop_Node,
    Heapreplace_Node,
    Merge_Node,
    Nlargest_Node,
    Nsmallest_Node,
)
