
from ryven.NENV import *

import functools


class NodeBase(Node):
    pass


class _C3_Merge_Node(NodeBase):
    """
    Merges MROs in *sequences* to a single MRO using the C3 algorithm.

    Adapted from http://www.python.org/download/releases/2.3/mro/.

    """
    
    title = '_c3_merge'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='sequences'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._c3_merge(self.input(0)))
        

class _C3_Mro_Node(NodeBase):
    """
    Computes the method resolution order using extended C3 linearization.

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

    """
    
    title = '_c3_mro'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='abcs', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._c3_mro(self.input(0), self.input(1)))
        

class _Compose_Mro_Node(NodeBase):
    """
    Calculates the method resolution order for a given class *cls*.

    Includes relevant abstract base classes (with their respective bases) from
    the *types* iterable. Uses a modified C3 linearization algorithm.

    """
    
    title = '_compose_mro'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='types'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._compose_mro(self.input(0), self.input(1)))
        

class _Find_Impl_Node(NodeBase):
    """
    Returns the best matching implementation from *registry* for type *cls*.

    Where there is no registered implementation for a specific type, its method
    resolution order is used to find a more generic implementation.

    Note: if *registry* does not contain an implementation for the base
    *object* type, this function may return None.

    """
    
    title = '_find_impl'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='registry'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._find_impl(self.input(0), self.input(1)))
        

class _Ge_From_Gt_Node(NodeBase):
    """
    Return a >= b.  Computed by @total_ordering from (a > b) or (a == b)."""
    
    title = '_ge_from_gt'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='NotImplemented', dtype=dtypes.Data(default=NotImplemented, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._ge_from_gt(self.input(0), self.input(1)))
        

class _Ge_From_Le_Node(NodeBase):
    """
    Return a >= b.  Computed by @total_ordering from (not a <= b) or (a == b)."""
    
    title = '_ge_from_le'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='NotImplemented', dtype=dtypes.Data(default=NotImplemented, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._ge_from_le(self.input(0), self.input(1)))
        

class _Ge_From_Lt_Node(NodeBase):
    """
    Return a >= b.  Computed by @total_ordering from (not a < b)."""
    
    title = '_ge_from_lt'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='NotImplemented', dtype=dtypes.Data(default=NotImplemented, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._ge_from_lt(self.input(0), self.input(1)))
        

class _Gt_From_Ge_Node(NodeBase):
    """
    Return a > b.  Computed by @total_ordering from (a >= b) and (a != b)."""
    
    title = '_gt_from_ge'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='NotImplemented', dtype=dtypes.Data(default=NotImplemented, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._gt_from_ge(self.input(0), self.input(1)))
        

class _Gt_From_Le_Node(NodeBase):
    """
    Return a > b.  Computed by @total_ordering from (not a <= b)."""
    
    title = '_gt_from_le'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='NotImplemented', dtype=dtypes.Data(default=NotImplemented, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._gt_from_le(self.input(0), self.input(1)))
        

class _Gt_From_Lt_Node(NodeBase):
    """
    Return a > b.  Computed by @total_ordering from (not a < b) and (a != b)."""
    
    title = '_gt_from_lt'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='NotImplemented', dtype=dtypes.Data(default=NotImplemented, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._gt_from_lt(self.input(0), self.input(1)))
        

class _Le_From_Ge_Node(NodeBase):
    """
    Return a <= b.  Computed by @total_ordering from (not a >= b) or (a == b)."""
    
    title = '_le_from_ge'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='NotImplemented', dtype=dtypes.Data(default=NotImplemented, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._le_from_ge(self.input(0), self.input(1)))
        

class _Le_From_Gt_Node(NodeBase):
    """
    Return a <= b.  Computed by @total_ordering from (not a > b)."""
    
    title = '_le_from_gt'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='NotImplemented', dtype=dtypes.Data(default=NotImplemented, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._le_from_gt(self.input(0), self.input(1)))
        

class _Le_From_Lt_Node(NodeBase):
    """
    Return a <= b.  Computed by @total_ordering from (a < b) or (a == b)."""
    
    title = '_le_from_lt'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='NotImplemented', dtype=dtypes.Data(default=NotImplemented, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._le_from_lt(self.input(0), self.input(1)))
        

class _Lt_From_Ge_Node(NodeBase):
    """
    Return a < b.  Computed by @total_ordering from (not a >= b)."""
    
    title = '_lt_from_ge'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='NotImplemented', dtype=dtypes.Data(default=NotImplemented, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._lt_from_ge(self.input(0), self.input(1)))
        

class _Lt_From_Gt_Node(NodeBase):
    """
    Return a < b.  Computed by @total_ordering from (not a > b) and (a != b)."""
    
    title = '_lt_from_gt'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='NotImplemented', dtype=dtypes.Data(default=NotImplemented, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._lt_from_gt(self.input(0), self.input(1)))
        

class _Lt_From_Le_Node(NodeBase):
    """
    Return a < b.  Computed by @total_ordering from (a <= b) and (a != b)."""
    
    title = '_lt_from_le'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='NotImplemented', dtype=dtypes.Data(default=NotImplemented, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._lt_from_le(self.input(0), self.input(1)))
        

