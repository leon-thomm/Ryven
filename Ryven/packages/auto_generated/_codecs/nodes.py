
from NENV import *

import _codecs


class NodeBase(Node):
    pass


class AutoNode__codecs__forget_codec(NodeBase):
    title = '_forget_codec'
    type_ = '_codecs'
    doc = """Purge the named codec from the internal codec lookup cache"""
    init_inputs = [
        NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs._forget_codec(self.input(0)))
        

class AutoNode__codecs_ascii_decode(NodeBase):
    title = 'ascii_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.ascii_decode(self.input(0), self.input(1)))
        

class AutoNode__codecs_ascii_encode(NodeBase):
    title = 'ascii_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.ascii_encode(self.input(0), self.input(1)))
        

class AutoNode__codecs_charmap_build(NodeBase):
    title = 'charmap_build'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='map'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.charmap_build(self.input(0)))
        

class AutoNode__codecs_charmap_decode(NodeBase):
    title = 'charmap_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='mapping'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.charmap_decode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_charmap_encode(NodeBase):
    title = 'charmap_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='mapping'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.charmap_encode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_code_page_decode(NodeBase):
    title = 'code_page_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='codepage'),
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='final'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.code_page_decode(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class AutoNode__codecs_code_page_encode(NodeBase):
    title = 'code_page_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='code_page'),
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.code_page_encode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_decode(NodeBase):
    title = 'decode'
    type_ = '_codecs'
    doc = """Decodes obj using the codec registered for encoding.

Default encoding is 'utf-8'.  errors may be given to set a
different error handling scheme.  Default is 'strict' meaning that encoding
errors raise a ValueError.  Other possible values are 'ignore', 'replace'
and 'backslashreplace' as well as any other name registered with
codecs.register_error that can handle ValueErrors."""
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='encoding'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.decode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_encode(NodeBase):
    title = 'encode'
    type_ = '_codecs'
    doc = """Encodes obj using the codec registered for encoding.

The default encoding is 'utf-8'.  errors may be given to set a
different error handling scheme.  Default is 'strict' meaning that encoding
errors raise a ValueError.  Other possible values are 'ignore', 'replace'
and 'backslashreplace' as well as any other name registered with
codecs.register_error that can handle ValueErrors."""
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='encoding'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.encode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_escape_decode(NodeBase):
    title = 'escape_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.escape_decode(self.input(0), self.input(1)))
        

class AutoNode__codecs_escape_encode(NodeBase):
    title = 'escape_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.escape_encode(self.input(0), self.input(1)))
        

class AutoNode__codecs_latin_1_decode(NodeBase):
    title = 'latin_1_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.latin_1_decode(self.input(0), self.input(1)))
        

class AutoNode__codecs_latin_1_encode(NodeBase):
    title = 'latin_1_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.latin_1_encode(self.input(0), self.input(1)))
        

class AutoNode__codecs_lookup(NodeBase):
    title = 'lookup'
    type_ = '_codecs'
    doc = """Looks up a codec tuple in the Python codec registry and returns a CodecInfo object."""
    init_inputs = [
        NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.lookup(self.input(0)))
        

class AutoNode__codecs_lookup_error(NodeBase):
    title = 'lookup_error'
    type_ = '_codecs'
    doc = """lookup_error(errors) -> handler

Return the error handler for the specified error handling name or raise a
LookupError, if no handler exists under this name."""
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.lookup_error(self.input(0)))
        

class AutoNode__codecs_mbcs_decode(NodeBase):
    title = 'mbcs_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='final'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.mbcs_decode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_mbcs_encode(NodeBase):
    title = 'mbcs_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.mbcs_encode(self.input(0), self.input(1)))
        

class AutoNode__codecs_oem_decode(NodeBase):
    title = 'oem_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='final'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.oem_decode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_oem_encode(NodeBase):
    title = 'oem_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.oem_encode(self.input(0), self.input(1)))
        

class AutoNode__codecs_raw_unicode_escape_decode(NodeBase):
    title = 'raw_unicode_escape_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.raw_unicode_escape_decode(self.input(0), self.input(1)))
        

class AutoNode__codecs_raw_unicode_escape_encode(NodeBase):
    title = 'raw_unicode_escape_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.raw_unicode_escape_encode(self.input(0), self.input(1)))
        

class AutoNode__codecs_readbuffer_encode(NodeBase):
    title = 'readbuffer_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.readbuffer_encode(self.input(0), self.input(1)))
        

