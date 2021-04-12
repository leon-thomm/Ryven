import ryvencore_qt as rc
import _codecs


class AutoNode__codecs__forget_codec(rc.Node):
    title = '_forget_codec'
    type_ = '_codecs'
    description = '''Purge the named codec from the internal codec lookup cache'''
    init_inputs = [
        rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs._forget_codec(self.input(0)))
        


class AutoNode__codecs_ascii_decode(rc.Node):
    title = 'ascii_decode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.ascii_decode(self.input(0), self.input(1)))
        


class AutoNode__codecs_ascii_encode(rc.Node):
    title = 'ascii_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.ascii_encode(self.input(0), self.input(1)))
        


class AutoNode__codecs_charmap_build(rc.Node):
    title = 'charmap_build'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='map'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.charmap_build(self.input(0)))
        


class AutoNode__codecs_charmap_decode(rc.Node):
    title = 'charmap_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.charmap_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_charmap_encode(rc.Node):
    title = 'charmap_encode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.charmap_encode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_code_page_decode(rc.Node):
    title = 'code_page_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.code_page_decode(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode__codecs_code_page_encode(rc.Node):
    title = 'code_page_encode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.code_page_encode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_decode(rc.Node):
    title = 'decode'
    type_ = '_codecs'
    description = '''Decodes obj using the codec registered for encoding.

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
        self.set_output_val(0, _codecs.decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_encode(rc.Node):
    title = 'encode'
    type_ = '_codecs'
    description = '''Encodes obj using the codec registered for encoding.

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
        self.set_output_val(0, _codecs.encode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_escape_decode(rc.Node):
    title = 'escape_decode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.escape_decode(self.input(0), self.input(1)))
        


class AutoNode__codecs_escape_encode(rc.Node):
    title = 'escape_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.escape_encode(self.input(0), self.input(1)))
        


class AutoNode__codecs_latin_1_decode(rc.Node):
    title = 'latin_1_decode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.latin_1_decode(self.input(0), self.input(1)))
        


class AutoNode__codecs_latin_1_encode(rc.Node):
    title = 'latin_1_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.latin_1_encode(self.input(0), self.input(1)))
        


class AutoNode__codecs_lookup(rc.Node):
    title = 'lookup'
    type_ = '_codecs'
    description = '''Looks up a codec tuple in the Python codec registry and returns a CodecInfo object.'''
    init_inputs = [
        rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.lookup(self.input(0)))
        


class AutoNode__codecs_lookup_error(rc.Node):
    title = 'lookup_error'
    type_ = '_codecs'
    description = '''lookup_error(errors) -> handler

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
        self.set_output_val(0, _codecs.lookup_error(self.input(0)))
        


class AutoNode__codecs_mbcs_decode(rc.Node):
    title = 'mbcs_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.mbcs_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_mbcs_encode(rc.Node):
    title = 'mbcs_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.mbcs_encode(self.input(0), self.input(1)))
        


class AutoNode__codecs_oem_decode(rc.Node):
    title = 'oem_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.oem_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_oem_encode(rc.Node):
    title = 'oem_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.oem_encode(self.input(0), self.input(1)))
        


class AutoNode__codecs_raw_unicode_escape_decode(rc.Node):
    title = 'raw_unicode_escape_decode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.raw_unicode_escape_decode(self.input(0), self.input(1)))
        


class AutoNode__codecs_raw_unicode_escape_encode(rc.Node):
    title = 'raw_unicode_escape_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.raw_unicode_escape_encode(self.input(0), self.input(1)))
        


class AutoNode__codecs_readbuffer_encode(rc.Node):
    title = 'readbuffer_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.readbuffer_encode(self.input(0), self.input(1)))
        


class AutoNode__codecs_register(rc.Node):
    title = 'register'
    type_ = '_codecs'
    description = '''Register a codec search function.

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
        self.set_output_val(0, _codecs.register(self.input(0)))
        


class AutoNode__codecs_register_error(rc.Node):
    title = 'register_error'
    type_ = '_codecs'
    description = '''Register the specified error handler under the name errors.

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
        self.set_output_val(0, _codecs.register_error(self.input(0), self.input(1)))
        


class AutoNode__codecs_unicode_escape_decode(rc.Node):
    title = 'unicode_escape_decode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.unicode_escape_decode(self.input(0), self.input(1)))
        


class AutoNode__codecs_unicode_escape_encode(rc.Node):
    title = 'unicode_escape_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.unicode_escape_encode(self.input(0), self.input(1)))
        


class AutoNode__codecs_utf_16_be_decode(rc.Node):
    title = 'utf_16_be_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.utf_16_be_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_utf_16_be_encode(rc.Node):
    title = 'utf_16_be_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_16_be_encode(self.input(0), self.input(1)))
        


class AutoNode__codecs_utf_16_decode(rc.Node):
    title = 'utf_16_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.utf_16_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_utf_16_encode(rc.Node):
    title = 'utf_16_encode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.utf_16_encode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_utf_16_ex_decode(rc.Node):
    title = 'utf_16_ex_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.utf_16_ex_decode(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode__codecs_utf_16_le_decode(rc.Node):
    title = 'utf_16_le_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.utf_16_le_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_utf_16_le_encode(rc.Node):
    title = 'utf_16_le_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_16_le_encode(self.input(0), self.input(1)))
        


class AutoNode__codecs_utf_32_be_decode(rc.Node):
    title = 'utf_32_be_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.utf_32_be_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_utf_32_be_encode(rc.Node):
    title = 'utf_32_be_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_32_be_encode(self.input(0), self.input(1)))
        


class AutoNode__codecs_utf_32_decode(rc.Node):
    title = 'utf_32_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.utf_32_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_utf_32_encode(rc.Node):
    title = 'utf_32_encode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.utf_32_encode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_utf_32_ex_decode(rc.Node):
    title = 'utf_32_ex_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.utf_32_ex_decode(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode__codecs_utf_32_le_decode(rc.Node):
    title = 'utf_32_le_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.utf_32_le_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_utf_32_le_encode(rc.Node):
    title = 'utf_32_le_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_32_le_encode(self.input(0), self.input(1)))
        


class AutoNode__codecs_utf_7_decode(rc.Node):
    title = 'utf_7_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.utf_7_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_utf_7_encode(rc.Node):
    title = 'utf_7_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_7_encode(self.input(0), self.input(1)))
        


class AutoNode__codecs_utf_8_decode(rc.Node):
    title = 'utf_8_decode'
    type_ = '_codecs'
    description = ''''''
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
        self.set_output_val(0, _codecs.utf_8_decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__codecs_utf_8_encode(rc.Node):
    title = 'utf_8_encode'
    type_ = '_codecs'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='str'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_8_encode(self.input(0), self.input(1)))
        