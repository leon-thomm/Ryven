import ryvencore_qt as rc
import gzip


class AutoNode_gzip_compress(rc.Node):
    title = 'compress'
    doc = '''Compress data in one shot and return the compressed string.
    Optional argument is the compression level, in range of 0-9.
    '''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='compresslevel'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gzip.compress(self.input(0), self.input(1)))
        


class AutoNode_gzip_decompress(rc.Node):
    title = 'decompress'
    doc = '''Decompress a gzip compressed string in one shot.
    Return the decompressed string.
    '''
    init_inputs = [
        rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gzip.decompress(self.input(0)))
        


class AutoNode_gzip_main(rc.Node):
    title = 'main'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gzip.main())
        


class AutoNode_gzip_open(rc.Node):
    title = 'open'
    doc = '''Open a gzip-compressed file in binary or text mode.

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

    '''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='mode'),
rc.NodeInputBP(label='compresslevel'),
rc.NodeInputBP(label='encoding'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='newline'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gzip.open(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode_gzip_write32u(rc.Node):
    title = 'write32u'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='output'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gzip.write32u(self.input(0), self.input(1)))
        