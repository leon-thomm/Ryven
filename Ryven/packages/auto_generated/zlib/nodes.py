import ryvencore_qt as rc
import zlib


class AutoNode_zlib_adler32(rc.Node):
    title = 'adler32'
    type_ = 'zlib'
    description = '''Compute an Adler-32 checksum of data.

  value
    Starting value of the checksum.

The returned checksum is an integer.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, zlib.adler32(self.input(0), self.input(1)))
        


class AutoNode_zlib_compress(rc.Node):
    title = 'compress'
    type_ = 'zlib'
    description = '''Returns a bytes object containing compressed data.

  data
    Binary data to be compressed.
  level
    Compression level, in 0-9 or -1.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='level'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, zlib.compress(self.input(0), self.input(1)))
        


class AutoNode_zlib_compressobj(rc.Node):
    title = 'compressobj'
    type_ = 'zlib'
    description = '''Return a compressor object.

  level
    The compression level (an integer in the range 0-9 or -1; default is
    currently equivalent to 6).  Higher compression levels are slower,
    but produce smaller results.
  method
    The compression algorithm.  If given, this must be DEFLATED.
  wbits
    +9 to +15: The base-two logarithm of the window size.  Include a zlib
        container.
    -9 to -15: Generate a raw stream.
    +25 to +31: Include a gzip container.
  memLevel
    Controls the amount of memory used for internal compression state.
    Valid values range from 1 to 9.  Higher values result in higher memory
    usage, faster compression, and smaller output.
  strategy
    Used to tune the compression algorithm.  Possible values are
    Z_DEFAULT_STRATEGY, Z_FILTERED, and Z_HUFFMAN_ONLY.
  zdict
    The predefined compression dictionary - a sequence of bytes
    containing subsequences that are likely to occur in the input data.'''
    init_inputs = [
        rc.NodeInputBP(label='level'),
rc.NodeInputBP(label='method'),
rc.NodeInputBP(label='wbits'),
rc.NodeInputBP(label='memLevel'),
rc.NodeInputBP(label='strategy'),
rc.NodeInputBP(label='zdict'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, zlib.compressobj(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode_zlib_crc32(rc.Node):
    title = 'crc32'
    type_ = 'zlib'
    description = '''Compute a CRC-32 checksum of data.

  value
    Starting value of the checksum.

The returned checksum is an integer.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, zlib.crc32(self.input(0), self.input(1)))
        


class AutoNode_zlib_decompress(rc.Node):
    title = 'decompress'
    type_ = 'zlib'
    description = '''Returns a bytes object containing the uncompressed data.

  data
    Compressed data.
  wbits
    The window buffer size and container format.
  bufsize
    The initial output buffer size.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='wbits'),
rc.NodeInputBP(label='bufsize'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, zlib.decompress(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_zlib_decompressobj(rc.Node):
    title = 'decompressobj'
    type_ = 'zlib'
    description = '''Return a decompressor object.

  wbits
    The window buffer size and container format.
  zdict
    The predefined compression dictionary.  This must be the same
    dictionary as used by the compressor that produced the input data.'''
    init_inputs = [
        rc.NodeInputBP(label='wbits'),
rc.NodeInputBP(label='zdict'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, zlib.decompressobj(self.input(0), self.input(1)))
        