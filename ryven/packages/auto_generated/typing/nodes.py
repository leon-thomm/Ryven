
from NENV import *

import typing


class NodeBase(Node):
    pass


class Namedtuple_Node(NodeBase):
    """
    Typed version of namedtuple.

    Usage in Python versions >= 3.6::

        class Employee(NamedTuple):
            name: str
            id: int

    This is equivalent to::

        Employee = collections.namedtuple('Employee', ['name', 'id'])

    The resulting class has an extra __annotations__ attribute, giving a
    dict that maps field names to types.  (The field names are also in
    the _fields attribute, which is part of the namedtuple API.)
    Alternative equivalent keyword syntax is also accepted::

        Employee = NamedTuple('Employee', name=str, id=int)

    In Python versions <= 3.5 use::

        Employee = NamedTuple('Employee', [('name', str), ('id', int)])
    """
    
    title = 'NamedTuple'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='typename'),
        NodeInputBP(label='fields', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing.NamedTuple(self.input(0), self.input(1)))
        

class Newtype_Node(NodeBase):
    """
    NewType creates simple unique types with almost zero
    runtime overhead. NewType(name, tp) is considered a subtype of tp
    by static type checkers. At runtime, NewType(name, tp) returns
    a dummy function that simply returns its argument. Usage::

        UserId = NewType('UserId', int)

        def name_by_id(user_id: UserId) -> str:
            ...

        UserId('user')          # Fails type check

        name_by_id(42)          # Fails type check
        name_by_id(UserId(42))  # OK

        num = UserId(5) + 1     # type: int
    """
    
    title = 'NewType'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='tp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing.NewType(self.input(0), self.input(1)))
        

class Typeddict_Node(NodeBase):
    """
    A simple typed namespace. At runtime it is equivalent to a plain dict.

    TypedDict creates a dictionary type that expects all of its
    instances to have a certain set of keys, where each key is
    associated with a value of a consistent type. This expectation
    is not checked at runtime but is only enforced by type checkers.
    Usage::

        class Point2D(TypedDict):
            x: int
            y: int
            label: str

        a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
        b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check

        assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')

    The type info can be accessed via the Point2D.__annotations__ dict, and
    the Point2D.__required_keys__ and Point2D.__optional_keys__ frozensets.
    TypedDict supports two additional equivalent forms::

        Point2D = TypedDict('Point2D', x=int, y=int, label=str)
        Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str})

    By default, all keys must be present in a TypedDict. It is possible
    to override this by specifying totality.
    Usage::

        class point2D(TypedDict, total=False):
            x: int
            y: int

    This means that a point2D TypedDict can have any of the keys omitted.A type
    checker is only expected to support a literal False or True as the value of
    the total argument. True is the default, and makes all items defined in the
    class body be required.

    The class syntax is only supported in Python 3.6+, while two other
    syntax forms work for Python 2.7 and 3.2+
    """
    
    title = 'TypedDict'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='typename'),
        NodeInputBP(label='fields', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing.TypedDict(self.input(0), self.input(1)))
        

class _Allow_Reckless_Class_Cheks_Node(NodeBase):
    """
    Allow instance and class checks for special stdlib modules.

    The abc and functools modules indiscriminately call isinstance() and
    issubclass() on the whole MRO of a user class, which may contain protocols.
    """
    
    title = '_allow_reckless_class_cheks'
    type_ = 'typing'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._allow_reckless_class_cheks())
        

class _Check_Generic_Node(NodeBase):
    """
    Check correct count for parameters of a generic cls (internal helper).
    This gives a nice error message in case of count mismatch.
    """
    
    title = '_check_generic'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='parameters'),
        NodeInputBP(label='elen'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._check_generic(self.input(0), self.input(1), self.input(2)))
        

