import ryvencore_qt as rc
import base64


class AutoNode_base64__85encode(rc.Node):
    title = '_85encode'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='b'),
rc.NodeInputBP(label='chars'),
rc.NodeInputBP(label='chars2'),
rc.NodeInputBP(label='pad'),
rc.NodeInputBP(label='foldnuls'),
rc.NodeInputBP(label='foldspaces'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64._85encode(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode_base64__bytes_from_decode_data(rc.Node):
    title = '_bytes_from_decode_data'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64._bytes_from_decode_data(self.input(0)))
        


class AutoNode_base64__input_type_check(rc.Node):
    title = '_input_type_check'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64._input_type_check(self.input(0)))
        


class AutoNode_base64_a85decode(rc.Node):
    title = 'a85decode'
    description = '''Decode the Ascii85 encoded bytes-like object or ASCII string b.

    foldspaces is a flag that specifies whether the 'y' short sequence should be
    accepted as shorthand for 4 consecutive spaces (ASCII 0x20). This feature is
    not supported by the "standard" Adobe encoding.

    adobe controls whether the input sequence is in Adobe Ascii85 format (i.e.
    is framed with <~ and ~>).

    ignorechars should be a byte string containing characters to ignore from the
    input. This should only contain whitespace characters, and by default
    contains all whitespace characters in ASCII.

    The result is returned as a bytes object.
    '''
    init_inputs = [
        rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.a85decode(self.input(0)))
        


class AutoNode_base64_a85encode(rc.Node):
    title = 'a85encode'
    description = '''Encode bytes-like object b using Ascii85 and return a bytes object.

    foldspaces is an optional flag that uses the special short sequence 'y'
    instead of 4 consecutive spaces (ASCII 0x20) as supported by 'btoa'. This
    feature is not supported by the "standard" Adobe encoding.

    wrapcol controls whether the output should have newline (b'\n') characters
    added to it. If this is non-zero, each output line will be at most this
    many characters long.

    pad controls whether the input is padded to a multiple of 4 before
    encoding. Note that the btoa implementation always pads.

    adobe controls whether the encoded byte sequence is framed with <~ and ~>,
    which is used by the Adobe implementation.
    '''
    init_inputs = [
        rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.a85encode(self.input(0)))
        


class AutoNode_base64_b16decode(rc.Node):
    title = 'b16decode'
    description = '''Decode the Base16 encoded bytes-like object or ASCII string s.

    Optional casefold is a flag specifying whether a lowercase alphabet is
    acceptable as input.  For security purposes, the default is False.

    The result is returned as a bytes object.  A binascii.Error is raised if
    s is incorrectly padded or if there are non-alphabet characters present
    in the input.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='casefold'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.b16decode(self.input(0), self.input(1)))
        


class AutoNode_base64_b16encode(rc.Node):
    title = 'b16encode'
    description = '''Encode the bytes-like object s using Base16 and return a bytes object.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.b16encode(self.input(0)))
        


class AutoNode_base64_b32decode(rc.Node):
    title = 'b32decode'
    description = '''Decode the Base32 encoded bytes-like object or ASCII string s.

    Optional casefold is a flag specifying whether a lowercase alphabet is
    acceptable as input.  For security purposes, the default is False.

    RFC 3548 allows for optional mapping of the digit 0 (zero) to the
    letter O (oh), and for optional mapping of the digit 1 (one) to
    either the letter I (eye) or letter L (el).  The optional argument
    map01 when not None, specifies which letter the digit 1 should be
    mapped to (when map01 is not None, the digit 0 is always mapped to
    the letter O).  For security purposes the default is None, so that
    0 and 1 are not allowed in the input.

    The result is returned as a bytes object.  A binascii.Error is raised if
    the input is incorrectly padded or if there are non-alphabet
    characters present in the input.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='casefold'),
rc.NodeInputBP(label='map01'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.b32decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_base64_b32encode(rc.Node):
    title = 'b32encode'
    description = '''Encode the bytes-like object s using Base32 and return a bytes object.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.b32encode(self.input(0)))
        


