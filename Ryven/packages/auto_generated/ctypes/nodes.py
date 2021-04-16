import ryvencore_qt as rc
import ctypes


class AutoNode_ctypes_ARRAY(rc.Node):
    title = 'ARRAY'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='typ'),
rc.NodeInputBP(label='len'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.ARRAY(self.input(0), self.input(1)))
        


class AutoNode_ctypes_CFUNCTYPE(rc.Node):
    title = 'CFUNCTYPE'
    doc = '''CFUNCTYPE(restype, *argtypes,
                 use_errno=False, use_last_error=False) -> function prototype.

    restype: the result type
    argtypes: a sequence specifying the argument types

    The function prototype can be called in different ways to create a
    callable object:

    prototype(integer address) -> foreign function
    prototype(callable) -> create and return a C callable function from callable
    prototype(integer index, method name[, paramflags]) -> foreign function calling a COM method
    prototype((ordinal number, dll object)[, paramflags]) -> foreign function exported by ordinal
    prototype((function name, dll object)[, paramflags]) -> foreign function exported by name
    '''
    init_inputs = [
        rc.NodeInputBP(label='restype'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.CFUNCTYPE(self.input(0)))
        


class AutoNode_ctypes_DllCanUnloadNow(rc.Node):
    title = 'DllCanUnloadNow'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.DllCanUnloadNow())
        


class AutoNode_ctypes_DllGetClassObject(rc.Node):
    title = 'DllGetClassObject'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='rclsid'),
rc.NodeInputBP(label='riid'),
rc.NodeInputBP(label='ppv'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.DllGetClassObject(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_ctypes_PYFUNCTYPE(rc.Node):
    title = 'PYFUNCTYPE'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='restype'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.PYFUNCTYPE(self.input(0)))
        


class AutoNode_ctypes_SetPointerType(rc.Node):
    title = 'SetPointerType'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='pointer'),
rc.NodeInputBP(label='cls'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.SetPointerType(self.input(0), self.input(1)))
        


class AutoNode_ctypes_WINFUNCTYPE(rc.Node):
    title = 'WINFUNCTYPE'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='restype'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.WINFUNCTYPE(self.input(0)))
        


class AutoNode_ctypes_WinError(rc.Node):
    title = 'WinError'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='code'),
rc.NodeInputBP(label='descr'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.WinError(self.input(0), self.input(1)))
        


class AutoNode_ctypes__calcsize(rc.Node):
    title = '_calcsize'
    doc = '''Return size in bytes of the struct described by the format string.'''
    init_inputs = [
        rc.NodeInputBP(label='format'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes._calcsize(self.input(0)))
        


class AutoNode_ctypes__check_size(rc.Node):
    title = '_check_size'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='typ'),
rc.NodeInputBP(label='typecode'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes._check_size(self.input(0), self.input(1)))
        


class AutoNode_ctypes__reset_cache(rc.Node):
    title = '_reset_cache'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes._reset_cache())
        


class AutoNode_ctypes_c_buffer(rc.Node):
    title = 'c_buffer'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='init'),
rc.NodeInputBP(label='size'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.c_buffer(self.input(0), self.input(1)))
        


class AutoNode_ctypes_cast(rc.Node):
    title = 'cast'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
rc.NodeInputBP(label='typ'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.cast(self.input(0), self.input(1)))
        


class AutoNode_ctypes_create_string_buffer(rc.Node):
    title = 'create_string_buffer'
    doc = '''create_string_buffer(aBytes) -> character array
    create_string_buffer(anInteger) -> character array
    create_string_buffer(aBytes, anInteger) -> character array
    '''
    init_inputs = [
        rc.NodeInputBP(label='init'),
rc.NodeInputBP(label='size'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.create_string_buffer(self.input(0), self.input(1)))
        


class AutoNode_ctypes_create_unicode_buffer(rc.Node):
    title = 'create_unicode_buffer'
    doc = '''create_unicode_buffer(aString) -> character array
    create_unicode_buffer(anInteger) -> character array
    create_unicode_buffer(aString, anInteger) -> character array
    '''
    init_inputs = [
        rc.NodeInputBP(label='init'),
rc.NodeInputBP(label='size'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.create_unicode_buffer(self.input(0), self.input(1)))
        


class AutoNode_ctypes_string_at(rc.Node):
    title = 'string_at'
    doc = '''string_at(addr[, size]) -> string

    Return the string at addr.'''
    init_inputs = [
        rc.NodeInputBP(label='ptr'),
rc.NodeInputBP(label='size'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.string_at(self.input(0), self.input(1)))
        


class AutoNode_ctypes_wstring_at(rc.Node):
    title = 'wstring_at'
    doc = '''wstring_at(addr[, size]) -> string

        Return the string at addr.'''
    init_inputs = [
        rc.NodeInputBP(label='ptr'),
rc.NodeInputBP(label='size'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ctypes.wstring_at(self.input(0), self.input(1)))
        