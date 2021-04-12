import ryvencore_qt as rc
import inspect


class AutoNode_inspect__check_class(rc.Node):
    title = '_check_class'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='klass'),
rc.NodeInputBP(label='attr'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._check_class(self.input(0), self.input(1)))
        


class AutoNode_inspect__check_instance(rc.Node):
    title = '_check_instance'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
rc.NodeInputBP(label='attr'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._check_instance(self.input(0), self.input(1)))
        


class AutoNode_inspect__findclass(rc.Node):
    title = '_findclass'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._findclass(self.input(0)))
        


class AutoNode_inspect__finddoc(rc.Node):
    title = '_finddoc'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._finddoc(self.input(0)))
        


class AutoNode_inspect__has_code_flag(rc.Node):
    title = '_has_code_flag'
    description = '''Return true if ``f`` is a function (or a method or functools.partial
    wrapper wrapping a function) whose code object has the given ``flag``
    set in its flags.'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
rc.NodeInputBP(label='flag'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._has_code_flag(self.input(0), self.input(1)))
        


class AutoNode_inspect__is_type(rc.Node):
    title = '_is_type'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._is_type(self.input(0)))
        


class AutoNode_inspect__main(rc.Node):
    title = '_main'
    description = ''' Logic for inspecting an object given at command line '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._main())
        


class AutoNode_inspect__missing_arguments(rc.Node):
    title = '_missing_arguments'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f_name'),
rc.NodeInputBP(label='argnames'),
rc.NodeInputBP(label='pos'),
rc.NodeInputBP(label='values'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._missing_arguments(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_inspect__shadowed_dict(rc.Node):
    title = '_shadowed_dict'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='klass'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._shadowed_dict(self.input(0)))
        


class AutoNode_inspect__signature_bound_method(rc.Node):
    title = '_signature_bound_method'
    description = '''Private helper to transform signatures for unbound
    functions to bound methods.
    '''
    init_inputs = [
        rc.NodeInputBP(label='sig'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._signature_bound_method(self.input(0)))
        


class AutoNode_inspect__signature_from_builtin(rc.Node):
    title = '_signature_from_builtin'
    description = '''Private helper function to get signature for
    builtin callables.
    '''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='func'),
rc.NodeInputBP(label='skip_bound_arg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._signature_from_builtin(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_inspect__signature_from_callable(rc.Node):
    title = '_signature_from_callable'
    description = '''Private helper function to get signature for arbitrary
    callable objects.
    '''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._signature_from_callable(self.input(0)))
        


class AutoNode_inspect__signature_from_function(rc.Node):
    title = '_signature_from_function'
    description = '''Private helper: constructs Signature for the given python function.'''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='func'),
rc.NodeInputBP(label='skip_bound_arg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._signature_from_function(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_inspect__signature_fromstr(rc.Node):
    title = '_signature_fromstr'
    description = '''Private helper to parse content of '__text_signature__'
    and return a Signature based on it.
    '''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='obj'),
rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='skip_bound_arg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._signature_fromstr(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_inspect__signature_get_bound_param(rc.Node):
    title = '_signature_get_bound_param'
    description = ''' Private helper to get first parameter name from a
    __text_signature__ of a builtin method, which should
    be in the following format: '($param1, ...)'.
    Assumptions are that the first argument won't have
    a default value or an annotation.
    '''
    init_inputs = [
        rc.NodeInputBP(label='spec'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._signature_get_bound_param(self.input(0)))
        


class AutoNode_inspect__signature_get_partial(rc.Node):
    title = '_signature_get_partial'
    description = '''Private helper to calculate how 'wrapped_sig' signature will
    look like after applying a 'functools.partial' object (or alike)
    on it.
    '''
    init_inputs = [
        rc.NodeInputBP(label='wrapped_sig'),
rc.NodeInputBP(label='partial'),
rc.NodeInputBP(label='extra_args'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._signature_get_partial(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_inspect__signature_get_user_defined_method(rc.Node):
    title = '_signature_get_user_defined_method'
    description = '''Private helper. Checks if ``cls`` has an attribute
    named ``method_name`` and returns it only if it is a
    pure python function.
    '''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='method_name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._signature_get_user_defined_method(self.input(0), self.input(1)))
        


class AutoNode_inspect__signature_is_builtin(rc.Node):
    title = '_signature_is_builtin'
    description = '''Private helper to test if `obj` is a callable that might
    support Argument Clinic's __text_signature__ protocol.
    '''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._signature_is_builtin(self.input(0)))
        


class AutoNode_inspect__signature_is_functionlike(rc.Node):
    title = '_signature_is_functionlike'
    description = '''Private helper to test if `obj` is a duck type of FunctionType.
    A good example of such objects are functions compiled with
    Cython, which have all attributes that a pure Python function
    would have, but have their code statically compiled.
    '''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._signature_is_functionlike(self.input(0)))
        


class AutoNode_inspect__signature_strip_non_python_syntax(rc.Node):
    title = '_signature_strip_non_python_syntax'
    description = '''
    Private helper function. Takes a signature in Argument Clinic's
    extended signature format.

    Returns a tuple of three things:
      * that signature re-rendered in standard Python syntax,
      * the index of the "self" parameter (generally 0), or None if
        the function does not have a "self" parameter, and
      * the index of the last "positional only" parameter,
        or None if the signature has no positional-only parameters.
    '''
    init_inputs = [
        rc.NodeInputBP(label='signature'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._signature_strip_non_python_syntax(self.input(0)))
        


class AutoNode_inspect__static_getmro(rc.Node):
    title = '_static_getmro'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='klass'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._static_getmro(self.input(0)))
        


class AutoNode_inspect__too_many(rc.Node):
    title = '_too_many'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f_name'),
rc.NodeInputBP(label='args'),
rc.NodeInputBP(label='kwonly'),
rc.NodeInputBP(label='varargs'),
rc.NodeInputBP(label='defcount'),
rc.NodeInputBP(label='given'),
rc.NodeInputBP(label='values'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect._too_many(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        


class AutoNode_inspect_classify_class_attrs(rc.Node):
    title = 'classify_class_attrs'
    description = '''Return list of attribute-descriptor tuples.

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
    '''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.classify_class_attrs(self.input(0)))
        


class AutoNode_inspect_cleandoc(rc.Node):
    title = 'cleandoc'
    description = '''Clean up indentation from docstrings.

    Any whitespace that can be uniformly removed from the second line
    onwards is removed.'''
    init_inputs = [
        rc.NodeInputBP(label='doc'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.cleandoc(self.input(0)))
        


class AutoNode_inspect_currentframe(rc.Node):
    title = 'currentframe'
    description = '''Return the frame of the caller or None if this is not possible.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.currentframe())
        


class AutoNode_inspect_findsource(rc.Node):
    title = 'findsource'
    description = '''Return the entire source file and starting line number for an object.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a list of all the lines
    in the file and the line number indexes a line in that list.  An OSError
    is raised if the source code cannot be retrieved.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.findsource(self.input(0)))
        


class AutoNode_inspect_formatannotation(rc.Node):
    title = 'formatannotation'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='annotation'),
rc.NodeInputBP(label='base_module'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.formatannotation(self.input(0), self.input(1)))
        


class AutoNode_inspect_formatannotationrelativeto(rc.Node):
    title = 'formatannotationrelativeto'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.formatannotationrelativeto(self.input(0)))
        


class AutoNode_inspect_formatargspec(rc.Node):
    title = 'formatargspec'
    description = '''Format an argument spec from the values returned by getfullargspec.

    The first seven arguments are (args, varargs, varkw, defaults,
    kwonlyargs, kwonlydefaults, annotations).  The other five arguments
    are the corresponding optional formatting functions that are called to
    turn names and values into strings.  The last argument is an optional
    function to format the sequence of arguments.

    Deprecated since Python 3.5: use the `signature` function and `Signature`
    objects.
    '''
    init_inputs = [
        rc.NodeInputBP(label='args'),
rc.NodeInputBP(label='varargs'),
rc.NodeInputBP(label='varkw'),
rc.NodeInputBP(label='defaults'),
rc.NodeInputBP(label='kwonlyargs'),
rc.NodeInputBP(label='kwonlydefaults'),
rc.NodeInputBP(label='annotations'),
rc.NodeInputBP(label='formatarg'),
rc.NodeInputBP(label='formatvarargs'),
rc.NodeInputBP(label='formatvarkw'),
rc.NodeInputBP(label='formatvalue'),
rc.NodeInputBP(label='formatreturns'),
rc.NodeInputBP(label='formatannotation'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.formatargspec(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7), self.input(8), self.input(9), self.input(10), self.input(11), self.input(12)))
        


class AutoNode_inspect_formatargvalues(rc.Node):
    title = 'formatargvalues'
    description = '''Format an argument spec from the 4 values returned by getargvalues.

    The first four arguments are (args, varargs, varkw, locals).  The
    next four arguments are the corresponding optional formatting functions
    that are called to turn names and values into strings.  The ninth
    argument is an optional function to format the sequence of arguments.'''
    init_inputs = [
        rc.NodeInputBP(label='args'),
rc.NodeInputBP(label='varargs'),
rc.NodeInputBP(label='varkw'),
rc.NodeInputBP(label='locals'),
rc.NodeInputBP(label='formatarg'),
rc.NodeInputBP(label='formatvarargs'),
rc.NodeInputBP(label='formatvarkw'),
rc.NodeInputBP(label='formatvalue'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.formatargvalues(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        


class AutoNode_inspect_getabsfile(rc.Node):
    title = 'getabsfile'
    description = '''Return an absolute path to the source or compiled file for an object.

    The idea is for each object to have a unique origin, so this routine
    normalizes the result as much as possible.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
rc.NodeInputBP(label='_filename'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getabsfile(self.input(0), self.input(1)))
        


class AutoNode_inspect_getargs(rc.Node):
    title = 'getargs'
    description = '''Get information about the arguments accepted by a code object.

    Three things are returned: (args, varargs, varkw), where
    'args' is the list of argument names. Keyword-only arguments are
    appended. 'varargs' and 'varkw' are the names of the * and **
    arguments or None.'''
    init_inputs = [
        rc.NodeInputBP(label='co'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getargs(self.input(0)))
        


class AutoNode_inspect_getargspec(rc.Node):
    title = 'getargspec'
    description = '''Get the names and default values of a function's parameters.

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
    '''
    init_inputs = [
        rc.NodeInputBP(label='func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getargspec(self.input(0)))
        


class AutoNode_inspect_getargvalues(rc.Node):
    title = 'getargvalues'
    description = '''Get information about arguments passed into a particular frame.

    A tuple of four things is returned: (args, varargs, varkw, locals).
    'args' is a list of the argument names.
    'varargs' and 'varkw' are the names of the * and ** arguments or None.
    'locals' is the locals dictionary of the given frame.'''
    init_inputs = [
        rc.NodeInputBP(label='frame'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getargvalues(self.input(0)))
        


class AutoNode_inspect_getattr_static(rc.Node):
    title = 'getattr_static'
    description = '''Retrieve attributes without triggering dynamic lookup via the
       descriptor protocol,  __getattr__ or __getattribute__.

       Note: this function may not be able to retrieve all attributes
       that getattr can fetch (like dynamically created attributes)
       and may find attributes that getattr can't (like descriptors
       that raise AttributeError). It can also return descriptor objects
       instead of instance members in some cases. See the
       documentation for details.
    '''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
rc.NodeInputBP(label='attr'),
rc.NodeInputBP(label='default'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getattr_static(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_inspect_getblock(rc.Node):
    title = 'getblock'
    description = '''Extract the block of code at the top of the given list of lines.'''
    init_inputs = [
        rc.NodeInputBP(label='lines'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getblock(self.input(0)))
        


class AutoNode_inspect_getcallargs(rc.Node):
    title = 'getcallargs'
    description = '''Get the mapping of arguments to values.

    A dict is returned, with keys the function argument names (including the
    names of the * and ** arguments, if any), and values the respective bound
    values from 'positional' and 'named'.'''
    init_inputs = [
        rc.NodeInputBP(label='func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getcallargs(self.input(0)))
        


class AutoNode_inspect_getclasstree(rc.Node):
    title = 'getclasstree'
    description = '''Arrange the given list of classes into a hierarchy of nested lists.

    Where a nested list appears, it contains classes derived from the class
    whose entry immediately precedes the list.  Each entry is a 2-tuple
    containing a class and a tuple of its base classes.  If the 'unique'
    argument is true, exactly one entry appears in the returned structure
    for each class in the given list.  Otherwise, classes using multiple
    inheritance and their descendants will appear multiple times.'''
    init_inputs = [
        rc.NodeInputBP(label='classes'),
rc.NodeInputBP(label='unique'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getclasstree(self.input(0), self.input(1)))
        


class AutoNode_inspect_getclosurevars(rc.Node):
    title = 'getclosurevars'
    description = '''
    Get the mapping of free variables to their current values.

    Returns a named tuple of dicts mapping the current nonlocal, global
    and builtin references as seen by the body of the function. A final
    set of unbound names that could not be resolved is also provided.
    '''
    init_inputs = [
        rc.NodeInputBP(label='func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getclosurevars(self.input(0)))
        


class AutoNode_inspect_getcomments(rc.Node):
    title = 'getcomments'
    description = '''Get lines of comments immediately preceding an object's source code.

    Returns None when source can't be found.
    '''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getcomments(self.input(0)))
        


class AutoNode_inspect_getcoroutinelocals(rc.Node):
    title = 'getcoroutinelocals'
    description = '''
    Get the mapping of coroutine local variables to their current values.

    A dict is returned, with the keys the local variable names and values the
    bound values.'''
    init_inputs = [
        rc.NodeInputBP(label='coroutine'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getcoroutinelocals(self.input(0)))
        


class AutoNode_inspect_getcoroutinestate(rc.Node):
    title = 'getcoroutinestate'
    description = '''Get current state of a coroutine object.

    Possible states are:
      CORO_CREATED: Waiting to start execution.
      CORO_RUNNING: Currently being executed by the interpreter.
      CORO_SUSPENDED: Currently suspended at an await expression.
      CORO_CLOSED: Execution has completed.
    '''
    init_inputs = [
        rc.NodeInputBP(label='coroutine'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getcoroutinestate(self.input(0)))
        


class AutoNode_inspect_getdoc(rc.Node):
    title = 'getdoc'
    description = '''Get the documentation string for an object.

    All tabs are expanded to spaces.  To clean up docstrings that are
    indented to line up with blocks of code, any whitespace than can be
    uniformly removed from the second line onwards is removed.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getdoc(self.input(0)))
        


class AutoNode_inspect_getfile(rc.Node):
    title = 'getfile'
    description = '''Work out which source or compiled file an object was defined in.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getfile(self.input(0)))
        


class AutoNode_inspect_getframeinfo(rc.Node):
    title = 'getframeinfo'
    description = '''Get information about a frame or traceback object.

    A tuple of five things is returned: the filename, the line number of
    the current line, the function name, a list of lines of context from
    the source code, and the index of the current line within that list.
    The optional second argument specifies the number of lines of context
    to return, which are centered around the current line.'''
    init_inputs = [
        rc.NodeInputBP(label='frame'),
rc.NodeInputBP(label='context'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getframeinfo(self.input(0), self.input(1)))
        


class AutoNode_inspect_getfullargspec(rc.Node):
    title = 'getfullargspec'
    description = '''Get the names and default values of a callable object's parameters.

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
    '''
    init_inputs = [
        rc.NodeInputBP(label='func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getfullargspec(self.input(0)))
        


class AutoNode_inspect_getgeneratorlocals(rc.Node):
    title = 'getgeneratorlocals'
    description = '''
    Get the mapping of generator local variables to their current values.

    A dict is returned, with the keys the local variable names and values the
    bound values.'''
    init_inputs = [
        rc.NodeInputBP(label='generator'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getgeneratorlocals(self.input(0)))
        


class AutoNode_inspect_getgeneratorstate(rc.Node):
    title = 'getgeneratorstate'
    description = '''Get current state of a generator-iterator.

    Possible states are:
      GEN_CREATED: Waiting to start execution.
      GEN_RUNNING: Currently being executed by the interpreter.
      GEN_SUSPENDED: Currently suspended at a yield expression.
      GEN_CLOSED: Execution has completed.
    '''
    init_inputs = [
        rc.NodeInputBP(label='generator'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getgeneratorstate(self.input(0)))
        


class AutoNode_inspect_getinnerframes(rc.Node):
    title = 'getinnerframes'
    description = '''Get a list of records for a traceback's frame and all lower frames.

    Each record contains a frame object, filename, line number, function
    name, a list of lines of context, and index within the context.'''
    init_inputs = [
        rc.NodeInputBP(label='tb'),
rc.NodeInputBP(label='context'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getinnerframes(self.input(0), self.input(1)))
        


class AutoNode_inspect_getlineno(rc.Node):
    title = 'getlineno'
    description = '''Get the line number from a frame object, allowing for optimization.'''
    init_inputs = [
        rc.NodeInputBP(label='frame'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getlineno(self.input(0)))
        


class AutoNode_inspect_getmembers(rc.Node):
    title = 'getmembers'
    description = '''Return all members of an object as (name, value) pairs sorted by name.
    Optionally, only return members that satisfy a given predicate.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
rc.NodeInputBP(label='predicate'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getmembers(self.input(0), self.input(1)))
        


class AutoNode_inspect_getmodule(rc.Node):
    title = 'getmodule'
    description = '''Return the module an object was defined in, or None if not found.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
rc.NodeInputBP(label='_filename'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getmodule(self.input(0), self.input(1)))
        


class AutoNode_inspect_getmodulename(rc.Node):
    title = 'getmodulename'
    description = '''Return the module name for a given file, or None.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getmodulename(self.input(0)))
        


class AutoNode_inspect_getmro(rc.Node):
    title = 'getmro'
    description = '''Return tuple of base classes (including cls) in method resolution order.'''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getmro(self.input(0)))
        


