import ryvencore_qt as rc
import functools


class AutoNode_functools__c3_merge(rc.Node):
    title = '_c3_merge'
    description = '''Merges MROs in *sequences* to a single MRO using the C3 algorithm.

    Adapted from http://www.python.org/download/releases/2.3/mro/.

    '''
    init_inputs = [
        rc.NodeInputBP(label='sequences'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._c3_merge(self.input(0)))
        


class AutoNode_functools__c3_mro(rc.Node):
    title = '_c3_mro'
    description = '''Computes the method resolution order using extended C3 linearization.

    If no *abcs* are given, the algorithm works exactly like the built-in C3
    linearization used for method resolution.

    If given, *abcs* is a list of abstract base classes that should be inserted
    into the resulting MRO. Unrelated ABCs are ignored and don't end up in the
    result. The algorithm inserts ABCs where their functionality is introduced,
    i.e. issubclass(cls, abc) returns True for the class itself but returns
    False for all its direct base classes. Implicit ABCs for a given class
    (either registered or inferred from the presence of a special method like
    __len__) are inserted directly after the last ABC explicitly listed in the
    MRO of said class. If two implicit ABCs end up next to each other in the
    resulting MRO, their ordering depends on the order of types in *abcs*.

    '''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='abcs'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._c3_mro(self.input(0), self.input(1)))
        


class AutoNode_functools__compose_mro(rc.Node):
    title = '_compose_mro'
    description = '''Calculates the method resolution order for a given class *cls*.

    Includes relevant abstract base classes (with their respective bases) from
    the *types* iterable. Uses a modified C3 linearization algorithm.

    '''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='types'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._compose_mro(self.input(0), self.input(1)))
        


class AutoNode_functools__find_impl(rc.Node):
    title = '_find_impl'
    description = '''Returns the best matching implementation from *registry* for type *cls*.

    Where there is no registered implementation for a specific type, its method
    resolution order is used to find a more generic implementation.

    Note: if *registry* does not contain an implementation for the base
    *object* type, this function may return None.

    '''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='registry'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._find_impl(self.input(0), self.input(1)))
        


class AutoNode_functools__ge_from_gt(rc.Node):
    title = '_ge_from_gt'
    description = '''Return a >= b.  Computed by @total_ordering from (a > b) or (a == b).'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='other'),
rc.NodeInputBP(label='NotImplemented'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._ge_from_gt(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_functools__ge_from_le(rc.Node):
    title = '_ge_from_le'
    description = '''Return a >= b.  Computed by @total_ordering from (not a <= b) or (a == b).'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='other'),
