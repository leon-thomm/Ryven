
from ryven.NENV import *

import secrets


class NodeBase(Node):
    pass


class Choice_Node(NodeBase):
    """
    Choose a random element from a non-empty sequence."""
    
    title = 'choice'
    type_ = 'secrets'
    init_inputs = [
        NodeInputBP(label='seq'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, secrets.choice(self.input(0)))
        

class Compare_Digest_Node(NodeBase):
    """
    Return 'a == b'.

This function uses an approach designed to prevent
timing analysis, making it appropriate for cryptography.

a and b must both be of the same type: either str (ASCII only),
or any bytes-like object.

Note: If a and b are of different lengths, or if an error occurs,
a timing attack could theoretically reveal information about the
types and lengths of a and b--but not their values."""
    
    title = 'compare_digest'
    type_ = 'secrets'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, secrets.compare_digest(self.input(0), self.input(1)))
        

class Randbelow_Node(NodeBase):
    """
    Return a random int in the range [0, n)."""
    
    title = 'randbelow'
    type_ = 'secrets'
    init_inputs = [
        NodeInputBP(label='exclusive_upper_bound'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, secrets.randbelow(self.input(0)))
        

class Randbits_Node(NodeBase):
    """
    getrandbits(k) -> x.  Generates an int with k random bits."""
    
    title = 'randbits'
    type_ = 'secrets'
    init_inputs = [
        NodeInputBP(label='k'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, secrets.randbits(self.input(0)))
        

class Token_Bytes_Node(NodeBase):
    """
    Return a random byte string containing *nbytes* bytes.

    If *nbytes* is ``None`` or not supplied, a reasonable
    default is used.

    >>> token_bytes(16)  #doctest:+SKIP
    b'\xebr\x17D*t\xae\xd4\xe3S\xb6\xe2\xebP1\x8b'

    """
    
    title = 'token_bytes'
    type_ = 'secrets'
    init_inputs = [
        NodeInputBP(label='nbytes', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, secrets.token_bytes(self.input(0)))
        

class Token_Hex_Node(NodeBase):
    """
    Return a random text string, in hexadecimal.

    The string has *nbytes* random bytes, each byte converted to two
    hex digits.  If *nbytes* is ``None`` or not supplied, a reasonable
    default is used.

    >>> token_hex(16)  #doctest:+SKIP
    'f9bf78b9a18ce6d46a0cd2b0b86df9da'

    """
    
    title = 'token_hex'
    type_ = 'secrets'
    init_inputs = [
        NodeInputBP(label='nbytes', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, secrets.token_hex(self.input(0)))
        

class Token_Urlsafe_Node(NodeBase):
    """
    Return a random URL-safe text string, in Base64 encoding.

    The string has *nbytes* random bytes.  If *nbytes* is ``None``
    or not supplied, a reasonable default is used.

    >>> token_urlsafe(16)  #doctest:+SKIP
    'Drmhze6EPcv0fN_81Bj-nA'

    """
    
    title = 'token_urlsafe'
    type_ = 'secrets'
    init_inputs = [
        NodeInputBP(label='nbytes', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, secrets.token_urlsafe(self.input(0)))
        


export_nodes(
    Choice_Node,
    Compare_Digest_Node,
    Randbelow_Node,
    Randbits_Node,
    Token_Bytes_Node,
    Token_Hex_Node,
    Token_Urlsafe_Node,
)
