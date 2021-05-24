
from NENV import *

import inspect


class NodeBase(Node):
    pass


class _Check_Class_Node(NodeBase):
    """
    """
    
    title = '_check_class'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='klass'),
        NodeInputBP(label='attr'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._check_class(self.input(0), self.input(1)))
        

class _Check_Instance_Node(NodeBase):
    """
    """
    
    title = '_check_instance'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='attr'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._check_instance(self.input(0), self.input(1)))
        

class _Findclass_Node(NodeBase):
    """
    """
    
    title = '_findclass'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._findclass(self.input(0)))
        

class _Finddoc_Node(NodeBase):
    """
    """
    
    title = '_finddoc'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._finddoc(self.input(0)))
        

class _Has_Code_Flag_Node(NodeBase):
    """
    Return true if ``f`` is a function (or a method or functools.partial
    wrapper wrapping a function) whose code object has the given ``flag``
    set in its flags."""
    
    title = '_has_code_flag'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='flag'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._has_code_flag(self.input(0), self.input(1)))
        

class _Is_Type_Node(NodeBase):
    """
    """
    
    title = '_is_type'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._is_type(self.input(0)))
        

class _Main_Node(NodeBase):
    """
     Logic for inspecting an object given at command line """
    
    title = '_main'
    type_ = 'inspect'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._main())
        

class _Missing_Arguments_Node(NodeBase):
    """
    """
    
    title = '_missing_arguments'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='f_name'),
        NodeInputBP(label='argnames'),
        NodeInputBP(label='pos'),
        NodeInputBP(label='values'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._missing_arguments(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Shadowed_Dict_Node(NodeBase):
    """
    """
    
    title = '_shadowed_dict'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='klass'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._shadowed_dict(self.input(0)))
        

class _Signature_Bound_Method_Node(NodeBase):
    """
    Private helper to transform signatures for unbound
    functions to bound methods.
    """
    
    title = '_signature_bound_method'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='sig'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._signature_bound_method(self.input(0)))
        

class _Signature_From_Builtin_Node(NodeBase):
    """
    Private helper function to get signature for
    builtin callables.
    """
    
    title = '_signature_from_builtin'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='func'),
        NodeInputBP(label='skip_bound_arg', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._signature_from_builtin(self.input(0), self.input(1), self.input(2)))
        

class _Signature_From_Callable_Node(NodeBase):
    """
    Private helper function to get signature for arbitrary
    callable objects.
    """
    
    title = '_signature_from_callable'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._signature_from_callable(self.input(0)))
        

class _Signature_From_Function_Node(NodeBase):
    """
    Private helper: constructs Signature for the given python function."""
    
    title = '_signature_from_function'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='func'),
        NodeInputBP(label='skip_bound_arg', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._signature_from_function(self.input(0), self.input(1), self.input(2)))
        

class _Signature_Fromstr_Node(NodeBase):
    """
    Private helper to parse content of '__text_signature__'
    and return a Signature based on it.
    """
    
    title = '_signature_fromstr'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='obj'),
        NodeInputBP(label='s'),
        NodeInputBP(label='skip_bound_arg', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._signature_fromstr(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Signature_Get_Bound_Param_Node(NodeBase):
    """
     Private helper to get first parameter name from a
    __text_signature__ of a builtin method, which should
    be in the following format: '($param1, ...)'.
    Assumptions are that the first argument won't have
    a default value or an annotation.
    """
    
    title = '_signature_get_bound_param'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='spec'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._signature_get_bound_param(self.input(0)))
        

class _Signature_Get_Partial_Node(NodeBase):
    """
    Private helper to calculate how 'wrapped_sig' signature will
    look like after applying a 'functools.partial' object (or alike)
    on it.
    """
    
    title = '_signature_get_partial'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='wrapped_sig'),
        NodeInputBP(label='partial'),
        NodeInputBP(label='extra_args', dtype=dtypes.Data(default=(), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._signature_get_partial(self.input(0), self.input(1), self.input(2)))
        

class _Signature_Get_User_Defined_Method_Node(NodeBase):
    """
    Private helper. Checks if ``cls`` has an attribute
    named ``method_name`` and returns it only if it is a
    pure python function.
    """
    
    title = '_signature_get_user_defined_method'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='method_name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._signature_get_user_defined_method(self.input(0), self.input(1)))
        

class _Signature_Is_Builtin_Node(NodeBase):
    """
    Private helper to test if `obj` is a callable that might
    support Argument Clinic's __text_signature__ protocol.
    """
    
    title = '_signature_is_builtin'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._signature_is_builtin(self.input(0)))
        

