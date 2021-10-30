
from ryven.NENV import *

import hmac


class NodeBase(Node):
    pass


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
    type_ = 'hmac'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, hmac.compare_digest(self.input(0), self.input(1)))
        

class Digest_Node(NodeBase):
    """
    Fast inline implementation of HMAC.

    key: bytes or buffer, The key for the keyed hash object.
    msg: bytes or buffer, Input message.
    digest: A hash name suitable for hashlib.new() for best performance. *OR*
            A hashlib constructor returning a new hash object. *OR*
            A module supporting PEP 247.
    """
    
    title = 'digest'
    type_ = 'hmac'
    init_inputs = [
        NodeInputBP(label='key'),
        NodeInputBP(label='msg'),
        NodeInputBP(label='digest'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, hmac.digest(self.input(0), self.input(1), self.input(2)))
        

class New_Node(NodeBase):
    """
    Create a new hashing object and return it.

    key: bytes or buffer, The starting key for the hash.
    msg: bytes or buffer, Initial input for the hash, or None.
    digestmod: A hash name suitable for hashlib.new(). *OR*
               A hashlib constructor returning a new hash object. *OR*
               A module supporting PEP 247.

               Required as of 3.8, despite its position after the optional
               msg argument.  Passing it as a keyword argument is
               recommended, though not required for legacy API reasons.

    You can now feed arbitrary bytes into the object using its update()
    method, and can ask for the hash value at any time by calling its digest()
    or hexdigest() methods.
    """
    
    title = 'new'
    type_ = 'hmac'
    init_inputs = [
        NodeInputBP(label='key'),
        NodeInputBP(label='msg', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='digestmod', dtype=dtypes.Data(default='', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, hmac.new(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    Compare_Digest_Node,
    Digest_Node,
    New_Node,
)
