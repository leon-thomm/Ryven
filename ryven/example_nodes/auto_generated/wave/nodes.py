
from ryven.NENV import *

import wave


class NodeBase(Node):
    pass


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
    type_ = 'wave'
    init_inputs = [
        NodeInputBP(label='typename'),
        NodeInputBP(label='field_names'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, wave.namedtuple(self.input(0), self.input(1)))
        

class Open_Node(NodeBase):
    """
    """
    
    title = 'open'
    type_ = 'wave'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='mode', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, wave.open(self.input(0), self.input(1)))
        


export_nodes(
    Namedtuple_Node,
    Open_Node,
)
