
from NENV import *

import typing


class NodeBase(Node):
    pass


class Newtype_Node(NodeBase):
    title = 'NewType'
    type_ = 'typing'
    doc = """NewType creates simple unique types with almost zero
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
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='tp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing.NewType(self.input(0), self.input(1)))
        

class _Alias_Node(NodeBase):
    title = '_alias'
    type_ = 'typing'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='origin'),
        NodeInputBP(label='params'),
        NodeInputBP(label='inst', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._alias(self.input(0), self.input(1), self.input(2)))
        

class _Allow_Reckless_Class_Cheks_Node(NodeBase):
    title = '_allow_reckless_class_cheks'
    type_ = 'typing'
    doc = """Allow instnance and class checks for special stdlib modules.

    The abc and functools modules indiscriminately call isinstance() and
    issubclass() on the whole MRO of a user class, which may contain protocols.
    """
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._allow_reckless_class_cheks())
        

class _Check_Fails_Node(NodeBase):
    title = '_check_fails'
    type_ = 'typing'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='other'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._check_fails(self.input(0), self.input(1)))
        

class _Check_Generic_Node(NodeBase):
    title = '_check_generic'
    type_ = 'typing'
    doc = """Check correct count for parameters of a generic cls (internal helper).
    This gives a nice error message in case of count mismatch.
    """
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='parameters'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._check_generic(self.input(0), self.input(1)))
        

class _Collect_Type_Vars_Node(NodeBase):
    title = '_collect_type_vars'
    type_ = 'typing'
    doc = """Collect all type variable contained in types in order of
    first appearance (lexicographic order). For example::

        _collect_type_vars((T, List[S, T])) == (T, S)
    """
    init_inputs = [
        NodeInputBP(label='types'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._collect_type_vars(self.input(0)))
        

class _Dict_New_Node(NodeBase):
    title = '_dict_new'
    type_ = 'typing'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._dict_new(self.input(0)))
        

class _Eval_Type_Node(NodeBase):
    title = '_eval_type'
    type_ = 'typing'
    doc = """Evaluate all forward references in the given type t.
    For use of globalns and localns see the docstring for get_type_hints().
    """
    init_inputs = [
        NodeInputBP(label='t'),
        NodeInputBP(label='globalns'),
        NodeInputBP(label='localns'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._eval_type(self.input(0), self.input(1), self.input(2)))
        

class _Get_Defaults_Node(NodeBase):
    title = '_get_defaults'
    type_ = 'typing'
    doc = """Internal helper to extract the default arguments, by name."""
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._get_defaults(self.input(0)))
        

class _Get_Protocol_Attrs_Node(NodeBase):
    title = '_get_protocol_attrs'
    type_ = 'typing'
    doc = """Collect protocol members from a protocol class objects.

    This includes names actually defined in the class dictionary, as well
    as names that appear in annotations. Special names (above) are skipped.
    """
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._get_protocol_attrs(self.input(0)))
        

class _Is_Callable_Members_Only_Node(NodeBase):
    title = '_is_callable_members_only'
    type_ = 'typing'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._is_callable_members_only(self.input(0)))
        

class _Is_Dunder_Node(NodeBase):
    title = '_is_dunder'
    type_ = 'typing'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='attr'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._is_dunder(self.input(0)))
        

class _Make_Nmtuple_Node(NodeBase):
    title = '_make_nmtuple'
    type_ = 'typing'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='types'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._make_nmtuple(self.input(0), self.input(1)))
        

class _No_Init_Node(NodeBase):
    title = '_no_init'
    type_ = 'typing'
    doc = """"""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._no_init())
        

class _Overload_Dummy_Node(NodeBase):
    title = '_overload_dummy'
    type_ = 'typing'
    doc = """Helper for @overload to raise when called."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._overload_dummy())
        

class _Remove_Dups_Flatten_Node(NodeBase):
    title = '_remove_dups_flatten'
    type_ = 'typing'
    doc = """An internal helper for Union creation and substitution: flatten Unions
    among parameters, then remove duplicates.
    """
    init_inputs = [
        NodeInputBP(label='parameters'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._remove_dups_flatten(self.input(0)))
        

class _Subs_Tvars_Node(NodeBase):
    title = '_subs_tvars'
    type_ = 'typing'
    doc = """Substitute type variables 'tvars' with substitutions 'subs'.
    These two must have the same length.
    """
    init_inputs = [
        NodeInputBP(label='tp'),
        NodeInputBP(label='tvars'),
        NodeInputBP(label='subs'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._subs_tvars(self.input(0), self.input(1), self.input(2)))
        

class _Tp_Cache_Node(NodeBase):
    title = '_tp_cache'
    type_ = 'typing'
    doc = """Internal wrapper caching __getitem__ of generic types with a fallback to
    original function for non-hashable arguments.
    """
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._tp_cache(self.input(0)))
        

class _Type_Check_Node(NodeBase):
    title = '_type_check'
    type_ = 'typing'
    doc = """Check that the argument is a type, and return it (internal helper).

    As a special case, accept None and return type(None) instead. Also wrap strings
    into ForwardRef instances. Consider several corner cases, for example plain
    special forms like Union are not valid, while Union[int, str] is OK, etc.
    The msg argument is a human-readable error message, e.g::

        "Union[arg, ...]: arg should be a type."

    We append the repr() of the actual value (truncated to 100 chars).
    """
    init_inputs = [
        NodeInputBP(label='arg'),
        NodeInputBP(label='msg'),
        NodeInputBP(label='is_argument', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._type_check(self.input(0), self.input(1), self.input(2)))
        

class _Type_Repr_Node(NodeBase):
    title = '_type_repr'
    type_ = 'typing'
    doc = """Return the repr() of an object, special-casing types (internal helper).

    If obj is a type, we return a shorter version than the default
    type.__repr__, based on the module and qualified name, which is
    typically enough to uniquely identify a type.  For everything
    else, we fall back on repr(obj).
    """
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._type_repr(self.input(0)))
        

class _Typeddict_New_Node(NodeBase):
    title = '_typeddict_new'
    type_ = 'typing'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='typename'),
        NodeInputBP(label='fields', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing._typeddict_new(self.input(0), self.input(1), self.input(2)))
        

