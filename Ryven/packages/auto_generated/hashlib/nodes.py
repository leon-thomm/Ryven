
from NENV import *

import hashlib


class NodeBase(Node):
    pass


class __Get_Builtin_Constructor_Node(NodeBase):
    title = '__get_builtin_constructor'
    type_ = 'hashlib'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.__get_builtin_constructor(self.input(0)))
        

class Md5_Node(NodeBase):
    title = 'md5'
    type_ = 'hashlib'
    doc = """Returns a md5 hash object; optionally initialized with a string"""
    init_inputs = [
        NodeInputBP(label='string', dtype=dtypes.Data(default=b'', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.md5(self.input(0)))
        

class New_Node(NodeBase):
    title = 'new'
    type_ = 'hashlib'
    doc = """new(name, data=b'') - Return a new hashing object using the named algorithm;
    optionally initialized with data (which must be a bytes-like object).
    """
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='data', dtype=dtypes.Data(default=b'', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.new(self.input(0), self.input(1)))
        

class Pbkdf2_Hmac_Node(NodeBase):
    title = 'pbkdf2_hmac'
    type_ = 'hashlib'
    doc = """Password based key derivation function 2 (PKCS #5 v2.0) with HMAC as pseudorandom function."""
    init_inputs = [
        NodeInputBP(label='hash_name'),
        NodeInputBP(label='password'),
        NodeInputBP(label='salt'),
        NodeInputBP(label='iterations'),
        NodeInputBP(label='dklen', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.pbkdf2_hmac(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Scrypt_Node(NodeBase):
    title = 'scrypt'
    type_ = 'hashlib'
    doc = """scrypt password-based key derivation function."""
    init_inputs = [
        NodeInputBP(label='password'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.scrypt(self.input(0)))
        

class Sha1_Node(NodeBase):
    title = 'sha1'
    type_ = 'hashlib'
    doc = """Returns a sha1 hash object; optionally initialized with a string"""
    init_inputs = [
        NodeInputBP(label='string', dtype=dtypes.Data(default=b'', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.sha1(self.input(0)))
        

class Sha224_Node(NodeBase):
    title = 'sha224'
    type_ = 'hashlib'
    doc = """Returns a sha224 hash object; optionally initialized with a string"""
    init_inputs = [
        NodeInputBP(label='string', dtype=dtypes.Data(default=b'', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.sha224(self.input(0)))
        

class Sha256_Node(NodeBase):
    title = 'sha256'
    type_ = 'hashlib'
    doc = """Returns a sha256 hash object; optionally initialized with a string"""
    init_inputs = [
        NodeInputBP(label='string', dtype=dtypes.Data(default=b'', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.sha256(self.input(0)))
        

class Sha384_Node(NodeBase):
    title = 'sha384'
    type_ = 'hashlib'
    doc = """Returns a sha384 hash object; optionally initialized with a string"""
    init_inputs = [
        NodeInputBP(label='string', dtype=dtypes.Data(default=b'', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.sha384(self.input(0)))
        

class Sha512_Node(NodeBase):
    title = 'sha512'
    type_ = 'hashlib'
    doc = """Returns a sha512 hash object; optionally initialized with a string"""
    init_inputs = [
        NodeInputBP(label='string', dtype=dtypes.Data(default=b'', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.sha512(self.input(0)))
        


export_nodes(
    __Get_Builtin_Constructor_Node,
    Md5_Node,
    New_Node,
    Pbkdf2_Hmac_Node,
    Scrypt_Node,
    Sha1_Node,
    Sha224_Node,
    Sha256_Node,
    Sha384_Node,
    Sha512_Node,
)
