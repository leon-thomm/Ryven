import ryvencore_qt as rc
import binascii


class AutoNode_binascii_a2b_base64(rc.Node):
    title = 'a2b_base64'
    type_ = 'binascii'
    doc = '''Decode a line of base64 data.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.a2b_base64(self.input(0)))
        


class AutoNode_binascii_a2b_hex(rc.Node):
    title = 'a2b_hex'
    type_ = 'binascii'
    doc = '''Binary data of hexadecimal representation.

hexstr must contain an even number of hex digits (upper or lower case).
This function is also available as "unhexlify()".'''
    init_inputs = [
        rc.NodeInputBP(label='hexstr'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.a2b_hex(self.input(0)))
        


class AutoNode_binascii_a2b_hqx(rc.Node):
    title = 'a2b_hqx'
    type_ = 'binascii'
    doc = '''Decode .hqx coding.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.a2b_hqx(self.input(0)))
        


class AutoNode_binascii_a2b_qp(rc.Node):
    title = 'a2b_qp'
    type_ = 'binascii'
    doc = '''Decode a string of qp-encoded data.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='header'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.a2b_qp(self.input(0), self.input(1)))
        


class AutoNode_binascii_a2b_uu(rc.Node):
    title = 'a2b_uu'
    type_ = 'binascii'
    doc = '''Decode a line of uuencoded data.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.a2b_uu(self.input(0)))
        


class AutoNode_binascii_b2a_base64(rc.Node):
    title = 'b2a_base64'
    type_ = 'binascii'
    doc = '''Base64-code line of data.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.b2a_base64(self.input(0)))
        


class AutoNode_binascii_b2a_hqx(rc.Node):
    title = 'b2a_hqx'
    type_ = 'binascii'
    doc = '''Encode .hqx data.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.b2a_hqx(self.input(0)))
        


class AutoNode_binascii_b2a_qp(rc.Node):
    title = 'b2a_qp'
    type_ = 'binascii'
    doc = '''Encode a string using quoted-printable encoding.

On encoding, when istext is set, newlines are not encoded, and white
space at end of lines is.  When istext is not set, \r and \n (CR/LF)
are both encoded.  When quotetabs is set, space and tabs are encoded.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='quotetabs'),
rc.NodeInputBP(label='istext'),
rc.NodeInputBP(label='header'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.b2a_qp(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_binascii_b2a_uu(rc.Node):
    title = 'b2a_uu'
    type_ = 'binascii'
    doc = '''Uuencode line of data.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.b2a_uu(self.input(0)))
        


class AutoNode_binascii_crc32(rc.Node):
    title = 'crc32'
    type_ = 'binascii'
    doc = '''Compute CRC-32 incrementally.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='crc'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.crc32(self.input(0), self.input(1)))
        


class AutoNode_binascii_crc_hqx(rc.Node):
    title = 'crc_hqx'
    type_ = 'binascii'
    doc = '''Compute CRC-CCITT incrementally.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
rc.NodeInputBP(label='crc'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.crc_hqx(self.input(0), self.input(1)))
        


class AutoNode_binascii_rlecode_hqx(rc.Node):
    title = 'rlecode_hqx'
    type_ = 'binascii'
    doc = '''Binhex RLE-code binary data.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.rlecode_hqx(self.input(0)))
        


class AutoNode_binascii_rledecode_hqx(rc.Node):
    title = 'rledecode_hqx'
    type_ = 'binascii'
    doc = '''Decode hexbin RLE-coded string.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.rledecode_hqx(self.input(0)))
        


class AutoNode_binascii_unhexlify(rc.Node):
    title = 'unhexlify'
    type_ = 'binascii'
    doc = '''Binary data of hexadecimal representation.

hexstr must contain an even number of hex digits (upper or lower case).'''
    init_inputs = [
        rc.NodeInputBP(label='hexstr'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binascii.unhexlify(self.input(0)))
        