class _Make_Key_Node(NodeBase):
    """
    Make a cache key from optionally typed positional and keyword arguments

    The key is constructed in a way that is flat as possible rather than
    as a nested structure that would take more memory.

    If there is only a single argument and its data type is known to cache
    its hash value, then that argument is returned without a wrapper.  This
    saves space and improves lookup speed.

    """
    
    title = '_make_key'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='args'),
        NodeInputBP(label='kwds'),
        NodeInputBP(label='typed'),
        NodeInputBP(label='kwd_mark', dtype=dtypes.Data(default=(<object object at 0x000001B83FB382A0>,), size='s')),
        NodeInputBP(label='fasttypes', dtype=dtypes.Data(default={<class 'str'>, <class 'int'>}, size='s')),
        NodeInputBP(label='tuple', dtype=dtypes.Data(default=tuple, size='s')),
        NodeInputBP(label='type', dtype=dtypes.Data(default=type, size='s')),
        NodeInputBP(label='len', dtype=dtypes.Data(default=<built-in function len>, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._make_key(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        

class _Unwrap_Partial_Node(NodeBase):
    """
    """
    
    title = '_unwrap_partial'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools._unwrap_partial(self.input(0)))
        

class Cache_Node(NodeBase):
    """
    Simple lightweight unbounded cache.  Sometimes called "memoize"."""
    
    title = 'cache'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='user_function'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools.cache(self.input(0)))
        

class Get_Cache_Token_Node(NodeBase):
    """
    Returns the current ABC cache token.

The token is an opaque object (supporting equality testing) identifying the
current version of the ABC cache for virtual subclasses. The token changes
with every call to register() on any ABC."""
    
    title = 'get_cache_token'
    type_ = 'functools'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools.get_cache_token())
        

class Lru_Cache_Node(NodeBase):
    """
    Least-recently-used cache decorator.

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

    """
    
    title = 'lru_cache'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='maxsize', dtype=dtypes.Data(default=128, size='s')),
        NodeInputBP(label='typed', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools.lru_cache(self.input(0), self.input(1)))
        

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
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='typename'),
        NodeInputBP(label='field_names'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools.namedtuple(self.input(0), self.input(1)))
        

class Recursive_Repr_Node(NodeBase):
    """
    Decorator to make a repr function return fillvalue for a recursive call"""
    
    title = 'recursive_repr'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='fillvalue', dtype=dtypes.Data(default='...', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools.recursive_repr(self.input(0)))
        

class Singledispatch_Node(NodeBase):
    """
    Single-dispatch generic function decorator.

    Transforms a function into a generic function, which can have different
    behaviours depending upon the type of its first argument. The decorated
    function acts as the default implementation, and additional
    implementations can be registered using the register() attribute of the
    generic function.
    """
    
    title = 'singledispatch'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools.singledispatch(self.input(0)))
        

class Total_Ordering_Node(NodeBase):
    """
    Class decorator that fills in missing ordering methods"""
    
    title = 'total_ordering'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools.total_ordering(self.input(0)))
        

class Update_Wrapper_Node(NodeBase):
    """
    Update a wrapper function to look like the wrapped function

       wrapper is the function to be updated
       wrapped is the original function
       assigned is a tuple naming the attributes assigned directly
       from the wrapped function to the wrapper function (defaults to
       functools.WRAPPER_ASSIGNMENTS)
       updated is a tuple naming the attributes of the wrapper that
       are updated with the corresponding attribute from the wrapped
       function (defaults to functools.WRAPPER_UPDATES)
    """
    
    title = 'update_wrapper'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='wrapper'),
        NodeInputBP(label='wrapped'),
        NodeInputBP(label='assigned', dtype=dtypes.Data(default=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), size='s')),
        NodeInputBP(label='updated', dtype=dtypes.Data(default=('__dict__',), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools.update_wrapper(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Wraps_Node(NodeBase):
    """
    Decorator factory to apply update_wrapper() to a wrapper function

       Returns a decorator that invokes update_wrapper() with the decorated
       function as the wrapper argument and the arguments to wraps() as the
       remaining arguments. Default arguments are as for update_wrapper().
       This is a convenience function to simplify applying partial() to
       update_wrapper().
    """
    
    title = 'wraps'
    type_ = 'functools'
    init_inputs = [
        NodeInputBP(label='wrapped'),
        NodeInputBP(label='assigned', dtype=dtypes.Data(default=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), size='s')),
        NodeInputBP(label='updated', dtype=dtypes.Data(default=('__dict__',), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, functools.wraps(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _C3_Merge_Node,
    _C3_Mro_Node,
    _Compose_Mro_Node,
    _Find_Impl_Node,
    _Ge_From_Gt_Node,
    _Ge_From_Le_Node,
    _Ge_From_Lt_Node,
    _Gt_From_Ge_Node,
    _Gt_From_Le_Node,
    _Gt_From_Lt_Node,
    _Le_From_Ge_Node,
    _Le_From_Gt_Node,
    _Le_From_Lt_Node,
    _Lt_From_Ge_Node,
    _Lt_From_Gt_Node,
    _Lt_From_Le_Node,
    _Make_Key_Node,
    _Unwrap_Partial_Node,
    Cache_Node,
    Get_Cache_Token_Node,
    Lru_Cache_Node,
    Namedtuple_Node,
    Recursive_Repr_Node,
    Singledispatch_Node,
    Total_Ordering_Node,
    Update_Wrapper_Node,
    Wraps_Node,
)
