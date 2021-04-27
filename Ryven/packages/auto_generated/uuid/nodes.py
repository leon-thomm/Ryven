
from NENV import *

import uuid


class NodeBase(Node):
    pass


class _Arp_Getnode_Node(NodeBase):
    title = '_arp_getnode'
    type_ = 'uuid'
    doc = """Get the hardware address on Unix by running arp."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._arp_getnode())
        

class _Find_Mac_Node(NodeBase):
    title = '_find_mac'
    type_ = 'uuid'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='command'),
        NodeInputBP(label='args'),
        NodeInputBP(label='hw_identifiers'),
        NodeInputBP(label='get_index'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._find_mac(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Ifconfig_Getnode_Node(NodeBase):
    title = '_ifconfig_getnode'
    type_ = 'uuid'
    doc = """Get the hardware address on Unix by running ifconfig."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._ifconfig_getnode())
        

class _Ip_Getnode_Node(NodeBase):
    title = '_ip_getnode'
    type_ = 'uuid'
    doc = """Get the hardware address on Unix by running ip."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._ip_getnode())
        

class _Ipconfig_Getnode_Node(NodeBase):
    title = '_ipconfig_getnode'
    type_ = 'uuid'
    doc = """Get the hardware address on Windows by running ipconfig.exe."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._ipconfig_getnode())
        

class _Is_Universal_Node(NodeBase):
    title = '_is_universal'
    type_ = 'uuid'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='mac'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._is_universal(self.input(0)))
        

class _Lanscan_Getnode_Node(NodeBase):
    title = '_lanscan_getnode'
    type_ = 'uuid'
    doc = """Get the hardware address on Unix by running lanscan."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._lanscan_getnode())
        

class _Load_System_Functions_Node(NodeBase):
    title = '_load_system_functions'
    type_ = 'uuid'
    doc = """
    Try to load platform-specific functions for generating uuids.
    """
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._load_system_functions())
        

class _Netbios_Getnode_Node(NodeBase):
    title = '_netbios_getnode'
    type_ = 'uuid'
    doc = """Get the hardware address on Windows using NetBIOS calls.
    See http://support.microsoft.com/kb/118623 for details."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._netbios_getnode())
        

class _Netstat_Getnode_Node(NodeBase):
    title = '_netstat_getnode'
    type_ = 'uuid'
    doc = """Get the hardware address on Unix by running netstat."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._netstat_getnode())
        

class _Popen_Node(NodeBase):
    title = '_popen'
    type_ = 'uuid'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='command'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._popen(self.input(0)))
        

class _Random_Getnode_Node(NodeBase):
    title = '_random_getnode'
    type_ = 'uuid'
    doc = """Get a random node ID."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._random_getnode())
        

class _Unix_Getnode_Node(NodeBase):
    title = '_unix_getnode'
    type_ = 'uuid'
    doc = """Get the hardware address on Unix using the _uuid extension module
    or ctypes."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._unix_getnode())
        

class _Windll_Getnode_Node(NodeBase):
    title = '_windll_getnode'
    type_ = 'uuid'
    doc = """Get the hardware address on Windows using ctypes."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid._windll_getnode())
        

class Getnode_Node(NodeBase):
    title = 'getnode'
    type_ = 'uuid'
    doc = """Get the hardware address as a 48-bit positive integer.

    The first time this runs, it may launch a separate program, which could
    be quite slow.  If all attempts to obtain the hardware address fail, we
    choose a random 48-bit number with its eighth bit set to 1 as recommended
    in RFC 4122.
    """
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid.getnode())
        

class Uuid1_Node(NodeBase):
    title = 'uuid1'
    type_ = 'uuid'
    doc = """Generate a UUID from a host ID, sequence number, and the current time.
    If 'node' is not given, getnode() is used to obtain the hardware
    address.  If 'clock_seq' is given, it is used as the sequence number;
    otherwise a random 14-bit sequence number is chosen."""
    init_inputs = [
        NodeInputBP(label='node', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='clock_seq', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid.uuid1(self.input(0), self.input(1)))
        

class Uuid3_Node(NodeBase):
    title = 'uuid3'
    type_ = 'uuid'
    doc = """Generate a UUID from the MD5 hash of a namespace UUID and a name."""
    init_inputs = [
        NodeInputBP(label='namespace'),
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid.uuid3(self.input(0), self.input(1)))
        

class Uuid4_Node(NodeBase):
    title = 'uuid4'
    type_ = 'uuid'
    doc = """Generate a random UUID."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid.uuid4())
        

class Uuid5_Node(NodeBase):
    title = 'uuid5'
    type_ = 'uuid'
    doc = """Generate a UUID from the SHA-1 hash of a namespace UUID and a name."""
    init_inputs = [
        NodeInputBP(label='namespace'),
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, uuid.uuid5(self.input(0), self.input(1)))
        


export_nodes(
    _Arp_Getnode_Node,
    _Find_Mac_Node,
    _Ifconfig_Getnode_Node,
    _Ip_Getnode_Node,
    _Ipconfig_Getnode_Node,
    _Is_Universal_Node,
    _Lanscan_Getnode_Node,
    _Load_System_Functions_Node,
    _Netbios_Getnode_Node,
    _Netstat_Getnode_Node,
    _Popen_Node,
    _Random_Getnode_Node,
    _Unix_Getnode_Node,
    _Windll_Getnode_Node,
    Getnode_Node,
    Uuid1_Node,
    Uuid3_Node,
    Uuid4_Node,
    Uuid5_Node,
)
