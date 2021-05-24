
from NENV import *

import pickletools


class NodeBase(Node):
    pass


class _Genops_Node(NodeBase):
    """
    """
    
    title = '_genops'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='yield_end_pos', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools._genops(self.input(0), self.input(1)))
        

class _Test_Node(NodeBase):
    """
    """
    
    title = '_test'
    type_ = 'pickletools'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools._test())
        

class _Unpack_Node(NodeBase):
    """
    Return a tuple containing values unpacked according to the format string.

The buffer's size in bytes must be calcsize(format).

See help(struct) for more on format strings."""
    
    title = '_unpack'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='format'),
        NodeInputBP(label='buffer'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools._unpack(self.input(0), self.input(1)))
        

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
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.decode_long(self.input(0)))
        

class Dis_Node(NodeBase):
    """
    Produce a symbolic disassembly of a pickle.

    'pickle' is a file-like object, or string, containing a (at least one)
    pickle.  The pickle is disassembled from the current position, through
    the first STOP opcode encountered.

    Optional arg 'out' is a file-like object to which the disassembly is
    printed.  It defaults to sys.stdout.

    Optional arg 'memo' is a Python dict, used as the pickle's memo.  It
    may be mutated by dis(), if the pickle contains PUT or BINPUT opcodes.
    Passing the same memo object to another dis() call then allows disassembly
    to proceed across multiple pickles that were all created by the same
    pickler with the same memo.  Ordinarily you don't need to worry about this.

    Optional arg 'indentlevel' is the number of blanks by which to indent
    a new MARK level.  It defaults to 4.

    Optional arg 'annotate' if nonzero instructs dis() to add short
    description of the opcode on each line of disassembled output.
    The value given to 'annotate' must be an integer and is used as a
    hint for the column where annotation should start.  The default
    value is 0, meaning no annotations.

    In addition to printing the disassembly, some sanity checks are made:

    + All embedded opcode arguments "make sense".

    + Explicit and implicit pop operations have enough items on the stack.

    + When an opcode implicitly refers to a markobject, a markobject is
      actually on the stack.

    + A memo entry isn't referenced before it's defined.

    + The markobject isn't stored in the memo.

    + A memo entry isn't redefined.
    """
    
    title = 'dis'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='pickle'),
        NodeInputBP(label='out', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='memo', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='indentlevel', dtype=dtypes.Data(default=4, size='s')),
        NodeInputBP(label='annotate', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.dis(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Genops_Node(NodeBase):
    """
    Generate all the opcodes in a pickle.

    'pickle' is a file-like object, or string, containing the pickle.

    Each opcode in the pickle is generated, from the current pickle position,
    stopping after a STOP opcode is delivered.  A triple is generated for
    each opcode:

        opcode, arg, pos

    opcode is an OpcodeInfo record, describing the current opcode.

    If the opcode has an argument embedded in the pickle, arg is its decoded
    value, as a Python object.  If the opcode doesn't have an argument, arg
    is None.

    If the pickle has a tell() method, pos was the value of pickle.tell()
    before reading the current opcode.  If the pickle is a bytes object,
    it's wrapped in a BytesIO object, and the latter's tell() result is
    used.  Else (the pickle doesn't have a tell(), and it's not obvious how
    to query its current position) pos is None.
    """
    
    title = 'genops'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='pickle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.genops(self.input(0)))
        

class Optimize_Node(NodeBase):
    """
    Optimize a pickle string by removing unused PUT opcodes"""
    
    title = 'optimize'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.optimize(self.input(0)))
        

class Read_Bytearray8_Node(NodeBase):
    """
    
    >>> import io, struct, sys
    >>> read_bytearray8(io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00abc"))
    bytearray(b'')
    >>> read_bytearray8(io.BytesIO(b"\x03\x00\x00\x00\x00\x00\x00\x00abcdef"))
    bytearray(b'abc')
    >>> bigsize8 = struct.pack("<Q", sys.maxsize//3)
    >>> read_bytearray8(io.BytesIO(bigsize8 + b"abcdef"))  #doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ValueError: expected ... bytes in a bytearray8, but only 6 remain
    """
    
    title = 'read_bytearray8'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_bytearray8(self.input(0)))
        

