import ryvencore_qt as rc
import lzma


class AutoNode_lzma__decode_filter_properties(rc.Node):
    title = '_decode_filter_properties'
    description = '''Return a bytes object encoding the options (properties) of the filter specified by *filter* (a dict).

The result does not include the filter ID itself, only the options.'''
    init_inputs = [
        rc.NodeInputBP(label='filter_id'),
rc.NodeInputBP(label='encoded_props'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, lzma._decode_filter_properties(self.input(0), self.input(1)))
        


class AutoNode_lzma__encode_filter_properties(rc.Node):
    title = '_encode_filter_properties'
    description = '''Return a bytes object encoding the options (properties) of the filter specified by *filter* (a dict).

The result does not include the filter ID itself, only the options.'''
    init_inputs = [
        rc.NodeInputBP(label='filter'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, lzma._encode_filter_properties(self.input(0)))
        


class AutoNode_lzma_compress(rc.Node):
    title = 'compress'
    description = '''Compress a block of data.

    Refer to LZMACompressor's docstring for a description of the
    optional arguments *format*, *check*, *preset* and *filters*.

    For incremental compression, use an LZMACompressor instead.
    '''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='format'),
rc.NodeInputBP(label='check'),
rc.NodeInputBP(label='preset'),
rc.NodeInputBP(label='filters'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, lzma.compress(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_lzma_decompress(rc.Node):
    title = 'decompress'
    description = '''Decompress a block of data.

    Refer to LZMADecompressor's docstring for a description of the
    optional arguments *format*, *check* and *filters*.

    For incremental decompression, use an LZMADecompressor instead.
    '''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='format'),
rc.NodeInputBP(label='memlimit'),
rc.NodeInputBP(label='filters'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, lzma.decompress(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_lzma_is_check_supported(rc.Node):
    title = 'is_check_supported'
    description = '''Test whether the given integrity check is supported.

Always returns True for CHECK_NONE and CHECK_CRC32.'''
    init_inputs = [
        rc.NodeInputBP(label='check_id'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, lzma.is_check_supported(self.input(0)))
        


class AutoNode_lzma_open(rc.Node):
    title = 'open'
    description = '''Open an LZMA-compressed file in binary or text mode.

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

    '''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='mode'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, lzma.open(self.input(0), self.input(1)))
        