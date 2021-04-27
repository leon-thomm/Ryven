
from NENV import *

import struct


class NodeBase(Node):
    pass


class _Clearcache_Node(NodeBase):
    title = '_clearcache'
    type_ = 'struct'
    doc = """Clear the internal cache."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, struct._clearcache())
        

class Calcsize_Node(NodeBase):
    title = 'calcsize'
    type_ = 'struct'
    doc = """Return size in bytes of the struct described by the format string."""
    init_inputs = [
        NodeInputBP(label='format'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, struct.calcsize(self.input(0)))
        

class Iter_Unpack_Node(NodeBase):
    title = 'iter_unpack'
    type_ = 'struct'
    doc = """Return an iterator yielding tuples unpacked from the given bytes.

The bytes are unpacked according to the format string, like
a repeated invocation of unpack_from().

Requires that the bytes length be a multiple of the format struct size."""
    init_inputs = [
        NodeInputBP(label='format'),
        NodeInputBP(label='buffer'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, struct.iter_unpack(self.input(0), self.input(1)))
        

class Unpack_Node(NodeBase):
    title = 'unpack'
    type_ = 'struct'
    doc = """Return a tuple containing values unpacked according to the format string.

The buffer's size in bytes must be calcsize(format).

See help(struct) for more on format strings."""
    init_inputs = [
        NodeInputBP(label='format'),
        NodeInputBP(label='buffer'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, struct.unpack(self.input(0), self.input(1)))
        

class Unpack_From_Node(NodeBase):
    title = 'unpack_from'
    type_ = 'struct'
    doc = """Return a tuple containing values unpacked according to the format string.

The buffer's size, minus offset, must be at least calcsize(format).

See help(struct) for more on format strings."""
    init_inputs = [
        NodeInputBP(label='format'),
        NodeInputBP(label='buffer'),
        NodeInputBP(label='offset', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, struct.unpack_from(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _Clearcache_Node,
    Calcsize_Node,
    Iter_Unpack_Node,
    Unpack_Node,
    Unpack_From_Node,
)
