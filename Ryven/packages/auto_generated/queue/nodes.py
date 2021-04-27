
from NENV import *

import queue


class NodeBase(Node):
    pass


class Heappop_Node(NodeBase):
    title = 'heappop'
    type_ = 'queue'
    doc = """Pop the smallest item off the heap, maintaining the heap invariant."""
    init_inputs = [
        NodeInputBP(label='heap'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, queue.heappop(self.input(0)))
        

class Heappush_Node(NodeBase):
    title = 'heappush'
    type_ = 'queue'
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
        self.set_output_val(0, queue.heappush(self.input(0), self.input(1)))
        


export_nodes(
    Heappop_Node,
    Heappush_Node,
)
