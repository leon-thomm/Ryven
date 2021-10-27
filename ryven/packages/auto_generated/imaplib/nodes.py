
from NENV import *

import imaplib


class NodeBase(Node):
    pass


class Int2Ap_Node(NodeBase):
    """
    Convert integer to A-P string representation."""
    
    title = 'Int2AP'
    type_ = 'imaplib'
    init_inputs = [
        NodeInputBP(label='num'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imaplib.Int2AP(self.input(0)))
        

class Internaldate2Tuple_Node(NodeBase):
    """
    Parse an IMAP4 INTERNALDATE string.

    Return corresponding local time.  The return value is a
    time.struct_time tuple or None if the string has wrong format.
    """
    
    title = 'Internaldate2tuple'
    type_ = 'imaplib'
    init_inputs = [
        NodeInputBP(label='resp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imaplib.Internaldate2tuple(self.input(0)))
        

class Parseflags_Node(NodeBase):
    """
    Convert IMAP4 flags response to python tuple."""
    
    title = 'ParseFlags'
    type_ = 'imaplib'
    init_inputs = [
        NodeInputBP(label='resp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imaplib.ParseFlags(self.input(0)))
        

class Time2Internaldate_Node(NodeBase):
    """
    Convert date_time to IMAP4 INTERNALDATE representation.

    Return string in form: '"DD-Mmm-YYYY HH:MM:SS +HHMM"'.  The
    date_time argument can be a number (int or float) representing
    seconds since epoch (as returned by time.time()), a 9-tuple
    representing local time, an instance of time.struct_time (as
    returned by time.localtime()), an aware datetime instance or a
    double-quoted string.  In the last case, it is assumed to already
    be in the correct format.
    """
    
    title = 'Time2Internaldate'
    type_ = 'imaplib'
    init_inputs = [
        NodeInputBP(label='date_time'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imaplib.Time2Internaldate(self.input(0)))
        


export_nodes(
    Int2Ap_Node,
    Internaldate2Tuple_Node,
    Parseflags_Node,
    Time2Internaldate_Node,
)
