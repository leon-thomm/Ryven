
from ryven.NENV import *

import aifc


class NodeBase(Node):
    pass


class _Read_Float_Node(NodeBase):
    """
    """
    
    title = '_read_float'
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc._read_float(self.input(0)))
        

class _Read_Long_Node(NodeBase):
    """
    """
    
    title = '_read_long'
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc._read_long(self.input(0)))
        

class _Read_Short_Node(NodeBase):
    """
    """
    
    title = '_read_short'
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc._read_short(self.input(0)))
        

class _Read_String_Node(NodeBase):
    """
    """
    
    title = '_read_string'
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc._read_string(self.input(0)))
        

class _Read_Ulong_Node(NodeBase):
    """
    """
    
    title = '_read_ulong'
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc._read_ulong(self.input(0)))
        

class _Read_Ushort_Node(NodeBase):
    """
    """
    
    title = '_read_ushort'
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc._read_ushort(self.input(0)))
        

class _Write_Float_Node(NodeBase):
    """
    """
    
    title = '_write_float'
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc._write_float(self.input(0), self.input(1)))
        

class _Write_Long_Node(NodeBase):
    """
    """
    
    title = '_write_long'
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc._write_long(self.input(0), self.input(1)))
        

class _Write_Short_Node(NodeBase):
    """
    """
    
    title = '_write_short'
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc._write_short(self.input(0), self.input(1)))
        

class _Write_String_Node(NodeBase):
    """
    """
    
    title = '_write_string'
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc._write_string(self.input(0), self.input(1)))
        

class _Write_Ulong_Node(NodeBase):
    """
    """
    
    title = '_write_ulong'
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc._write_ulong(self.input(0), self.input(1)))
        

class _Write_Ushort_Node(NodeBase):
    """
    """
    
    title = '_write_ushort'
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc._write_ushort(self.input(0), self.input(1)))
        

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
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='typename'),
        NodeInputBP(label='field_names'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc.namedtuple(self.input(0), self.input(1)))
        

class Open_Node(NodeBase):
    """
    """
    
    title = 'open'
    type_ = 'aifc'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='mode', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, aifc.open(self.input(0), self.input(1)))
        


export_nodes(
    _Read_Float_Node,
    _Read_Long_Node,
    _Read_Short_Node,
    _Read_String_Node,
    _Read_Ulong_Node,
    _Read_Ushort_Node,
    _Write_Float_Node,
    _Write_Long_Node,
    _Write_Short_Node,
    _Write_String_Node,
    _Write_Ulong_Node,
    _Write_Ushort_Node,
    Namedtuple_Node,
    Open_Node,
)
