import ryvencore_qt as rc
import _heapq


class AutoNode__heapq__heapify_max(rc.Node):
    title = '_heapify_max'
    type_ = '_heapq'
    description = '''Maxheap variant of heapify.'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq._heapify_max(self.input(0)))
        


class AutoNode__heapq__heappop_max(rc.Node):
    title = '_heappop_max'
    type_ = '_heapq'
    description = '''Maxheap variant of heappop.'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq._heappop_max(self.input(0)))
        


class AutoNode__heapq__heapreplace_max(rc.Node):
    title = '_heapreplace_max'
    type_ = '_heapq'
    description = '''Maxheap variant of heapreplace.'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
rc.NodeInputBP(label='item'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq._heapreplace_max(self.input(0), self.input(1)))
        


class AutoNode__heapq_heapify(rc.Node):
    title = 'heapify'
    type_ = '_heapq'
    description = '''Transform list into a heap, in-place, in O(len(heap)) time.'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq.heapify(self.input(0)))
        


class AutoNode__heapq_heappop(rc.Node):
    title = 'heappop'
    type_ = '_heapq'
    description = '''Pop the smallest item off the heap, maintaining the heap invariant.'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq.heappop(self.input(0)))
        


class AutoNode__heapq_heappush(rc.Node):
    title = 'heappush'
    type_ = '_heapq'
    description = '''Push item onto heap, maintaining the heap invariant.'''
    init_inputs = [
        rc.NodeInputBP(label='heap'),
rc.NodeInputBP(label='item'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _heapq.heappush(self.input(0), self.input(1)))
        


class AutoNode__heapq_heappushpop(rc.Node):
    title = 'heappushpop'
    type_ = '_heapq'
    description = '''Push item on the heap, then pop and return the smallest item from the heap.

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
        self.set_output_val(0, _heapq.heappushpop(self.input(0), self.input(1)))
        


class AutoNode__heapq_heapreplace(rc.Node):
    title = 'heapreplace'
    type_ = '_heapq'
    description = '''Pop and return the current smallest value, and add the new item.

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
        self.set_output_val(0, _heapq.heapreplace(self.input(0), self.input(1)))
        