class Read_Bytes1_Node(NodeBase):
    """
    
    >>> import io
    >>> read_bytes1(io.BytesIO(b"\x00"))
    b''
    >>> read_bytes1(io.BytesIO(b"\x03abcdef"))
    b'abc'
    """
    
    title = 'read_bytes1'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_bytes1(self.input(0)))
        

class Read_Bytes4_Node(NodeBase):
    """
    
    >>> import io
    >>> read_bytes4(io.BytesIO(b"\x00\x00\x00\x00abc"))
    b''
    >>> read_bytes4(io.BytesIO(b"\x03\x00\x00\x00abcdef"))
    b'abc'
    >>> read_bytes4(io.BytesIO(b"\x00\x00\x00\x03abcdef"))
    Traceback (most recent call last):
    ...
    ValueError: expected 50331648 bytes in a bytes4, but only 6 remain
    """
    
    title = 'read_bytes4'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_bytes4(self.input(0)))
        

class Read_Bytes8_Node(NodeBase):
    """
    
    >>> import io, struct, sys
    >>> read_bytes8(io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00abc"))
    b''
    >>> read_bytes8(io.BytesIO(b"\x03\x00\x00\x00\x00\x00\x00\x00abcdef"))
    b'abc'
    >>> bigsize8 = struct.pack("<Q", sys.maxsize//3)
    >>> read_bytes8(io.BytesIO(bigsize8 + b"abcdef"))  #doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ValueError: expected ... bytes in a bytes8, but only 6 remain
    """
    
    title = 'read_bytes8'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_bytes8(self.input(0)))
        

class Read_Decimalnl_Long_Node(NodeBase):
    """
    
    >>> import io

    >>> read_decimalnl_long(io.BytesIO(b"1234L\n56"))
    1234

    >>> read_decimalnl_long(io.BytesIO(b"123456789012345678901234L\n6"))
    123456789012345678901234
    """
    
    title = 'read_decimalnl_long'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_decimalnl_long(self.input(0)))
        

class Read_Decimalnl_Short_Node(NodeBase):
    """
    
    >>> import io
    >>> read_decimalnl_short(io.BytesIO(b"1234\n56"))
    1234

    >>> read_decimalnl_short(io.BytesIO(b"1234L\n56"))
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 10: b'1234L'
    """
    
    title = 'read_decimalnl_short'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_decimalnl_short(self.input(0)))
        

class Read_Float8_Node(NodeBase):
    """
    
    >>> import io, struct
    >>> raw = struct.pack(">d", -1.25)
    >>> raw
    b'\xbf\xf4\x00\x00\x00\x00\x00\x00'
    >>> read_float8(io.BytesIO(raw + b"\n"))
    -1.25
    """
    
    title = 'read_float8'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_float8(self.input(0)))
        

class Read_Floatnl_Node(NodeBase):
    """
    
    >>> import io
    >>> read_floatnl(io.BytesIO(b"-1.25\n6"))
    -1.25
    """
    
    title = 'read_floatnl'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_floatnl(self.input(0)))
        

class Read_Int4_Node(NodeBase):
    """
    
    >>> import io
    >>> read_int4(io.BytesIO(b'\xff\x00\x00\x00'))
    255
    >>> read_int4(io.BytesIO(b'\x00\x00\x00\x80')) == -(2**31)
    True
    """
    
    title = 'read_int4'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_int4(self.input(0)))
        

class Read_Long1_Node(NodeBase):
    """
    
    >>> import io
    >>> read_long1(io.BytesIO(b"\x00"))
    0
    >>> read_long1(io.BytesIO(b"\x02\xff\x00"))
    255
    >>> read_long1(io.BytesIO(b"\x02\xff\x7f"))
    32767
    >>> read_long1(io.BytesIO(b"\x02\x00\xff"))
    -256
    >>> read_long1(io.BytesIO(b"\x02\x00\x80"))
    -32768
    """
    
    title = 'read_long1'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_long1(self.input(0)))
        