class _Signature_Is_Functionlike_Node(NodeBase):
    """
    Private helper to test if `obj` is a duck type of FunctionType.
    A good example of such objects are functions compiled with
    Cython, which have all attributes that a pure Python function
    would have, but have their code statically compiled.
    """
    
    title = '_signature_is_functionlike'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._signature_is_functionlike(self.input(0)))
        

class _Signature_Strip_Non_Python_Syntax_Node(NodeBase):
    """
    
    Private helper function. Takes a signature in Argument Clinic's
    extended signature format.

    Returns a tuple of three things:
      * that signature re-rendered in standard Python syntax,
      * the index of the "self" parameter (generally 0), or None if
        the function does not have a "self" parameter, and
      * the index of the last "positional only" parameter,
        or None if the signature has no positional-only parameters.
    """
    
    title = '_signature_strip_non_python_syntax'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='signature'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._signature_strip_non_python_syntax(self.input(0)))
        

class _Static_Getmro_Node(NodeBase):
    """
    """
    
    title = '_static_getmro'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='klass'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._static_getmro(self.input(0)))
        

class _Too_Many_Node(NodeBase):
    """
    """
    
    title = '_too_many'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='f_name'),
        NodeInputBP(label='args'),
        NodeInputBP(label='kwonly'),
        NodeInputBP(label='varargs'),
        NodeInputBP(label='defcount'),
        NodeInputBP(label='given'),
        NodeInputBP(label='values'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect._too_many(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        

class Classify_Class_Attrs_Node(NodeBase):
    """
    Return list of attribute-descriptor tuples.

    For each name in dir(cls), the return list contains a 4-tuple
    with these elements:

        0. The name (a string).

        1. The kind of attribute this is, one of these strings:
               'class method'    created via classmethod()
               'static method'   created via staticmethod()
               'property'        created via property()
               'method'          any other flavor of method or descriptor
               'data'            not a method

        2. The class which defined this attribute (a class).

        3. The object as obtained by calling getattr; if this fails, or if the
           resulting object does not live anywhere in the class' mro (including
           metaclasses) then the object is looked up in the defining class's
           dict (found by walking the mro).

    If one of the items in dir(cls) is stored in the metaclass it will now
    be discovered and not have None be listed as the class in which it was
    defined.  Any items whose home class cannot be discovered are skipped.
    """
    
    title = 'classify_class_attrs'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.classify_class_attrs(self.input(0)))
        

class Cleandoc_Node(NodeBase):
    """
    Clean up indentation from docstrings.

    Any whitespace that can be uniformly removed from the second line
    onwards is removed."""
    
    title = 'cleandoc'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='doc'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.cleandoc(self.input(0)))
        

class Currentframe_Node(NodeBase):
    """
    Return the frame of the caller or None if this is not possible."""
    
    title = 'currentframe'
    type_ = 'inspect'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.currentframe())
        

class Findsource_Node(NodeBase):
    """
    Return the entire source file and starting line number for an object.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a list of all the lines
    in the file and the line number indexes a line in that list.  An OSError
    is raised if the source code cannot be retrieved."""
    
    title = 'findsource'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.findsource(self.input(0)))
        

class Formatannotation_Node(NodeBase):
    """
    """
    
    title = 'formatannotation'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='annotation'),
        NodeInputBP(label='base_module', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.formatannotation(self.input(0), self.input(1)))
        

class Formatannotationrelativeto_Node(NodeBase):
    """
    """
    
    title = 'formatannotationrelativeto'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.formatannotationrelativeto(self.input(0)))
        