class AutoNode_inspect_getouterframes(rc.Node):
    title = 'getouterframes'
    description = '''Get a list of records for a frame and all higher (calling) frames.

    Each record contains a frame object, filename, line number, function
    name, a list of lines of context, and index within the context.'''
    init_inputs = [
        rc.NodeInputBP(label='frame'),
rc.NodeInputBP(label='context'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getouterframes(self.input(0), self.input(1)))
        


class AutoNode_inspect_getsource(rc.Node):
    title = 'getsource'
    description = '''Return the text of the source code for an object.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a single string.  An
    OSError is raised if the source code cannot be retrieved.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getsource(self.input(0)))
        


class AutoNode_inspect_getsourcefile(rc.Node):
    title = 'getsourcefile'
    description = '''Return the filename that can be used to locate an object's source.
    Return None if no way can be identified to get the source.
    '''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getsourcefile(self.input(0)))
        


class AutoNode_inspect_getsourcelines(rc.Node):
    title = 'getsourcelines'
    description = '''Return a list of source lines and starting line number for an object.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a list of the lines
    corresponding to the object and the line number indicates where in the
    original source file the first line of code was found.  An OSError is
    raised if the source code cannot be retrieved.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.getsourcelines(self.input(0)))
        


class AutoNode_inspect_indentsize(rc.Node):
    title = 'indentsize'
    description = '''Return the indent size, in spaces, at the start of a line of text.'''
    init_inputs = [
        rc.NodeInputBP(label='line'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.indentsize(self.input(0)))
        


class AutoNode_inspect_isabstract(rc.Node):
    title = 'isabstract'
    description = '''Return true if the object is an abstract base class (ABC).'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.isabstract(self.input(0)))
        


class AutoNode_inspect_isasyncgen(rc.Node):
    title = 'isasyncgen'
    description = '''Return true if the object is an asynchronous generator.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.isasyncgen(self.input(0)))
        


