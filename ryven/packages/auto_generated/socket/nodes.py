
from NENV import *

import socket


class NodeBase(Node):
    pass


class _Intenum_Converter_Node(NodeBase):
    """
    Convert a numeric family value to an IntEnum member.

    If it's not a known member, return the numeric value itself.
    """
    
    title = '_intenum_converter'
    type_ = 'socket'
    init_inputs = [
        NodeInputBP(label='value'),
        NodeInputBP(label='enum_klass'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, socket._intenum_converter(self.input(0), self.input(1)))
        

class Create_Connection_Node(NodeBase):
    """
    Connect to *address* and return the socket object.

    Convenience function.  Connect to *address* (a 2-tuple ``(host,
    port)``) and return the socket object.  Passing the optional
    *timeout* parameter will set the timeout on the socket instance
    before attempting to connect.  If no *timeout* is supplied, the
    global default timeout setting returned by :func:`getdefaulttimeout`
    is used.  If *source_address* is set it must be a tuple of (host, port)
    for the socket to bind as a source address before making the connection.
    A host of '' or port 0 tells the OS to use the default.
    """
    
    title = 'create_connection'
    type_ = 'socket'
    init_inputs = [
        NodeInputBP(label='address'),
        NodeInputBP(label='timeout', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='source_address', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, socket.create_connection(self.input(0), self.input(1), self.input(2)))
        

class Create_Server_Node(NodeBase):
    """
    Convenience function which creates a SOCK_STREAM type socket
    bound to *address* (a 2-tuple (host, port)) and return the socket
    object.

    *family* should be either AF_INET or AF_INET6.
    *backlog* is the queue size passed to socket.listen().
    *reuse_port* dictates whether to use the SO_REUSEPORT socket option.
    *dualstack_ipv6*: if true and the platform supports it, it will
    create an AF_INET6 socket able to accept both IPv4 or IPv6
    connections. When false it will explicitly disable this option on
    platforms that enable it by default (e.g. Linux).

    >>> with create_server(('', 8000)) as server:
    ...     while True:
    ...         conn, addr = server.accept()
    ...         # handle new connection
    """
    
    title = 'create_server'
    type_ = 'socket'
    init_inputs = [
        NodeInputBP(label='address'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, socket.create_server(self.input(0)))
        

class Fromfd_Node(NodeBase):
    """
     fromfd(fd, family, type[, proto]) -> socket object

    Create a socket object from a duplicate of the given file
    descriptor.  The remaining arguments are the same as for socket().
    """
    
    title = 'fromfd'
    type_ = 'socket'
    init_inputs = [
        NodeInputBP(label='fd'),
        NodeInputBP(label='family'),
        NodeInputBP(label='type'),
        NodeInputBP(label='proto', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, socket.fromfd(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Fromshare_Node(NodeBase):
    """
     fromshare(info) -> socket object

        Create a socket object from the bytes object returned by
        socket.share(pid).
        """
    
    title = 'fromshare'
    type_ = 'socket'
    init_inputs = [
        NodeInputBP(label='info'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, socket.fromshare(self.input(0)))
        

class Getaddrinfo_Node(NodeBase):
    """
    Resolve host and port into list of address info entries.

    Translate the host/port argument into a sequence of 5-tuples that contain
    all the necessary arguments for creating a socket connected to that service.
    host is a domain name, a string representation of an IPv4/v6 address or
    None. port is a string service name such as 'http', a numeric port number or
    None. By passing None as the value of host and port, you can pass NULL to
    the underlying C API.

    The family, type and proto arguments can be optionally specified in order to
    narrow the list of addresses returned. Passing zero as a value for each of
    these arguments selects the full range of results.
    """
    
    title = 'getaddrinfo'
    type_ = 'socket'
    init_inputs = [
        NodeInputBP(label='host'),
        NodeInputBP(label='port'),
        NodeInputBP(label='family', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='type', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='proto', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, socket.getaddrinfo(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class Getfqdn_Node(NodeBase):
    """
    Get fully qualified domain name from name.

    An empty argument is interpreted as meaning the local host.

    First the hostname returned by gethostbyaddr() is checked, then
    possibly existing aliases. In case no FQDN is available, hostname
    from gethostname() is returned.
    """
    
    title = 'getfqdn'
    type_ = 'socket'
    init_inputs = [
        NodeInputBP(label='name', dtype=dtypes.Data(default='', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, socket.getfqdn(self.input(0)))
        

class Has_Dualstack_Ipv6_Node(NodeBase):
    """
    Return True if the platform supports creating a SOCK_STREAM socket
    which can handle both AF_INET and AF_INET6 (IPv4 / IPv6) connections.
    """
    
    title = 'has_dualstack_ipv6'
    type_ = 'socket'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, socket.has_dualstack_ipv6())
        

class Socketpair_Node(NodeBase):
    """
    socketpair([family[, type[, proto]]]) -> (socket object, socket object)
Create a pair of socket objects from the sockets returned by the platform
socketpair() function.
The arguments are the same as for socket() except the default family is AF_UNIX
if defined on the platform; otherwise, the default is AF_INET.
"""
    
    title = 'socketpair'
    type_ = 'socket'
    init_inputs = [
        NodeInputBP(label='family', dtype=dtypes.Data(default=2, size='s')),
        NodeInputBP(label='type', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='proto', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, socket.socketpair(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _Intenum_Converter_Node,
    Create_Connection_Node,
    Create_Server_Node,
    Fromfd_Node,
    Fromshare_Node,
    Getaddrinfo_Node,
    Getfqdn_Node,
    Has_Dualstack_Ipv6_Node,
    Socketpair_Node,
)