class Formatargspec_Node(NodeBase):
    """
    Format an argument spec from the values returned by getfullargspec.

    The first seven arguments are (args, varargs, varkw, defaults,
    kwonlyargs, kwonlydefaults, annotations).  The other five arguments
    are the corresponding optional formatting functions that are called to
    turn names and values into strings.  The last argument is an optional
    function to format the sequence of arguments.

    Deprecated since Python 3.5: use the `signature` function and `Signature`
    objects.
    """
    
    title = 'formatargspec'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='args'),
        NodeInputBP(label='varargs', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='varkw', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='defaults', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='kwonlyargs', dtype=dtypes.Data(default=(), size='s')),
        NodeInputBP(label='kwonlydefaults', dtype=dtypes.Data(default={}, size='s')),
        NodeInputBP(label='annotations', dtype=dtypes.Data(default={}, size='s')),
        NodeInputBP(label='formatarg', dtype=dtypes.Data(default=str, size='s')),
        NodeInputBP(label='formatvarargs', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='formatvarkw', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='formatvalue', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='formatreturns', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='formatannotation', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.formatargspec(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7), self.input(8), self.input(9), self.input(10), self.input(11), self.input(12)))
        

class Formatargvalues_Node(NodeBase):
    """
    Format an argument spec from the 4 values returned by getargvalues.

    The first four arguments are (args, varargs, varkw, locals).  The
    next four arguments are the corresponding optional formatting functions
    that are called to turn names and values into strings.  The ninth
    argument is an optional function to format the sequence of arguments."""
    
    title = 'formatargvalues'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='args'),
        NodeInputBP(label='varargs'),
        NodeInputBP(label='varkw'),
        NodeInputBP(label='locals'),
        NodeInputBP(label='formatarg', dtype=dtypes.Data(default=str, size='s')),
        NodeInputBP(label='formatvarargs', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='formatvarkw', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='formatvalue', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.formatargvalues(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        

class Getabsfile_Node(NodeBase):
    """
    Return an absolute path to the source or compiled file for an object.

    The idea is for each object to have a unique origin, so this routine
    normalizes the result as much as possible."""
    
    title = 'getabsfile'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getabsfile(self.input(0)))
        

class Getargs_Node(NodeBase):
    """
    Get information about the arguments accepted by a code object.

    Three things are returned: (args, varargs, varkw), where
    'args' is the list of argument names. Keyword-only arguments are
    appended. 'varargs' and 'varkw' are the names of the * and **
    arguments or None."""
    
    title = 'getargs'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='co'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getargs(self.input(0)))
        

class Getargspec_Node(NodeBase):
    """
    Get the names and default values of a function's parameters.

    A tuple of four things is returned: (args, varargs, keywords, defaults).
    'args' is a list of the argument names, including keyword-only argument names.
    'varargs' and 'keywords' are the names of the * and ** parameters or None.
    'defaults' is an n-tuple of the default values of the last n parameters.

    This function is deprecated, as it does not support annotations or
    keyword-only parameters and will raise ValueError if either is present
    on the supplied callable.

    For a more structured introspection API, use inspect.signature() instead.

    Alternatively, use getfullargspec() for an API with a similar namedtuple
    based interface, but full support for annotations and keyword-only
    parameters.

    Deprecated since Python 3.5, use `inspect.getfullargspec()`.
    """
    
    title = 'getargspec'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getargspec(self.input(0)))
        

class Getargvalues_Node(NodeBase):
    """
    Get information about arguments passed into a particular frame.

    A tuple of four things is returned: (args, varargs, varkw, locals).
    'args' is a list of the argument names.
    'varargs' and 'varkw' are the names of the * and ** arguments or None.
    'locals' is the locals dictionary of the given frame."""
    
    title = 'getargvalues'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='frame'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getargvalues(self.input(0)))
        

class Getattr_Static_Node(NodeBase):
    """
    Retrieve attributes without triggering dynamic lookup via the
       descriptor protocol,  __getattr__ or __getattribute__.

       Note: this function may not be able to retrieve all attributes
       that getattr can fetch (like dynamically created attributes)
       and may find attributes that getattr can't (like descriptors
       that raise AttributeError). It can also return descriptor objects
       instead of instance members in some cases. See the
       documentation for details.
    """
    
    title = 'getattr_static'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='attr'),
        NodeInputBP(label='default', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getattr_static(self.input(0), self.input(1), self.input(2)))
        

