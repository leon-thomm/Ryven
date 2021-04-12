import ryvencore_qt as rc
import nntplib


class AutoNode_nntplib__email_decode_header(rc.Node):
    title = '_email_decode_header'
    description = '''Decode a message header value without converting charset.

    Returns a list of (string, charset) pairs containing each of the decoded
    parts of the header.  Charset is None for non-encoded parts of the header,
    otherwise a lower-case string containing the name of the character set
    specified in the encoded string.

    header may be a string that may or may not contain RFC2047 encoded words,
    or it may be a Header object.

    An email.errors.HeaderParseError may be raised when certain decoding error
    occurs (e.g. a base64 decoding exception).
    '''
    init_inputs = [
        rc.NodeInputBP(label='header'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nntplib._email_decode_header(self.input(0)))
        


class AutoNode_nntplib__encrypt_on(rc.Node):
    title = '_encrypt_on'
    description = '''Wrap a socket in SSL/TLS. Arguments:
        - sock: Socket to wrap
        - context: SSL context to use for the encrypted connection
        Returns:
        - sock: New, encrypted socket.
        '''
    init_inputs = [
        rc.NodeInputBP(label='sock'),
rc.NodeInputBP(label='context'),
rc.NodeInputBP(label='hostname'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nntplib._encrypt_on(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_nntplib__parse_datetime(rc.Node):
    title = '_parse_datetime'
    description = '''Parse a pair of (date, time) strings, and return a datetime object.
    If only the date is given, it is assumed to be date and time
    concatenated together (e.g. response to the DATE command).
    '''
    init_inputs = [
        rc.NodeInputBP(label='date_str'),
rc.NodeInputBP(label='time_str'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nntplib._parse_datetime(self.input(0), self.input(1)))
        


class AutoNode_nntplib__parse_overview(rc.Node):
    title = '_parse_overview'
    description = '''Parse the response to an OVER or XOVER command according to the
    overview format `fmt`.'''
    init_inputs = [
        rc.NodeInputBP(label='lines'),
rc.NodeInputBP(label='fmt'),
rc.NodeInputBP(label='data_process_func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nntplib._parse_overview(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_nntplib__parse_overview_fmt(rc.Node):
    title = '_parse_overview_fmt'
    description = '''Parse a list of string representing the response to LIST OVERVIEW.FMT
    and return a list of header/metadata names.
    Raises NNTPDataError if the response is not compliant
    (cf. RFC 3977, section 8.4).'''
    init_inputs = [
        rc.NodeInputBP(label='lines'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nntplib._parse_overview_fmt(self.input(0)))
        


class AutoNode_nntplib__unparse_datetime(rc.Node):
    title = '_unparse_datetime'
    description = '''Format a date or datetime object as a pair of (date, time) strings
    in the format required by the NEWNEWS and NEWGROUPS commands.  If a
    date object is passed, the time is assumed to be midnight (00h00).

    The returned representation depends on the legacy flag:
    * if legacy is False (the default):
      date has the YYYYMMDD format and time the HHMMSS format
    * if legacy is True:
      date has the YYMMDD format and time the HHMMSS format.
    RFC 3977 compliant servers should understand both formats; therefore,
    legacy is only needed when talking to old servers.
    '''
    init_inputs = [
        rc.NodeInputBP(label='dt'),
rc.NodeInputBP(label='legacy'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nntplib._unparse_datetime(self.input(0), self.input(1)))
        


class AutoNode_nntplib_decode_header(rc.Node):
    title = 'decode_header'
    description = '''Takes a unicode string representing a munged header value
    and decodes it as a (possibly non-ASCII) readable value.'''
    init_inputs = [
        rc.NodeInputBP(label='header_str'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nntplib.decode_header(self.input(0)))
        