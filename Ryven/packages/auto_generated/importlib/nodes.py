import ryvencore_qt as rc
import importlib


class AutoNode_importlib___import__(rc.Node):
    title = '__import__'
    doc = '''Import a module.

    The 'globals' argument is used to infer where the import is occurring from
    to handle relative imports. The 'locals' argument is ignored. The
    'fromlist' argument specifies what should exist as attributes on the module
    being imported (e.g. ``from module import <fromlist>``).  The 'level'
    argument represents the package location to import from in a relative
    import (e.g. ``from ..pkg import mod`` would have a 'level' of 2).

    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='globals'),
rc.NodeInputBP(label='locals'),
rc.NodeInputBP(label='fromlist'),
rc.NodeInputBP(label='level'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, importlib.__import__(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_importlib__pack_uint32(rc.Node):
    title = '_pack_uint32'
    doc = '''Convert a 32-bit integer to little-endian.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, importlib._pack_uint32(self.input(0)))
        


class AutoNode_importlib__unpack_uint32(rc.Node):
    title = '_unpack_uint32'
    doc = '''Convert 4 bytes in little-endian to an integer.'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, importlib._unpack_uint32(self.input(0)))
        


class AutoNode_importlib_find_loader(rc.Node):
    title = 'find_loader'
    doc = '''Return the loader for the specified module.

    This is a backward-compatible wrapper around find_spec().

    This function is deprecated in favor of importlib.util.find_spec().

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
        self.set_output_val(0, importlib.find_loader(self.input(0), self.input(1)))
        


class AutoNode_importlib_import_module(rc.Node):
    title = 'import_module'
    doc = '''Import a module.

    The 'package' argument is required when performing a relative import. It
    specifies the package to use as the anchor point from which to resolve the
    relative import to an absolute import.

    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='package'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, importlib.import_module(self.input(0), self.input(1)))
        


class AutoNode_importlib_invalidate_caches(rc.Node):
    title = 'invalidate_caches'
    doc = '''Call the invalidate_caches() method on all meta path finders stored in
    sys.meta_path (where implemented).'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, importlib.invalidate_caches())
        


class AutoNode_importlib_reload(rc.Node):
    title = 'reload'
    doc = '''Reload the module and return it.

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
        self.set_output_val(0, importlib.reload(self.input(0)))
        