class Getblock_Node(NodeBase):
    """
    Extract the block of code at the top of the given list of lines."""
    
    title = 'getblock'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='lines'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getblock(self.input(0)))
        

class Getcallargs_Node(NodeBase):
    """
    Get the mapping of arguments to values.

    A dict is returned, with keys the function argument names (including the
    names of the * and ** arguments, if any), and values the respective bound
    values from 'positional' and 'named'."""
    
    title = 'getcallargs'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getcallargs(self.input(0)))
        

class Getclasstree_Node(NodeBase):
    """
    Arrange the given list of classes into a hierarchy of nested lists.

    Where a nested list appears, it contains classes derived from the class
    whose entry immediately precedes the list.  Each entry is a 2-tuple
    containing a class and a tuple of its base classes.  If the 'unique'
    argument is true, exactly one entry appears in the returned structure
    for each class in the given list.  Otherwise, classes using multiple
    inheritance and their descendants will appear multiple times."""
    
    title = 'getclasstree'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='classes'),
        NodeInputBP(label='unique', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getclasstree(self.input(0), self.input(1)))
        

class Getclosurevars_Node(NodeBase):
    """
    
    Get the mapping of free variables to their current values.

    Returns a named tuple of dicts mapping the current nonlocal, global
    and builtin references as seen by the body of the function. A final
    set of unbound names that could not be resolved is also provided.
    """
    
    title = 'getclosurevars'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getclosurevars(self.input(0)))
        

class Getcomments_Node(NodeBase):
    """
    Get lines of comments immediately preceding an object's source code.

    Returns None when source can't be found.
    """
    
    title = 'getcomments'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getcomments(self.input(0)))
        

class Getcoroutinelocals_Node(NodeBase):
    """
    
    Get the mapping of coroutine local variables to their current values.

    A dict is returned, with the keys the local variable names and values the
    bound values."""
    
    title = 'getcoroutinelocals'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='coroutine'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getcoroutinelocals(self.input(0)))
        

class Getcoroutinestate_Node(NodeBase):
    """
    Get current state of a coroutine object.

    Possible states are:
      CORO_CREATED: Waiting to start execution.
      CORO_RUNNING: Currently being executed by the interpreter.
      CORO_SUSPENDED: Currently suspended at an await expression.
      CORO_CLOSED: Execution has completed.
    """
    
    title = 'getcoroutinestate'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='coroutine'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getcoroutinestate(self.input(0)))
        

class Getdoc_Node(NodeBase):
    """
    Get the documentation string for an object.

    All tabs are expanded to spaces.  To clean up docstrings that are
    indented to line up with blocks of code, any whitespace than can be
    uniformly removed from the second line onwards is removed."""
    
    title = 'getdoc'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getdoc(self.input(0)))
        

class Getfile_Node(NodeBase):
    """
    Work out which source or compiled file an object was defined in."""
    
    title = 'getfile'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getfile(self.input(0)))
        

class Getframeinfo_Node(NodeBase):
    """
    Get information about a frame or traceback object.

    A tuple of five things is returned: the filename, the line number of
    the current line, the function name, a list of lines of context from
    the source code, and the index of the current line within that list.
    The optional second argument specifies the number of lines of context
    to return, which are centered around the current line."""
    
    title = 'getframeinfo'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='frame'),
        NodeInputBP(label='context', dtype=dtypes.Data(default=1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getframeinfo(self.input(0), self.input(1)))
        

class Getfullargspec_Node(NodeBase):
    """
    Get the names and default values of a callable object's parameters.

    A tuple of seven things is returned:
    (args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations).
    'args' is a list of the parameter names.
    'varargs' and 'varkw' are the names of the * and ** parameters or None.
    'defaults' is an n-tuple of the default values of the last n parameters.
    'kwonlyargs' is a list of keyword-only parameter names.
    'kwonlydefaults' is a dictionary mapping names from kwonlyargs to defaults.
    'annotations' is a dictionary mapping parameter names to annotations.

    Notable differences from inspect.signature():
      - the "self" parameter is always reported, even for bound methods
      - wrapper chains defined by __wrapped__ *not* unwrapped automatically
    """
    
    title = 'getfullargspec'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getfullargspec(self.input(0)))
        

