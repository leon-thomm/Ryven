import ryvencore_qt as rc
import aifc


class AutoNode_aifc__read_float(rc.Node):
    title = '_read_float'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc._read_float(self.input(0)))
        


class AutoNode_aifc__read_long(rc.Node):
    title = '_read_long'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc._read_long(self.input(0)))
        


class AutoNode_aifc__read_short(rc.Node):
    title = '_read_short'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc._read_short(self.input(0)))
        


class AutoNode_aifc__read_string(rc.Node):
    title = '_read_string'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc._read_string(self.input(0)))
        


class AutoNode_aifc__read_ulong(rc.Node):
    title = '_read_ulong'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc._read_ulong(self.input(0)))
        


class AutoNode_aifc__read_ushort(rc.Node):
    title = '_read_ushort'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc._read_ushort(self.input(0)))
        


class AutoNode_aifc__write_float(rc.Node):
    title = '_write_float'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc._write_float(self.input(0), self.input(1)))
        


class AutoNode_aifc__write_long(rc.Node):
    title = '_write_long'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc._write_long(self.input(0), self.input(1)))
        


class AutoNode_aifc__write_short(rc.Node):
    title = '_write_short'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc._write_short(self.input(0), self.input(1)))
        


class AutoNode_aifc__write_string(rc.Node):
    title = '_write_string'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc._write_string(self.input(0), self.input(1)))
        


class AutoNode_aifc__write_ulong(rc.Node):
    title = '_write_ulong'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc._write_ulong(self.input(0), self.input(1)))
        


class AutoNode_aifc__write_ushort(rc.Node):
    title = '_write_ushort'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc._write_ushort(self.input(0), self.input(1)))
        


class AutoNode_aifc_namedtuple(rc.Node):
    title = 'namedtuple'
    description = '''Returns a new subclass of tuple with named fields.

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

    '''
    init_inputs = [
        rc.NodeInputBP(label='typename'),
rc.NodeInputBP(label='field_names'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc.namedtuple(self.input(0), self.input(1)))
        


class AutoNode_aifc_open(rc.Node):
    title = 'open'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
rc.NodeInputBP(label='mode'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc.open(self.input(0), self.input(1)))
        


class AutoNode_aifc_openfp(rc.Node):
    title = 'openfp'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
rc.NodeInputBP(label='mode'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, aifc.openfp(self.input(0), self.input(1)))
        