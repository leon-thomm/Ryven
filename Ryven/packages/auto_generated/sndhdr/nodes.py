
from NENV import *

import sndhdr


class NodeBase(Node):
    pass


class Get_Long_Be_Node(NodeBase):
    """
    """
    
    title = 'get_long_be'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.get_long_be(self.input(0)))
        

class Get_Long_Le_Node(NodeBase):
    """
    """
    
    title = 'get_long_le'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.get_long_le(self.input(0)))
        

class Get_Short_Be_Node(NodeBase):
    """
    """
    
    title = 'get_short_be'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.get_short_be(self.input(0)))
        

class Get_Short_Le_Node(NodeBase):
    """
    """
    
    title = 'get_short_le'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.get_short_le(self.input(0)))
        

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
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='typename'),
        NodeInputBP(label='field_names'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.namedtuple(self.input(0), self.input(1)))
        

class Test_Node(NodeBase):
    """
    """
    
    title = 'test'
    type_ = 'sndhdr'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.test())
        

class Test_8Svx_Node(NodeBase):
    """
    """
    
    title = 'test_8svx'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.test_8svx(self.input(0), self.input(1)))
        

class Test_Aifc_Node(NodeBase):
    """
    """
    
    title = 'test_aifc'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.test_aifc(self.input(0), self.input(1)))
        

class Test_Au_Node(NodeBase):
    """
    """
    
    title = 'test_au'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.test_au(self.input(0), self.input(1)))
        

class Test_Hcom_Node(NodeBase):
    """
    """
    
    title = 'test_hcom'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.test_hcom(self.input(0), self.input(1)))
        

class Test_Sndr_Node(NodeBase):
    """
    """
    
    title = 'test_sndr'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.test_sndr(self.input(0), self.input(1)))
        

class Test_Sndt_Node(NodeBase):
    """
    """
    
    title = 'test_sndt'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.test_sndt(self.input(0), self.input(1)))
        

class Test_Voc_Node(NodeBase):
    """
    """
    
    title = 'test_voc'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.test_voc(self.input(0), self.input(1)))
        

class Test_Wav_Node(NodeBase):
    """
    """
    
    title = 'test_wav'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.test_wav(self.input(0), self.input(1)))
        

class Testall_Node(NodeBase):
    """
    """
    
    title = 'testall'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='list'),
        NodeInputBP(label='recursive'),
        NodeInputBP(label='toplevel'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.testall(self.input(0), self.input(1), self.input(2)))
        

class What_Node(NodeBase):
    """
    Guess the type of a sound file."""
    
    title = 'what'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.what(self.input(0)))
        

class Whathdr_Node(NodeBase):
    """
    Recognize sound headers."""
    
    title = 'whathdr'
    type_ = 'sndhdr'
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sndhdr.whathdr(self.input(0)))
        


export_nodes(
    Get_Long_Be_Node,
    Get_Long_Le_Node,
    Get_Short_Be_Node,
    Get_Short_Le_Node,
    Namedtuple_Node,
    Test_Node,
    Test_8Svx_Node,
    Test_Aifc_Node,
    Test_Au_Node,
    Test_Hcom_Node,
    Test_Sndr_Node,
    Test_Sndt_Node,
    Test_Voc_Node,
    Test_Wav_Node,
    Testall_Node,
    What_Node,
    Whathdr_Node,
)
