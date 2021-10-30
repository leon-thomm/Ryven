
from ryven.NENV import *

import gzip


class NodeBase(Node):
    pass


class Compress_Node(NodeBase):
    """
    Compress data in one shot and return the compressed string.
    Optional argument is the compression level, in range of 0-9.
    """
    
    title = 'compress'
    type_ = 'gzip'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='compresslevel', dtype=dtypes.Data(default=9, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gzip.compress(self.input(0), self.input(1)))
        

class Decompress_Node(NodeBase):
    """
    Decompress a gzip compressed string in one shot.
    Return the decompressed string.
    """
    
    title = 'decompress'
    type_ = 'gzip'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gzip.decompress(self.input(0)))
        

class Main_Node(NodeBase):
    """
    """
    
    title = 'main'
    type_ = 'gzip'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gzip.main())
        

class Open_Node(NodeBase):
    """
    Open a gzip-compressed file in binary or text mode.

    The filename argument can be an actual filename (a str or bytes object), or
    an existing file object to read from or write to.

    The mode argument can be "r", "rb", "w", "wb", "x", "xb", "a" or "ab" for
    binary mode, or "rt", "wt", "xt" or "at" for text mode. The default mode is
    "rb", and the default compresslevel is 9.

    For binary mode, this function is equivalent to the GzipFile constructor:
    GzipFile(filename, mode, compresslevel). In this case, the encoding, errors
    and newline arguments must not be provided.

    For text mode, a GzipFile object is created, and wrapped in an
    io.TextIOWrapper instance with the specified encoding, error handling
    behavior, and line ending(s).

    """
    
    title = 'open'
    type_ = 'gzip'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='mode', dtype=dtypes.Data(default='rb', size='s')),
        NodeInputBP(label='compresslevel', dtype=dtypes.Data(default=9, size='s')),
        NodeInputBP(label='encoding', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='newline', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gzip.open(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class Write32U_Node(NodeBase):
    """
    """
    
    title = 'write32u'
    type_ = 'gzip'
    init_inputs = [
        NodeInputBP(label='output'),
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gzip.write32u(self.input(0), self.input(1)))
        


export_nodes(
    Compress_Node,
    Decompress_Node,
    Main_Node,
    Open_Node,
    Write32U_Node,
)