class Getgeneratorlocals_Node(NodeBase):
    """
    
    Get the mapping of generator local variables to their current values.

    A dict is returned, with the keys the local variable names and values the
    bound values."""
    
    title = 'getgeneratorlocals'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='generator'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getgeneratorlocals(self.input(0)))
        

class Getgeneratorstate_Node(NodeBase):
    """
    Get current state of a generator-iterator.

    Possible states are:
      GEN_CREATED: Waiting to start execution.
      GEN_RUNNING: Currently being executed by the interpreter.
      GEN_SUSPENDED: Currently suspended at a yield expression.
      GEN_CLOSED: Execution has completed.
    """
    
    title = 'getgeneratorstate'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='generator'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getgeneratorstate(self.input(0)))
        

class Getinnerframes_Node(NodeBase):
    """
    Get a list of records for a traceback's frame and all lower frames.

    Each record contains a frame object, filename, line number, function
    name, a list of lines of context, and index within the context."""
    
    title = 'getinnerframes'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='tb'),
        NodeInputBP(label='context', dtype=dtypes.Data(default=1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getinnerframes(self.input(0), self.input(1)))
        

class Getlineno_Node(NodeBase):
    """
    Get the line number from a frame object, allowing for optimization."""
    
    title = 'getlineno'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='frame'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getlineno(self.input(0)))
        

class Getmembers_Node(NodeBase):
    """
    Return all members of an object as (name, value) pairs sorted by name.
    Optionally, only return members that satisfy a given predicate."""
    
    title = 'getmembers'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
        NodeInputBP(label='predicate', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getmembers(self.input(0), self.input(1)))
        

class Getmodule_Node(NodeBase):
    """
    Return the module an object was defined in, or None if not found."""
    
    title = 'getmodule'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getmodule(self.input(0)))
        

class Getmodulename_Node(NodeBase):
    """
    Return the module name for a given file, or None."""
    
    title = 'getmodulename'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getmodulename(self.input(0)))
        

class Getmro_Node(NodeBase):
    """
    Return tuple of base classes (including cls) in method resolution order."""
    
    title = 'getmro'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getmro(self.input(0)))
        

class Getouterframes_Node(NodeBase):
    """
    Get a list of records for a frame and all higher (calling) frames.

    Each record contains a frame object, filename, line number, function
    name, a list of lines of context, and index within the context."""
    
    title = 'getouterframes'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='frame'),
        NodeInputBP(label='context', dtype=dtypes.Data(default=1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getouterframes(self.input(0), self.input(1)))
        

class Getsource_Node(NodeBase):
    """
    Return the text of the source code for an object.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a single string.  An
    OSError is raised if the source code cannot be retrieved."""
    
    title = 'getsource'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getsource(self.input(0)))
        

class Getsourcefile_Node(NodeBase):
    """
    Return the filename that can be used to locate an object's source.
    Return None if no way can be identified to get the source.
    """
    
    title = 'getsourcefile'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getsourcefile(self.input(0)))
        

class Getsourcelines_Node(NodeBase):
    """
    Return a list of source lines and starting line number for an object.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a list of the lines
    corresponding to the object and the line number indicates where in the
    original source file the first line of code was found.  An OSError is
    raised if the source code cannot be retrieved."""
    
    title = 'getsourcelines'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.getsourcelines(self.input(0)))
        

class Indentsize_Node(NodeBase):
    """
    Return the indent size, in spaces, at the start of a line of text."""
    
    title = 'indentsize'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='line'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.indentsize(self.input(0)))
        

class Isabstract_Node(NodeBase):
    """
    Return true if the object is an abstract base class (ABC)."""
    
    title = 'isabstract'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.isabstract(self.input(0)))
        

