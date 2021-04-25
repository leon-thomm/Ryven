
from NENV import *

import binascii


class NodeBase(Node):
    pass


class AutoNode_binascii_a2b_base64(NodeBase):
    title = 'a2b_base64'
    type_ = 'binascii'
    doc = """Decode a line of base64 data."""
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.a2b_base64(self.input(0)))
        

class AutoNode_binascii_a2b_hex(NodeBase):
    title = 'a2b_hex'
    type_ = 'binascii'
    doc = """Binary data of hexadecimal representation.

hexstr must contain an even number of hex digits (upper or lower case).
This function is also available as "unhexlify()"."""
    init_inputs = [
        NodeInputBP(label='hexstr'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.a2b_hex(self.input(0)))
        

class AutoNode_binascii_a2b_hqx(NodeBase):
    title = 'a2b_hqx'
    type_ = 'binascii'
    doc = """Decode .hqx coding."""
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.a2b_hqx(self.input(0)))
        

class AutoNode_binascii_a2b_qp(NodeBase):
    title = 'a2b_qp'
    type_ = 'binascii'
    doc = """Decode a string of qp-encoded data."""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='header'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.a2b_qp(self.input(0), self.input(1)))
        

class AutoNode_binascii_a2b_uu(NodeBase):
    title = 'a2b_uu'
    type_ = 'binascii'
    doc = """Decode a line of uuencoded data."""
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.a2b_uu(self.input(0)))
        

class AutoNode_binascii_b2a_base64(NodeBase):
    title = 'b2a_base64'
    type_ = 'binascii'
    doc = """Base64-code line of data."""
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.b2a_base64(self.input(0)))
        

class AutoNode_binascii_b2a_hqx(NodeBase):
    title = 'b2a_hqx'
    type_ = 'binascii'
    doc = """Encode .hqx data."""
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.b2a_hqx(self.input(0)))
        

class AutoNode_binascii_b2a_qp(NodeBase):
    title = 'b2a_qp'
    type_ = 'binascii'
    doc = """Encode a string using quoted-printable encoding.

On encoding, when istext is set, newlines are not encoded, and white
space at end of lines is.  When istext is not set, \r and \n (CR/LF)
are both encoded.  When quotetabs is set, space and tabs are encoded."""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='quotetabs'),
        NodeInputBP(label='istext'),
        NodeInputBP(label='header'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.b2a_qp(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class AutoNode_binascii_b2a_uu(NodeBase):
    title = 'b2a_uu'
    type_ = 'binascii'
    doc = """Uuencode line of data."""
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.b2a_uu(self.input(0)))
        

class AutoNode_binascii_crc32(NodeBase):
    title = 'crc32'
    type_ = 'binascii'
    doc = """Compute CRC-32 incrementally."""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='crc'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.crc32(self.input(0), self.input(1)))
        

class AutoNode_binascii_crc_hqx(NodeBase):
    title = 'crc_hqx'
    type_ = 'binascii'
    doc = """Compute CRC-CCITT incrementally."""
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='crc'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.crc_hqx(self.input(0), self.input(1)))
        

class AutoNode_binascii_rlecode_hqx(NodeBase):
    title = 'rlecode_hqx'
    type_ = 'binascii'
    doc = """Binhex RLE-code binary data."""
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.rlecode_hqx(self.input(0)))
        

class AutoNode_binascii_rledecode_hqx(NodeBase):
    title = 'rledecode_hqx'
    type_ = 'binascii'
    doc = """Decode hexbin RLE-coded string."""
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.rledecode_hqx(self.input(0)))
        

class AutoNode_binascii_unhexlify(NodeBase):
    title = 'unhexlify'
    type_ = 'binascii'
    doc = """Binary data of hexadecimal representation.

hexstr must contain an even number of hex digits (upper or lower case)."""
    init_inputs = [
        NodeInputBP(label='hexstr'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.unhexlify(self.input(0)))
        


export_nodes(
    AutoNode_binascii_a2b_base64,
    AutoNode_binascii_a2b_hex,
    AutoNode_binascii_a2b_hqx,
    AutoNode_binascii_a2b_qp,
    AutoNode_binascii_a2b_uu,
    AutoNode_binascii_b2a_base64,
    AutoNode_binascii_b2a_hqx,
    AutoNode_binascii_b2a_qp,
    AutoNode_binascii_b2a_uu,
    AutoNode_binascii_crc32,
    AutoNode_binascii_crc_hqx,
    AutoNode_binascii_rlecode_hqx,
    AutoNode_binascii_rledecode_hqx,
    AutoNode_binascii_unhexlify,
)
