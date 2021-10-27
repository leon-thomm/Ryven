
from NENV import *

import codecs


class NodeBase(Node):
    pass


class Encodedfile_Node(NodeBase):
    """
     Return a wrapped version of file which provides transparent
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

    """
    
    title = 'EncodedFile'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='file'),
        NodeInputBP(label='data_encoding'),
        NodeInputBP(label='file_encoding', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='errors', dtype=dtypes.Data(default='strict', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.EncodedFile(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Ascii_Decode_Node(NodeBase):
    """
    """
    
    title = 'ascii_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.ascii_decode(self.input(0), self.input(1)))
        

class Ascii_Encode_Node(NodeBase):
    """
    """
    
    title = 'ascii_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.ascii_encode(self.input(0), self.input(1)))
        

class Charmap_Build_Node(NodeBase):
    """
    """
    
    title = 'charmap_build'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='map'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.charmap_build(self.input(0)))
        

class Charmap_Decode_Node(NodeBase):
    """
    """
    
    title = 'charmap_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='mapping', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.charmap_decode(self.input(0), self.input(1), self.input(2)))
        

class Charmap_Encode_Node(NodeBase):
    """
    """
    
    title = 'charmap_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='mapping', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.charmap_encode(self.input(0), self.input(1), self.input(2)))
        

class Code_Page_Decode_Node(NodeBase):
    """
    """
    
    title = 'code_page_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='codepage'),
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='final', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.code_page_decode(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Code_Page_Encode_Node(NodeBase):
    """
    """
    
    title = 'code_page_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='code_page'),
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.code_page_encode(self.input(0), self.input(1), self.input(2)))
        

class Decode_Node(NodeBase):
    """
    Decodes obj using the codec registered for encoding.

Default encoding is 'utf-8'.  errors may be given to set a
different error handling scheme.  Default is 'strict' meaning that encoding
errors raise a ValueError.  Other possible values are 'ignore', 'replace'
and 'backslashreplace' as well as any other name registered with
codecs.register_error that can handle ValueErrors."""
    
    title = 'decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='encoding', dtype=dtypes.Data(default='utf-8', size='s')),
        NodeInputBP(label='errors', dtype=dtypes.Data(default='strict', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.decode(self.input(0), self.input(1), self.input(2)))
        

class Encode_Node(NodeBase):
    """
    Encodes obj using the codec registered for encoding.

The default encoding is 'utf-8'.  errors may be given to set a
different error handling scheme.  Default is 'strict' meaning that encoding
errors raise a ValueError.  Other possible values are 'ignore', 'replace'
and 'backslashreplace' as well as any other name registered with
codecs.register_error that can handle ValueErrors."""
    
    title = 'encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='encoding', dtype=dtypes.Data(default='utf-8', size='s')),
        NodeInputBP(label='errors', dtype=dtypes.Data(default='strict', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.encode(self.input(0), self.input(1), self.input(2)))
        

class Escape_Decode_Node(NodeBase):
    """
    """
    
    title = 'escape_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.escape_decode(self.input(0), self.input(1)))
        

class Escape_Encode_Node(NodeBase):
    """
    """
    
    title = 'escape_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.escape_encode(self.input(0), self.input(1)))
        

class Getdecoder_Node(NodeBase):
    """
     Lookup up the codec for the given encoding and return
        its decoder function.

        Raises a LookupError in case the encoding cannot be found.

    """
    
    title = 'getdecoder'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.getdecoder(self.input(0)))
        

class Getencoder_Node(NodeBase):
    """
     Lookup up the codec for the given encoding and return
        its encoder function.

        Raises a LookupError in case the encoding cannot be found.

    """
    
    title = 'getencoder'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.getencoder(self.input(0)))
        

class Getincrementaldecoder_Node(NodeBase):
    """
     Lookup up the codec for the given encoding and return
        its IncrementalDecoder class or factory function.

        Raises a LookupError in case the encoding cannot be found
        or the codecs doesn't provide an incremental decoder.

    """
    
    title = 'getincrementaldecoder'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.getincrementaldecoder(self.input(0)))
        

class Getincrementalencoder_Node(NodeBase):
    """
     Lookup up the codec for the given encoding and return
        its IncrementalEncoder class or factory function.

        Raises a LookupError in case the encoding cannot be found
        or the codecs doesn't provide an incremental encoder.

    """
    
    title = 'getincrementalencoder'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.getincrementalencoder(self.input(0)))
        

class Getreader_Node(NodeBase):
    """
     Lookup up the codec for the given encoding and return
        its StreamReader class or factory function.

        Raises a LookupError in case the encoding cannot be found.

    """
    
    title = 'getreader'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.getreader(self.input(0)))
        

class Getwriter_Node(NodeBase):
    """
     Lookup up the codec for the given encoding and return
        its StreamWriter class or factory function.

        Raises a LookupError in case the encoding cannot be found.

    """
    
    title = 'getwriter'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.getwriter(self.input(0)))
        

