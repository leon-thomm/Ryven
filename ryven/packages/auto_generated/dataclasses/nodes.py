
from NENV import *

import dataclasses


class NodeBase(Node):
    pass


class _Asdict_Inner_Node(NodeBase):
    """
    """
    
    title = '_asdict_inner'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='dict_factory'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._asdict_inner(self.input(0), self.input(1)))
        

class _Astuple_Inner_Node(NodeBase):
    """
    """
    
    title = '_astuple_inner'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='tuple_factory'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._astuple_inner(self.input(0), self.input(1)))
        

class _Cmp_Fn_Node(NodeBase):
    """
    """
    
    title = '_cmp_fn'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='op'),
        NodeInputBP(label='self_tuple'),
        NodeInputBP(label='other_tuple'),
        NodeInputBP(label='globals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._cmp_fn(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class _Create_Fn_Node(NodeBase):
    """
    """
    
    title = '_create_fn'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='args'),
        NodeInputBP(label='body'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._create_fn(self.input(0), self.input(1), self.input(2)))
        

class _Field_Assign_Node(NodeBase):
    """
    """
    
    title = '_field_assign'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='frozen'),
        NodeInputBP(label='name'),
        NodeInputBP(label='value'),
        NodeInputBP(label='self_name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._field_assign(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Field_Init_Node(NodeBase):
    """
    """
    
    title = '_field_init'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='frozen'),
        NodeInputBP(label='globals'),
        NodeInputBP(label='self_name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._field_init(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Frozen_Get_Del_Attr_Node(NodeBase):
    """
    """
    
    title = '_frozen_get_del_attr'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='fields'),
        NodeInputBP(label='globals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._frozen_get_del_attr(self.input(0), self.input(1), self.input(2)))
        

class _Get_Field_Node(NodeBase):
    """
    """
    
    title = '_get_field'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='a_name'),
        NodeInputBP(label='a_type'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._get_field(self.input(0), self.input(1), self.input(2)))
        

class _Hash_Add_Node(NodeBase):
    """
    """
    
    title = '_hash_add'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='fields'),
        NodeInputBP(label='globals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._hash_add(self.input(0), self.input(1), self.input(2)))
        

class _Hash_Exception_Node(NodeBase):
    """
    """
    
    title = '_hash_exception'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='fields'),
        NodeInputBP(label='globals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._hash_exception(self.input(0), self.input(1), self.input(2)))
        

class _Hash_Fn_Node(NodeBase):
    """
    """
    
    title = '_hash_fn'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='fields'),
        NodeInputBP(label='globals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._hash_fn(self.input(0), self.input(1)))
        

class _Hash_Set_None_Node(NodeBase):
    """
    """
    
    title = '_hash_set_none'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='fields'),
        NodeInputBP(label='globals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._hash_set_none(self.input(0), self.input(1), self.input(2)))
        

class _Init_Fn_Node(NodeBase):
    """
    """
    
    title = '_init_fn'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='fields'),
        NodeInputBP(label='frozen'),
        NodeInputBP(label='has_post_init'),
        NodeInputBP(label='self_name'),
        NodeInputBP(label='globals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._init_fn(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class _Init_Param_Node(NodeBase):
    """
    """
    
    title = '_init_param'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._init_param(self.input(0)))
        

class _Is_Classvar_Node(NodeBase):
    """
    """
    
    title = '_is_classvar'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='a_type'),
        NodeInputBP(label='typing'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._is_classvar(self.input(0), self.input(1)))
        

class _Is_Dataclass_Instance_Node(NodeBase):
    """
    Returns True if obj is an instance of a dataclass."""
    
    title = '_is_dataclass_instance'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._is_dataclass_instance(self.input(0)))
        

class _Is_Initvar_Node(NodeBase):
    """
    """
    
    title = '_is_initvar'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='a_type'),
        NodeInputBP(label='dataclasses'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._is_initvar(self.input(0), self.input(1)))
        

