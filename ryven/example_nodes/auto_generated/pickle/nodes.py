
from ryven.NENV import *

import pickle


class NodeBase(Node):
    pass


class _Dump_Node(NodeBase):
    """
    """
    
    title = '_dump'
    type_ = 'pickle'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='file'),
        NodeInputBP(label='protocol', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle._dump(self.input(0), self.input(1), self.input(2)))
        

class _Dumps_Node(NodeBase):
    """
    """
    
    title = '_dumps'
    type_ = 'pickle'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='protocol', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle._dumps(self.input(0), self.input(1)))
        

class _Getattribute_Node(NodeBase):
    """
    """
    
    title = '_getattribute'
    type_ = 'pickle'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle._getattribute(self.input(0), self.input(1)))
        

class _Load_Node(NodeBase):
    """
    """
    
    title = '_load'
    type_ = 'pickle'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle._load(self.input(0)))
        

class _Loads_Node(NodeBase):
    """
    """
    
    title = '_loads'
    type_ = 'pickle'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle._loads(self.input(0)))
        

class _Test_Node(NodeBase):
    """
    """
    
    title = '_test'
    type_ = 'pickle'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle._test())
        

class Decode_Long_Node(NodeBase):
    """
    Decode a long from a two's complement little-endian binary string.

    >>> decode_long(b'')
    0
    >>> decode_long(b"\xff\x00")
    255
    >>> decode_long(b"\xff\x7f")
    32767
    >>> decode_long(b"\x00\xff")
    -256
    >>> decode_long(b"\x00\x80")
    -32768
    >>> decode_long(b"\x80")
    -128
    >>> decode_long(b"\x7f")
    127
    """
    
    title = 'decode_long'
    type_ = 'pickle'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle.decode_long(self.input(0)))
        

class Dump_Node(NodeBase):
    """
    Write a pickled representation of obj to the open file object file.

This is equivalent to ``Pickler(file, protocol).dump(obj)``, but may
be more efficient.

The optional *protocol* argument tells the pickler to use the given
protocol; supported protocols are 0, 1, 2, 3, 4 and 5.  The default
protocol is 4. It was introduced in Python 3.4, and is incompatible
with previous versions.

Specifying a negative protocol version selects the highest protocol
version supported.  The higher the protocol used, the more recent the
version of Python needed to read the pickle produced.

The *file* argument must have a write() method that accepts a single
bytes argument.  It can thus be a file object opened for binary
writing, an io.BytesIO instance, or any other custom object that meets
this interface.

If *fix_imports* is True and protocol is less than 3, pickle will try
to map the new Python 3 names to the old module names used in Python
2, so that the pickle data stream is readable with Python 2.

If *buffer_callback* is None (the default), buffer views are serialized
into *file* as part of the pickle stream.  It is an error if
*buffer_callback* is not None and *protocol* is None or smaller than 5."""
    
    title = 'dump'
    type_ = 'pickle'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='file'),
        NodeInputBP(label='protocol', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle.dump(self.input(0), self.input(1), self.input(2)))
        

class Dumps_Node(NodeBase):
    """
    Return the pickled representation of the object as a bytes object.

The optional *protocol* argument tells the pickler to use the given
protocol; supported protocols are 0, 1, 2, 3, 4 and 5.  The default
protocol is 4. It was introduced in Python 3.4, and is incompatible
with previous versions.

Specifying a negative protocol version selects the highest protocol
version supported.  The higher the protocol used, the more recent the
version of Python needed to read the pickle produced.

If *fix_imports* is True and *protocol* is less than 3, pickle will
try to map the new Python 3 names to the old module names used in
Python 2, so that the pickle data stream is readable with Python 2.

If *buffer_callback* is None (the default), buffer views are serialized
into *file* as part of the pickle stream.  It is an error if
*buffer_callback* is not None and *protocol* is None or smaller than 5."""
    
    title = 'dumps'
    type_ = 'pickle'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='protocol', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle.dumps(self.input(0), self.input(1)))
        

class Encode_Long_Node(NodeBase):
    """
    Encode a long to a two's complement little-endian binary string.
    Note that 0 is a special case, returning an empty string, to save a
    byte in the LONG1 pickling context.

    >>> encode_long(0)
    b''
    >>> encode_long(255)
    b'\xff\x00'
    >>> encode_long(32767)
    b'\xff\x7f'
    >>> encode_long(-256)
    b'\x00\xff'
    >>> encode_long(-32768)
    b'\x00\x80'
    >>> encode_long(-128)
    b'\x80'
    >>> encode_long(127)
    b'\x7f'
    >>>
    """
    
    title = 'encode_long'
    type_ = 'pickle'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle.encode_long(self.input(0)))
        

class Load_Node(NodeBase):
    """
    Read and return an object from the pickle data stored in a file.

This is equivalent to ``Unpickler(file).load()``, but may be more
efficient.

The protocol version of the pickle is detected automatically, so no
protocol argument is needed.  Bytes past the pickled object's
representation are ignored.

The argument *file* must have two methods, a read() method that takes
an integer argument, and a readline() method that requires no
arguments.  Both methods should return bytes.  Thus *file* can be a
binary file object opened for reading, an io.BytesIO object, or any
other custom object that meets this interface.

Optional keyword arguments are *fix_imports*, *encoding* and *errors*,
which are used to control compatibility support for pickle stream
generated by Python 2.  If *fix_imports* is True, pickle will try to
map the old Python 2 names to the new names used in Python 3.  The
*encoding* and *errors* tell pickle how to decode 8-bit string
instances pickled by Python 2; these default to 'ASCII' and 'strict',
respectively.  The *encoding* can be 'bytes' to read these 8-bit
string instances as bytes objects."""
    
    title = 'load'
    type_ = 'pickle'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle.load(self.input(0)))
        

class Loads_Node(NodeBase):
    """
    Read and return an object from the given pickle data.

The protocol version of the pickle is detected automatically, so no
protocol argument is needed.  Bytes past the pickled object's
representation are ignored.

Optional keyword arguments are *fix_imports*, *encoding* and *errors*,
which are used to control compatibility support for pickle stream
generated by Python 2.  If *fix_imports* is True, pickle will try to
map the old Python 2 names to the new names used in Python 3.  The
*encoding* and *errors* tell pickle how to decode 8-bit string
instances pickled by Python 2; these default to 'ASCII' and 'strict',
respectively.  The *encoding* can be 'bytes' to read these 8-bit
string instances as bytes objects."""
    
    title = 'loads'
    type_ = 'pickle'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle.loads(self.input(0)))
        

class Unpack_Node(NodeBase):
    """
    Return a tuple containing values unpacked according to the format string.

The buffer's size in bytes must be calcsize(format).

See help(struct) for more on format strings."""
    
    title = 'unpack'
    type_ = 'pickle'
    init_inputs = [
        NodeInputBP(label='format'),
        NodeInputBP(label='buffer'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle.unpack(self.input(0), self.input(1)))
        

class Whichmodule_Node(NodeBase):
    """
    Find the module an object belong to."""
    
    title = 'whichmodule'
    type_ = 'pickle'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickle.whichmodule(self.input(0), self.input(1)))
        


export_nodes(
    _Dump_Node,
    _Dumps_Node,
    _Getattribute_Node,
    _Load_Node,
    _Loads_Node,
    _Test_Node,
    Decode_Long_Node,
    Dump_Node,
    Dumps_Node,
    Encode_Long_Node,
    Load_Node,
    Loads_Node,
    Unpack_Node,
    Whichmodule_Node,
)