class Read_Long4_Node(NodeBase):
    """
    
    >>> import io
    >>> read_long4(io.BytesIO(b"\x02\x00\x00\x00\xff\x00"))
    255
    >>> read_long4(io.BytesIO(b"\x02\x00\x00\x00\xff\x7f"))
    32767
    >>> read_long4(io.BytesIO(b"\x02\x00\x00\x00\x00\xff"))
    -256
    >>> read_long4(io.BytesIO(b"\x02\x00\x00\x00\x00\x80"))
    -32768
    >>> read_long1(io.BytesIO(b"\x00\x00\x00\x00"))
    0
    """
    
    title = 'read_long4'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_long4(self.input(0)))
        

class Read_String1_Node(NodeBase):
    """
    
    >>> import io
    >>> read_string1(io.BytesIO(b"\x00"))
    ''
    >>> read_string1(io.BytesIO(b"\x03abcdef"))
    'abc'
    """
    
    title = 'read_string1'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_string1(self.input(0)))
        

class Read_String4_Node(NodeBase):
    """
    
    >>> import io
    >>> read_string4(io.BytesIO(b"\x00\x00\x00\x00abc"))
    ''
    >>> read_string4(io.BytesIO(b"\x03\x00\x00\x00abcdef"))
    'abc'
    >>> read_string4(io.BytesIO(b"\x00\x00\x00\x03abcdef"))
    Traceback (most recent call last):
    ...
    ValueError: expected 50331648 bytes in a string4, but only 6 remain
    """
    
    title = 'read_string4'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_string4(self.input(0)))
        

class Read_Stringnl_Node(NodeBase):
    """
    
    >>> import io
    >>> read_stringnl(io.BytesIO(b"'abcd'\nefg\n"))
    'abcd'

    >>> read_stringnl(io.BytesIO(b"\n"))
    Traceback (most recent call last):
    ...
    ValueError: no string quotes around b''

    >>> read_stringnl(io.BytesIO(b"\n"), stripquotes=False)
    ''

    >>> read_stringnl(io.BytesIO(b"''\n"))
    ''

    >>> read_stringnl(io.BytesIO(b'"abcd"'))
    Traceback (most recent call last):
    ...
    ValueError: no newline found when trying to read stringnl

    Embedded escapes are undone in the result.
    >>> read_stringnl(io.BytesIO(br"'a\n\\b\x00c\td'" + b"\n'e'"))
    'a\n\\b\x00c\td'
    """
    
    title = 'read_stringnl'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='decode', dtype=dtypes.Data(default=True, size='s')),
        NodeInputBP(label='stripquotes', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_stringnl(self.input(0), self.input(1), self.input(2)))
        

class Read_Stringnl_Noescape_Node(NodeBase):
    """
    """
    
    title = 'read_stringnl_noescape'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_stringnl_noescape(self.input(0)))
        

class Read_Stringnl_Noescape_Pair_Node(NodeBase):
    """
    
    >>> import io
    >>> read_stringnl_noescape_pair(io.BytesIO(b"Queue\nEmpty\njunk"))
    'Queue Empty'
    """
    
    title = 'read_stringnl_noescape_pair'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_stringnl_noescape_pair(self.input(0)))
        

class Read_Uint1_Node(NodeBase):
    """
    
    >>> import io
    >>> read_uint1(io.BytesIO(b'\xff'))
    255
    """
    
    title = 'read_uint1'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_uint1(self.input(0)))
        

class Read_Uint2_Node(NodeBase):
    """
    
    >>> import io
    >>> read_uint2(io.BytesIO(b'\xff\x00'))
    255
    >>> read_uint2(io.BytesIO(b'\xff\xff'))
    65535
    """
    
    title = 'read_uint2'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_uint2(self.input(0)))
        

class Read_Uint4_Node(NodeBase):
    """
    
    >>> import io
    >>> read_uint4(io.BytesIO(b'\xff\x00\x00\x00'))
    255
    >>> read_uint4(io.BytesIO(b'\x00\x00\x00\x80')) == 2**31
    True
    """
    
    title = 'read_uint4'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_uint4(self.input(0)))
        

