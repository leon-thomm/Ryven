
from NENV import *

import collections


class NodeBase(Node):
    pass


class __Getattr___Node(NodeBase):
    title = '__getattr__'
    type_ = 'collections'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, collections.__getattr__(self.input(0)))
        

class _Count_Elements_Node(NodeBase):
    title = '_count_elements'
    type_ = 'collections'
    doc = """Count elements in the iterable, updating the mapping"""
    init_inputs = [
        NodeInputBP(label='mapping'),
        NodeInputBP(label='iterable'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, collections._count_elements(self.input(0), self.input(1)))
        

class _Eq_Node(NodeBase):
    title = '_eq'
    type_ = 'collections'
    doc = """Same as a == b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, collections._eq(self.input(0), self.input(1)))
        

class _Recursive_Repr_Node(NodeBase):
    title = '_recursive_repr'
    type_ = 'collections'
    doc = """Decorator to make a repr function return fillvalue for a recursive call"""
    init_inputs = [
        NodeInputBP(label='fillvalue', dtype=dtypes.Data(default='...', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, collections._recursive_repr(self.input(0)))
        

class Namedtuple_Node(NodeBase):
    title = 'namedtuple'
    type_ = 'collections'
    doc = """Returns a new subclass of tuple with named fields.

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
    init_inputs = [
        NodeInputBP(label='typename'),
        NodeInputBP(label='field_names'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, collections.namedtuple(self.input(0), self.input(1)))
        


export_nodes(
    __Getattr___Node,
    _Count_Elements_Node,
    _Eq_Node,
    _Recursive_Repr_Node,
    Namedtuple_Node,
)
