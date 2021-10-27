
from NENV import *

import lzma


class NodeBase(Node):
    pass


class _Decode_Filter_Properties_Node(NodeBase):
    """
    Return a bytes object encoding the options (properties) of the filter specified by *filter* (a dict).

The result does not include the filter ID itself, only the options."""
    
    title = '_decode_filter_properties'
    type_ = 'lzma'
    init_inputs = [
        NodeInputBP(label='filter_id'),
        NodeInputBP(label='encoded_props'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, lzma._decode_filter_properties(self.input(0), self.input(1)))
        

class _Encode_Filter_Properties_Node(NodeBase):
    """
    Return a bytes object encoding the options (properties) of the filter specified by *filter* (a dict).

The result does not include the filter ID itself, only the options."""
    
    title = '_encode_filter_properties'
    type_ = 'lzma'
    init_inputs = [
        NodeInputBP(label='filter'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, lzma._encode_filter_properties(self.input(0)))
        

class Compress_Node(NodeBase):
    """
    Compress a block of data.

    Refer to LZMACompressor's docstring for a description of the
    optional arguments *format*, *check*, *preset* and *filters*.

    For incremental compression, use an LZMACompressor instead.
    """
    
    title = 'compress'
    type_ = 'lzma'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='format', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='check', dtype=dtypes.Data(default=-1, size='s')),
        NodeInputBP(label='preset', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='filters', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, lzma.compress(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Decompress_Node(NodeBase):
    """
    Decompress a block of data.

    Refer to LZMADecompressor's docstring for a description of the
    optional arguments *format*, *check* and *filters*.

    For incremental decompression, use an LZMADecompressor instead.
    """
    
    title = 'decompress'
    type_ = 'lzma'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='format', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='memlimit', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='filters', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, lzma.decompress(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Is_Check_Supported_Node(NodeBase):
    """
    Test whether the given integrity check is supported.

Always returns True for CHECK_NONE and CHECK_CRC32."""
    
    title = 'is_check_supported'
    type_ = 'lzma'
    init_inputs = [
        NodeInputBP(label='check_id'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, lzma.is_check_supported(self.input(0)))
        

class Open_Node(NodeBase):
    """
    Open an LZMA-compressed file in binary or text mode.

    filename can be either an actual file name (given as a str, bytes,
    or PathLike object), in which case the named file is opened, or it
    can be an existing file object to read from or write to.

    The mode argument can be "r", "rb" (default), "w", "wb", "x", "xb",
    "a", or "ab" for binary mode, or "rt", "wt", "xt", or "at" for text
    mode.

    The format, check, preset and filters arguments specify the
    compression settings, as for LZMACompressor, LZMADecompressor and
    LZMAFile.

    For binary mode, this function is equivalent to the LZMAFile
    constructor: LZMAFile(filename, mode, ...). In this case, the
    encoding, errors and newline arguments must not be provided.

    For text mode, an LZMAFile object is created, and wrapped in an
    io.TextIOWrapper instance with the specified encoding, error
    handling behavior, and line ending(s).

    """
    
    title = 'open'
    type_ = 'lzma'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='mode', dtype=dtypes.Data(default='rb', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, lzma.open(self.input(0), self.input(1)))
        


export_nodes(
    _Decode_Filter_Properties_Node,
    _Encode_Filter_Properties_Node,
    Compress_Node,
    Decompress_Node,
    Is_Check_Supported_Node,
    Open_Node,
)
