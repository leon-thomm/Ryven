
from NENV import *

import ssl


class NodeBase(Node):
    pass


class Der_Cert_To_Pem_Cert_Node(NodeBase):
    """
    Takes a certificate in binary DER format and returns the
    PEM version of it as a string."""
    
    title = 'DER_cert_to_PEM_cert'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='der_cert_bytes'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.DER_cert_to_PEM_cert(self.input(0)))
        

class Pem_Cert_To_Der_Cert_Node(NodeBase):
    """
    Takes a certificate in ASCII PEM format and returns the
    DER-encoded version of it as a byte sequence"""
    
    title = 'PEM_cert_to_DER_cert'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='pem_cert_string'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.PEM_cert_to_DER_cert(self.input(0)))
        

class Rand_Add_Node(NodeBase):
    """
    Mix string into the OpenSSL PRNG state.

entropy (a float) is a lower bound on the entropy contained in
string.  See RFC 4086."""
    
    title = 'RAND_add'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='string'),
        NodeInputBP(label='entropy'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.RAND_add(self.input(0), self.input(1)))
        

class Rand_Bytes_Node(NodeBase):
    """
    Generate n cryptographically strong pseudo-random bytes."""
    
    title = 'RAND_bytes'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.RAND_bytes(self.input(0)))
        

class Rand_Pseudo_Bytes_Node(NodeBase):
    """
    Generate n pseudo-random bytes.

Return a pair (bytes, is_cryptographic).  is_cryptographic is True
if the bytes generated are cryptographically strong."""
    
    title = 'RAND_pseudo_bytes'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.RAND_pseudo_bytes(self.input(0)))
        

class Rand_Status_Node(NodeBase):
    """
    Returns 1 if the OpenSSL PRNG has been seeded with enough data and 0 if not.

It is necessary to seed the PRNG with RAND_add() on some platforms before
using the ssl() function."""
    
    title = 'RAND_status'
    type_ = 'ssl'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.RAND_status())
        

class _Create_Default_Https_Context_Node(NodeBase):
    """
    Create a SSLContext object with default settings.

    NOTE: The protocol and settings may change anytime without prior
          deprecation. The values represent a fair balance between maximum
          compatibility and security.
    """
    
    title = '_create_default_https_context'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='purpose', dtype=dtypes.Data(default=_ASN1Object(nid=129, shortname='serverAuth', longname='TLS Web Server Authentication', oid='1.3.6.1.5.5.7.3.1'), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl._create_default_https_context(self.input(0)))
        

class _Create_Stdlib_Context_Node(NodeBase):
    """
    Create a SSLContext object for Python stdlib modules

    All Python stdlib modules shall use this function to create SSLContext
    objects in order to keep common settings in one place. The configuration
    is less restrict than create_default_context()'s to increase backward
    compatibility.
    """
    
    title = '_create_stdlib_context'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='protocol', dtype=dtypes.Data(default=2, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl._create_stdlib_context(self.input(0)))
        

class _Create_Unverified_Context_Node(NodeBase):
    """
    Create a SSLContext object for Python stdlib modules

    All Python stdlib modules shall use this function to create SSLContext
    objects in order to keep common settings in one place. The configuration
    is less restrict than create_default_context()'s to increase backward
    compatibility.
    """
    
    title = '_create_unverified_context'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='protocol', dtype=dtypes.Data(default=2, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl._create_unverified_context(self.input(0)))
        

class _Dnsname_Match_Node(NodeBase):
    """
    Matching according to RFC 6125, section 6.4.3

    - Hostnames are compared lower case.
    - For IDNA, both dn and hostname must be encoded as IDN A-label (ACE).
    - Partial wildcards like 'www*.example.org', multiple wildcards, sole
      wildcard or wildcards in labels other then the left-most label are not
      supported and a CertificateError is raised.
    - A wildcard must match at least one character.
    """
    
    title = '_dnsname_match'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='dn'),
        NodeInputBP(label='hostname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl._dnsname_match(self.input(0), self.input(1)))
        

class _Inet_Paton_Node(NodeBase):
    """
    Try to convert an IP address to packed binary form

    Supports IPv4 addresses on all platforms and IPv6 on platforms with IPv6
    support.
    """
    
    title = '_inet_paton'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='ipname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl._inet_paton(self.input(0)))
        

class _Ipaddress_Match_Node(NodeBase):
    """
    Exact matching of IP addresses.

    RFC 6125 explicitly doesn't define an algorithm for this
    (section 1.7.2 - "Out of Scope").
    """
    
    title = '_ipaddress_match'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='cert_ipaddress'),
        NodeInputBP(label='host_ip'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl._ipaddress_match(self.input(0), self.input(1)))
        

class _Nid2Obj_Node(NodeBase):
    """
    Lookup NID, short name, long name and OID of an ASN1_OBJECT by NID."""
    
    title = '_nid2obj'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='nid'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl._nid2obj(self.input(0)))
        

class _Sslcopydoc_Node(NodeBase):
    """
    Copy docstring from SSLObject to SSLSocket"""
    
    title = '_sslcopydoc'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl._sslcopydoc(self.input(0)))
        

class _Txt2Obj_Node(NodeBase):
    """
    Lookup NID, short name, long name and OID of an ASN1_OBJECT.

By default objects are looked up by OID. With name=True short and
long name are also matched."""
    
    title = '_txt2obj'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='txt'),
        NodeInputBP(label='name', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl._txt2obj(self.input(0), self.input(1)))
        

