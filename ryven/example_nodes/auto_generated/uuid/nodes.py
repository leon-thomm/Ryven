
from ryven.NENV import *

import uuid


class NodeBase(Node):
    pass


class _Arp_Getnode_Node(NodeBase):
    """
    Get the hardware address on Unix by running arp."""
    
    title = '_arp_getnode'
    type_ = 'uuid'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._arp_getnode())
        

class _Find_Mac_Near_Keyword_Node(NodeBase):
    """
    Searches a command's output for a MAC address near a keyword.

    Each line of words in the output is case-insensitively searched for
    any of the given keywords.  Upon a match, get_word_index is invoked
    to pick a word from the line, given the index of the match.  For
    example, lambda i: 0 would get the first word on the line, while
    lambda i: i - 1 would get the word preceding the keyword.
    """
    
    title = '_find_mac_near_keyword'
    type_ = 'uuid'
    init_inputs = [
        NodeInputBP(label='command'),
        NodeInputBP(label='args'),
        NodeInputBP(label='keywords'),
        NodeInputBP(label='get_word_index'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._find_mac_near_keyword(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Find_Mac_Under_Heading_Node(NodeBase):
    """
    Looks for a MAC address under a heading in a command's output.

    The first line of words in the output is searched for the given
    heading. Words at the same word index as the heading in subsequent
    lines are then examined to see if they look like MAC addresses.
    """
    
    title = '_find_mac_under_heading'
    type_ = 'uuid'
    init_inputs = [
        NodeInputBP(label='command'),
        NodeInputBP(label='args'),
        NodeInputBP(label='heading'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._find_mac_under_heading(self.input(0), self.input(1), self.input(2)))
        

class _Get_Command_Stdout_Node(NodeBase):
    """
    """
    
    title = '_get_command_stdout'
    type_ = 'uuid'
    init_inputs = [
        NodeInputBP(label='command'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._get_command_stdout(self.input(0)))
        

class _Ifconfig_Getnode_Node(NodeBase):
    """
    Get the hardware address on Unix by running ifconfig."""
    
    title = '_ifconfig_getnode'
    type_ = 'uuid'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._ifconfig_getnode())
        

class _Ip_Getnode_Node(NodeBase):
    """
    Get the hardware address on Unix by running ip."""
    
    title = '_ip_getnode'
    type_ = 'uuid'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._ip_getnode())
        

class _Ipconfig_Getnode_Node(NodeBase):
    """
    [DEPRECATED] Get the hardware address on Windows."""
    
    title = '_ipconfig_getnode'
    type_ = 'uuid'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._ipconfig_getnode())
        

class _Is_Universal_Node(NodeBase):
    """
    """
    
    title = '_is_universal'
    type_ = 'uuid'
    init_inputs = [
        NodeInputBP(label='mac'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._is_universal(self.input(0)))
        

class _Lanscan_Getnode_Node(NodeBase):
    """
    Get the hardware address on Unix by running lanscan."""
    
    title = '_lanscan_getnode'
    type_ = 'uuid'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._lanscan_getnode())
        

class _Load_System_Functions_Node(NodeBase):
    """
    [DEPRECATED] Platform-specific functions loaded at import time"""
    
    title = '_load_system_functions'
    type_ = 'uuid'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._load_system_functions())
        

class _Netbios_Getnode_Node(NodeBase):
    """
    [DEPRECATED] Get the hardware address on Windows."""
    
    title = '_netbios_getnode'
    type_ = 'uuid'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._netbios_getnode())
        

class _Netstat_Getnode_Node(NodeBase):
    """
    Get the hardware address on Unix by running netstat."""
    
    title = '_netstat_getnode'
    type_ = 'uuid'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._netstat_getnode())
        

class _Parse_Mac_Node(NodeBase):
    """
    """
    
    title = '_parse_mac'
    type_ = 'uuid'
    init_inputs = [
        NodeInputBP(label='word'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._parse_mac(self.input(0)))
        

class _Random_Getnode_Node(NodeBase):
    """
    Get a random node ID."""
    
    title = '_random_getnode'
    type_ = 'uuid'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._random_getnode())
        

class _Unix_Getnode_Node(NodeBase):
    """
    Get the hardware address on Unix using the _uuid extension module."""
    
    title = '_unix_getnode'
    type_ = 'uuid'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._unix_getnode())
        

class _Windll_Getnode_Node(NodeBase):
    """
    Get the hardware address on Windows using the _uuid extension module."""
    
    title = '_windll_getnode'
    type_ = 'uuid'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid._windll_getnode())
        

class Getnode_Node(NodeBase):
    """
    Get the hardware address as a 48-bit positive integer.

    The first time this runs, it may launch a separate program, which could
    be quite slow.  If all attempts to obtain the hardware address fail, we
    choose a random 48-bit number with its eighth bit set to 1 as recommended
    in RFC 4122.
    """
    
    title = 'getnode'
    type_ = 'uuid'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid.getnode())
        

class Uuid1_Node(NodeBase):
    """
    Generate a UUID from a host ID, sequence number, and the current time.
    If 'node' is not given, getnode() is used to obtain the hardware
    address.  If 'clock_seq' is given, it is used as the sequence number;
    otherwise a random 14-bit sequence number is chosen."""
    
    title = 'uuid1'
    type_ = 'uuid'
    init_inputs = [
        NodeInputBP(label='node', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='clock_seq', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid.uuid1(self.input(0), self.input(1)))
        

class Uuid3_Node(NodeBase):
    """
    Generate a UUID from the MD5 hash of a namespace UUID and a name."""
    
    title = 'uuid3'
    type_ = 'uuid'
    init_inputs = [
        NodeInputBP(label='namespace'),
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid.uuid3(self.input(0), self.input(1)))
        

class Uuid4_Node(NodeBase):
    """
    Generate a random UUID."""
    
    title = 'uuid4'
    type_ = 'uuid'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid.uuid4())
        

class Uuid5_Node(NodeBase):
    """
    Generate a UUID from the SHA-1 hash of a namespace UUID and a name."""
    
    title = 'uuid5'
    type_ = 'uuid'
    init_inputs = [
        NodeInputBP(label='namespace'),
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, uuid.uuid5(self.input(0), self.input(1)))
        


export_nodes(
    _Arp_Getnode_Node,
    _Find_Mac_Near_Keyword_Node,
    _Find_Mac_Under_Heading_Node,
    _Get_Command_Stdout_Node,
    _Ifconfig_Getnode_Node,
    _Ip_Getnode_Node,
    _Ipconfig_Getnode_Node,
    _Is_Universal_Node,
    _Lanscan_Getnode_Node,
    _Load_System_Functions_Node,
    _Netbios_Getnode_Node,
    _Netstat_Getnode_Node,
    _Parse_Mac_Node,
    _Random_Getnode_Node,
    _Unix_Getnode_Node,
    _Windll_Getnode_Node,
    Getnode_Node,
    Uuid1_Node,
    Uuid3_Node,
    Uuid4_Node,
    Uuid5_Node,
)