class AutoNode_inspect_isasyncgenfunction(rc.Node):
    title = 'isasyncgenfunction'
    description = '''Return true if the object is an asynchronous generator function.

    Asynchronous generator functions are defined with "async def"
    syntax and have "yield" expressions in their body.
    '''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.isasyncgenfunction(self.input(0)))
        


class AutoNode_inspect_isawaitable(rc.Node):
    title = 'isawaitable'
    description = '''Return true if object can be passed to an ``await`` expression.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.isawaitable(self.input(0)))
        


class AutoNode_inspect_isbuiltin(rc.Node):
    title = 'isbuiltin'
    description = '''Return true if the object is a built-in function or method.

    Built-in functions and methods provide these attributes:
        __doc__         documentation string
        __name__        original name of this function or method
        __self__        instance to which a method is bound, or None'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.isbuiltin(self.input(0)))
        


class AutoNode_inspect_isclass(rc.Node):
    title = 'isclass'
    description = '''Return true if the object is a class.

    Class objects provide these attributes:
        __doc__         documentation string
        __module__      name of module in which this class was defined'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.isclass(self.input(0)))
        


class AutoNode_inspect_iscode(rc.Node):
    title = 'iscode'
    description = '''Return true if the object is a code object.

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
        co_varnames         tuple of names of arguments and local variables'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.iscode(self.input(0)))
        


