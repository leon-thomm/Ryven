
from ryven.NENV import *

import imp


class NodeBase(Node):
    pass


class _Builtin_From_Name_Node(NodeBase):
    """
    """
    
    title = '_builtin_from_name'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp._builtin_from_name(self.input(0)))
        

class _Exec_Node(NodeBase):
    """
    Execute the spec's specified module in an existing module's namespace."""
    
    title = '_exec'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='spec'),
        NodeInputBP(label='module'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp._exec(self.input(0), self.input(1)))
        

class _Fix_Co_Filename_Node(NodeBase):
    """
    Changes code.co_filename to specify the passed-in file path.

  code
    Code object to change.
  path
    File path to use."""
    
    title = '_fix_co_filename'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp._fix_co_filename(self.input(0), self.input(1)))
        

class _Load_Node(NodeBase):
    """
    Return a new module object, loaded by the spec's loader.

    The module is not added to its parent.

    If a module is already in sys.modules, that existing module gets
    clobbered.

    """
    
    title = '_load'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='spec'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp._load(self.input(0)))
        

class Acquire_Lock_Node(NodeBase):
    """
    Acquires the interpreter's import lock for the current thread.

This lock should be used by import hooks to ensure thread-safety when importing
modules. On platforms without threads, this function does nothing."""
    
    title = 'acquire_lock'
    type_ = 'imp'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.acquire_lock())
        

class Cache_From_Source_Node(NodeBase):
    """
    **DEPRECATED**

    Given the path to a .py file, return the path to its .pyc file.

    The .py file does not need to exist; this simply returns the path to the
    .pyc file calculated as if the .py file were imported.

    If debug_override is not None, then it must be a boolean and is used in
    place of sys.flags.optimize.

    If sys.implementation.cache_tag is None then NotImplementedError is raised.

    """
    
    title = 'cache_from_source'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='debug_override', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.cache_from_source(self.input(0), self.input(1)))
        

class Find_Module_Node(NodeBase):
    """
    **DEPRECATED**

    Search for a module.

    If path is omitted or None, search for a built-in, frozen or special
    module and continue search in sys.path. The module name cannot
    contain '.'; to search for a submodule of a package, pass the
    submodule name and the package's __path__.

    """
    
    title = 'find_module'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='path', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.find_module(self.input(0), self.input(1)))
        

class Get_Frozen_Object_Node(NodeBase):
    """
    Create a code object for a frozen module."""
    
    title = 'get_frozen_object'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.get_frozen_object(self.input(0)))
        

class Get_Magic_Node(NodeBase):
    """
    **DEPRECATED**

    Return the magic number for .pyc files.
    """
    
    title = 'get_magic'
    type_ = 'imp'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.get_magic())
        

class Get_Suffixes_Node(NodeBase):
    """
    **DEPRECATED**"""
    
    title = 'get_suffixes'
    type_ = 'imp'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.get_suffixes())
        

class Get_Tag_Node(NodeBase):
    """
    Return the magic tag for .pyc files."""
    
    title = 'get_tag'
    type_ = 'imp'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.get_tag())
        

class Init_Builtin_Node(NodeBase):
    """
    **DEPRECATED**

    Load and return a built-in module by name, or None is such module doesn't
    exist
    """
    
    title = 'init_builtin'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.init_builtin(self.input(0)))
        

class Init_Frozen_Node(NodeBase):
    """
    Initializes a frozen module."""
    
    title = 'init_frozen'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.init_frozen(self.input(0)))
        

class Is_Builtin_Node(NodeBase):
    """
    Returns True if the module name corresponds to a built-in module."""
    
    title = 'is_builtin'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.is_builtin(self.input(0)))
        

class Is_Frozen_Node(NodeBase):
    """
    Returns True if the module name corresponds to a frozen module."""
    
    title = 'is_frozen'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.is_frozen(self.input(0)))
        

class Is_Frozen_Package_Node(NodeBase):
    """
    Returns True if the module name is of a frozen package."""
    
    title = 'is_frozen_package'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.is_frozen_package(self.input(0)))
        

class Load_Compiled_Node(NodeBase):
    """
    **DEPRECATED**"""
    
    title = 'load_compiled'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='pathname'),
        NodeInputBP(label='file', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.load_compiled(self.input(0), self.input(1), self.input(2)))
        

class Load_Dynamic_Node(NodeBase):
    """
    **DEPRECATED**

        Load an extension module.
        """
    
    title = 'load_dynamic'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='path'),
        NodeInputBP(label='file', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.load_dynamic(self.input(0), self.input(1), self.input(2)))
        

class Load_Module_Node(NodeBase):
    """
    **DEPRECATED**

    Load a module, given information returned by find_module().

    The module name must include the full package name, if any.

    """
    
    title = 'load_module'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='file'),
        NodeInputBP(label='filename'),
        NodeInputBP(label='details'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.load_module(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Load_Package_Node(NodeBase):
    """
    **DEPRECATED**"""
    
    title = 'load_package'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.load_package(self.input(0), self.input(1)))
        

class Load_Source_Node(NodeBase):
    """
    """
    
    title = 'load_source'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='pathname'),
        NodeInputBP(label='file', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.load_source(self.input(0), self.input(1), self.input(2)))
        

class Lock_Held_Node(NodeBase):
    """
    Return True if the import lock is currently held, else False.

On platforms without threads, return False."""
    
    title = 'lock_held'
    type_ = 'imp'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.lock_held())
        

class New_Module_Node(NodeBase):
    """
    **DEPRECATED**

    Create a new module.

    The module is not entered into sys.modules.

    """
    
    title = 'new_module'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.new_module(self.input(0)))
        

class Release_Lock_Node(NodeBase):
    """
    Release the interpreter's import lock.

On platforms without threads, this function does nothing."""
    
    title = 'release_lock'
    type_ = 'imp'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.release_lock())
        

class Reload_Node(NodeBase):
    """
    **DEPRECATED**

    Reload the module and return it.

    The module must have been successfully imported before.

    """
    
    title = 'reload'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='module'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.reload(self.input(0)))
        

class Source_From_Cache_Node(NodeBase):
    """
    **DEPRECATED**

    Given the path to a .pyc. file, return the path to its .py file.

    The .pyc file does not need to exist; this simply returns the path to
    the .py file calculated to correspond to the .pyc file.  If path does
    not conform to PEP 3147 format, ValueError will be raised. If
    sys.implementation.cache_tag is None then NotImplementedError is raised.

    """
    
    title = 'source_from_cache'
    type_ = 'imp'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, imp.source_from_cache(self.input(0)))
        


export_nodes(
    _Builtin_From_Name_Node,
    _Exec_Node,
    _Fix_Co_Filename_Node,
    _Load_Node,
    Acquire_Lock_Node,
    Cache_From_Source_Node,
    Find_Module_Node,
    Get_Frozen_Object_Node,
    Get_Magic_Node,
    Get_Suffixes_Node,
    Get_Tag_Node,
    Init_Builtin_Node,
    Init_Frozen_Node,
    Is_Builtin_Node,
    Is_Frozen_Node,
    Is_Frozen_Package_Node,
    Load_Compiled_Node,
    Load_Dynamic_Node,
    Load_Module_Node,
    Load_Package_Node,
    Load_Source_Node,
    Lock_Held_Node,
    New_Module_Node,
    Release_Lock_Node,
    Reload_Node,
    Source_From_Cache_Node,
)
