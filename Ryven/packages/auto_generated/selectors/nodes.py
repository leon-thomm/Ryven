
from NENV import *

import selectors


class NodeBase(Node):
    pass


class _Can_Use_Node(NodeBase):
    """
    Check if we can use the selector depending upon the
    operating system. """
    
    title = '_can_use'
    type_ = 'selectors'
    init_inputs = [
        NodeInputBP(label='method'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, selectors._can_use(self.input(0)))
        

class _Fileobj_To_Fd_Node(NodeBase):
    """
    Return a file descriptor from a file object.

    Parameters:
    fileobj -- file object or file descriptor

    Returns:
    corresponding file descriptor

    Raises:
    ValueError if the object is invalid
    """
    
    title = '_fileobj_to_fd'
    type_ = 'selectors'
    init_inputs = [
        NodeInputBP(label='fileobj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, selectors._fileobj_to_fd(self.input(0)))
        

class Abstractmethod_Node(NodeBase):
    """
    A decorator indicating abstract methods.

    Requires that the metaclass is ABCMeta or derived from it.  A
    class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods are overridden.
    The abstract methods can be called using any of the normal
    'super' call mechanisms.  abstractmethod() may be used to declare
    abstract methods for properties and descriptors.

    Usage:

        class C(metaclass=ABCMeta):
            @abstractmethod
            def my_abstract_method(self, ...):
                ...
    """
    
    title = 'abstractmethod'
    type_ = 'selectors'
    init_inputs = [
        NodeInputBP(label='funcobj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, selectors.abstractmethod(self.input(0)))
        

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
    type_ = 'selectors'
    init_inputs = [
        NodeInputBP(label='typename'),
        NodeInputBP(label='field_names'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, selectors.namedtuple(self.input(0), self.input(1)))
        


export_nodes(
    _Can_Use_Node,
    _Fileobj_To_Fd_Node,
    Abstractmethod_Node,
    Namedtuple_Node,
)