class Read_Uint8_Node(NodeBase):
    """
    
    >>> import io
    >>> read_uint8(io.BytesIO(b'\xff\x00\x00\x00\x00\x00\x00\x00'))
    255
    >>> read_uint8(io.BytesIO(b'\xff' * 8)) == 2**64-1
    True
    """
    
    title = 'read_uint8'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_uint8(self.input(0)))
        

class Read_Unicodestring1_Node(NodeBase):
    """
    
    >>> import io
    >>> s = 'abcd\uabcd'
    >>> enc = s.encode('utf-8')
    >>> enc
    b'abcd\xea\xaf\x8d'
    >>> n = bytes([len(enc)])  # little-endian 1-byte length
    >>> t = read_unicodestring1(io.BytesIO(n + enc + b'junk'))
    >>> s == t
    True

    >>> read_unicodestring1(io.BytesIO(n + enc[:-1]))
    Traceback (most recent call last):
    ...
    ValueError: expected 7 bytes in a unicodestring1, but only 6 remain
    """
    
    title = 'read_unicodestring1'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_unicodestring1(self.input(0)))
        

class Read_Unicodestring4_Node(NodeBase):
    """
    
    >>> import io
    >>> s = 'abcd\uabcd'
    >>> enc = s.encode('utf-8')
    >>> enc
    b'abcd\xea\xaf\x8d'
    >>> n = bytes([len(enc), 0, 0, 0])  # little-endian 4-byte length
    >>> t = read_unicodestring4(io.BytesIO(n + enc + b'junk'))
    >>> s == t
    True

    >>> read_unicodestring4(io.BytesIO(n + enc[:-1]))
    Traceback (most recent call last):
    ...
    ValueError: expected 7 bytes in a unicodestring4, but only 6 remain
    """
    
    title = 'read_unicodestring4'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_unicodestring4(self.input(0)))
        

class Read_Unicodestring8_Node(NodeBase):
    """
    
    >>> import io
    >>> s = 'abcd\uabcd'
    >>> enc = s.encode('utf-8')
    >>> enc
    b'abcd\xea\xaf\x8d'
    >>> n = bytes([len(enc)]) + b'\0' * 7  # little-endian 8-byte length
    >>> t = read_unicodestring8(io.BytesIO(n + enc + b'junk'))
    >>> s == t
    True

    >>> read_unicodestring8(io.BytesIO(n + enc[:-1]))
    Traceback (most recent call last):
    ...
    ValueError: expected 7 bytes in a unicodestring8, but only 6 remain
    """
    
    title = 'read_unicodestring8'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_unicodestring8(self.input(0)))
        

class Read_Unicodestringnl_Node(NodeBase):
    """
    
    >>> import io
    >>> read_unicodestringnl(io.BytesIO(b"abc\\uabcd\njunk")) == 'abc\uabcd'
    True
    """
    
    title = 'read_unicodestringnl'
    type_ = 'pickletools'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pickletools.read_unicodestringnl(self.input(0)))
        


export_nodes(
    _Genops_Node,
    _Test_Node,
    _Unpack_Node,
    Decode_Long_Node,
    Dis_Node,
    Genops_Node,
    Optimize_Node,
    Read_Bytearray8_Node,
    Read_Bytes1_Node,
    Read_Bytes4_Node,
    Read_Bytes8_Node,
    Read_Decimalnl_Long_Node,
    Read_Decimalnl_Short_Node,
    Read_Float8_Node,
    Read_Floatnl_Node,
    Read_Int4_Node,
    Read_Long1_Node,
    Read_Long4_Node,
    Read_String1_Node,
    Read_String4_Node,
    Read_Stringnl_Node,
    Read_Stringnl_Noescape_Node,
    Read_Stringnl_Noescape_Pair_Node,
    Read_Uint1_Node,
    Read_Uint2_Node,
    Read_Uint4_Node,
    Read_Uint8_Node,
    Read_Unicodestring1_Node,
    Read_Unicodestring4_Node,
    Read_Unicodestring8_Node,
    Read_Unicodestringnl_Node,
)