class Isasyncgen_Node(NodeBase):
    """
    Return true if the object is an asynchronous generator."""
    
    title = 'isasyncgen'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.isasyncgen(self.input(0)))
        

class Isasyncgenfunction_Node(NodeBase):
    """
    Return true if the object is an asynchronous generator function.

    Asynchronous generator functions are defined with "async def"
    syntax and have "yield" expressions in their body.
    """
    
    title = 'isasyncgenfunction'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.isasyncgenfunction(self.input(0)))
        

class Isawaitable_Node(NodeBase):
    """
    Return true if object can be passed to an ``await`` expression."""
    
    title = 'isawaitable'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.isawaitable(self.input(0)))
        

class Isbuiltin_Node(NodeBase):
    """
    Return true if the object is a built-in function or method.

    Built-in functions and methods provide these attributes:
        __doc__         documentation string
        __name__        original name of this function or method
        __self__        instance to which a method is bound, or None"""
    
    title = 'isbuiltin'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.isbuiltin(self.input(0)))
        

class Isclass_Node(NodeBase):
    """
    Return true if the object is a class.

    Class objects provide these attributes:
        __doc__         documentation string
        __module__      name of module in which this class was defined"""
    
    title = 'isclass'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.isclass(self.input(0)))
        

class Iscode_Node(NodeBase):
    """
    Return true if the object is a code object.

    Code objects provide these attributes:
        co_argcount         number of arguments (not including *, ** args
                            or keyword only arguments)
        co_code             string of raw compiled bytecode
        co_cellvars         tuple of names of cell variables
        co_consts           tuple of constants used in the bytecode
        co_filename         name of file in which this code object was created
        co_firstlineno      number of first line in Python source code
        co_flags            bitmap: 1=optimized | 2=newlocals | 4=*arg | 8=**arg
                            | 16=nested | 32=generator | 64=nofree | 128=coroutine
                            | 256=iterable_coroutine | 512=async_generator
        co_freevars         tuple of names of free variables
        co_posonlyargcount  number of positional only arguments
        co_kwonlyargcount   number of keyword only arguments (not including ** arg)
        co_lnotab           encoded mapping of line numbers to bytecode indices
        co_name             name with which this code object was defined
        co_names            tuple of names of local variables
        co_nlocals          number of local variables
        co_stacksize        virtual machine stack space required
        co_varnames         tuple of names of arguments and local variables"""
    
    title = 'iscode'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.iscode(self.input(0)))
        

class Iscoroutine_Node(NodeBase):
    """
    Return true if the object is a coroutine."""
    
    title = 'iscoroutine'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.iscoroutine(self.input(0)))
        

class Iscoroutinefunction_Node(NodeBase):
    """
    Return true if the object is a coroutine function.

    Coroutine functions are defined with "async def" syntax.
    """
    
    title = 'iscoroutinefunction'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.iscoroutinefunction(self.input(0)))
        

class Isdatadescriptor_Node(NodeBase):
    """
    Return true if the object is a data descriptor.

    Data descriptors have a __set__ or a __delete__ attribute.  Examples are
    properties (defined in Python) and getsets and members (defined in C).
    Typically, data descriptors will also have __name__ and __doc__ attributes
    (properties, getsets, and members have both of these attributes), but this
    is not guaranteed."""
    
    title = 'isdatadescriptor'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.isdatadescriptor(self.input(0)))
        

class Isframe_Node(NodeBase):
    """
    Return true if the object is a frame object.

    Frame objects provide these attributes:
        f_back          next outer frame object (this frame's caller)
        f_builtins      built-in namespace seen by this frame
        f_code          code object being executed in this frame
        f_globals       global namespace seen by this frame
        f_lasti         index of last attempted instruction in bytecode
        f_lineno        current line number in Python source code
        f_locals        local namespace seen by this frame
        f_trace         tracing function for this frame, or None"""
    
    title = 'isframe'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.isframe(self.input(0)))
        

