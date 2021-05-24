
from NENV import *

import smtplib


class NodeBase(Node):
    pass


class _Addr_Only_Node(NodeBase):
    """
    """
    
    title = '_addr_only'
    type_ = 'smtplib'
    init_inputs = [
        NodeInputBP(label='addrstring'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, smtplib._addr_only(self.input(0)))
        

class _Fix_Eols_Node(NodeBase):
    """
    """
    
    title = '_fix_eols'
    type_ = 'smtplib'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, smtplib._fix_eols(self.input(0)))
        

class _Quote_Periods_Node(NodeBase):
    """
    """
    
    title = '_quote_periods'
    type_ = 'smtplib'
    init_inputs = [
        NodeInputBP(label='bindata'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, smtplib._quote_periods(self.input(0)))
        

class Encode_Base64_Node(NodeBase):
    """
    Encode a string with base64.

    Each line will be wrapped at, at most, maxlinelen characters (defaults to
    76 characters).

    Each line of encoded text will end with eol, which defaults to "\n".  Set
    this to "\r\n" if you will be using the result of this function directly
    in an email.
    """
    
    title = 'encode_base64'
    type_ = 'smtplib'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='maxlinelen', dtype=dtypes.Data(default=76, size='s')),
        NodeInputBP(label='eol', dtype=dtypes.Data(default='
', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, smtplib.encode_base64(self.input(0), self.input(1), self.input(2)))
        

class Quoteaddr_Node(NodeBase):
    """
    Quote a subset of the email addresses defined by RFC 821.

    Should be able to handle anything email.utils.parseaddr can handle.
    """
    
    title = 'quoteaddr'
    type_ = 'smtplib'
    init_inputs = [
        NodeInputBP(label='addrstring'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, smtplib.quoteaddr(self.input(0)))
        

class Quotedata_Node(NodeBase):
    """
    Quote data for email.

    Double leading '.', and change Unix newline '\n', or Mac '\r' into
    Internet CRLF end-of-line.
    """
    
    title = 'quotedata'
    type_ = 'smtplib'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, smtplib.quotedata(self.input(0)))
        


export_nodes(
    _Addr_Only_Node,
    _Fix_Eols_Node,
    _Quote_Periods_Node,
    Encode_Base64_Node,
    Quoteaddr_Node,
    Quotedata_Node,
)
