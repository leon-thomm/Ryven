
from NENV import *

import ctypes.test.test_win32


class NodeBase(Node):
    pass


class Array_Node(NodeBase):
    """
    """
    
    title = 'ARRAY'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='typ'),
        NodeInputBP(label='len'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.ARRAY(self.input(0), self.input(1)))
        

class Cfunctype_Node(NodeBase):
    """
    CFUNCTYPE(restype, *argtypes,
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
    """
    
    title = 'CFUNCTYPE'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='restype'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.CFUNCTYPE(self.input(0)))
        

class Dllcanunloadnow_Node(NodeBase):
    """
    """
    
    title = 'DllCanUnloadNow'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.DllCanUnloadNow())
        

class Dllgetclassobject_Node(NodeBase):
    """
    """
    
    title = 'DllGetClassObject'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='rclsid'),
        NodeInputBP(label='riid'),
        NodeInputBP(label='ppv'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.DllGetClassObject(self.input(0), self.input(1), self.input(2)))
        

class Pyfunctype_Node(NodeBase):
    """
    """
    
    title = 'PYFUNCTYPE'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='restype'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.PYFUNCTYPE(self.input(0)))
        

class Setpointertype_Node(NodeBase):
    """
    """
    
    title = 'SetPointerType'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='pointer'),
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.SetPointerType(self.input(0), self.input(1)))
        

class Winfunctype_Node(NodeBase):
    """
    """
    
    title = 'WINFUNCTYPE'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='restype'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.WINFUNCTYPE(self.input(0)))
        

class Winerror_Node(NodeBase):
    """
    """
    
    title = 'WinError'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='code', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='descr', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.WinError(self.input(0), self.input(1)))
        

class _Calcsize_Node(NodeBase):
    """
    Return size in bytes of the struct described by the format string."""
    
    title = '_calcsize'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='format'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32._calcsize(self.input(0)))
        

class _Check_Size_Node(NodeBase):
    """
    """
    
    title = '_check_size'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='typ'),
        NodeInputBP(label='typecode', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32._check_size(self.input(0), self.input(1)))
        

class _Reset_Cache_Node(NodeBase):
    """
    """
    
    title = '_reset_cache'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32._reset_cache())
        

class C_Buffer_Node(NodeBase):
    """
    """
    
    title = 'c_buffer'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='init'),
        NodeInputBP(label='size', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.c_buffer(self.input(0), self.input(1)))
        

class Cast_Node(NodeBase):
    """
    """
    
    title = 'cast'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='typ'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.cast(self.input(0), self.input(1)))
        

class Create_String_Buffer_Node(NodeBase):
    """
    create_string_buffer(aBytes) -> character array
    create_string_buffer(anInteger) -> character array
    create_string_buffer(aBytes, anInteger) -> character array
    """
    
    title = 'create_string_buffer'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='init'),
        NodeInputBP(label='size', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.create_string_buffer(self.input(0), self.input(1)))
        

class Create_Unicode_Buffer_Node(NodeBase):
    """
    create_unicode_buffer(aString) -> character array
    create_unicode_buffer(anInteger) -> character array
    create_unicode_buffer(aString, anInteger) -> character array
    """
    
    title = 'create_unicode_buffer'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='init'),
        NodeInputBP(label='size', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.create_unicode_buffer(self.input(0), self.input(1)))
        

class String_At_Node(NodeBase):
    """
    string_at(addr[, size]) -> string

    Return the string at addr."""
    
    title = 'string_at'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='ptr'),
        NodeInputBP(label='size', dtype=dtypes.Data(default=-1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.string_at(self.input(0), self.input(1)))
        

class Wstring_At_Node(NodeBase):
    """
    wstring_at(addr[, size]) -> string

        Return the string at addr."""
    
    title = 'wstring_at'
    type_ = 'ctypes.test.test_win32'
    init_inputs = [
        NodeInputBP(label='ptr'),
        NodeInputBP(label='size', dtype=dtypes.Data(default=-1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ctypes.test.test_win32.wstring_at(self.input(0), self.input(1)))
        


export_nodes(
    Array_Node,
    Cfunctype_Node,
    Dllcanunloadnow_Node,
    Dllgetclassobject_Node,
    Pyfunctype_Node,
    Setpointertype_Node,
    Winfunctype_Node,
    Winerror_Node,
    _Calcsize_Node,
    _Check_Size_Node,
    _Reset_Cache_Node,
    C_Buffer_Node,
    Cast_Node,
    Create_String_Buffer_Node,
    Create_Unicode_Buffer_Node,
    String_At_Node,
    Wstring_At_Node,
)