class Isfunction_Node(NodeBase):
    """
    Return true if the object is a user-defined function.

    Function objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this function was defined
        __code__        code object containing compiled function bytecode
        __defaults__    tuple of any default values for arguments
        __globals__     global namespace in which this function was defined
        __annotations__ dict of parameter annotations
        __kwdefaults__  dict of keyword only parameters with defaults"""
    
    title = 'isfunction'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.isfunction(self.input(0)))
        

class Isgenerator_Node(NodeBase):
    """
    Return true if the object is a generator.

    Generator objects provide these attributes:
        __iter__        defined to support iteration over container
        close           raises a new GeneratorExit exception inside the
                        generator to terminate the iteration
        gi_code         code object
        gi_frame        frame object or possibly None once the generator has
                        been exhausted
        gi_running      set to 1 when generator is executing, 0 otherwise
        next            return the next item from the container
        send            resumes the generator and "sends" a value that becomes
                        the result of the current yield-expression
        throw           used to raise an exception inside the generator"""
    
    title = 'isgenerator'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.isgenerator(self.input(0)))
        

class Isgeneratorfunction_Node(NodeBase):
    """
    Return true if the object is a user-defined generator function.

    Generator function objects provide the same attributes as functions.
    See help(isfunction) for a list of attributes."""
    
    title = 'isgeneratorfunction'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.isgeneratorfunction(self.input(0)))
        

class Isgetsetdescriptor_Node(NodeBase):
    """
    Return true if the object is a getset descriptor.

        getset descriptors are specialized descriptors defined in extension
        modules."""
    
    title = 'isgetsetdescriptor'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.isgetsetdescriptor(self.input(0)))
        

class Ismemberdescriptor_Node(NodeBase):
    """
    Return true if the object is a member descriptor.

        Member descriptors are specialized descriptors defined in extension
        modules."""
    
    title = 'ismemberdescriptor'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.ismemberdescriptor(self.input(0)))
        

class Ismethod_Node(NodeBase):
    """
    Return true if the object is an instance method.

    Instance method objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this method was defined
        __func__        function object containing implementation of method
        __self__        instance to which this method is bound"""
    
    title = 'ismethod'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.ismethod(self.input(0)))
        

class Ismethoddescriptor_Node(NodeBase):
    """
    Return true if the object is a method descriptor.

    But not if ismethod() or isclass() or isfunction() are true.

    This is new in Python 2.2, and, for example, is true of int.__add__.
    An object passing this test has a __get__ attribute but not a __set__
    attribute, but beyond that the set of attributes varies.  __name__ is
    usually sensible, and __doc__ often is.

    Methods implemented via descriptors that also pass one of the other
    tests return false from the ismethoddescriptor() test, simply because
    the other tests promise more -- you can, e.g., count on having the
    __func__ attribute (etc) when an object passes ismethod()."""
    
    title = 'ismethoddescriptor'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.ismethoddescriptor(self.input(0)))
        

class Ismodule_Node(NodeBase):
    """
    Return true if the object is a module.

    Module objects provide these attributes:
        __cached__      pathname to byte compiled file
        __doc__         documentation string
        __file__        filename (missing for built-in modules)"""
    
    title = 'ismodule'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.ismodule(self.input(0)))
        

class Isroutine_Node(NodeBase):
    """
    Return true if the object is any kind of function or method."""
    
    title = 'isroutine'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.isroutine(self.input(0)))
        

class Istraceback_Node(NodeBase):
    """
    Return true if the object is a traceback.

    Traceback objects provide these attributes:
        tb_frame        frame object at this level
        tb_lasti        index of last attempted instruction in bytecode
        tb_lineno       current line number in Python source code
        tb_next         next inner traceback object (called by this level)"""
    
    title = 'istraceback'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.istraceback(self.input(0)))
        

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
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='typename'),
        NodeInputBP(label='field_names'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.namedtuple(self.input(0), self.input(1)))
        

class Signature_Node(NodeBase):
    """
    Get a signature object for the passed callable."""
    
    title = 'signature'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.signature(self.input(0)))
        

class Stack_Node(NodeBase):
    """
    Return a list of records for the stack above the caller's frame."""
    
    title = 'stack'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='context', dtype=dtypes.Data(default=1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.stack(self.input(0)))
        