class AutoNode_inspect_iscoroutine(rc.Node):
    title = 'iscoroutine'
    description = '''Return true if the object is a coroutine.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.iscoroutine(self.input(0)))
        


class AutoNode_inspect_iscoroutinefunction(rc.Node):
    title = 'iscoroutinefunction'
    description = '''Return true if the object is a coroutine function.

    Coroutine functions are defined with "async def" syntax.
    '''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.iscoroutinefunction(self.input(0)))
        


class AutoNode_inspect_isdatadescriptor(rc.Node):
    title = 'isdatadescriptor'
    description = '''Return true if the object is a data descriptor.

    Data descriptors have a __set__ or a __delete__ attribute.  Examples are
    properties (defined in Python) and getsets and members (defined in C).
    Typically, data descriptors will also have __name__ and __doc__ attributes
    (properties, getsets, and members have both of these attributes), but this
    is not guaranteed.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.isdatadescriptor(self.input(0)))
        


class AutoNode_inspect_isframe(rc.Node):
    title = 'isframe'
    description = '''Return true if the object is a frame object.

    Frame objects provide these attributes:
        f_back          next outer frame object (this frame's caller)
        f_builtins      built-in namespace seen by this frame
        f_code          code object being executed in this frame
        f_globals       global namespace seen by this frame
        f_lasti         index of last attempted instruction in bytecode
        f_lineno        current line number in Python source code
        f_locals        local namespace seen by this frame
        f_trace         tracing function for this frame, or None'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.isframe(self.input(0)))
        


class AutoNode_inspect_isfunction(rc.Node):
    title = 'isfunction'
    description = '''Return true if the object is a user-defined function.

    Function objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this function was defined
        __code__        code object containing compiled function bytecode
        __defaults__    tuple of any default values for arguments
        __globals__     global namespace in which this function was defined
        __annotations__ dict of parameter annotations
        __kwdefaults__  dict of keyword only parameters with defaults'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.isfunction(self.input(0)))
        


