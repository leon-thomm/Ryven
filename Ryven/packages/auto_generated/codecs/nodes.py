import ryvencore_qt as rc
import codecs


class AutoNode_codecs_EncodedFile(rc.Node):
    title = 'EncodedFile'
    doc = ''' Return a wrapped version of file which provides transparent
        encoding translation.

        Data written to the wrapped file is decoded according
        to the given data_encoding and then encoded to the underlying
        file using file_encoding. The intermediate data type
        will usually be Unicode but depends on the specified codecs.

        Bytes read from the file are decoded using file_encoding and then
        passed back to the caller encoded using data_encoding.

        If file_encoding is not given, it defaults to data_encoding.

        errors may be given to define the error handling. It defaults
        to 'strict' which causes ValueErrors to be raised in case an
        encoding error occurs.

        The returned wrapped file object provides two extra attributes
        .data_encoding and .file_encoding which reflect the given
        parameters of the same name. The attributes can be used for
        introspection by Python programs.

    '''
    init_inputs = [
        rc.NodeInputBP(label='file'),
rc.NodeInputBP(label='data_encoding'),
rc.NodeInputBP(label='file_encoding'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.EncodedFile(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_codecs_ascii_decode(rc.Node):
    title = 'ascii_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.ascii_decode(self.input(0), self.input(1)))
        


class AutoNode_codecs_ascii_encode(rc.Node):
    title = 'ascii_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.ascii_encode(self.input(0), self.input(1)))
        


class AutoNode_codecs_charmap_build(rc.Node):
    title = 'charmap_build'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='map'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.charmap_build(self.input(0)))
        


class AutoNode_codecs_charmap_decode(rc.Node):
    title = 'charmap_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='mapping'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.charmap_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_charmap_encode(rc.Node):
    title = 'charmap_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='mapping'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.charmap_encode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_code_page_decode(rc.Node):
    title = 'code_page_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='codepage'),
rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='final'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.code_page_decode(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_codecs_code_page_encode(rc.Node):
    title = 'code_page_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='code_page'),
rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.code_page_encode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_decode(rc.Node):
    title = 'decode'
    doc = '''Decodes obj using the codec registered for encoding.

Default encoding is 'utf-8'.  errors may be given to set a
different error handling scheme.  Default is 'strict' meaning that encoding
errors raise a ValueError.  Other possible values are 'ignore', 'replace'
and 'backslashreplace' as well as any other name registered with
codecs.register_error that can handle ValueErrors.'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
rc.NodeInputBP(label='encoding'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_encode(rc.Node):
    title = 'encode'
    doc = '''Encodes obj using the codec registered for encoding.

The default encoding is 'utf-8'.  errors may be given to set a
different error handling scheme.  Default is 'strict' meaning that encoding
errors raise a ValueError.  Other possible values are 'ignore', 'replace'
and 'backslashreplace' as well as any other name registered with
codecs.register_error that can handle ValueErrors.'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
rc.NodeInputBP(label='encoding'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.encode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_escape_decode(rc.Node):
    title = 'escape_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.escape_decode(self.input(0), self.input(1)))
        


class AutoNode_codecs_escape_encode(rc.Node):
    title = 'escape_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.escape_encode(self.input(0), self.input(1)))
        


class AutoNode_codecs_getdecoder(rc.Node):
    title = 'getdecoder'
    doc = ''' Lookup up the codec for the given encoding and return
        its decoder function.

        Raises a LookupError in case the encoding cannot be found.

    '''
    init_inputs = [
        rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.getdecoder(self.input(0)))
        


class AutoNode_codecs_getencoder(rc.Node):
    title = 'getencoder'
    doc = ''' Lookup up the codec for the given encoding and return
        its encoder function.

        Raises a LookupError in case the encoding cannot be found.

    '''
    init_inputs = [
        rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.getencoder(self.input(0)))
        


class AutoNode_codecs_getincrementaldecoder(rc.Node):
    title = 'getincrementaldecoder'
    doc = ''' Lookup up the codec for the given encoding and return
        its IncrementalDecoder class or factory function.

        Raises a LookupError in case the encoding cannot be found
        or the codecs doesn't provide an incremental decoder.

    '''
    init_inputs = [
        rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.getincrementaldecoder(self.input(0)))
        


class AutoNode_codecs_getincrementalencoder(rc.Node):
    title = 'getincrementalencoder'
    doc = ''' Lookup up the codec for the given encoding and return
        its IncrementalEncoder class or factory function.

        Raises a LookupError in case the encoding cannot be found
        or the codecs doesn't provide an incremental encoder.

    '''
    init_inputs = [
        rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.getincrementalencoder(self.input(0)))
        


class AutoNode_codecs_getreader(rc.Node):
    title = 'getreader'
    doc = ''' Lookup up the codec for the given encoding and return
        its StreamReader class or factory function.

        Raises a LookupError in case the encoding cannot be found.

    '''
    init_inputs = [
        rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.getreader(self.input(0)))
        


class AutoNode_codecs_getwriter(rc.Node):
    title = 'getwriter'
    doc = ''' Lookup up the codec for the given encoding and return
        its StreamWriter class or factory function.

        Raises a LookupError in case the encoding cannot be found.

    '''
    init_inputs = [
        rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.getwriter(self.input(0)))
        


class AutoNode_codecs_iterdecode(rc.Node):
    title = 'iterdecode'
    doc = '''
    Decoding iterator.

    Decodes the input strings from the iterator using an IncrementalDecoder.

    errors and kwargs are passed through to the IncrementalDecoder
    constructor.
    '''
    init_inputs = [
        rc.NodeInputBP(label='iterator'),
rc.NodeInputBP(label='encoding'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.iterdecode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_iterencode(rc.Node):
    title = 'iterencode'
    doc = '''
    Encoding iterator.

    Encodes the input strings from the iterator using an IncrementalEncoder.

    errors and kwargs are passed through to the IncrementalEncoder
    constructor.
    '''
    init_inputs = [
        rc.NodeInputBP(label='iterator'),
rc.NodeInputBP(label='encoding'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.iterencode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_latin_1_decode(rc.Node):
    title = 'latin_1_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.latin_1_decode(self.input(0), self.input(1)))
        


class AutoNode_codecs_latin_1_encode(rc.Node):
    title = 'latin_1_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.latin_1_encode(self.input(0), self.input(1)))
        


class AutoNode_codecs_lookup(rc.Node):
    title = 'lookup'
    doc = '''Looks up a codec tuple in the Python codec registry and returns a CodecInfo object.'''
    init_inputs = [
        rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.lookup(self.input(0)))
        


class AutoNode_codecs_lookup_error(rc.Node):
    title = 'lookup_error'
    doc = '''lookup_error(errors) -> handler

Return the error handler for the specified error handling name or raise a
LookupError, if no handler exists under this name.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.lookup_error(self.input(0)))
        


class AutoNode_codecs_make_encoding_map(rc.Node):
    title = 'make_encoding_map'
    doc = ''' Creates an encoding map from a decoding map.

        If a target mapping in the decoding map occurs multiple
        times, then that target is mapped to None (undefined mapping),
        causing an exception when encountered by the charmap codec
        during translation.

        One example where this happens is cp875.py which decodes
        multiple character to \u001a.

    '''
    init_inputs = [
        rc.NodeInputBP(label='decoding_map'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.make_encoding_map(self.input(0)))
        


class AutoNode_codecs_make_identity_dict(rc.Node):
    title = 'make_identity_dict'
    doc = ''' make_identity_dict(rng) -> dict

        Return a dictionary where elements of the rng sequence are
        mapped to themselves.

    '''
    init_inputs = [
        rc.NodeInputBP(label='rng'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.make_identity_dict(self.input(0)))
        


class AutoNode_codecs_mbcs_decode(rc.Node):
    title = 'mbcs_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='final'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.mbcs_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_mbcs_encode(rc.Node):
    title = 'mbcs_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.mbcs_encode(self.input(0), self.input(1)))
        


class AutoNode_codecs_oem_decode(rc.Node):
    title = 'oem_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='final'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.oem_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_oem_encode(rc.Node):
    title = 'oem_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.oem_encode(self.input(0), self.input(1)))
        


class AutoNode_codecs_open(rc.Node):
    title = 'open'
    doc = ''' Open an encoded file using the given mode and return
        a wrapped version providing transparent encoding/decoding.

        Note: The wrapped version will only accept the object format
        defined by the codecs, i.e. Unicode objects for most builtin
        codecs. Output is also codec dependent and will usually be
        Unicode as well.

        Underlying encoded files are always opened in binary mode.
        The default file mode is 'r', meaning to open the file in read mode.

        encoding specifies the encoding which is to be used for the
        file.

        errors may be given to define the error handling. It defaults
        to 'strict' which causes ValueErrors to be raised in case an
        encoding error occurs.

        buffering has the same meaning as for the builtin open() API.
        It defaults to -1 which means that the default buffer size will
        be used.

        The returned wrapped file object provides an extra attribute
        .encoding which allows querying the used encoding. This
        attribute is only available if an encoding was specified as
        parameter.

    '''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='mode'),
rc.NodeInputBP(label='encoding'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='buffering'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.open(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_codecs_raw_unicode_escape_decode(rc.Node):
    title = 'raw_unicode_escape_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.raw_unicode_escape_decode(self.input(0), self.input(1)))
        


class AutoNode_codecs_raw_unicode_escape_encode(rc.Node):
    title = 'raw_unicode_escape_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.raw_unicode_escape_encode(self.input(0), self.input(1)))
        


class AutoNode_codecs_readbuffer_encode(rc.Node):
    title = 'readbuffer_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.readbuffer_encode(self.input(0), self.input(1)))
        


class AutoNode_codecs_register(rc.Node):
    title = 'register'
    doc = '''Register a codec search function.

Search functions are expected to take one argument, the encoding name in
all lower case letters, and either return None, or a tuple of functions
(encoder, decoder, stream_reader, stream_writer) (or a CodecInfo object).'''
    init_inputs = [
        rc.NodeInputBP(label='search_function'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.register(self.input(0)))
        


class AutoNode_codecs_register_error(rc.Node):
    title = 'register_error'
    doc = '''Register the specified error handler under the name errors.

handler must be a callable object, that will be called with an exception
instance containing information about the location of the encoding/decoding
error and must return a (replacement, new position) tuple.'''
    init_inputs = [
        rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='handler'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.register_error(self.input(0), self.input(1)))
        


class AutoNode_codecs_unicode_escape_decode(rc.Node):
    title = 'unicode_escape_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.unicode_escape_decode(self.input(0), self.input(1)))
        


class AutoNode_codecs_unicode_escape_encode(rc.Node):
    title = 'unicode_escape_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.unicode_escape_encode(self.input(0), self.input(1)))
        


class AutoNode_codecs_utf_16_be_decode(rc.Node):
    title = 'utf_16_be_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='final'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_16_be_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_utf_16_be_encode(rc.Node):
    title = 'utf_16_be_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_16_be_encode(self.input(0), self.input(1)))
        


class AutoNode_codecs_utf_16_decode(rc.Node):
    title = 'utf_16_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='final'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_16_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_utf_16_encode(rc.Node):
    title = 'utf_16_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='byteorder'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_16_encode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_utf_16_ex_decode(rc.Node):
    title = 'utf_16_ex_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='byteorder'),
rc.NodeInputBP(label='final'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_16_ex_decode(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_codecs_utf_16_le_decode(rc.Node):
    title = 'utf_16_le_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='final'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_16_le_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_utf_16_le_encode(rc.Node):
    title = 'utf_16_le_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_16_le_encode(self.input(0), self.input(1)))
        


class AutoNode_codecs_utf_32_be_decode(rc.Node):
    title = 'utf_32_be_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='final'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_32_be_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_utf_32_be_encode(rc.Node):
    title = 'utf_32_be_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_32_be_encode(self.input(0), self.input(1)))
        


class AutoNode_codecs_utf_32_decode(rc.Node):
    title = 'utf_32_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='final'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_32_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_utf_32_encode(rc.Node):
    title = 'utf_32_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='byteorder'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_32_encode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_utf_32_ex_decode(rc.Node):
    title = 'utf_32_ex_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='byteorder'),
rc.NodeInputBP(label='final'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_32_ex_decode(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_codecs_utf_32_le_decode(rc.Node):
    title = 'utf_32_le_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='final'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_32_le_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_utf_32_le_encode(rc.Node):
    title = 'utf_32_le_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_32_le_encode(self.input(0), self.input(1)))
        


class AutoNode_codecs_utf_7_decode(rc.Node):
    title = 'utf_7_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='final'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_7_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_utf_7_encode(rc.Node):
    title = 'utf_7_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_7_encode(self.input(0), self.input(1)))
        


class AutoNode_codecs_utf_8_decode(rc.Node):
    title = 'utf_8_decode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
rc.NodeInputBP(label='final'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_8_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_codecs_utf_8_encode(rc.Node):
    title = 'utf_8_encode'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, codecs.utf_8_encode(self.input(0), self.input(1)))
        