class Trace_Node(NodeBase):
    """
    Return a list of records for the stack below the current exception."""
    
    title = 'trace'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='context', dtype=dtypes.Data(default=1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.trace(self.input(0)))
        

class Unwrap_Node(NodeBase):
    """
    Get the object wrapped by *func*.

   Follows the chain of :attr:`__wrapped__` attributes returning the last
   object in the chain.

   *stop* is an optional callback accepting an object in the wrapper chain
   as its sole argument that allows the unwrapping to be terminated early if
   the callback returns a true value. If the callback never returns a true
   value, the last object in the chain is returned as usual. For example,
   :func:`signature` uses this to stop unwrapping if any object in the
   chain has a ``__signature__`` attribute defined.

   :exc:`ValueError` is raised if a cycle is encountered.

    """
    
    title = 'unwrap'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.unwrap(self.input(0)))
        

class Walktree_Node(NodeBase):
    """
    Recursive helper function for getclasstree()."""
    
    title = 'walktree'
    type_ = 'inspect'
    init_inputs = [
        NodeInputBP(label='classes'),
        NodeInputBP(label='children'),
        NodeInputBP(label='parent'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, inspect.walktree(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _Check_Class_Node,
    _Check_Instance_Node,
    _Findclass_Node,
    _Finddoc_Node,
    _Has_Code_Flag_Node,
    _Is_Type_Node,
    _Main_Node,
    _Missing_Arguments_Node,
    _Shadowed_Dict_Node,
    _Signature_Bound_Method_Node,
    _Signature_From_Builtin_Node,
    _Signature_From_Callable_Node,
    _Signature_From_Function_Node,
    _Signature_Fromstr_Node,
    _Signature_Get_Bound_Param_Node,
    _Signature_Get_Partial_Node,
    _Signature_Get_User_Defined_Method_Node,
    _Signature_Is_Builtin_Node,
    _Signature_Is_Functionlike_Node,
    _Signature_Strip_Non_Python_Syntax_Node,
    _Static_Getmro_Node,
    _Too_Many_Node,
    Classify_Class_Attrs_Node,
    Cleandoc_Node,
    Currentframe_Node,
    Findsource_Node,
    Formatannotation_Node,
    Formatannotationrelativeto_Node,
    Formatargspec_Node,
    Formatargvalues_Node,
    Getabsfile_Node,
    Getargs_Node,
    Getargspec_Node,
    Getargvalues_Node,
    Getattr_Static_Node,
    Getblock_Node,
    Getcallargs_Node,
    Getclasstree_Node,
    Getclosurevars_Node,
    Getcomments_Node,
    Getcoroutinelocals_Node,
    Getcoroutinestate_Node,
    Getdoc_Node,
    Getfile_Node,
    Getframeinfo_Node,
    Getfullargspec_Node,
    Getgeneratorlocals_Node,
    Getgeneratorstate_Node,
    Getinnerframes_Node,
    Getlineno_Node,
    Getmembers_Node,
    Getmodule_Node,
    Getmodulename_Node,
    Getmro_Node,
    Getouterframes_Node,
    Getsource_Node,
    Getsourcefile_Node,
    Getsourcelines_Node,
    Indentsize_Node,
    Isabstract_Node,
    Isasyncgen_Node,
    Isasyncgenfunction_Node,
    Isawaitable_Node,
    Isbuiltin_Node,
    Isclass_Node,
    Iscode_Node,
    Iscoroutine_Node,
    Iscoroutinefunction_Node,
    Isdatadescriptor_Node,
    Isframe_Node,
    Isfunction_Node,
    Isgenerator_Node,
    Isgeneratorfunction_Node,
    Isgetsetdescriptor_Node,
    Ismemberdescriptor_Node,
    Ismethod_Node,
    Ismethoddescriptor_Node,
    Ismodule_Node,
    Isroutine_Node,
    Istraceback_Node,
    Namedtuple_Node,
    Signature_Node,
    Stack_Node,
    Trace_Node,
    Unwrap_Node,
    Walktree_Node,
)