class AutoNode__codecs_register(NodeBase):
    title = 'register'
    type_ = '_codecs'
    doc = """Register a codec search function.

Search functions are expected to take one argument, the encoding name in
all lower case letters, and either return None, or a tuple of functions
(encoder, decoder, stream_reader, stream_writer) (or a CodecInfo object)."""
    init_inputs = [
        NodeInputBP(label='search_function'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.register(self.input(0)))
        

class AutoNode__codecs_register_error(NodeBase):
    title = 'register_error'
    type_ = '_codecs'
    doc = """Register the specified error handler under the name errors.

handler must be a callable object, that will be called with an exception
instance containing information about the location of the encoding/decoding
error and must return a (replacement, new position) tuple."""
    init_inputs = [
        NodeInputBP(label='errors'),
        NodeInputBP(label='handler'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.register_error(self.input(0), self.input(1)))
        

class AutoNode__codecs_unicode_escape_decode(NodeBase):
    title = 'unicode_escape_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.unicode_escape_decode(self.input(0), self.input(1)))
        

class AutoNode__codecs_unicode_escape_encode(NodeBase):
    title = 'unicode_escape_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.unicode_escape_encode(self.input(0), self.input(1)))
        

class AutoNode__codecs_utf_16_be_decode(NodeBase):
    title = 'utf_16_be_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='final'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_16_be_decode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_utf_16_be_encode(NodeBase):
    title = 'utf_16_be_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_16_be_encode(self.input(0), self.input(1)))
        

class AutoNode__codecs_utf_16_decode(NodeBase):
    title = 'utf_16_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='final'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_16_decode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_utf_16_encode(NodeBase):
    title = 'utf_16_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='byteorder'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_16_encode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_utf_16_ex_decode(NodeBase):
    title = 'utf_16_ex_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='byteorder'),
        NodeInputBP(label='final'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_16_ex_decode(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class AutoNode__codecs_utf_16_le_decode(NodeBase):
    title = 'utf_16_le_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='final'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_16_le_decode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_utf_16_le_encode(NodeBase):
    title = 'utf_16_le_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_16_le_encode(self.input(0), self.input(1)))
        

class AutoNode__codecs_utf_32_be_decode(NodeBase):
    title = 'utf_32_be_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='final'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_32_be_decode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_utf_32_be_encode(NodeBase):
    title = 'utf_32_be_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_32_be_encode(self.input(0), self.input(1)))
        

class AutoNode__codecs_utf_32_decode(NodeBase):
    title = 'utf_32_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='final'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_32_decode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_utf_32_encode(NodeBase):
    title = 'utf_32_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='byteorder'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_32_encode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_utf_32_ex_decode(NodeBase):
    title = 'utf_32_ex_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='byteorder'),
        NodeInputBP(label='final'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_32_ex_decode(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class AutoNode__codecs_utf_32_le_decode(NodeBase):
    title = 'utf_32_le_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='final'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_32_le_decode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_utf_32_le_encode(NodeBase):
    title = 'utf_32_le_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_32_le_encode(self.input(0), self.input(1)))
        

class AutoNode__codecs_utf_7_decode(NodeBase):
    title = 'utf_7_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='final'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_7_decode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_utf_7_encode(NodeBase):
    title = 'utf_7_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_7_encode(self.input(0), self.input(1)))
        

class AutoNode__codecs_utf_8_decode(NodeBase):
    title = 'utf_8_decode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='final'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_8_decode(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__codecs_utf_8_encode(NodeBase):
    title = 'utf_8_encode'
    type_ = '_codecs'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _codecs.utf_8_encode(self.input(0), self.input(1)))
        


export_nodes(
    AutoNode__codecs__forget_codec,
    AutoNode__codecs_ascii_decode,
    AutoNode__codecs_ascii_encode,
    AutoNode__codecs_charmap_build,
    AutoNode__codecs_charmap_decode,
    AutoNode__codecs_charmap_encode,
    AutoNode__codecs_code_page_decode,
    AutoNode__codecs_code_page_encode,
    AutoNode__codecs_decode,
    AutoNode__codecs_encode,
    AutoNode__codecs_escape_decode,
    AutoNode__codecs_escape_encode,
    AutoNode__codecs_latin_1_decode,
    AutoNode__codecs_latin_1_encode,
    AutoNode__codecs_lookup,
    AutoNode__codecs_lookup_error,
    AutoNode__codecs_mbcs_decode,
    AutoNode__codecs_mbcs_encode,
    AutoNode__codecs_oem_decode,
    AutoNode__codecs_oem_encode,
    AutoNode__codecs_raw_unicode_escape_decode,
    AutoNode__codecs_raw_unicode_escape_encode,
    AutoNode__codecs_readbuffer_encode,
    AutoNode__codecs_register,
    AutoNode__codecs_register_error,
    AutoNode__codecs_unicode_escape_decode,
    AutoNode__codecs_unicode_escape_encode,
    AutoNode__codecs_utf_16_be_decode,
    AutoNode__codecs_utf_16_be_encode,
    AutoNode__codecs_utf_16_decode,
    AutoNode__codecs_utf_16_encode,
    AutoNode__codecs_utf_16_ex_decode,
    AutoNode__codecs_utf_16_le_decode,
    AutoNode__codecs_utf_16_le_encode,
    AutoNode__codecs_utf_32_be_decode,
    AutoNode__codecs_utf_32_be_encode,
    AutoNode__codecs_utf_32_decode,
    AutoNode__codecs_utf_32_encode,
    AutoNode__codecs_utf_32_ex_decode,
    AutoNode__codecs_utf_32_le_decode,
    AutoNode__codecs_utf_32_le_encode,
    AutoNode__codecs_utf_7_decode,
    AutoNode__codecs_utf_7_encode,
    AutoNode__codecs_utf_8_decode,
    AutoNode__codecs_utf_8_encode,
)
