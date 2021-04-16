import ryvencore_qt as rc
import heapq


class AutoNode_heapq__heapify_max(rc.Node):
    title = '_heapify_max'
    doc = '''Maxheap variant of heapify.'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq._heapify_max(self.input(0)))
        


class AutoNode_heapq__heappop_max(rc.Node):
    title = '_heappop_max'
    doc = '''Maxheap variant of heappop.'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq._heappop_max(self.input(0)))
        


class AutoNode_heapq__heapreplace_max(rc.Node):
    title = '_heapreplace_max'
    doc = '''Maxheap variant of heapreplace.'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
rc.NodeInputBP(label='item'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq._heapreplace_max(self.input(0), self.input(1)))
        


class AutoNode_heapq__siftdown(rc.Node):
    title = '_siftdown'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
rc.NodeInputBP(label='startpos'),
rc.NodeInputBP(label='pos'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq._siftdown(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_heapq__siftdown_max(rc.Node):
    title = '_siftdown_max'
    doc = '''Maxheap variant of _siftdown'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
rc.NodeInputBP(label='startpos'),
rc.NodeInputBP(label='pos'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq._siftdown_max(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_heapq__siftup(rc.Node):
    title = '_siftup'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
rc.NodeInputBP(label='pos'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq._siftup(self.input(0), self.input(1)))
        


class AutoNode_heapq__siftup_max(rc.Node):
    title = '_siftup_max'
    doc = '''Maxheap variant of _siftup'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
rc.NodeInputBP(label='pos'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq._siftup_max(self.input(0), self.input(1)))
        


class AutoNode_heapq_heapify(rc.Node):
    title = 'heapify'
    doc = '''Transform list into a heap, in-place, in O(len(heap)) time.'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq.heapify(self.input(0)))
        


class AutoNode_heapq_heappop(rc.Node):
    title = 'heappop'
    doc = '''Pop the smallest item off the heap, maintaining the heap invariant.'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq.heappop(self.input(0)))
        


class AutoNode_heapq_heappush(rc.Node):
    title = 'heappush'
    doc = '''Push item onto heap, maintaining the heap invariant.'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
rc.NodeInputBP(label='item'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq.heappush(self.input(0), self.input(1)))
        


class AutoNode_heapq_heappushpop(rc.Node):
    title = 'heappushpop'
    doc = '''Push item on the heap, then pop and return the smallest item from the heap.

The combined action runs more efficiently than heappush() followed by
a separate call to heappop().'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
rc.NodeInputBP(label='item'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq.heappushpop(self.input(0), self.input(1)))
        


class AutoNode_heapq_heapreplace(rc.Node):
    title = 'heapreplace'
    doc = '''Pop and return the current smallest value, and add the new item.

This is more efficient than heappop() followed by heappush(), and can be
more appropriate when using a fixed-size heap.  Note that the value
returned may be larger than item!  That constrains reasonable uses of
this routine unless written as part of a conditional replacement:

    if item > heap[0]:
        item = heapreplace(heap, item)'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
rc.NodeInputBP(label='item'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq.heapreplace(self.input(0), self.input(1)))
        


class AutoNode_heapq_merge(rc.Node):
    title = 'merge'
    doc = '''Merge multiple sorted inputs into a single sorted output.

    Similar to sorted(itertools.chain(*iterables)) but returns a generator,
    does not pull the data into memory all at once, and assumes that each of
    the input streams is already sorted (smallest to largest).

    >>> list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
    [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]

    If *key* is not None, applies a key function to each element to determine
    its sort order.

    >>> list(merge(['dog', 'horse'], ['cat', 'fish', 'kangaroo'], key=len))
    ['dog', 'cat', 'fish', 'horse', 'kangaroo']

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq.merge())
        


class AutoNode_heapq_nlargest(rc.Node):
    title = 'nlargest'
    doc = '''Find the n largest elements in a dataset.

    Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]
    '''
    init_inputs = [
        rc.NodeInputBP(label='n'),
rc.NodeInputBP(label='iterable'),
rc.NodeInputBP(label='key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq.nlargest(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_heapq_nsmallest(rc.Node):
    title = 'nsmallest'
    doc = '''Find the n smallest elements in a dataset.

    Equivalent to:  sorted(iterable, key=key)[:n]
    '''
    init_inputs = [
        rc.NodeInputBP(label='n'),
rc.NodeInputBP(label='iterable'),
rc.NodeInputBP(label='key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, heapq.nsmallest(self.input(0), self.input(1), self.input(2)))
        