class _Collect_Type_Vars_Node(NodeBase):
    """
    Collect all type variable contained in types in order of
    first appearance (lexicographic order). For example::

        _collect_type_vars((T, List[S, T])) == (T, S)
    """
    
    title = '_collect_type_vars'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='types'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._collect_type_vars(self.input(0)))
        

class _Deduplicate_Node(NodeBase):
    """
    """
    
    title = '_deduplicate'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='params'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._deduplicate(self.input(0)))
        

class _Eval_Type_Node(NodeBase):
    """
    Evaluate all forward references in the given type t.
    For use of globalns and localns see the docstring for get_type_hints().
    recursive_guard is used to prevent prevent infinite recursion
    with recursive ForwardRef.
    """
    
    title = '_eval_type'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='t'),
        NodeInputBP(label='globalns'),
        NodeInputBP(label='localns'),
        NodeInputBP(label='recursive_guard', dtype=dtypes.Data(default=frozenset(), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._eval_type(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Flatten_Literal_Params_Node(NodeBase):
    """
    An internal helper for Literal creation: flatten Literals among parameters"""
    
    title = '_flatten_literal_params'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='parameters'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._flatten_literal_params(self.input(0)))
        

class _Get_Defaults_Node(NodeBase):
    """
    Internal helper to extract the default arguments, by name."""
    
    title = '_get_defaults'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._get_defaults(self.input(0)))
        

class _Get_Protocol_Attrs_Node(NodeBase):
    """
    Collect protocol members from a protocol class objects.

    This includes names actually defined in the class dictionary, as well
    as names that appear in annotations. Special names (above) are skipped.
    """
    
    title = '_get_protocol_attrs'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._get_protocol_attrs(self.input(0)))
        

class _Is_Callable_Members_Only_Node(NodeBase):
    """
    """
    
    title = '_is_callable_members_only'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._is_callable_members_only(self.input(0)))
        

class _Is_Dunder_Node(NodeBase):
    """
    """
    
    title = '_is_dunder'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='attr'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._is_dunder(self.input(0)))
        

class _Make_Nmtuple_Node(NodeBase):
    """
    """
    
    title = '_make_nmtuple'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='types'),
        NodeInputBP(label='module'),
        NodeInputBP(label='defaults', dtype=dtypes.Data(default=(), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._make_nmtuple(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Namedtuple_Mro_Entries_Node(NodeBase):
    """
    """
    
    title = '_namedtuple_mro_entries'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='bases'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._namedtuple_mro_entries(self.input(0)))
        

class _No_Init_Node(NodeBase):
    """
    """
    
    title = '_no_init'
    type_ = 'typing'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._no_init())
        

class _Overload_Dummy_Node(NodeBase):
    """
    Helper for @overload to raise when called."""
    
    title = '_overload_dummy'
    type_ = 'typing'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._overload_dummy())
        

class _Remove_Dups_Flatten_Node(NodeBase):
    """
    An internal helper for Union creation and substitution: flatten Unions
    among parameters, then remove duplicates.
    """
    
    title = '_remove_dups_flatten'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='parameters'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._remove_dups_flatten(self.input(0)))
        

class _Strip_Annotations_Node(NodeBase):
    """
    Strips the annotations from a given type.
    """
    
    title = '_strip_annotations'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='t'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._strip_annotations(self.input(0)))
        

class _Tp_Cache_Node(NodeBase):
    """
    Internal wrapper caching __getitem__ of generic types with a fallback to
    original function for non-hashable arguments.
    """
    
    title = '_tp_cache'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='func', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._tp_cache(self.input(0)))
        

class _Type_Check_Node(NodeBase):
    """
    Check that the argument is a type, and return it (internal helper).

    As a special case, accept None and return type(None) instead. Also wrap strings
    into ForwardRef instances. Consider several corner cases, for example plain
    special forms like Union are not valid, while Union[int, str] is OK, etc.
    The msg argument is a human-readable error message, e.g::

        "Union[arg, ...]: arg should be a type."

    We append the repr() of the actual value (truncated to 100 chars).
    """
    
    title = '_type_check'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='arg'),
        NodeInputBP(label='msg'),
        NodeInputBP(label='is_argument', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._type_check(self.input(0), self.input(1), self.input(2)))
        

