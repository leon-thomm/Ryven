
from ryven.NENV import *

import bisect


class NodeBase(Node):
    pass


class Bisect_Node(NodeBase):
    """
    Return the index where to insert item x in list a, assuming a is sorted.

The return value i is such that all e in a[:i] have e <= x, and all e in
a[i:] have e > x.  So if x already appears in the list, i points just
beyond the rightmost x already there

Optional args lo (default 0) and hi (default len(a)) bound the
slice of a to be searched."""
    
    title = 'bisect'
    type_ = 'bisect'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='x'),
        NodeInputBP(label='lo', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='hi', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, bisect.bisect(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Bisect_Left_Node(NodeBase):
    """
    Return the index where to insert item x in list a, assuming a is sorted.

The return value i is such that all e in a[:i] have e < x, and all e in
a[i:] have e >= x.  So if x already appears in the list, i points just
before the leftmost x already there.

Optional args lo (default 0) and hi (default len(a)) bound the
slice of a to be searched."""
    
    title = 'bisect_left'
    type_ = 'bisect'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='x'),
        NodeInputBP(label='lo', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='hi', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, bisect.bisect_left(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Bisect_Right_Node(NodeBase):
    """
    Return the index where to insert item x in list a, assuming a is sorted.

The return value i is such that all e in a[:i] have e <= x, and all e in
a[i:] have e > x.  So if x already appears in the list, i points just
beyond the rightmost x already there

Optional args lo (default 0) and hi (default len(a)) bound the
slice of a to be searched."""
    
    title = 'bisect_right'
    type_ = 'bisect'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='x'),
        NodeInputBP(label='lo', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='hi', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, bisect.bisect_right(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Insort_Node(NodeBase):
    """
    Insert item x in list a, and keep it sorted assuming a is sorted.

If x is already in a, insert it to the right of the rightmost x.

Optional args lo (default 0) and hi (default len(a)) bound the
slice of a to be searched."""
    
    title = 'insort'
    type_ = 'bisect'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='x'),
        NodeInputBP(label='lo', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='hi', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, bisect.insort(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Insort_Left_Node(NodeBase):
    """
    Insert item x in list a, and keep it sorted assuming a is sorted.

If x is already in a, insert it to the left of the leftmost x.

Optional args lo (default 0) and hi (default len(a)) bound the
slice of a to be searched."""
    
    title = 'insort_left'
    type_ = 'bisect'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='x'),
        NodeInputBP(label='lo', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='hi', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, bisect.insort_left(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Insort_Right_Node(NodeBase):
    """
    Insert item x in list a, and keep it sorted assuming a is sorted.

If x is already in a, insert it to the right of the rightmost x.

Optional args lo (default 0) and hi (default len(a)) bound the
slice of a to be searched."""
    
    title = 'insort_right'
    type_ = 'bisect'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='x'),
        NodeInputBP(label='lo', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='hi', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, bisect.insort_right(self.input(0), self.input(1), self.input(2), self.input(3)))
        


export_nodes(
    Bisect_Node,
    Bisect_Left_Node,
    Bisect_Right_Node,
    Insort_Node,
    Insort_Left_Node,
    Insort_Right_Node,
)