class Iterdecode_Node(NodeBase):
    """
    
    Decoding iterator.

    Decodes the input strings from the iterator using an IncrementalDecoder.

    errors and kwargs are passed through to the IncrementalDecoder
    constructor.
    """
    
    title = 'iterdecode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='iterator'),
        NodeInputBP(label='encoding'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default='strict', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.iterdecode(self.input(0), self.input(1), self.input(2)))
        

class Iterencode_Node(NodeBase):
    """
    
    Encoding iterator.

    Encodes the input strings from the iterator using an IncrementalEncoder.

    errors and kwargs are passed through to the IncrementalEncoder
    constructor.
    """
    
    title = 'iterencode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='iterator'),
        NodeInputBP(label='encoding'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default='strict', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.iterencode(self.input(0), self.input(1), self.input(2)))
        

class Latin_1_Decode_Node(NodeBase):
    """
    """
    
    title = 'latin_1_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.latin_1_decode(self.input(0), self.input(1)))
        

class Latin_1_Encode_Node(NodeBase):
    """
    """
    
    title = 'latin_1_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.latin_1_encode(self.input(0), self.input(1)))
        

class Lookup_Node(NodeBase):
    """
    Looks up a codec tuple in the Python codec registry and returns a CodecInfo object."""
    
    title = 'lookup'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.lookup(self.input(0)))
        

class Lookup_Error_Node(NodeBase):
    """
    lookup_error(errors) -> handler

Return the error handler for the specified error handling name or raise a
LookupError, if no handler exists under this name."""
    
    title = 'lookup_error'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.lookup_error(self.input(0)))
        

class Make_Encoding_Map_Node(NodeBase):
    """
     Creates an encoding map from a decoding map.

        If a target mapping in the decoding map occurs multiple
        times, then that target is mapped to None (undefined mapping),
        causing an exception when encountered by the charmap codec
        during translation.

        One example where this happens is cp875.py which decodes
        multiple character to \u001a.

    """
    
    title = 'make_encoding_map'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='decoding_map'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.make_encoding_map(self.input(0)))
        

class Make_Identity_Dict_Node(NodeBase):
    """
     make_identity_dict(rng) -> dict

        Return a dictionary where elements of the rng sequence are
        mapped to themselves.

    """
    
    title = 'make_identity_dict'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='rng'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.make_identity_dict(self.input(0)))
        

class Mbcs_Decode_Node(NodeBase):
    """
    """
    
    title = 'mbcs_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='final', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.mbcs_decode(self.input(0), self.input(1), self.input(2)))
        

class Mbcs_Encode_Node(NodeBase):
    """
    """
    
    title = 'mbcs_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.mbcs_encode(self.input(0), self.input(1)))
        

class Oem_Decode_Node(NodeBase):
    """
    """
    
    title = 'oem_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='final', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.oem_decode(self.input(0), self.input(1), self.input(2)))
        

class Oem_Encode_Node(NodeBase):
    """
    """
    
    title = 'oem_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.oem_encode(self.input(0), self.input(1)))
        

