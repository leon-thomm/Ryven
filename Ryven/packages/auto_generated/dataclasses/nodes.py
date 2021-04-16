import ryvencore_qt as rc
import dataclasses


class AutoNode_dataclasses__asdict_inner(rc.Node):
    title = '_asdict_inner'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
rc.NodeInputBP(label='dict_factory'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._asdict_inner(self.input(0), self.input(1)))
        


class AutoNode_dataclasses__astuple_inner(rc.Node):
    title = '_astuple_inner'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
rc.NodeInputBP(label='tuple_factory'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._astuple_inner(self.input(0), self.input(1)))
        


class AutoNode_dataclasses__cmp_fn(rc.Node):
    title = '_cmp_fn'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='op'),
rc.NodeInputBP(label='self_tuple'),
rc.NodeInputBP(label='other_tuple'),
rc.NodeInputBP(label='globals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._cmp_fn(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_dataclasses__create_fn(rc.Node):
    title = '_create_fn'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='args'),
rc.NodeInputBP(label='body'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._create_fn(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_dataclasses__field_assign(rc.Node):
    title = '_field_assign'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='frozen'),
rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='value'),
rc.NodeInputBP(label='self_name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._field_assign(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_dataclasses__field_init(rc.Node):
    title = '_field_init'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
rc.NodeInputBP(label='frozen'),
rc.NodeInputBP(label='globals'),
rc.NodeInputBP(label='self_name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._field_init(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_dataclasses__frozen_get_del_attr(rc.Node):
    title = '_frozen_get_del_attr'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='fields'),
rc.NodeInputBP(label='globals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._frozen_get_del_attr(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_dataclasses__get_field(rc.Node):
    title = '_get_field'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='a_name'),
rc.NodeInputBP(label='a_type'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._get_field(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_dataclasses__hash_add(rc.Node):
    title = '_hash_add'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='fields'),
rc.NodeInputBP(label='globals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._hash_add(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_dataclasses__hash_exception(rc.Node):
    title = '_hash_exception'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='fields'),
rc.NodeInputBP(label='globals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._hash_exception(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_dataclasses__hash_fn(rc.Node):
    title = '_hash_fn'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='fields'),
rc.NodeInputBP(label='globals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._hash_fn(self.input(0), self.input(1)))
        


class AutoNode_dataclasses__hash_set_none(rc.Node):
    title = '_hash_set_none'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='fields'),
rc.NodeInputBP(label='globals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._hash_set_none(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_dataclasses__init_fn(rc.Node):
    title = '_init_fn'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='fields'),
rc.NodeInputBP(label='frozen'),
rc.NodeInputBP(label='has_post_init'),
rc.NodeInputBP(label='self_name'),
rc.NodeInputBP(label='globals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._init_fn(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_dataclasses__init_param(rc.Node):
    title = '_init_param'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._init_param(self.input(0)))
        


class AutoNode_dataclasses__is_classvar(rc.Node):
    title = '_is_classvar'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='a_type'),
rc.NodeInputBP(label='typing'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._is_classvar(self.input(0), self.input(1)))
        


class AutoNode_dataclasses__is_dataclass_instance(rc.Node):
    title = '_is_dataclass_instance'
    doc = '''Returns True if obj is an instance of a dataclass.'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._is_dataclass_instance(self.input(0)))
        


class AutoNode_dataclasses__is_initvar(rc.Node):
    title = '_is_initvar'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='a_type'),
rc.NodeInputBP(label='dataclasses'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._is_initvar(self.input(0), self.input(1)))
        


class AutoNode_dataclasses__is_type(rc.Node):
    title = '_is_type'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='annotation'),
rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='a_module'),
rc.NodeInputBP(label='a_type'),
rc.NodeInputBP(label='is_type_predicate'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._is_type(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_dataclasses__process_class(rc.Node):
    title = '_process_class'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='init'),
rc.NodeInputBP(label='repr'),
rc.NodeInputBP(label='eq'),
rc.NodeInputBP(label='order'),
rc.NodeInputBP(label='unsafe_hash'),
rc.NodeInputBP(label='frozen'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._process_class(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        


class AutoNode_dataclasses__recursive_repr(rc.Node):
    title = '_recursive_repr'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='user_function'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._recursive_repr(self.input(0)))
        


class AutoNode_dataclasses__repr_fn(rc.Node):
    title = '_repr_fn'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='fields'),
rc.NodeInputBP(label='globals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._repr_fn(self.input(0), self.input(1)))
        


class AutoNode_dataclasses__set_new_attribute(rc.Node):
    title = '_set_new_attribute'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._set_new_attribute(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_dataclasses__tuple_str(rc.Node):
    title = '_tuple_str'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='obj_name'),
rc.NodeInputBP(label='fields'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses._tuple_str(self.input(0), self.input(1)))
        


class AutoNode_dataclasses_asdict(rc.Node):
    title = 'asdict'
    doc = '''Return the fields of a dataclass instance as a new dictionary mapping
    field names to field values.

    Example usage:

      @dataclass
      class C:
          x: int
          y: int

      c = C(1, 2)
      assert asdict(c) == {'x': 1, 'y': 2}

    If given, 'dict_factory' will be used instead of built-in dict.
    The function applies recursively to field values that are
    dataclass instances. This will also look into built-in containers:
    tuples, lists, and dicts.
    '''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses.asdict(self.input(0)))
        


class AutoNode_dataclasses_astuple(rc.Node):
    title = 'astuple'
    doc = '''Return the fields of a dataclass instance as a new tuple of field values.

    Example usage::

      @dataclass
      class C:
          x: int
          y: int

    c = C(1, 2)
    assert astuple(c) == (1, 2)

    If given, 'tuple_factory' will be used instead of built-in tuple.
    The function applies recursively to field values that are
    dataclass instances. This will also look into built-in containers:
    tuples, lists, and dicts.
    '''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses.astuple(self.input(0)))
        


class AutoNode_dataclasses_dataclass(rc.Node):
    title = 'dataclass'
    doc = '''Returns the same class as was passed in, with dunder methods
    added based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If
    repr is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method function is added. If frozen is true, fields may
    not be assigned to after instance creation.
    '''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses.dataclass(self.input(0)))
        


class AutoNode_dataclasses_field(rc.Node):
    title = 'field'
    doc = '''Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is True, the field will be a parameter to the class's __init__()
    function.  If repr is True, the field will be included in the
    object's repr().  If hash is True, the field will be included in
    the object's hash().  If compare is True, the field will be used
    in comparison functions.  metadata, if specified, must be a
    mapping which is stored but not otherwise examined by dataclass.

    It is an error to specify both default and default_factory.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses.field())
        


