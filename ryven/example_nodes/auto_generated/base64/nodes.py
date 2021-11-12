
from ryven.NENV import *

import base64


class NodeBase(Node):
    pass


class _85Encode_Node(NodeBase):
    """
    """
    
    title = '_85encode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='b'),
        NodeInputBP(label='chars'),
        NodeInputBP(label='chars2'),
        NodeInputBP(label='pad', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='foldnuls', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='foldspaces', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64._85encode(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class _Bytes_From_Decode_Data_Node(NodeBase):
    """
    """
    
    title = '_bytes_from_decode_data'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64._bytes_from_decode_data(self.input(0)))
        

class _Input_Type_Check_Node(NodeBase):
    """
    """
    
    title = '_input_type_check'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64._input_type_check(self.input(0)))
        

class A85Decode_Node(NodeBase):
    """
    Decode the Ascii85 encoded bytes-like object or ASCII string b.

    foldspaces is a flag that specifies whether the 'y' short sequence should be
    accepted as shorthand for 4 consecutive spaces (ASCII 0x20). This feature is
    not supported by the "standard" Adobe encoding.

    adobe controls whether the input sequence is in Adobe Ascii85 format (i.e.
    is framed with <~ and ~>).

    ignorechars should be a byte string containing characters to ignore from the
    input. This should only contain whitespace characters, and by default
    contains all whitespace characters in ASCII.

    The result is returned as a bytes object.
    """
    
    title = 'a85decode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.a85decode(self.input(0)))
        

class A85Encode_Node(NodeBase):
    """
    Encode bytes-like object b using Ascii85 and return a bytes object.

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
    """
    
    title = 'a85encode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.a85encode(self.input(0)))
        

class B16Decode_Node(NodeBase):
    """
    Decode the Base16 encoded bytes-like object or ASCII string s.

    Optional casefold is a flag specifying whether a lowercase alphabet is
    acceptable as input.  For security purposes, the default is False.

    The result is returned as a bytes object.  A binascii.Error is raised if
    s is incorrectly padded or if there are non-alphabet characters present
    in the input.
    """
    
    title = 'b16decode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='casefold', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.b16decode(self.input(0), self.input(1)))
        

class B16Encode_Node(NodeBase):
    """
    Encode the bytes-like object s using Base16 and return a bytes object.
    """
    
    title = 'b16encode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.b16encode(self.input(0)))
        

class B32Decode_Node(NodeBase):
    """
    Decode the Base32 encoded bytes-like object or ASCII string s.

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
    """
    
    title = 'b32decode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='casefold', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='map01', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.b32decode(self.input(0), self.input(1), self.input(2)))
        

class B32Encode_Node(NodeBase):
    """
    Encode the bytes-like object s using Base32 and return a bytes object.
    """
    
    title = 'b32encode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.b32encode(self.input(0)))
        

class B64Decode_Node(NodeBase):
    """
    Decode the Base64 encoded bytes-like object or ASCII string s.

    Optional altchars must be a bytes-like object or ASCII string of length 2
    which specifies the alternative alphabet used instead of the '+' and '/'
    characters.

    The result is returned as a bytes object.  A binascii.Error is raised if
    s is incorrectly padded.

    If validate is False (the default), characters that are neither in the
    normal base-64 alphabet nor the alternative alphabet are discarded prior
    to the padding check.  If validate is True, these non-alphabet characters
    in the input result in a binascii.Error.
    """
    
    title = 'b64decode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='altchars', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='validate', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.b64decode(self.input(0), self.input(1), self.input(2)))
        

class B64Encode_Node(NodeBase):
    """
    Encode the bytes-like object s using Base64 and return a bytes object.

    Optional altchars should be a byte string of length 2 which specifies an
    alternative alphabet for the '+' and '/' characters.  This allows an
    application to e.g. generate url or filesystem safe Base64 strings.
    """
    
    title = 'b64encode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='altchars', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.b64encode(self.input(0), self.input(1)))
        

