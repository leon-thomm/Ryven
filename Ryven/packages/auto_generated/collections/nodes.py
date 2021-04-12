import ryvencore_qt as rc
import collections


class AutoNode_collections___getattr__(rc.Node):
    title = '__getattr__'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, collections.__getattr__(self.input(0)))
        


class AutoNode_collections__count_elements(rc.Node):
    title = '_count_elements'
    description = '''Count elements in the iterable, updating the mapping'''
    init_inputs = [
        rc.NodeInputBP(label='mapping'),
rc.NodeInputBP(label='iterable'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, collections._count_elements(self.input(0), self.input(1)))
        


class AutoNode_collections__eq(rc.Node):
    title = '_eq'
    description = '''Same as a == b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, collections._eq(self.input(0), self.input(1)))
        


class AutoNode_collections__recursive_repr(rc.Node):
    title = '_recursive_repr'
    description = '''Decorator to make a repr function return fillvalue for a recursive call'''
    init_inputs = [
        rc.NodeInputBP(label='fillvalue'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, collections._recursive_repr(self.input(0)))
        


class AutoNode_collections_namedtuple(rc.Node):
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
        self.set_output_val(0, collections.namedtuple(self.input(0), self.input(1)))
        