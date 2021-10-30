
from ryven.NENV import *

import zipfile


class NodeBase(Node):
    pass


class _Endrecdata_Node(NodeBase):
    """
    Return data from the "End of Central Directory" record, or None.

    The data is a list of the nine items in the ZIP "End of central dir"
    record followed by a tenth item, the file seek offset of this record."""
    
    title = '_EndRecData'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='fpin'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile._EndRecData(self.input(0)))
        

class _Endrecdata64_Node(NodeBase):
    """
    
    Read the ZIP64 end-of-archive records and use that to update endrec
    """
    
    title = '_EndRecData64'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='fpin'),
        NodeInputBP(label='offset'),
        NodeInputBP(label='endrec'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile._EndRecData64(self.input(0), self.input(1), self.input(2)))
        

class _Zipdecrypter_Node(NodeBase):
    """
    """
    
    title = '_ZipDecrypter'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='pwd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile._ZipDecrypter(self.input(0)))
        

class _Ancestry_Node(NodeBase):
    """
    
    Given a path with elements separated by
    posixpath.sep, generate all elements of that path

    >>> list(_ancestry('b/d'))
    ['b/d', 'b']
    >>> list(_ancestry('/b/d/'))
    ['/b/d', '/b']
    >>> list(_ancestry('b/d/f/'))
    ['b/d/f', 'b/d', 'b']
    >>> list(_ancestry('b'))
    ['b']
    >>> list(_ancestry(''))
    []
    """
    
    title = '_ancestry'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile._ancestry(self.input(0)))
        

class _Check_Compression_Node(NodeBase):
    """
    """
    
    title = '_check_compression'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='compression'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile._check_compression(self.input(0)))
        

class _Check_Zipfile_Node(NodeBase):
    """
    """
    
    title = '_check_zipfile'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='fp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile._check_zipfile(self.input(0)))
        

class _Dedupe_Node(NodeBase):
    """
    Create a new dictionary with keys from iterable and values set to value."""
    
    title = '_dedupe'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='type'),
        NodeInputBP(label='iterable'),
        NodeInputBP(label='value', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile._dedupe(self.input(0), self.input(1), self.input(2)))
        

class _Difference_Node(NodeBase):
    """
    
    Return items in minuend not in subtrahend, retaining order
    with O(1) lookup.
    """
    
    title = '_difference'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='minuend'),
        NodeInputBP(label='subtrahend'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile._difference(self.input(0), self.input(1)))
        

class _Gen_Crc_Node(NodeBase):
    """
    """
    
    title = '_gen_crc'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='crc'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile._gen_crc(self.input(0)))
        

class _Get_Compressor_Node(NodeBase):
    """
    """
    
    title = '_get_compressor'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='compress_type'),
        NodeInputBP(label='compresslevel', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile._get_compressor(self.input(0), self.input(1)))
        

class _Get_Decompressor_Node(NodeBase):
    """
    """
    
    title = '_get_decompressor'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='compress_type'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile._get_decompressor(self.input(0)))
        

class _Parents_Node(NodeBase):
    """
    
    Given a path with elements separated by
    posixpath.sep, generate all parents of that path.

    >>> list(_parents('b/d'))
    ['b']
    >>> list(_parents('/b/d/'))
    ['/b']
    >>> list(_parents('b/d/f/'))
    ['b/d', 'b']
    >>> list(_parents('b'))
    []
    >>> list(_parents(''))
    []
    """
    
    title = '_parents'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile._parents(self.input(0)))
        

class _Strip_Extra_Node(NodeBase):
    """
    """
    
    title = '_strip_extra'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='extra'),
        NodeInputBP(label='xids'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile._strip_extra(self.input(0), self.input(1)))
        

class Crc32_Node(NodeBase):
    """
    Compute a CRC-32 checksum of data.

  value
    Starting value of the checksum.

The returned checksum is an integer."""
    
    title = 'crc32'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='value', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile.crc32(self.input(0), self.input(1)))
        

class Is_Zipfile_Node(NodeBase):
    """
    Quickly see if a file is a ZIP file by checking the magic number.

    The filename argument may be a file or file-like object too.
    """
    
    title = 'is_zipfile'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile.is_zipfile(self.input(0)))
        

class Main_Node(NodeBase):
    """
    """
    
    title = 'main'
    type_ = 'zipfile'
    init_inputs = [
        NodeInputBP(label='args', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipfile.main(self.input(0)))
        


export_nodes(
    _Endrecdata_Node,
    _Endrecdata64_Node,
    _Zipdecrypter_Node,
    _Ancestry_Node,
    _Check_Compression_Node,
    _Check_Zipfile_Node,
    _Dedupe_Node,
    _Difference_Node,
    _Gen_Crc_Node,
    _Get_Compressor_Node,
    _Get_Decompressor_Node,
    _Parents_Node,
    _Strip_Extra_Node,
    Crc32_Node,
    Is_Zipfile_Node,
    Main_Node,
)