class Cert_Time_To_Seconds_Node(NodeBase):
    """
    Return the time in seconds since the Epoch, given the timestring
    representing the "notBefore" or "notAfter" date from a certificate
    in ``"%b %d %H:%M:%S %Y %Z"`` strptime format (C locale).

    "notBefore" or "notAfter" dates must use UTC (RFC 5280).

    Month is one of: Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
    UTC should be specified as GMT (see ASN1_TIME_print())
    """
    
    title = 'cert_time_to_seconds'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='cert_time'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.cert_time_to_seconds(self.input(0)))
        

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
    type_ = 'ssl'
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
        self.set_output_val(0, ssl.create_connection(self.input(0), self.input(1), self.input(2)))
        

class Create_Default_Context_Node(NodeBase):
    """
    Create a SSLContext object with default settings.

    NOTE: The protocol and settings may change anytime without prior
          deprecation. The values represent a fair balance between maximum
          compatibility and security.
    """
    
    title = 'create_default_context'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='purpose', dtype=dtypes.Data(default=_ASN1Object(nid=129, shortname='serverAuth', longname='TLS Web Server Authentication', oid='1.3.6.1.5.5.7.3.1'), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.create_default_context(self.input(0)))
        

class Enum_Certificates_Node(NodeBase):
    """
    Retrieve certificates from Windows' cert store.

store_name may be one of 'CA', 'ROOT' or 'MY'.  The system may provide
more cert storages, too.  The function returns a list of (bytes,
encoding_type, trust) tuples.  The encoding_type flag can be interpreted
with X509_ASN_ENCODING or PKCS_7_ASN_ENCODING. The trust setting is either
a set of OIDs or the boolean True."""
    
    title = 'enum_certificates'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='store_name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.enum_certificates(self.input(0)))
        

class Enum_Crls_Node(NodeBase):
    """
    Retrieve CRLs from Windows' cert store.

store_name may be one of 'CA', 'ROOT' or 'MY'.  The system may provide
more cert storages, too.  The function returns a list of (bytes,
encoding_type) tuples.  The encoding_type flag can be interpreted with
X509_ASN_ENCODING or PKCS_7_ASN_ENCODING."""
    
    title = 'enum_crls'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='store_name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.enum_crls(self.input(0)))
        

class Get_Default_Verify_Paths_Node(NodeBase):
    """
    Return paths to default cafile and capath.
    """
    
    title = 'get_default_verify_paths'
    type_ = 'ssl'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.get_default_verify_paths())
        

class Get_Protocol_Name_Node(NodeBase):
    """
    """
    
    title = 'get_protocol_name'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='protocol_code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.get_protocol_name(self.input(0)))
        

class Get_Server_Certificate_Node(NodeBase):
    """
    Retrieve the certificate from the server at the specified address,
    and return it as a PEM-encoded string.
    If 'ca_certs' is specified, validate the server cert against it.
    If 'ssl_version' is specified, use it in the connection attempt."""
    
    title = 'get_server_certificate'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='addr'),
        NodeInputBP(label='ssl_version', dtype=dtypes.Data(default=2, size='s')),
        NodeInputBP(label='ca_certs', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.get_server_certificate(self.input(0), self.input(1), self.input(2)))
        

class Match_Hostname_Node(NodeBase):
    """
    Verify that *cert* (in decoded format as returned by
    SSLSocket.getpeercert()) matches the *hostname*.  RFC 2818 and RFC 6125
    rules are followed.

    The function matches IP addresses rather than dNSNames if hostname is a
    valid ipaddress string. IPv4 addresses are supported on all platforms.
    IPv6 addresses are supported on platforms with IPv6 support (AF_INET6
    and inet_pton).

    CertificateError is raised on failure. On success, the function
    returns nothing.
    """
    
    title = 'match_hostname'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='cert'),
        NodeInputBP(label='hostname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.match_hostname(self.input(0), self.input(1)))
        

class Namedtuple_Node(NodeBase):
    """
    Returns a new subclass of tuple with named fields.

    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessible by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)

    """
    
    title = 'namedtuple'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='typename'),
        NodeInputBP(label='field_names'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.namedtuple(self.input(0), self.input(1)))
        

class Wrap_Socket_Node(NodeBase):
    """
    """
    
    title = 'wrap_socket'
    type_ = 'ssl'
    init_inputs = [
        NodeInputBP(label='sock'),
        NodeInputBP(label='keyfile', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='certfile', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='server_side', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='cert_reqs', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='ssl_version', dtype=dtypes.Data(default=2, size='s')),
        NodeInputBP(label='ca_certs', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='do_handshake_on_connect', dtype=dtypes.Data(default=True, size='s')),
        NodeInputBP(label='suppress_ragged_eofs', dtype=dtypes.Data(default=True, size='s')),
        NodeInputBP(label='ciphers', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ssl.wrap_socket(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7), self.input(8), self.input(9)))
        


export_nodes(
    Der_Cert_To_Pem_Cert_Node,
    Pem_Cert_To_Der_Cert_Node,
    Rand_Add_Node,
    Rand_Bytes_Node,
    Rand_Pseudo_Bytes_Node,
    Rand_Status_Node,
    _Create_Default_Https_Context_Node,
    _Create_Stdlib_Context_Node,
    _Create_Unverified_Context_Node,
    _Dnsname_Match_Node,
    _Inet_Paton_Node,
    _Ipaddress_Match_Node,
    _Nid2Obj_Node,
    _Sslcopydoc_Node,
    _Txt2Obj_Node,
    Cert_Time_To_Seconds_Node,
    Create_Connection_Node,
    Create_Default_Context_Node,
    Enum_Certificates_Node,
    Enum_Crls_Node,
    Get_Default_Verify_Paths_Node,
    Get_Protocol_Name_Node,
    Get_Server_Certificate_Node,
    Match_Hostname_Node,
    Namedtuple_Node,
    Wrap_Socket_Node,
)