class AutoNode_dataclasses_fields(rc.Node):
    title = 'fields'
    doc = '''Return a tuple describing the fields of this dataclass.

    Accepts a dataclass or an instance of one. Tuple elements are of
    type Field.
    '''
    init_inputs = [
        rc.NodeInputBP(label='class_or_instance'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses.fields(self.input(0)))
        


class AutoNode_dataclasses_is_dataclass(rc.Node):
    title = 'is_dataclass'
    doc = '''Returns True if obj is a dataclass or an instance of a
    dataclass.'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses.is_dataclass(self.input(0)))
        


class AutoNode_dataclasses_make_dataclass(rc.Node):
    title = 'make_dataclass'
    doc = '''Return a new dynamically created dataclass.

    The dataclass name will be 'cls_name'.  'fields' is an iterable
    of either (name), (name, type) or (name, type, Field) objects. If type is
    omitted, use the string 'typing.Any'.  Field objects are created by
    the equivalent of calling 'field(name, type [, Field-info])'.

      C = make_dataclass('C', ['x', ('y', int), ('z', int, field(init=False))], bases=(Base,))

    is equivalent to:

      @dataclass
      class C(Base):
          x: 'typing.Any'
          y: int
          z: int = field(init=False)

    For the bases and namespace parameters, see the builtin type() function.

    The parameters init, repr, eq, order, unsafe_hash, and frozen are passed to
    dataclass().
    '''
    init_inputs = [
        rc.NodeInputBP(label='cls_name'),
rc.NodeInputBP(label='fields'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses.make_dataclass(self.input(0), self.input(1)))
        


class AutoNode_dataclasses_replace(rc.Node):
    title = 'replace'
    doc = '''Return a new object replacing specified fields with new values.

    This is especially useful for frozen classes.  Example usage:

      @dataclass(frozen=True)
      class C:
          x: int
          y: int

      c = C(1, 2)
      c1 = replace(c, x=3)
      assert c1.x == 3 and c1.y == 2
      '''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dataclasses.replace(self.input(0)))
        