rc.NodeInputBP(label='NotImplemented'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._ge_from_le(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_functools__ge_from_lt(rc.Node):
    title = '_ge_from_lt'
    description = '''Return a >= b.  Computed by @total_ordering from (not a < b).'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='other'),
rc.NodeInputBP(label='NotImplemented'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._ge_from_lt(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_functools__gt_from_ge(rc.Node):
    title = '_gt_from_ge'
    description = '''Return a > b.  Computed by @total_ordering from (a >= b) and (a != b).'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='other'),
rc.NodeInputBP(label='NotImplemented'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._gt_from_ge(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_functools__gt_from_le(rc.Node):
    title = '_gt_from_le'
    description = '''Return a > b.  Computed by @total_ordering from (not a <= b).'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='other'),
rc.NodeInputBP(label='NotImplemented'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._gt_from_le(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_functools__gt_from_lt(rc.Node):
    title = '_gt_from_lt'
    description = '''Return a > b.  Computed by @total_ordering from (not a < b) and (a != b).'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='other'),
rc.NodeInputBP(label='NotImplemented'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._gt_from_lt(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_functools__le_from_ge(rc.Node):
    title = '_le_from_ge'
    description = '''Return a <= b.  Computed by @total_ordering from (not a >= b) or (a == b).'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='other'),
rc.NodeInputBP(label='NotImplemented'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._le_from_ge(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_functools__le_from_gt(rc.Node):
    title = '_le_from_gt'
    description = '''Return a <= b.  Computed by @total_ordering from (not a > b).'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='other'),
rc.NodeInputBP(label='NotImplemented'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._le_from_gt(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_functools__le_from_lt(rc.Node):
    title = '_le_from_lt'
    description = '''Return a <= b.  Computed by @total_ordering from (a < b) or (a == b).'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='other'),
rc.NodeInputBP(label='NotImplemented'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._le_from_lt(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_functools__lt_from_ge(rc.Node):
    title = '_lt_from_ge'
    description = '''Return a < b.  Computed by @total_ordering from (not a >= b).'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='other'),
rc.NodeInputBP(label='NotImplemented'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._lt_from_ge(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_functools__lt_from_gt(rc.Node):
    title = '_lt_from_gt'
    description = '''Return a < b.  Computed by @total_ordering from (not a > b) and (a != b).'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='other'),
rc.NodeInputBP(label='NotImplemented'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._lt_from_gt(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_functools__lt_from_le(rc.Node):
    title = '_lt_from_le'
    description = '''Return a < b.  Computed by @total_ordering from (a <= b) and (a != b).'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='other'),
rc.NodeInputBP(label='NotImplemented'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._lt_from_le(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_functools__make_key(rc.Node):
    title = '_make_key'
    description = '''Make a cache key from optionally typed positional and keyword arguments

    The key is constructed in a way that is flat as possible rather than
    as a nested structure that would take more memory.

    If there is only a single argument and its data type is known to cache
    its hash value, then that argument is returned without a wrapper.  This
    saves space and improves lookup speed.

    '''
    init_inputs = [
        rc.NodeInputBP(label='args'),
rc.NodeInputBP(label='kwds'),
rc.NodeInputBP(label='typed'),
rc.NodeInputBP(label='kwd_mark'),
rc.NodeInputBP(label='fasttypes'),
rc.NodeInputBP(label='tuple'),
rc.NodeInputBP(label='type'),
rc.NodeInputBP(label='len'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._make_key(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        


class AutoNode_functools__unwrap_partial(rc.Node):
    title = '_unwrap_partial'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools._unwrap_partial(self.input(0)))
        


class AutoNode_functools_get_cache_token(rc.Node):
    title = 'get_cache_token'
    description = '''Returns the current ABC cache token.

The token is an opaque object (supporting equality testing) identifying the
current version of the ABC cache for virtual subclasses. The token changes
with every call to register() on any ABC.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools.get_cache_token())
        


class AutoNode_functools_lru_cache(rc.Node):
    title = 'lru_cache'
    description = '''Least-recently-used cache decorator.

    If *maxsize* is set to None, the LRU features are disabled and the cache
    can grow without bound.

    If *typed* is True, arguments of different types will be cached separately.
    For example, f(3.0) and f(3) will be treated as distinct calls with
    distinct results.

    Arguments to the cached function must be hashable.

    View the cache statistics named tuple (hits, misses, maxsize, currsize)
    with f.cache_info().  Clear the cache and statistics with f.cache_clear().
    Access the underlying function with f.__wrapped__.

    See:  http://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)

    '''
    init_inputs = [
        rc.NodeInputBP(label='maxsize'),
rc.NodeInputBP(label='typed'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools.lru_cache(self.input(0), self.input(1)))
        


class AutoNode_functools_namedtuple(rc.Node):
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
        self.set_output_val(0, functools.namedtuple(self.input(0), self.input(1)))
        


class AutoNode_functools_recursive_repr(rc.Node):
    title = 'recursive_repr'
    description = '''Decorator to make a repr function return fillvalue for a recursive call'''
    init_inputs = [
        rc.NodeInputBP(label='fillvalue'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools.recursive_repr(self.input(0)))
        


class AutoNode_functools_singledispatch(rc.Node):
    title = 'singledispatch'
    description = '''Single-dispatch generic function decorator.

    Transforms a function into a generic function, which can have different
    behaviours depending upon the type of its first argument. The decorated
    function acts as the default implementation, and additional
    implementations can be registered using the register() attribute of the
    generic function.
    '''
    init_inputs = [
        rc.NodeInputBP(label='func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools.singledispatch(self.input(0)))
        


class AutoNode_functools_total_ordering(rc.Node):
    title = 'total_ordering'
    description = '''Class decorator that fills in missing ordering methods'''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools.total_ordering(self.input(0)))
        


class AutoNode_functools_update_wrapper(rc.Node):
    title = 'update_wrapper'
    description = '''Update a wrapper function to look like the wrapped function

       wrapper is the function to be updated
       wrapped is the original function
       assigned is a tuple naming the attributes assigned directly
       from the wrapped function to the wrapper function (defaults to
       functools.WRAPPER_ASSIGNMENTS)
       updated is a tuple naming the attributes of the wrapper that
       are updated with the corresponding attribute from the wrapped
       function (defaults to functools.WRAPPER_UPDATES)
    '''
    init_inputs = [
        rc.NodeInputBP(label='wrapper'),
rc.NodeInputBP(label='wrapped'),
rc.NodeInputBP(label='assigned'),
rc.NodeInputBP(label='updated'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools.update_wrapper(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_functools_wraps(rc.Node):
    title = 'wraps'
    description = '''Decorator factory to apply update_wrapper() to a wrapper function

       Returns a decorator that invokes update_wrapper() with the decorated
       function as the wrapper argument and the arguments to wraps() as the
       remaining arguments. Default arguments are as for update_wrapper().
       This is a convenience function to simplify applying partial() to
       update_wrapper().
    '''
    init_inputs = [
        rc.NodeInputBP(label='wrapped'),
rc.NodeInputBP(label='assigned'),
rc.NodeInputBP(label='updated'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, functools.wraps(self.input(0), self.input(1), self.input(2)))
        