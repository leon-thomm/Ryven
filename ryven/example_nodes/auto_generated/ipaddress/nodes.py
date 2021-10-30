
from ryven.NENV import *

import ipaddress


class NodeBase(Node):
    pass


class _Collapse_Addresses_Internal_Node(NodeBase):
    """
    Loops through the addresses, collapsing concurrent netblocks.

    Example:

        ip1 = IPv4Network('192.0.2.0/26')
        ip2 = IPv4Network('192.0.2.64/26')
        ip3 = IPv4Network('192.0.2.128/26')
        ip4 = IPv4Network('192.0.2.192/26')

        _collapse_addresses_internal([ip1, ip2, ip3, ip4]) ->
          [IPv4Network('192.0.2.0/24')]

        This shouldn't be called directly; it is called via
          collapse_addresses([]).

    Args:
        addresses: A list of IPv4Network's or IPv6Network's

    Returns:
        A list of IPv4Network's or IPv6Network's depending on what we were
        passed.

    """
    
    title = '_collapse_addresses_internal'
    type_ = 'ipaddress'
    init_inputs = [
        NodeInputBP(label='addresses'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ipaddress._collapse_addresses_internal(self.input(0)))
        

class _Count_Righthand_Zero_Bits_Node(NodeBase):
    """
    Count the number of zero bits on the right hand side.

    Args:
        number: an integer.
        bits: maximum number of bits to count.

    Returns:
        The number of zero bits on the right hand side of the number.

    """
    
    title = '_count_righthand_zero_bits'
    type_ = 'ipaddress'
    init_inputs = [
        NodeInputBP(label='number'),
        NodeInputBP(label='bits'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ipaddress._count_righthand_zero_bits(self.input(0), self.input(1)))
        

class _Find_Address_Range_Node(NodeBase):
    """
    Find a sequence of sorted deduplicated IPv#Address.

    Args:
        addresses: a list of IPv#Address objects.

    Yields:
        A tuple containing the first and last IP addresses in the sequence.

    """
    
    title = '_find_address_range'
    type_ = 'ipaddress'
    init_inputs = [
        NodeInputBP(label='addresses'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ipaddress._find_address_range(self.input(0)))
        

class _Split_Optional_Netmask_Node(NodeBase):
    """
    Helper to split the netmask and raise AddressValueError if needed"""
    
    title = '_split_optional_netmask'
    type_ = 'ipaddress'
    init_inputs = [
        NodeInputBP(label='address'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ipaddress._split_optional_netmask(self.input(0)))
        

class Collapse_Addresses_Node(NodeBase):
    """
    Collapse a list of IP objects.

    Example:
        collapse_addresses([IPv4Network('192.0.2.0/25'),
                            IPv4Network('192.0.2.128/25')]) ->
                           [IPv4Network('192.0.2.0/24')]

    Args:
        addresses: An iterator of IPv4Network or IPv6Network objects.

    Returns:
        An iterator of the collapsed IPv(4|6)Network objects.

    Raises:
        TypeError: If passed a list of mixed version objects.

    """
    
    title = 'collapse_addresses'
    type_ = 'ipaddress'
    init_inputs = [
        NodeInputBP(label='addresses'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ipaddress.collapse_addresses(self.input(0)))
        

class Get_Mixed_Type_Key_Node(NodeBase):
    """
    Return a key suitable for sorting between networks and addresses.

    Address and Network objects are not sortable by default; they're
    fundamentally different so the expression

        IPv4Address('192.0.2.0') <= IPv4Network('192.0.2.0/24')

    doesn't make any sense.  There are some times however, where you may wish
    to have ipaddress sort these for you anyway. If you need to do this, you
    can use this function as the key= argument to sorted().

    Args:
      obj: either a Network or Address object.
    Returns:
      appropriate key.

    """
    
    title = 'get_mixed_type_key'
    type_ = 'ipaddress'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ipaddress.get_mixed_type_key(self.input(0)))
        

class Ip_Address_Node(NodeBase):
    """
    Take an IP string/int and return an object of the correct type.

    Args:
        address: A string or integer, the IP address.  Either IPv4 or
          IPv6 addresses may be supplied; integers less than 2**32 will
          be considered to be IPv4 by default.

    Returns:
        An IPv4Address or IPv6Address object.

    Raises:
        ValueError: if the *address* passed isn't either a v4 or a v6
          address

    """
    
    title = 'ip_address'
    type_ = 'ipaddress'
    init_inputs = [
        NodeInputBP(label='address'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ipaddress.ip_address(self.input(0)))
        

class Ip_Interface_Node(NodeBase):
    """
    Take an IP string/int and return an object of the correct type.

    Args:
        address: A string or integer, the IP address.  Either IPv4 or
          IPv6 addresses may be supplied; integers less than 2**32 will
          be considered to be IPv4 by default.

    Returns:
        An IPv4Interface or IPv6Interface object.

    Raises:
        ValueError: if the string passed isn't either a v4 or a v6
          address.

    Notes:
        The IPv?Interface classes describe an Address on a particular
        Network, so they're basically a combination of both the Address
        and Network classes.

    """
    
    title = 'ip_interface'
    type_ = 'ipaddress'
    init_inputs = [
        NodeInputBP(label='address'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ipaddress.ip_interface(self.input(0)))
        

class Ip_Network_Node(NodeBase):
    """
    Take an IP string/int and return an object of the correct type.

    Args:
        address: A string or integer, the IP network.  Either IPv4 or
          IPv6 networks may be supplied; integers less than 2**32 will
          be considered to be IPv4 by default.

    Returns:
        An IPv4Network or IPv6Network object.

    Raises:
        ValueError: if the string passed isn't either a v4 or a v6
          address. Or if the network has host bits set.

    """
    
    title = 'ip_network'
    type_ = 'ipaddress'
    init_inputs = [
        NodeInputBP(label='address'),
        NodeInputBP(label='strict', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ipaddress.ip_network(self.input(0), self.input(1)))
        

class Summarize_Address_Range_Node(NodeBase):
    """
    Summarize a network range given the first and last IP addresses.

    Example:
        >>> list(summarize_address_range(IPv4Address('192.0.2.0'),
        ...                              IPv4Address('192.0.2.130')))
        ...                                #doctest: +NORMALIZE_WHITESPACE
        [IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/31'),
         IPv4Network('192.0.2.130/32')]

    Args:
        first: the first IPv4Address or IPv6Address in the range.
        last: the last IPv4Address or IPv6Address in the range.

    Returns:
        An iterator of the summarized IPv(4|6) network objects.

    Raise:
        TypeError:
            If the first and last objects are not IP addresses.
            If the first and last objects are not the same version.
        ValueError:
            If the last object is not greater than the first.
            If the version of the first address is not 4 or 6.

    """
    
    title = 'summarize_address_range'
    type_ = 'ipaddress'
    init_inputs = [
        NodeInputBP(label='first'),
        NodeInputBP(label='last'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ipaddress.summarize_address_range(self.input(0), self.input(1)))
        

class V4_Int_To_Packed_Node(NodeBase):
    """
    Represent an address as 4 packed bytes in network (big-endian) order.

    Args:
        address: An integer representation of an IPv4 IP address.

    Returns:
        The integer address packed as 4 bytes in network (big-endian) order.

    Raises:
        ValueError: If the integer is negative or too large to be an
          IPv4 IP address.

    """
    
    title = 'v4_int_to_packed'
    type_ = 'ipaddress'
    init_inputs = [
        NodeInputBP(label='address'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ipaddress.v4_int_to_packed(self.input(0)))
        

class V6_Int_To_Packed_Node(NodeBase):
    """
    Represent an address as 16 packed bytes in network (big-endian) order.

    Args:
        address: An integer representation of an IPv6 IP address.

    Returns:
        The integer address packed as 16 bytes in network (big-endian) order.

    """
    
    title = 'v6_int_to_packed'
    type_ = 'ipaddress'
    init_inputs = [
        NodeInputBP(label='address'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ipaddress.v6_int_to_packed(self.input(0)))
        


export_nodes(
    _Collapse_Addresses_Internal_Node,
    _Count_Righthand_Zero_Bits_Node,
    _Find_Address_Range_Node,
    _Split_Optional_Netmask_Node,
    Collapse_Addresses_Node,
    Get_Mixed_Type_Key_Node,
    Ip_Address_Node,
    Ip_Interface_Node,
    Ip_Network_Node,
    Summarize_Address_Range_Node,
    V4_Int_To_Packed_Node,
    V6_Int_To_Packed_Node,
)