class _Type_Convert_Node(NodeBase):
    """
    For converting None to type(None), and strings to ForwardRef."""
    
    title = '_type_convert'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='arg'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._type_convert(self.input(0)))
        

class _Type_Repr_Node(NodeBase):
    """
    Return the repr() of an object, special-casing types (internal helper).

    If obj is a type, we return a shorter version than the default
    type.__repr__, based on the module and qualified name, which is
    typically enough to uniquely identify a type.  For everything
    else, we fall back on repr(obj).
    """
    
    title = '_type_repr'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._type_repr(self.input(0)))
        

class _Value_And_Type_Iter_Node(NodeBase):
    """
    """
    
    title = '_value_and_type_iter'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='parameters'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing._value_and_type_iter(self.input(0)))
        

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
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='funcobj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing.abstractmethod(self.input(0)))
        

class Cast_Node(NodeBase):
    """
    Cast a value to a type.

    This returns the value unchanged.  To the type checker this
    signals that the return value has the designated type, but at
    runtime we intentionally don't check anything (we want this
    to be as fast as possible).
    """
    
    title = 'cast'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='typ'),
        NodeInputBP(label='val'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing.cast(self.input(0), self.input(1)))
        

class Final_Node(NodeBase):
    """
    A decorator to indicate final methods and final classes.

    Use this decorator to indicate to type checkers that the decorated
    method cannot be overridden, and decorated class cannot be subclassed.
    For example:

      class Base:
          @final
          def done(self) -> None:
              ...
      class Sub(Base):
          def done(self) -> None:  # Error reported by type checker
                ...

      @final
      class Leaf:
          ...
      class Other(Leaf):  # Error reported by type checker
          ...

    There is no runtime checking of these properties.
    """
    
    title = 'final'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing.final(self.input(0)))
        

class Get_Args_Node(NodeBase):
    """
    Get type arguments with all substitutions performed.

    For unions, basic simplifications used by Union constructor are performed.
    Examples::
        get_args(Dict[str, int]) == (str, int)
        get_args(int) == ()
        get_args(Union[int, Union[T, int], str][int]) == (int, str)
        get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
        get_args(Callable[[], T][int]) == ([], int)
    """
    
    title = 'get_args'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='tp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing.get_args(self.input(0)))
        

class Get_Origin_Node(NodeBase):
    """
    Get the unsubscripted version of a type.

    This supports generic types, Callable, Tuple, Union, Literal, Final, ClassVar
    and Annotated. Return None for unsupported types. Examples::

        get_origin(Literal[42]) is Literal
        get_origin(int) is None
        get_origin(ClassVar[int]) is ClassVar
        get_origin(Generic) is Generic
        get_origin(Generic[T]) is Generic
        get_origin(Union[T, int]) is Union
        get_origin(List[Tuple[T, T]][int]) == list
    """
    
    title = 'get_origin'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='tp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing.get_origin(self.input(0)))
        

