
from ryven.NENV import *

import plistlib


class NodeBase(Node):
    pass


class _Count_To_Size_Node(NodeBase):
    """
    """
    
    title = '_count_to_size'
    type_ = 'plistlib'
    init_inputs = [
        NodeInputBP(label='count'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, plistlib._count_to_size(self.input(0)))
        

class _Date_From_String_Node(NodeBase):
    """
    """
    
    title = '_date_from_string'
    type_ = 'plistlib'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, plistlib._date_from_string(self.input(0)))
        

class _Date_To_String_Node(NodeBase):
    """
    """
    
    title = '_date_to_string'
    type_ = 'plistlib'
    init_inputs = [
        NodeInputBP(label='d'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, plistlib._date_to_string(self.input(0)))
        

class _Decode_Base64_Node(NodeBase):
    """
    """
    
    title = '_decode_base64'
    type_ = 'plistlib'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, plistlib._decode_base64(self.input(0)))
        

class _Encode_Base64_Node(NodeBase):
    """
    """
    
    title = '_encode_base64'
    type_ = 'plistlib'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='maxlinelength', dtype=dtypes.Data(default=76, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, plistlib._encode_base64(self.input(0), self.input(1)))
        

class _Escape_Node(NodeBase):
    """
    """
    
    title = '_escape'
    type_ = 'plistlib'
    init_inputs = [
        NodeInputBP(label='text'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, plistlib._escape(self.input(0)))
        

class _Is_Fmt_Binary_Node(NodeBase):
    """
    """
    
    title = '_is_fmt_binary'
    type_ = 'plistlib'
    init_inputs = [
        NodeInputBP(label='header'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, plistlib._is_fmt_binary(self.input(0)))
        

class _Is_Fmt_Xml_Node(NodeBase):
    """
    """
    
    title = '_is_fmt_xml'
    type_ = 'plistlib'
    init_inputs = [
        NodeInputBP(label='header'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, plistlib._is_fmt_xml(self.input(0)))
        

class Dump_Node(NodeBase):
    """
    Write 'value' to a .plist file. 'fp' should be a writable,
    binary file object.
    """
    
    title = 'dump'
    type_ = 'plistlib'
    init_inputs = [
        NodeInputBP(label='value'),
        NodeInputBP(label='fp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, plistlib.dump(self.input(0), self.input(1)))
        

class Dumps_Node(NodeBase):
    """
    Return a bytes object with the contents for a .plist file.
    """
    
    title = 'dumps'
    type_ = 'plistlib'
    init_inputs = [
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, plistlib.dumps(self.input(0)))
        

class Load_Node(NodeBase):
    """
    Read a .plist file. 'fp' should be a readable and binary file object.
    Return the unpacked root object (which usually is a dictionary).
    """
    
    title = 'load'
    type_ = 'plistlib'
    init_inputs = [
        NodeInputBP(label='fp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, plistlib.load(self.input(0)))
        

class Loads_Node(NodeBase):
    """
    Read a .plist file from a bytes object.
    Return the unpacked root object (which usually is a dictionary).
    """
    
    title = 'loads'
    type_ = 'plistlib'
    init_inputs = [
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, plistlib.loads(self.input(0)))
        


export_nodes(
    _Count_To_Size_Node,
    _Date_From_String_Node,
    _Date_To_String_Node,
    _Decode_Base64_Node,
    _Encode_Base64_Node,
    _Escape_Node,
    _Is_Fmt_Binary_Node,
    _Is_Fmt_Xml_Node,
    Dump_Node,
    Dumps_Node,
    Load_Node,
    Loads_Node,
)