class AutoNode_inspect_isgenerator(rc.Node):
    title = 'isgenerator'
    description = '''Return true if the object is a generator.

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
        throw           used to raise an exception inside the generator'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.isgenerator(self.input(0)))
        


class AutoNode_inspect_isgeneratorfunction(rc.Node):
    title = 'isgeneratorfunction'
    description = '''Return true if the object is a user-defined generator function.

    Generator function objects provide the same attributes as functions.
    See help(isfunction) for a list of attributes.'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.isgeneratorfunction(self.input(0)))
        


class AutoNode_inspect_isgetsetdescriptor(rc.Node):
    title = 'isgetsetdescriptor'
    description = '''Return true if the object is a getset descriptor.

        getset descriptors are specialized descriptors defined in extension
        modules.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.isgetsetdescriptor(self.input(0)))
        


class AutoNode_inspect_ismemberdescriptor(rc.Node):
    title = 'ismemberdescriptor'
    description = '''Return true if the object is a member descriptor.

        Member descriptors are specialized descriptors defined in extension
        modules.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.ismemberdescriptor(self.input(0)))
        


class AutoNode_inspect_ismethod(rc.Node):
    title = 'ismethod'
    description = '''Return true if the object is an instance method.

    Instance method objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this method was defined
        __func__        function object containing implementation of method
        __self__        instance to which this method is bound'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.ismethod(self.input(0)))
        


class AutoNode_inspect_ismethoddescriptor(rc.Node):
    title = 'ismethoddescriptor'
    description = '''Return true if the object is a method descriptor.

    But not if ismethod() or isclass() or isfunction() are true.

    This is new in Python 2.2, and, for example, is true of int.__add__.
    An object passing this test has a __get__ attribute but not a __set__
    attribute, but beyond that the set of attributes varies.  __name__ is
    usually sensible, and __doc__ often is.

    Methods implemented via descriptors that also pass one of the other
    tests return false from the ismethoddescriptor() test, simply because
    the other tests promise more -- you can, e.g., count on having the
    __func__ attribute (etc) when an object passes ismethod().'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.ismethoddescriptor(self.input(0)))
        