class Abstractmethod_Node(NodeBase):
    title = 'abstractmethod'
    type_ = 'typing'
    doc = """A decorator indicating abstract methods.

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
    init_inputs = [
        NodeInputBP(label='funcobj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing.abstractmethod(self.input(0)))
        

class Cast_Node(NodeBase):
    title = 'cast'
    type_ = 'typing'
    doc = """Cast a value to a type.

    This returns the value unchanged.  To the type checker this
    signals that the return value has the designated type, but at
    runtime we intentionally don't check anything (we want this
    to be as fast as possible).
    """
    init_inputs = [
        NodeInputBP(label='typ'),
        NodeInputBP(label='val'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing.cast(self.input(0), self.input(1)))
        

class Final_Node(NodeBase):
    title = 'final'
    type_ = 'typing'
    doc = """A decorator to indicate final methods and final classes.

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
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing.final(self.input(0)))
        

class Get_Args_Node(NodeBase):
    title = 'get_args'
    type_ = 'typing'
    doc = """Get type arguments with all substitutions performed.

    For unions, basic simplifications used by Union constructor are performed.
    Examples::
        get_args(Dict[str, int]) == (str, int)
        get_args(int) == ()
        get_args(Union[int, Union[T, int], str][int]) == (int, str)
        get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
        get_args(Callable[[], T][int]) == ([], int)
    """
    init_inputs = [
        NodeInputBP(label='tp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing.get_args(self.input(0)))
        

class Get_Origin_Node(NodeBase):
    title = 'get_origin'
    type_ = 'typing'
    doc = """Get the unsubscripted version of a type.

    This supports generic types, Callable, Tuple, Union, Literal, Final and ClassVar.
    Return None for unsupported types. Examples::

        get_origin(Literal[42]) is Literal
        get_origin(int) is None
        get_origin(ClassVar[int]) is ClassVar
        get_origin(Generic) is Generic
        get_origin(Generic[T]) is Generic
        get_origin(Union[T, int]) is Union
        get_origin(List[Tuple[T, T]][int]) == list
    """
    init_inputs = [
        NodeInputBP(label='tp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing.get_origin(self.input(0)))
        

class Get_Type_Hints_Node(NodeBase):
    title = 'get_type_hints'
    type_ = 'typing'
    doc = """Return type hints for an object.

    This is often the same as obj.__annotations__, but it handles
    forward references encoded as string literals, and if necessary
    adds Optional[t] if a default value equal to None is set.

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
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='globalns', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='localns', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing.get_type_hints(self.input(0), self.input(1), self.input(2)))
        

class No_Type_Check_Node(NodeBase):
    title = 'no_type_check'
    type_ = 'typing'
    doc = """Decorator to indicate that annotations are not type hints.

    The argument must be a class or function; if it is a class, it
    applies recursively to all methods and classes defined in that class
    (but not to methods defined in its superclasses or subclasses).

    This mutates the function(s) or class(es) in place.
    """
    init_inputs = [
        NodeInputBP(label='arg'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing.no_type_check(self.input(0)))
        

class No_Type_Check_Decorator_Node(NodeBase):
    title = 'no_type_check_decorator'
    type_ = 'typing'
    doc = """Decorator to give another decorator the @no_type_check effect.

    This wraps the decorator with something that wraps the decorated
    function in @no_type_check.
    """
    init_inputs = [
        NodeInputBP(label='decorator'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing.no_type_check_decorator(self.input(0)))
        

class Overload_Node(NodeBase):
    title = 'overload'
    type_ = 'typing'
    doc = """Decorator for overloaded functions/methods.

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
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing.overload(self.input(0)))
        

class Runtime_Checkable_Node(NodeBase):
    title = 'runtime_checkable'
    type_ = 'typing'
    doc = """Mark a protocol class as a runtime protocol.

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
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, typing.runtime_checkable(self.input(0)))
        


export_nodes(
    Newtype_Node,
    _Alias_Node,
    _Allow_Reckless_Class_Cheks_Node,
    _Check_Fails_Node,
    _Check_Generic_Node,
    _Collect_Type_Vars_Node,
    _Dict_New_Node,
    _Eval_Type_Node,
    _Get_Defaults_Node,
    _Get_Protocol_Attrs_Node,
    _Is_Callable_Members_Only_Node,
    _Is_Dunder_Node,
    _Make_Nmtuple_Node,
    _No_Init_Node,
    _Overload_Dummy_Node,
    _Remove_Dups_Flatten_Node,
    _Subs_Tvars_Node,
    _Tp_Cache_Node,
    _Type_Check_Node,
    _Type_Repr_Node,
    _Typeddict_New_Node,
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
