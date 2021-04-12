import ryvencore_qt as rc
import hashlib


class AutoNode_hashlib___get_builtin_constructor(rc.Node):
    title = '__get_builtin_constructor'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.__get_builtin_constructor(self.input(0)))
        


class AutoNode_hashlib_md5(rc.Node):
    title = 'md5'
    description = '''Returns a md5 hash object; optionally initialized with a string'''
    init_inputs = [
        rc.NodeInputBP(label='string'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.md5(self.input(0)))
        


class AutoNode_hashlib_new(rc.Node):
    title = 'new'
    description = '''new(name, data=b'') - Return a new hashing object using the named algorithm;
    optionally initialized with data (which must be a bytes-like object).
    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.new(self.input(0), self.input(1)))
        


class AutoNode_hashlib_pbkdf2_hmac(rc.Node):
    title = 'pbkdf2_hmac'
    description = '''Password based key derivation function 2 (PKCS #5 v2.0) with HMAC as pseudorandom function.'''
    init_inputs = [
        rc.NodeInputBP(label='hash_name'),
rc.NodeInputBP(label='password'),
rc.NodeInputBP(label='salt'),
rc.NodeInputBP(label='iterations'),
rc.NodeInputBP(label='dklen'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.pbkdf2_hmac(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_hashlib_scrypt(rc.Node):
    title = 'scrypt'
    description = '''scrypt password-based key derivation function.'''
    init_inputs = [
        rc.NodeInputBP(label='password'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.scrypt(self.input(0)))
        


class AutoNode_hashlib_sha1(rc.Node):
    title = 'sha1'
    description = '''Returns a sha1 hash object; optionally initialized with a string'''
    init_inputs = [
        rc.NodeInputBP(label='string'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.sha1(self.input(0)))
        


class AutoNode_hashlib_sha224(rc.Node):
    title = 'sha224'
    description = '''Returns a sha224 hash object; optionally initialized with a string'''
    init_inputs = [
        rc.NodeInputBP(label='string'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.sha224(self.input(0)))
        


class AutoNode_hashlib_sha256(rc.Node):
    title = 'sha256'
    description = '''Returns a sha256 hash object; optionally initialized with a string'''
    init_inputs = [
        rc.NodeInputBP(label='string'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.sha256(self.input(0)))
        


class AutoNode_hashlib_sha384(rc.Node):
    title = 'sha384'
    description = '''Returns a sha384 hash object; optionally initialized with a string'''
    init_inputs = [
        rc.NodeInputBP(label='string'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.sha384(self.input(0)))
        


class AutoNode_hashlib_sha512(rc.Node):
    title = 'sha512'
    description = '''Returns a sha512 hash object; optionally initialized with a string'''
    init_inputs = [
        rc.NodeInputBP(label='string'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, hashlib.sha512(self.input(0)))
        