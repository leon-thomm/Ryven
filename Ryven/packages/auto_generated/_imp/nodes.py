
from NENV import *

import _imp


class NodeBase(Node):
    pass


class AutoNode__imp__fix_co_filename(NodeBase):
    title = '_fix_co_filename'
    type_ = '_imp'
    doc = """Changes code.co_filename to specify the passed-in file path.

  code
    Code object to change.
  path
    File path to use."""
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp._fix_co_filename(self.input(0), self.input(1)))
        

class AutoNode__imp_acquire_lock(NodeBase):
    title = 'acquire_lock'
    type_ = '_imp'
    doc = """Acquires the interpreter's import lock for the current thread.

This lock should be used by import hooks to ensure thread-safety when importing
modules. On platforms without threads, this function does nothing."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.acquire_lock())
        

class AutoNode__imp_create_builtin(NodeBase):
    title = 'create_builtin'
    type_ = '_imp'
    doc = """Create an extension module."""
    init_inputs = [
        NodeInputBP(label='spec'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.create_builtin(self.input(0)))
        

class AutoNode__imp_exec_builtin(NodeBase):
    title = 'exec_builtin'
    type_ = '_imp'
    doc = """Initialize a built-in module."""
    init_inputs = [
        NodeInputBP(label='mod'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.exec_builtin(self.input(0)))
        

class AutoNode__imp_exec_dynamic(NodeBase):
    title = 'exec_dynamic'
    type_ = '_imp'
    doc = """Initialize an extension module."""
    init_inputs = [
        NodeInputBP(label='mod'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.exec_dynamic(self.input(0)))
        

class AutoNode__imp_extension_suffixes(NodeBase):
    title = 'extension_suffixes'
    type_ = '_imp'
    doc = """Returns the list of file suffixes used to identify extension modules."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.extension_suffixes())
        

class AutoNode__imp_get_frozen_object(NodeBase):
    title = 'get_frozen_object'
    type_ = '_imp'
    doc = """Create a code object for a frozen module."""
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.get_frozen_object(self.input(0)))
        

class AutoNode__imp_init_frozen(NodeBase):
    title = 'init_frozen'
    type_ = '_imp'
    doc = """Initializes a frozen module."""
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.init_frozen(self.input(0)))
        

class AutoNode__imp_is_builtin(NodeBase):
    title = 'is_builtin'
    type_ = '_imp'
    doc = """Returns True if the module name corresponds to a built-in module."""
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.is_builtin(self.input(0)))
        

class AutoNode__imp_is_frozen(NodeBase):
    title = 'is_frozen'
    type_ = '_imp'
    doc = """Returns True if the module name corresponds to a frozen module."""
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.is_frozen(self.input(0)))
        

class AutoNode__imp_is_frozen_package(NodeBase):
    title = 'is_frozen_package'
    type_ = '_imp'
    doc = """Returns True if the module name is of a frozen package."""
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.is_frozen_package(self.input(0)))
        

class AutoNode__imp_lock_held(NodeBase):
    title = 'lock_held'
    type_ = '_imp'
    doc = """Return True if the import lock is currently held, else False.

On platforms without threads, return False."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.lock_held())
        

class AutoNode__imp_release_lock(NodeBase):
    title = 'release_lock'
    type_ = '_imp'
    doc = """Release the interpreter's import lock.

On platforms without threads, this function does nothing."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.release_lock())
        

class AutoNode__imp_source_hash(NodeBase):
    title = 'source_hash'
    type_ = '_imp'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='key'),
        NodeInputBP(label='source'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.source_hash(self.input(0), self.input(1)))
        


export_nodes(
    AutoNode__imp__fix_co_filename,
    AutoNode__imp_acquire_lock,
    AutoNode__imp_create_builtin,
    AutoNode__imp_exec_builtin,
    AutoNode__imp_exec_dynamic,
    AutoNode__imp_extension_suffixes,
    AutoNode__imp_get_frozen_object,
    AutoNode__imp_init_frozen,
    AutoNode__imp_is_builtin,
    AutoNode__imp_is_frozen,
    AutoNode__imp_is_frozen_package,
    AutoNode__imp_lock_held,
    AutoNode__imp_release_lock,
    AutoNode__imp_source_hash,
)