class AutoNode_inspect_ismodule(rc.Node):
    title = 'ismodule'
    description = '''Return true if the object is a module.

    Module objects provide these attributes:
        __cached__      pathname to byte compiled file
        __doc__         documentation string
        __file__        filename (missing for built-in modules)'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.ismodule(self.input(0)))
        


class AutoNode_inspect_isroutine(rc.Node):
    title = 'isroutine'
    description = '''Return true if the object is any kind of function or method.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.isroutine(self.input(0)))
        


class AutoNode_inspect_istraceback(rc.Node):
    title = 'istraceback'
    description = '''Return true if the object is a traceback.

    Traceback objects provide these attributes:
        tb_frame        frame object at this level
        tb_lasti        index of last attempted instruction in bytecode
        tb_lineno       current line number in Python source code
        tb_next         next inner traceback object (called by this level)'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.istraceback(self.input(0)))
        


class AutoNode_inspect_namedtuple(rc.Node):
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
        self.set_output_val(0, inspect.namedtuple(self.input(0), self.input(1)))
        


class AutoNode_inspect_signature(rc.Node):
    title = 'signature'
    description = '''Get a signature object for the passed callable.'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.signature(self.input(0)))
        


class AutoNode_inspect_stack(rc.Node):
    title = 'stack'
    description = '''Return a list of records for the stack above the caller's frame.'''
    init_inputs = [
        rc.NodeInputBP(label='context'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.stack(self.input(0)))
        


class AutoNode_inspect_trace(rc.Node):
    title = 'trace'
    description = '''Return a list of records for the stack below the current exception.'''
    init_inputs = [
        rc.NodeInputBP(label='context'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.trace(self.input(0)))
        


class AutoNode_inspect_unwrap(rc.Node):
    title = 'unwrap'
    description = '''Get the object wrapped by *func*.

   Follows the chain of :attr:`__wrapped__` attributes returning the last
   object in the chain.

   *stop* is an optional callback accepting an object in the wrapper chain
   as its sole argument that allows the unwrapping to be terminated early if
   the callback returns a true value. If the callback never returns a true
   value, the last object in the chain is returned as usual. For example,
   :func:`signature` uses this to stop unwrapping if any object in the
   chain has a ``__signature__`` attribute defined.

   :exc:`ValueError` is raised if a cycle is encountered.

    '''
    init_inputs = [
        rc.NodeInputBP(label='func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.unwrap(self.input(0)))
        


class AutoNode_inspect_walktree(rc.Node):
    title = 'walktree'
    description = '''Recursive helper function for getclasstree().'''
    init_inputs = [
        rc.NodeInputBP(label='classes'),
rc.NodeInputBP(label='children'),
rc.NodeInputBP(label='parent'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, inspect.walktree(self.input(0), self.input(1), self.input(2)))
        