import ryvencore_qt as rc
import imp


class AutoNode_imp__builtin_from_name(rc.Node):
    title = '_builtin_from_name'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp._builtin_from_name(self.input(0)))
        


class AutoNode_imp__exec(rc.Node):
    title = '_exec'
    doc = '''Execute the spec's specified module in an existing module's namespace.'''
    init_inputs = [
        rc.NodeInputBP(label='spec'),
rc.NodeInputBP(label='module'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp._exec(self.input(0), self.input(1)))
        


class AutoNode_imp__fix_co_filename(rc.Node):
    title = '_fix_co_filename'
    doc = '''Changes code.co_filename to specify the passed-in file path.

  code
    Code object to change.
  path
    File path to use.'''
    init_inputs = [
        rc.NodeInputBP(label='code'),
rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp._fix_co_filename(self.input(0), self.input(1)))
        


class AutoNode_imp__load(rc.Node):
    title = '_load'
    doc = '''Return a new module object, loaded by the spec's loader.

    The module is not added to its parent.

    If a module is already in sys.modules, that existing module gets
    clobbered.

    '''
    init_inputs = [
        rc.NodeInputBP(label='spec'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp._load(self.input(0)))
        


class AutoNode_imp_acquire_lock(rc.Node):
    title = 'acquire_lock'
    doc = '''Acquires the interpreter's import lock for the current thread.

This lock should be used by import hooks to ensure thread-safety when importing
modules. On platforms without threads, this function does nothing.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.acquire_lock())
        


class AutoNode_imp_cache_from_source(rc.Node):
    title = 'cache_from_source'
    doc = '''**DEPRECATED**

    Given the path to a .py file, return the path to its .pyc file.

    The .py file does not need to exist; this simply returns the path to the
    .pyc file calculated as if the .py file were imported.

    If debug_override is not None, then it must be a boolean and is used in
    place of sys.flags.optimize.

    If sys.implementation.cache_tag is None then NotImplementedError is raised.

    '''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='debug_override'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.cache_from_source(self.input(0), self.input(1)))
        


class AutoNode_imp_find_module(rc.Node):
    title = 'find_module'
    doc = '''**DEPRECATED**

    Search for a module.

    If path is omitted or None, search for a built-in, frozen or special
    module and continue search in sys.path. The module name cannot
    contain '.'; to search for a submodule of a package, pass the
    submodule name and the package's __path__.

    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.find_module(self.input(0), self.input(1)))
        


class AutoNode_imp_get_frozen_object(rc.Node):
    title = 'get_frozen_object'
    doc = '''Create a code object for a frozen module.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.get_frozen_object(self.input(0)))
        


class AutoNode_imp_get_magic(rc.Node):
    title = 'get_magic'
    doc = '''**DEPRECATED**

    Return the magic number for .pyc files.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.get_magic())
        


class AutoNode_imp_get_suffixes(rc.Node):
    title = 'get_suffixes'
    doc = '''**DEPRECATED**'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.get_suffixes())
        


class AutoNode_imp_get_tag(rc.Node):
    title = 'get_tag'
    doc = '''Return the magic tag for .pyc files.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.get_tag())
        


class AutoNode_imp_init_builtin(rc.Node):
    title = 'init_builtin'
    doc = '''**DEPRECATED**

    Load and return a built-in module by name, or None is such module doesn't
    exist
    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.init_builtin(self.input(0)))
        


class AutoNode_imp_init_frozen(rc.Node):
    title = 'init_frozen'
    doc = '''Initializes a frozen module.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.init_frozen(self.input(0)))
        


class AutoNode_imp_is_builtin(rc.Node):
    title = 'is_builtin'
    doc = '''Returns True if the module name corresponds to a built-in module.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.is_builtin(self.input(0)))
        


class AutoNode_imp_is_frozen(rc.Node):
    title = 'is_frozen'
    doc = '''Returns True if the module name corresponds to a frozen module.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.is_frozen(self.input(0)))
        


class AutoNode_imp_is_frozen_package(rc.Node):
    title = 'is_frozen_package'
    doc = '''Returns True if the module name is of a frozen package.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.is_frozen_package(self.input(0)))
        


class AutoNode_imp_load_compiled(rc.Node):
    title = 'load_compiled'
    doc = '''**DEPRECATED**'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='pathname'),
rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.load_compiled(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_imp_load_dynamic(rc.Node):
    title = 'load_dynamic'
    doc = '''**DEPRECATED**

        Load an extension module.
        '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.load_dynamic(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_imp_load_module(rc.Node):
    title = 'load_module'
    doc = '''**DEPRECATED**

    Load a module, given information returned by find_module().

    The module name must include the full package name, if any.

    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='file'),
rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='details'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.load_module(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_imp_load_package(rc.Node):
    title = 'load_package'
    doc = '''**DEPRECATED**'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.load_package(self.input(0), self.input(1)))
        


class AutoNode_imp_load_source(rc.Node):
    title = 'load_source'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='pathname'),
rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.load_source(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_imp_lock_held(rc.Node):
    title = 'lock_held'
    doc = '''Return True if the import lock is currently held, else False.

On platforms without threads, return False.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.lock_held())
        


class AutoNode_imp_new_module(rc.Node):
    title = 'new_module'
    doc = '''**DEPRECATED**

    Create a new module.

    The module is not entered into sys.modules.

    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.new_module(self.input(0)))
        


class AutoNode_imp_release_lock(rc.Node):
    title = 'release_lock'
    doc = '''Release the interpreter's import lock.

On platforms without threads, this function does nothing.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.release_lock())
        


class AutoNode_imp_reload(rc.Node):
    title = 'reload'
    doc = '''**DEPRECATED**

    Reload the module and return it.

    The module must have been successfully imported before.

    '''
    init_inputs = [
        rc.NodeInputBP(label='module'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.reload(self.input(0)))
        


class AutoNode_imp_source_from_cache(rc.Node):
    title = 'source_from_cache'
    doc = '''**DEPRECATED**

    Given the path to a .pyc. file, return the path to its .py file.

    The .pyc file does not need to exist; this simply returns the path to
    the .py file calculated to correspond to the .pyc file.  If path does
    not conform to PEP 3147 format, ValueError will be raised. If
    sys.implementation.cache_tag is None then NotImplementedError is raised.

    '''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imp.source_from_cache(self.input(0)))
        