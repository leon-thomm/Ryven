
from ryven.NENV import *

import quopri


class NodeBase(Node):
    pass


class A2B_Qp_Node(NodeBase):
    """
    Decode a string of qp-encoded data."""
    
    title = 'a2b_qp'
    type_ = 'quopri'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='header', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, quopri.a2b_qp(self.input(0), self.input(1)))
        

class B2A_Qp_Node(NodeBase):
    """
    Encode a string using quoted-printable encoding.

On encoding, when istext is set, newlines are not encoded, and white
space at end of lines is.  When istext is not set, \r and \n (CR/LF)
are both encoded.  When quotetabs is set, space and tabs are encoded."""
    
    title = 'b2a_qp'
    type_ = 'quopri'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='quotetabs', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='istext', dtype=dtypes.Data(default=True, size='s')),
        NodeInputBP(label='header', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, quopri.b2a_qp(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Decode_Node(NodeBase):
    """
    Read 'input', apply quoted-printable decoding, and write to 'output'.
    'input' and 'output' are binary file objects.
    If 'header' is true, decode underscore as space (per RFC 1522)."""
    
    title = 'decode'
    type_ = 'quopri'
    init_inputs = [
        NodeInputBP(label='input'),
        NodeInputBP(label='output'),
        NodeInputBP(label='header', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, quopri.decode(self.input(0), self.input(1), self.input(2)))
        

class Decodestring_Node(NodeBase):
    """
    """
    
    title = 'decodestring'
    type_ = 'quopri'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='header', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, quopri.decodestring(self.input(0), self.input(1)))
        

class Encode_Node(NodeBase):
    """
    Read 'input', apply quoted-printable encoding, and write to 'output'.

    'input' and 'output' are binary file objects. The 'quotetabs' flag
    indicates whether embedded tabs and spaces should be quoted. Note that
    line-ending tabs and spaces are always encoded, as per RFC 1521.
    The 'header' flag indicates whether we are encoding spaces as _ as per RFC
    1522."""
    
    title = 'encode'
    type_ = 'quopri'
    init_inputs = [
        NodeInputBP(label='input'),
        NodeInputBP(label='output'),
        NodeInputBP(label='quotetabs'),
        NodeInputBP(label='header', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, quopri.encode(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Encodestring_Node(NodeBase):
    """
    """
    
    title = 'encodestring'
    type_ = 'quopri'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='quotetabs', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='header', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, quopri.encodestring(self.input(0), self.input(1), self.input(2)))
        

class Ishex_Node(NodeBase):
    """
    Return true if the byte ordinal 'c' is a hexadecimal digit in ASCII."""
    
    title = 'ishex'
    type_ = 'quopri'
    init_inputs = [
        NodeInputBP(label='c'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, quopri.ishex(self.input(0)))
        

class Main_Node(NodeBase):
    """
    """
    
    title = 'main'
    type_ = 'quopri'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, quopri.main())
        

class Needsquoting_Node(NodeBase):
    """
    Decide whether a particular byte ordinal needs to be quoted.

    The 'quotetabs' flag indicates whether embedded tabs and spaces should be
    quoted.  Note that line-ending tabs and spaces are always encoded, as per
    RFC 1521.
    """
    
    title = 'needsquoting'
    type_ = 'quopri'
    init_inputs = [
        NodeInputBP(label='c'),
        NodeInputBP(label='quotetabs'),
        NodeInputBP(label='header'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, quopri.needsquoting(self.input(0), self.input(1), self.input(2)))
        

class Quote_Node(NodeBase):
    """
    Quote a single character."""
    
    title = 'quote'
    type_ = 'quopri'
    init_inputs = [
        NodeInputBP(label='c'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, quopri.quote(self.input(0)))
        

class Unhex_Node(NodeBase):
    """
    Get the integer value of a hexadecimal number."""
    
    title = 'unhex'
    type_ = 'quopri'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, quopri.unhex(self.input(0)))
        


export_nodes(
    A2B_Qp_Node,
    B2A_Qp_Node,
    Decode_Node,
    Decodestring_Node,
    Encode_Node,
    Encodestring_Node,
    Ishex_Node,
    Main_Node,
    Needsquoting_Node,
    Quote_Node,
    Unhex_Node,
)
