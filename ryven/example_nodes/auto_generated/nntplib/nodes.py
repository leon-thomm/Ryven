
from ryven.NENV import *

import nntplib


class NodeBase(Node):
    pass


class _Email_Decode_Header_Node(NodeBase):
    """
    Decode a message header value without converting charset.

    Returns a list of (string, charset) pairs containing each of the decoded
    parts of the header.  Charset is None for non-encoded parts of the header,
    otherwise a lower-case string containing the name of the character set
    specified in the encoded string.

    header may be a string that may or may not contain RFC2047 encoded words,
    or it may be a Header object.

    An email.errors.HeaderParseError may be raised when certain decoding error
    occurs (e.g. a base64 decoding exception).
    """
    
    title = '_email_decode_header'
    type_ = 'nntplib'
    init_inputs = [
        NodeInputBP(label='header'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, nntplib._email_decode_header(self.input(0)))
        

class _Encrypt_On_Node(NodeBase):
    """
    Wrap a socket in SSL/TLS. Arguments:
        - sock: Socket to wrap
        - context: SSL context to use for the encrypted connection
        Returns:
        - sock: New, encrypted socket.
        """
    
    title = '_encrypt_on'
    type_ = 'nntplib'
    init_inputs = [
        NodeInputBP(label='sock'),
        NodeInputBP(label='context'),
        NodeInputBP(label='hostname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, nntplib._encrypt_on(self.input(0), self.input(1), self.input(2)))
        

class _Parse_Datetime_Node(NodeBase):
    """
    Parse a pair of (date, time) strings, and return a datetime object.
    If only the date is given, it is assumed to be date and time
    concatenated together (e.g. response to the DATE command).
    """
    
    title = '_parse_datetime'
    type_ = 'nntplib'
    init_inputs = [
        NodeInputBP(label='date_str'),
        NodeInputBP(label='time_str', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, nntplib._parse_datetime(self.input(0), self.input(1)))
        

class _Parse_Overview_Node(NodeBase):
    """
    Parse the response to an OVER or XOVER command according to the
    overview format `fmt`."""
    
    title = '_parse_overview'
    type_ = 'nntplib'
    init_inputs = [
        NodeInputBP(label='lines'),
        NodeInputBP(label='fmt'),
        NodeInputBP(label='data_process_func', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, nntplib._parse_overview(self.input(0), self.input(1), self.input(2)))
        

class _Parse_Overview_Fmt_Node(NodeBase):
    """
    Parse a list of string representing the response to LIST OVERVIEW.FMT
    and return a list of header/metadata names.
    Raises NNTPDataError if the response is not compliant
    (cf. RFC 3977, section 8.4)."""
    
    title = '_parse_overview_fmt'
    type_ = 'nntplib'
    init_inputs = [
        NodeInputBP(label='lines'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, nntplib._parse_overview_fmt(self.input(0)))
        

class _Unparse_Datetime_Node(NodeBase):
    """
    Format a date or datetime object as a pair of (date, time) strings
    in the format required by the NEWNEWS and NEWGROUPS commands.  If a
    date object is passed, the time is assumed to be midnight (00h00).

    The returned representation depends on the legacy flag:
    * if legacy is False (the default):
      date has the YYYYMMDD format and time the HHMMSS format
    * if legacy is True:
      date has the YYMMDD format and time the HHMMSS format.
    RFC 3977 compliant servers should understand both formats; therefore,
    legacy is only needed when talking to old servers.
    """
    
    title = '_unparse_datetime'
    type_ = 'nntplib'
    init_inputs = [
        NodeInputBP(label='dt'),
        NodeInputBP(label='legacy', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, nntplib._unparse_datetime(self.input(0), self.input(1)))
        

class Decode_Header_Node(NodeBase):
    """
    Takes a unicode string representing a munged header value
    and decodes it as a (possibly non-ASCII) readable value."""
    
    title = 'decode_header'
    type_ = 'nntplib'
    init_inputs = [
        NodeInputBP(label='header_str'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, nntplib.decode_header(self.input(0)))
        


export_nodes(
    _Email_Decode_Header_Node,
    _Encrypt_On_Node,
    _Parse_Datetime_Node,
    _Parse_Overview_Node,
    _Parse_Overview_Fmt_Node,
    _Unparse_Datetime_Node,
    Decode_Header_Node,
)