class Open_Node(NodeBase):
    """
     Open an encoded file using the given mode and return
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

    """
    
    title = 'open'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='mode', dtype=dtypes.Data(default='r', size='s')),
        NodeInputBP(label='encoding', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='errors', dtype=dtypes.Data(default='strict', size='s')),
        NodeInputBP(label='buffering', dtype=dtypes.Data(default=-1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.open(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Raw_Unicode_Escape_Decode_Node(NodeBase):
    """
    """
    
    title = 'raw_unicode_escape_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.raw_unicode_escape_decode(self.input(0), self.input(1)))
        

class Raw_Unicode_Escape_Encode_Node(NodeBase):
    """
    """
    
    title = 'raw_unicode_escape_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.raw_unicode_escape_encode(self.input(0), self.input(1)))
        

class Readbuffer_Encode_Node(NodeBase):
    """
    """
    
    title = 'readbuffer_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.readbuffer_encode(self.input(0), self.input(1)))
        

class Register_Node(NodeBase):
    """
    Register a codec search function.

Search functions are expected to take one argument, the encoding name in
all lower case letters, and either return None, or a tuple of functions
(encoder, decoder, stream_reader, stream_writer) (or a CodecInfo object)."""
    
    title = 'register'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='search_function'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.register(self.input(0)))
        

class Register_Error_Node(NodeBase):
    """
    Register the specified error handler under the name errors.

handler must be a callable object, that will be called with an exception
instance containing information about the location of the encoding/decoding
error and must return a (replacement, new position) tuple."""
    
    title = 'register_error'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='errors'),
        NodeInputBP(label='handler'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.register_error(self.input(0), self.input(1)))
        

class Unicode_Escape_Decode_Node(NodeBase):
    """
    """
    
    title = 'unicode_escape_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.unicode_escape_decode(self.input(0), self.input(1)))
        

class Unicode_Escape_Encode_Node(NodeBase):
    """
    """
    
    title = 'unicode_escape_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.unicode_escape_encode(self.input(0), self.input(1)))
        

class Utf_16_Be_Decode_Node(NodeBase):
    """
    """
    
    title = 'utf_16_be_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='final', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_16_be_decode(self.input(0), self.input(1), self.input(2)))
        

class Utf_16_Be_Encode_Node(NodeBase):
    """
    """
    
    title = 'utf_16_be_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_16_be_encode(self.input(0), self.input(1)))
        

class Utf_16_Decode_Node(NodeBase):
    """
    """
    
    title = 'utf_16_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='final', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_16_decode(self.input(0), self.input(1), self.input(2)))
        

class Utf_16_Encode_Node(NodeBase):
    """
    """
    
    title = 'utf_16_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='byteorder', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_16_encode(self.input(0), self.input(1), self.input(2)))
        

class Utf_16_Ex_Decode_Node(NodeBase):
    """
    """
    
    title = 'utf_16_ex_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='byteorder', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='final', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_16_ex_decode(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Utf_16_Le_Decode_Node(NodeBase):
    """
    """
    
    title = 'utf_16_le_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='final', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_16_le_decode(self.input(0), self.input(1), self.input(2)))
        

class Utf_16_Le_Encode_Node(NodeBase):
    """
    """
    
    title = 'utf_16_le_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_16_le_encode(self.input(0), self.input(1)))
        

class Utf_32_Be_Decode_Node(NodeBase):
    """
    """
    
    title = 'utf_32_be_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='final', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_32_be_decode(self.input(0), self.input(1), self.input(2)))
        

class Utf_32_Be_Encode_Node(NodeBase):
    """
    """
    
    title = 'utf_32_be_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_32_be_encode(self.input(0), self.input(1)))
        

class Utf_32_Decode_Node(NodeBase):
    """
    """
    
    title = 'utf_32_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='final', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_32_decode(self.input(0), self.input(1), self.input(2)))
        

class Utf_32_Encode_Node(NodeBase):
    """
    """
    
    title = 'utf_32_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='byteorder', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_32_encode(self.input(0), self.input(1), self.input(2)))
        

class Utf_32_Ex_Decode_Node(NodeBase):
    """
    """
    
    title = 'utf_32_ex_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='byteorder', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='final', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_32_ex_decode(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Utf_32_Le_Decode_Node(NodeBase):
    """
    """
    
    title = 'utf_32_le_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='final', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_32_le_decode(self.input(0), self.input(1), self.input(2)))
        

class Utf_32_Le_Encode_Node(NodeBase):
    """
    """
    
    title = 'utf_32_le_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_32_le_encode(self.input(0), self.input(1)))
        

class Utf_7_Decode_Node(NodeBase):
    """
    """
    
    title = 'utf_7_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='final', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_7_decode(self.input(0), self.input(1), self.input(2)))
        

class Utf_7_Encode_Node(NodeBase):
    """
    """
    
    title = 'utf_7_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_7_encode(self.input(0), self.input(1)))
        

class Utf_8_Decode_Node(NodeBase):
    """
    """
    
    title = 'utf_8_decode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='final', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_8_decode(self.input(0), self.input(1), self.input(2)))
        

class Utf_8_Encode_Node(NodeBase):
    """
    """
    
    title = 'utf_8_encode'
    type_ = 'codecs'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, codecs.utf_8_encode(self.input(0), self.input(1)))
        


export_nodes(
    Encodedfile_Node,
    Ascii_Decode_Node,
    Ascii_Encode_Node,
    Charmap_Build_Node,
    Charmap_Decode_Node,
    Charmap_Encode_Node,
    Code_Page_Decode_Node,
    Code_Page_Encode_Node,
    Decode_Node,
    Encode_Node,
    Escape_Decode_Node,
    Escape_Encode_Node,
    Getdecoder_Node,
    Getencoder_Node,
    Getincrementaldecoder_Node,
    Getincrementalencoder_Node,
    Getreader_Node,
    Getwriter_Node,
    Iterdecode_Node,
    Iterencode_Node,
    Latin_1_Decode_Node,
    Latin_1_Encode_Node,
    Lookup_Node,
    Lookup_Error_Node,
    Make_Encoding_Map_Node,
    Make_Identity_Dict_Node,
    Mbcs_Decode_Node,
    Mbcs_Encode_Node,
    Oem_Decode_Node,
    Oem_Encode_Node,
    Open_Node,
    Raw_Unicode_Escape_Decode_Node,
    Raw_Unicode_Escape_Encode_Node,
    Readbuffer_Encode_Node,
    Register_Node,
    Register_Error_Node,
    Unicode_Escape_Decode_Node,
    Unicode_Escape_Encode_Node,
    Utf_16_Be_Decode_Node,
    Utf_16_Be_Encode_Node,
    Utf_16_Decode_Node,
    Utf_16_Encode_Node,
    Utf_16_Ex_Decode_Node,
    Utf_16_Le_Decode_Node,
    Utf_16_Le_Encode_Node,
    Utf_32_Be_Decode_Node,
    Utf_32_Be_Encode_Node,
    Utf_32_Decode_Node,
    Utf_32_Encode_Node,
    Utf_32_Ex_Decode_Node,
    Utf_32_Le_Decode_Node,
    Utf_32_Le_Encode_Node,
    Utf_7_Decode_Node,
    Utf_7_Encode_Node,
    Utf_8_Decode_Node,
    Utf_8_Encode_Node,
)