class Get_Type_Hints_Node(NodeBase):
    """
    Return type hints for an object.

    This is often the same as obj.__annotations__, but it handles
    forward references encoded as string literals, adds Optional[t] if a
    default value equal to None is set and recursively replaces all
    'Annotated[T, ...]' with 'T' (unless 'include_extras=True').

    The argument may be a module, class, method, or function. The annotations
    are returned as a dictionary. For classes, annotations include also
    inherited members.

    TypeError is raised if the argument is not of a type that can contain
    annotations, and an empty dictionary is returned if no annotations are
    present.

    BEWARE -- the behavior of globalns and localns is counterintuitive
    (unless you are familiar with how eval() and exec() work).  The
    search order is locals first, then globals.

    - If no dict arguments are passed, an attempt is made to use the
      globals from obj (or the respective module's globals for classes),
      and these are also used as the locals.  If the object does not appear
      to have globals, an empty dictionary is used.

    - If one dict argument is passed, it is used for both globals and
      locals.

    - If two dict arguments are passed, they specify globals and
      locals, respectively.
    """
    
    title = 'get_type_hints'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='globalns', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='localns', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='include_extras', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing.get_type_hints(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class No_Type_Check_Node(NodeBase):
    """
    Decorator to indicate that annotations are not type hints.

    The argument must be a class or function; if it is a class, it
    applies recursively to all methods and classes defined in that class
    (but not to methods defined in its superclasses or subclasses).

    This mutates the function(s) or class(es) in place.
    """
    
    title = 'no_type_check'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='arg'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing.no_type_check(self.input(0)))
        

class No_Type_Check_Decorator_Node(NodeBase):
    """
    Decorator to give another decorator the @no_type_check effect.

    This wraps the decorator with something that wraps the decorated
    function in @no_type_check.
    """
    
    title = 'no_type_check_decorator'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='decorator'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing.no_type_check_decorator(self.input(0)))
        

class Overload_Node(NodeBase):
    """
    Decorator for overloaded functions/methods.

    In a stub file, place two or more stub definitions for the same
    function in a row, each decorated with @overload.  For example:

      @overload
      def utf8(value: None) -> None: ...
      @overload
      def utf8(value: bytes) -> bytes: ...
      @overload
      def utf8(value: str) -> bytes: ...

    In a non-stub file (i.e. a regular .py file), do the same but
    follow it with an implementation.  The implementation should *not*
    be decorated with @overload.  For example:

      @overload
      def utf8(value: None) -> None: ...
      @overload
      def utf8(value: bytes) -> bytes: ...
      @overload
      def utf8(value: str) -> bytes: ...
      def utf8(value):
          # implementation goes here
    """
    
    title = 'overload'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing.overload(self.input(0)))
        

class Runtime_Checkable_Node(NodeBase):
    """
    Mark a protocol class as a runtime protocol.

    Such protocol can be used with isinstance() and issubclass().
    Raise TypeError if applied to a non-protocol class.
    This allows a simple-minded structural check very similar to
    one trick ponies in collections.abc such as Iterable.
    For example::

        @runtime_checkable
        class Closable(Protocol):
            def close(self): ...

        assert isinstance(open('/some/file'), Closable)

    Warning: this will check only the presence of the required methods,
    not their type signatures!
    """
    
    title = 'runtime_checkable'
    type_ = 'typing'
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, typing.runtime_checkable(self.input(0)))
        


export_nodes(
    Namedtuple_Node,
    Newtype_Node,
    Typeddict_Node,
    _Allow_Reckless_Class_Cheks_Node,
    _Check_Generic_Node,
    _Collect_Type_Vars_Node,
    _Deduplicate_Node,
    _Eval_Type_Node,
    _Flatten_Literal_Params_Node,
    _Get_Defaults_Node,
    _Get_Protocol_Attrs_Node,
    _Is_Callable_Members_Only_Node,
    _Is_Dunder_Node,
    _Make_Nmtuple_Node,
    _Namedtuple_Mro_Entries_Node,
    _No_Init_Node,
    _Overload_Dummy_Node,
    _Remove_Dups_Flatten_Node,
    _Strip_Annotations_Node,
    _Tp_Cache_Node,
    _Type_Check_Node,
    _Type_Convert_Node,
    _Type_Repr_Node,
    _Value_And_Type_Iter_Node,
    Abstractmethod_Node,
    Cast_Node,
    Final_Node,
    Get_Args_Node,
    Get_Origin_Node,
    Get_Type_Hints_Node,
    No_Type_Check_Node,
    No_Type_Check_Decorator_Node,
    Overload_Node,
    Runtime_Checkable_Node,
)
