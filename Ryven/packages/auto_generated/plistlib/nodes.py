
from NENV import *

import plistlib


class NodeBase(Node):
    pass


class _Count_To_Size_Node(NodeBase):
    title = '_count_to_size'
    type_ = 'plistlib'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='count'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._count_to_size(self.input(0)))
        

class _Date_From_String_Node(NodeBase):
    title = '_date_from_string'
    type_ = 'plistlib'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._date_from_string(self.input(0)))
        

class _Date_To_String_Node(NodeBase):
    title = '_date_to_string'
    type_ = 'plistlib'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='d'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._date_to_string(self.input(0)))
        

class _Decode_Base64_Node(NodeBase):
    title = '_decode_base64'
    type_ = 'plistlib'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._decode_base64(self.input(0)))
        

class _Encode_Base64_Node(NodeBase):
    title = '_encode_base64'
    type_ = 'plistlib'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='maxlinelength', dtype=dtypes.Data(default=76, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._encode_base64(self.input(0), self.input(1)))
        

class _Escape_Node(NodeBase):
    title = '_escape'
    type_ = 'plistlib'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='text'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._escape(self.input(0)))
        

class _Is_Fmt_Binary_Node(NodeBase):
    title = '_is_fmt_binary'
    type_ = 'plistlib'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='header'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._is_fmt_binary(self.input(0)))
        

class _Is_Fmt_Xml_Node(NodeBase):
    title = '_is_fmt_xml'
    type_ = 'plistlib'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='header'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._is_fmt_xml(self.input(0)))
        

class _Maybe_Open_Node(NodeBase):
    title = '_maybe_open'
    type_ = 'plistlib'
    doc = """"""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._maybe_open())
        

class Dump_Node(NodeBase):
    title = 'dump'
    type_ = 'plistlib'
    doc = """Write 'value' to a .plist file. 'fp' should be a writable,
    binary file object.
    """
    init_inputs = [
        NodeInputBP(label='value'),
        NodeInputBP(label='fp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.dump(self.input(0), self.input(1)))
        

class Dumps_Node(NodeBase):
    title = 'dumps'
    type_ = 'plistlib'
    doc = """Return a bytes object with the contents for a .plist file.
    """
    init_inputs = [
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.dumps(self.input(0)))
        

class Load_Node(NodeBase):
    title = 'load'
    type_ = 'plistlib'
    doc = """Read a .plist file. 'fp' should be a readable and binary file object.
    Return the unpacked root object (which usually is a dictionary).
    """
    init_inputs = [
        NodeInputBP(label='fp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.load(self.input(0)))
        

class Loads_Node(NodeBase):
    title = 'loads'
    type_ = 'plistlib'
    doc = """Read a .plist file from a bytes object.
    Return the unpacked root object (which usually is a dictionary).
    """
    init_inputs = [
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.loads(self.input(0)))
        

class Readplist_Node(NodeBase):
    title = 'readPlist'
    type_ = 'plistlib'
    doc = """
    Read a .plist from a path or file. pathOrFile should either
    be a file name, or a readable binary file object.

    This function is deprecated, use load instead.
    """
    init_inputs = [
        NodeInputBP(label='pathOrFile'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.readPlist(self.input(0)))
        

class Readplistfrombytes_Node(NodeBase):
    title = 'readPlistFromBytes'
    type_ = 'plistlib'
    doc = """
    Read a plist data from a bytes object. Return the root object.

    This function is deprecated, use loads instead.
    """
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.readPlistFromBytes(self.input(0)))
        

class Warn_Node(NodeBase):
    title = 'warn'
    type_ = 'plistlib'
    doc = """Issue a warning, or maybe ignore it or raise an exception."""
    init_inputs = [
        NodeInputBP(label='message'),
        NodeInputBP(label='category', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='stacklevel', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='source', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.warn(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Writeplist_Node(NodeBase):
    title = 'writePlist'
    type_ = 'plistlib'
    doc = """
    Write 'value' to a .plist file. 'pathOrFile' may either be a
    file name or a (writable) file object.

    This function is deprecated, use dump instead.
    """
    init_inputs = [
        NodeInputBP(label='value'),
        NodeInputBP(label='pathOrFile'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.writePlist(self.input(0), self.input(1)))
        

class Writeplisttobytes_Node(NodeBase):
    title = 'writePlistToBytes'
    type_ = 'plistlib'
    doc = """
    Return 'value' as a plist-formatted bytes object.

    This function is deprecated, use dumps instead.
    """
    init_inputs = [
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.writePlistToBytes(self.input(0)))
        


export_nodes(
    _Count_To_Size_Node,
    _Date_From_String_Node,
    _Date_To_String_Node,
    _Decode_Base64_Node,
    _Encode_Base64_Node,
    _Escape_Node,
    _Is_Fmt_Binary_Node,
    _Is_Fmt_Xml_Node,
    _Maybe_Open_Node,
    Dump_Node,
    Dumps_Node,
    Load_Node,
    Loads_Node,
    Readplist_Node,
    Readplistfrombytes_Node,
    Warn_Node,
    Writeplist_Node,
    Writeplisttobytes_Node,
)