class B85Decode_Node(NodeBase):
    """
    Decode the base85-encoded bytes-like object or ASCII string b

    The result is returned as a bytes object.
    """
    
    title = 'b85decode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.b85decode(self.input(0)))
        

class B85Encode_Node(NodeBase):
    """
    Encode bytes-like object b in base85 format and return a bytes object.

    If pad is true, the input is padded with b'\0' so its length is a multiple of
    4 bytes before encoding.
    """
    
    title = 'b85encode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='b'),
        NodeInputBP(label='pad', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.b85encode(self.input(0), self.input(1)))
        

class Decode_Node(NodeBase):
    """
    Decode a file; input and output are binary files."""
    
    title = 'decode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='input'),
        NodeInputBP(label='output'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.decode(self.input(0), self.input(1)))
        

class Decodebytes_Node(NodeBase):
    """
    Decode a bytestring of base-64 data into a bytes object."""
    
    title = 'decodebytes'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.decodebytes(self.input(0)))
        

class Encode_Node(NodeBase):
    """
    Encode a file; input and output are binary files."""
    
    title = 'encode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='input'),
        NodeInputBP(label='output'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.encode(self.input(0), self.input(1)))
        

class Encodebytes_Node(NodeBase):
    """
    Encode a bytestring into a bytes object containing multiple lines
    of base-64 data."""
    
    title = 'encodebytes'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.encodebytes(self.input(0)))
        

class Main_Node(NodeBase):
    """
    Small main program"""
    
    title = 'main'
    type_ = 'base64'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.main())
        

class Standard_B64Decode_Node(NodeBase):
    """
    Decode bytes encoded with the standard Base64 alphabet.

    Argument s is a bytes-like object or ASCII string to decode.  The result
    is returned as a bytes object.  A binascii.Error is raised if the input
    is incorrectly padded.  Characters that are not in the standard alphabet
    are discarded prior to the padding check.
    """
    
    title = 'standard_b64decode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.standard_b64decode(self.input(0)))
        

class Standard_B64Encode_Node(NodeBase):
    """
    Encode bytes-like object s using the standard Base64 alphabet.

    The result is returned as a bytes object.
    """
    
    title = 'standard_b64encode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.standard_b64encode(self.input(0)))
        

class Test_Node(NodeBase):
    """
    """
    
    title = 'test'
    type_ = 'base64'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.test())
        

class Urlsafe_B64Decode_Node(NodeBase):
    """
    Decode bytes using the URL- and filesystem-safe Base64 alphabet.

    Argument s is a bytes-like object or ASCII string to decode.  The result
    is returned as a bytes object.  A binascii.Error is raised if the input
    is incorrectly padded.  Characters that are not in the URL-safe base-64
    alphabet, and are not a plus '+' or slash '/', are discarded prior to the
    padding check.

    The alphabet uses '-' instead of '+' and '_' instead of '/'.
    """
    
    title = 'urlsafe_b64decode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.urlsafe_b64decode(self.input(0)))
        

class Urlsafe_B64Encode_Node(NodeBase):
    """
    Encode bytes using the URL- and filesystem-safe Base64 alphabet.

    Argument s is a bytes-like object to encode.  The result is returned as a
    bytes object.  The alphabet uses '-' instead of '+' and '_' instead of
    '/'.
    """
    
    title = 'urlsafe_b64encode'
    type_ = 'base64'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, base64.urlsafe_b64encode(self.input(0)))
        


export_nodes(
    _85Encode_Node,
    _Bytes_From_Decode_Data_Node,
    _Input_Type_Check_Node,
    A85Decode_Node,
    A85Encode_Node,
    B16Decode_Node,
    B16Encode_Node,
    B32Decode_Node,
    B32Encode_Node,
    B64Decode_Node,
    B64Encode_Node,
    B85Decode_Node,
    B85Encode_Node,
    Decode_Node,
    Decodebytes_Node,
    Encode_Node,
    Encodebytes_Node,
    Main_Node,
    Standard_B64Decode_Node,
    Standard_B64Encode_Node,
    Test_Node,
    Urlsafe_B64Decode_Node,
    Urlsafe_B64Encode_Node,
)
