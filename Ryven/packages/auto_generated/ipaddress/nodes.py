import ryvencore_qt as rc
import ipaddress


class AutoNode_ipaddress__collapse_addresses_internal(rc.Node):
    title = '_collapse_addresses_internal'
    doc = '''Loops through the addresses, collapsing concurrent netblocks.

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

    '''
    init_inputs = [
        rc.NodeInputBP(label='addresses'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ipaddress._collapse_addresses_internal(self.input(0)))
        


class AutoNode_ipaddress__count_righthand_zero_bits(rc.Node):
    title = '_count_righthand_zero_bits'
    doc = '''Count the number of zero bits on the right hand side.

    Args:
        number: an integer.
        bits: maximum number of bits to count.

    Returns:
        The number of zero bits on the right hand side of the number.

    '''
    init_inputs = [
        rc.NodeInputBP(label='number'),
rc.NodeInputBP(label='bits'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ipaddress._count_righthand_zero_bits(self.input(0), self.input(1)))
        


class AutoNode_ipaddress__find_address_range(rc.Node):
    title = '_find_address_range'
    doc = '''Find a sequence of sorted deduplicated IPv#Address.

    Args:
        addresses: a list of IPv#Address objects.

    Yields:
        A tuple containing the first and last IP addresses in the sequence.

    '''
    init_inputs = [
        rc.NodeInputBP(label='addresses'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ipaddress._find_address_range(self.input(0)))
        


class AutoNode_ipaddress__split_optional_netmask(rc.Node):
    title = '_split_optional_netmask'
    doc = '''Helper to split the netmask and raise AddressValueError if needed'''
    init_inputs = [
        rc.NodeInputBP(label='address'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ipaddress._split_optional_netmask(self.input(0)))
        


class AutoNode_ipaddress_collapse_addresses(rc.Node):
    title = 'collapse_addresses'
    doc = '''Collapse a list of IP objects.

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

    '''
    init_inputs = [
        rc.NodeInputBP(label='addresses'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ipaddress.collapse_addresses(self.input(0)))
        


class AutoNode_ipaddress_get_mixed_type_key(rc.Node):
    title = 'get_mixed_type_key'
    doc = '''Return a key suitable for sorting between networks and addresses.

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

    '''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ipaddress.get_mixed_type_key(self.input(0)))
        


class AutoNode_ipaddress_ip_address(rc.Node):
    title = 'ip_address'
    doc = '''Take an IP string/int and return an object of the correct type.

    Args:
        address: A string or integer, the IP address.  Either IPv4 or
          IPv6 addresses may be supplied; integers less than 2**32 will
          be considered to be IPv4 by default.

    Returns:
        An IPv4Address or IPv6Address object.

    Raises:
        ValueError: if the *address* passed isn't either a v4 or a v6
          address

    '''
    init_inputs = [
        rc.NodeInputBP(label='address'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ipaddress.ip_address(self.input(0)))
        


class AutoNode_ipaddress_ip_interface(rc.Node):
    title = 'ip_interface'
    doc = '''Take an IP string/int and return an object of the correct type.

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

    '''
    init_inputs = [
        rc.NodeInputBP(label='address'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ipaddress.ip_interface(self.input(0)))
        


class AutoNode_ipaddress_ip_network(rc.Node):
    title = 'ip_network'
    doc = '''Take an IP string/int and return an object of the correct type.

    Args:
        address: A string or integer, the IP network.  Either IPv4 or
          IPv6 networks may be supplied; integers less than 2**32 will
          be considered to be IPv4 by default.

    Returns:
        An IPv4Network or IPv6Network object.

    Raises:
        ValueError: if the string passed isn't either a v4 or a v6
          address. Or if the network has host bits set.

    '''
    init_inputs = [
        rc.NodeInputBP(label='address'),
rc.NodeInputBP(label='strict'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ipaddress.ip_network(self.input(0), self.input(1)))
        


class AutoNode_ipaddress_summarize_address_range(rc.Node):
    title = 'summarize_address_range'
    doc = '''Summarize a network range given the first and last IP addresses.

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

    '''
    init_inputs = [
        rc.NodeInputBP(label='first'),
rc.NodeInputBP(label='last'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ipaddress.summarize_address_range(self.input(0), self.input(1)))
        


class AutoNode_ipaddress_v4_int_to_packed(rc.Node):
    title = 'v4_int_to_packed'
    doc = '''Represent an address as 4 packed bytes in network (big-endian) order.

    Args:
        address: An integer representation of an IPv4 IP address.

    Returns:
        The integer address packed as 4 bytes in network (big-endian) order.

    Raises:
        ValueError: If the integer is negative or too large to be an
          IPv4 IP address.

    '''
    init_inputs = [
        rc.NodeInputBP(label='address'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ipaddress.v4_int_to_packed(self.input(0)))
        


class AutoNode_ipaddress_v6_int_to_packed(rc.Node):
    title = 'v6_int_to_packed'
    doc = '''Represent an address as 16 packed bytes in network (big-endian) order.

    Args:
        address: An integer representation of an IPv6 IP address.

    Returns:
        The integer address packed as 16 bytes in network (big-endian) order.

    '''
    init_inputs = [
        rc.NodeInputBP(label='address'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ipaddress.v6_int_to_packed(self.input(0)))
        