class _Is_Type_Node(NodeBase):
    """
    """
    
    title = '_is_type'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='annotation'),
        NodeInputBP(label='cls'),
        NodeInputBP(label='a_module'),
        NodeInputBP(label='a_type'),
        NodeInputBP(label='is_type_predicate'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._is_type(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class _Process_Class_Node(NodeBase):
    """
    """
    
    title = '_process_class'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='init'),
        NodeInputBP(label='repr'),
        NodeInputBP(label='eq'),
        NodeInputBP(label='order'),
        NodeInputBP(label='unsafe_hash'),
        NodeInputBP(label='frozen'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._process_class(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        

class _Recursive_Repr_Node(NodeBase):
    """
    """
    
    title = '_recursive_repr'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='user_function'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._recursive_repr(self.input(0)))
        

class _Repr_Fn_Node(NodeBase):
    """
    """
    
    title = '_repr_fn'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='fields'),
        NodeInputBP(label='globals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._repr_fn(self.input(0), self.input(1)))
        

class _Set_New_Attribute_Node(NodeBase):
    """
    """
    
    title = '_set_new_attribute'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='name'),
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._set_new_attribute(self.input(0), self.input(1), self.input(2)))
        

class _Tuple_Str_Node(NodeBase):
    """
    """
    
    title = '_tuple_str'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='obj_name'),
        NodeInputBP(label='fields'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses._tuple_str(self.input(0), self.input(1)))
        

class Asdict_Node(NodeBase):
    """
    Return the fields of a dataclass instance as a new dictionary mapping
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
    """
    
    title = 'asdict'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses.asdict(self.input(0)))
        

class Astuple_Node(NodeBase):
    """
    Return the fields of a dataclass instance as a new tuple of field values.

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
    """
    
    title = 'astuple'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses.astuple(self.input(0)))
        

class Dataclass_Node(NodeBase):
    """
    Returns the same class as was passed in, with dunder methods
    added based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If
    repr is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method function is added. If frozen is true, fields may
    not be assigned to after instance creation.
    """
    
    title = 'dataclass'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='cls', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses.dataclass(self.input(0)))
        

class Field_Node(NodeBase):
    """
    Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is True, the field will be a parameter to the class's __init__()
    function.  If repr is True, the field will be included in the
    object's repr().  If hash is True, the field will be included in
    the object's hash().  If compare is True, the field will be used
    in comparison functions.  metadata, if specified, must be a
    mapping which is stored but not otherwise examined by dataclass.

    It is an error to specify both default and default_factory.
    """
    
    title = 'field'
    type_ = 'dataclasses'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses.field())
        

class Fields_Node(NodeBase):
    """
    Return a tuple describing the fields of this dataclass.

    Accepts a dataclass or an instance of one. Tuple elements are of
    type Field.
    """
    
    title = 'fields'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='class_or_instance'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses.fields(self.input(0)))
        

class Is_Dataclass_Node(NodeBase):
    """
    Returns True if obj is a dataclass or an instance of a
    dataclass."""
    
    title = 'is_dataclass'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses.is_dataclass(self.input(0)))
        

class Make_Dataclass_Node(NodeBase):
    """
    Return a new dynamically created dataclass.

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
    """
    
    title = 'make_dataclass'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='cls_name'),
        NodeInputBP(label='fields'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses.make_dataclass(self.input(0), self.input(1)))
        

class Replace_Node(NodeBase):
    """
    Return a new object replacing specified fields with new values.

    This is especially useful for frozen classes.  Example usage:

      @dataclass(frozen=True)
      class C:
          x: int
          y: int

      c = C(1, 2)
      c1 = replace(c, x=3)
      assert c1.x == 3 and c1.y == 2
      """
    
    title = 'replace'
    type_ = 'dataclasses'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dataclasses.replace(self.input(0)))
        


export_nodes(
    _Asdict_Inner_Node,
    _Astuple_Inner_Node,
    _Cmp_Fn_Node,
    _Create_Fn_Node,
    _Field_Assign_Node,
    _Field_Init_Node,
    _Frozen_Get_Del_Attr_Node,
    _Get_Field_Node,
    _Hash_Add_Node,
    _Hash_Exception_Node,
    _Hash_Fn_Node,
    _Hash_Set_None_Node,
    _Init_Fn_Node,
    _Init_Param_Node,
    _Is_Classvar_Node,
    _Is_Dataclass_Instance_Node,
    _Is_Initvar_Node,
    _Is_Type_Node,
    _Process_Class_Node,
    _Recursive_Repr_Node,
    _Repr_Fn_Node,
    _Set_New_Attribute_Node,
    _Tuple_Str_Node,
    Asdict_Node,
    Astuple_Node,
    Dataclass_Node,
    Field_Node,
    Fields_Node,
    Is_Dataclass_Node,
    Make_Dataclass_Node,
    Replace_Node,
)
