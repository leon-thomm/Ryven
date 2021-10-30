
from ryven.NENV import *

import compileall


class NodeBase(Node):
    pass


class _Walk_Dir_Node(NodeBase):
    """
    """
    
    title = '_walk_dir'
    type_ = 'compileall'
    init_inputs = [
        NodeInputBP(label='dir'),
        NodeInputBP(label='maxlevels'),
        NodeInputBP(label='quiet', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, compileall._walk_dir(self.input(0), self.input(1), self.input(2)))
        

class Compile_Dir_Node(NodeBase):
    """
    Byte-compile all modules in the given directory tree.

    Arguments (only dir is required):

    dir:       the directory to byte-compile
    maxlevels: maximum recursion level (default `sys.getrecursionlimit()`)
    ddir:      the directory that will be prepended to the path to the
               file as it is compiled into each byte-code file.
    force:     if True, force compilation, even if timestamps are up-to-date
    quiet:     full output with False or 0, errors only with 1,
               no output with 2
    legacy:    if True, produce legacy pyc paths instead of PEP 3147 paths
    optimize:  int or list of optimization levels or -1 for level of
               the interpreter. Multiple levels leads to multiple compiled
               files each with one optimization level.
    workers:   maximum number of parallel workers
    invalidation_mode: how the up-to-dateness of the pyc will be checked
    stripdir:  part of path to left-strip from source file path
    prependdir: path to prepend to beginning of original file path, applied
               after stripdir
    limit_sl_dest: ignore symlinks if they are pointing outside of
                   the defined path
    hardlink_dupes: hardlink duplicated pyc files
    """
    
    title = 'compile_dir'
    type_ = 'compileall'
    init_inputs = [
        NodeInputBP(label='dir'),
        NodeInputBP(label='maxlevels', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='ddir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='force', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='rx', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='quiet', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='legacy', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='optimize', dtype=dtypes.Data(default=-1, size='s')),
        NodeInputBP(label='workers', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='invalidation_mode', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, compileall.compile_dir(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7), self.input(8), self.input(9)))
        

class Compile_File_Node(NodeBase):
    """
    Byte-compile one file.

    Arguments (only fullname is required):

    fullname:  the file to byte-compile
    ddir:      if given, the directory name compiled in to the
               byte-code file.
    force:     if True, force compilation, even if timestamps are up-to-date
    quiet:     full output with False or 0, errors only with 1,
               no output with 2
    legacy:    if True, produce legacy pyc paths instead of PEP 3147 paths
    optimize:  int or list of optimization levels or -1 for level of
               the interpreter. Multiple levels leads to multiple compiled
               files each with one optimization level.
    invalidation_mode: how the up-to-dateness of the pyc will be checked
    stripdir:  part of path to left-strip from source file path
    prependdir: path to prepend to beginning of original file path, applied
               after stripdir
    limit_sl_dest: ignore symlinks if they are pointing outside of
                   the defined path.
    hardlink_dupes: hardlink duplicated pyc files
    """
    
    title = 'compile_file'
    type_ = 'compileall'
    init_inputs = [
        NodeInputBP(label='fullname'),
        NodeInputBP(label='ddir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='force', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='rx', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='quiet', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='legacy', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='optimize', dtype=dtypes.Data(default=-1, size='s')),
        NodeInputBP(label='invalidation_mode', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, compileall.compile_file(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        

class Compile_Path_Node(NodeBase):
    """
    Byte-compile all module on sys.path.

    Arguments (all optional):

    skip_curdir: if true, skip current directory (default True)
    maxlevels:   max recursion level (default 0)
    force: as for compile_dir() (default False)
    quiet: as for compile_dir() (default 0)
    legacy: as for compile_dir() (default False)
    optimize: as for compile_dir() (default -1)
    invalidation_mode: as for compiler_dir()
    """
    
    title = 'compile_path'
    type_ = 'compileall'
    init_inputs = [
        NodeInputBP(label='skip_curdir', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='maxlevels', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='force', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='quiet', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='legacy', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='optimize', dtype=dtypes.Data(default=-1, size='s')),
        NodeInputBP(label='invalidation_mode', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, compileall.compile_path(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        

class Main_Node(NodeBase):
    """
    Script main program."""
    
    title = 'main'
    type_ = 'compileall'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, compileall.main())
        


export_nodes(
    _Walk_Dir_Node,
    Compile_Dir_Node,
    Compile_File_Node,
    Compile_Path_Node,
    Main_Node,
)