class AutoNode_base64_b64decode(rc.Node):
    title = 'b64decode'
    description = '''Decode the Base64 encoded bytes-like object or ASCII string s.

    Optional altchars must be a bytes-like object or ASCII string of length 2
    which specifies the alternative alphabet used instead of the '+' and '/'
    characters.

    The result is returned as a bytes object.  A binascii.Error is raised if
    s is incorrectly padded.

    If validate is False (the default), characters that are neither in the
    normal base-64 alphabet nor the alternative alphabet are discarded prior
    to the padding check.  If validate is True, these non-alphabet characters
    in the input result in a binascii.Error.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='altchars'),
rc.NodeInputBP(label='validate'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.b64decode(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_base64_b64encode(rc.Node):
    title = 'b64encode'
    description = '''Encode the bytes-like object s using Base64 and return a bytes object.

    Optional altchars should be a byte string of length 2 which specifies an
    alternative alphabet for the '+' and '/' characters.  This allows an
    application to e.g. generate url or filesystem safe Base64 strings.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='altchars'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.b64encode(self.input(0), self.input(1)))
        


class AutoNode_base64_b85decode(rc.Node):
    title = 'b85decode'
    description = '''Decode the base85-encoded bytes-like object or ASCII string b

    The result is returned as a bytes object.
    '''
    init_inputs = [
        rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.b85decode(self.input(0)))
        


class AutoNode_base64_b85encode(rc.Node):
    title = 'b85encode'
    description = '''Encode bytes-like object b in base85 format and return a bytes object.

    If pad is true, the input is padded with b'\0' so its length is a multiple of
    4 bytes before encoding.
    '''
    init_inputs = [
        rc.NodeInputBP(label='b'),
rc.NodeInputBP(label='pad'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.b85encode(self.input(0), self.input(1)))
        


class AutoNode_base64_decode(rc.Node):
    title = 'decode'
    description = '''Decode a file; input and output are binary files.'''
    init_inputs = [
        rc.NodeInputBP(label='input'),
rc.NodeInputBP(label='output'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.decode(self.input(0), self.input(1)))
        


class AutoNode_base64_decodebytes(rc.Node):
    title = 'decodebytes'
    description = '''Decode a bytestring of base-64 data into a bytes object.'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.decodebytes(self.input(0)))
        


class AutoNode_base64_decodestring(rc.Node):
    title = 'decodestring'
    description = '''Legacy alias of decodebytes().'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.decodestring(self.input(0)))
        


class AutoNode_base64_encode(rc.Node):
    title = 'encode'
    description = '''Encode a file; input and output are binary files.'''
    init_inputs = [
        rc.NodeInputBP(label='input'),
rc.NodeInputBP(label='output'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.encode(self.input(0), self.input(1)))
        


class AutoNode_base64_encodebytes(rc.Node):
    title = 'encodebytes'
    description = '''Encode a bytestring into a bytes object containing multiple lines
    of base-64 data.'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.encodebytes(self.input(0)))
        


class AutoNode_base64_encodestring(rc.Node):
    title = 'encodestring'
    description = '''Legacy alias of encodebytes().'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.encodestring(self.input(0)))
        


class AutoNode_base64_main(rc.Node):
    title = 'main'
    description = '''Small main program'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.main())
        


class AutoNode_base64_standard_b64decode(rc.Node):
    title = 'standard_b64decode'
    description = '''Decode bytes encoded with the standard Base64 alphabet.

    Argument s is a bytes-like object or ASCII string to decode.  The result
    is returned as a bytes object.  A binascii.Error is raised if the input
    is incorrectly padded.  Characters that are not in the standard alphabet
    are discarded prior to the padding check.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.standard_b64decode(self.input(0)))
        


class AutoNode_base64_standard_b64encode(rc.Node):
    title = 'standard_b64encode'
    description = '''Encode bytes-like object s using the standard Base64 alphabet.

    The result is returned as a bytes object.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.standard_b64encode(self.input(0)))
        


class AutoNode_base64_test(rc.Node):
    title = 'test'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.test())
        


class AutoNode_base64_urlsafe_b64decode(rc.Node):
    title = 'urlsafe_b64decode'
    description = '''Decode bytes using the URL- and filesystem-safe Base64 alphabet.

    Argument s is a bytes-like object or ASCII string to decode.  The result
    is returned as a bytes object.  A binascii.Error is raised if the input
    is incorrectly padded.  Characters that are not in the URL-safe base-64
    alphabet, and are not a plus '+' or slash '/', are discarded prior to the
    padding check.

    The alphabet uses '-' instead of '+' and '_' instead of '/'.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.urlsafe_b64decode(self.input(0)))
        


class AutoNode_base64_urlsafe_b64encode(rc.Node):
    title = 'urlsafe_b64encode'
    description = '''Encode bytes using the URL- and filesystem-safe Base64 alphabet.

    Argument s is a bytes-like object to encode.  The result is returned as a
    bytes object.  The alphabet uses '-' instead of '+' and '_' instead of
    '/'.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, base64.urlsafe_b64encode(self.input(0)))
        