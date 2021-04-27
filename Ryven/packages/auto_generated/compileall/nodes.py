
from NENV import *

import compileall


class NodeBase(Node):
    pass


class _Compile_File_Tuple_Node(NodeBase):
    title = '_compile_file_tuple'
    type_ = 'compileall'
    doc = """Needs to be toplevel for ProcessPoolExecutor."""
    init_inputs = [
        NodeInputBP(label='file_and_dfile'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, compileall._compile_file_tuple(self.input(0)))
        

class _Walk_Dir_Node(NodeBase):
    title = '_walk_dir'
    type_ = 'compileall'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='dir'),
        NodeInputBP(label='ddir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='maxlevels', dtype=dtypes.Data(default=10, size='s')),
        NodeInputBP(label='quiet', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, compileall._walk_dir(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Compile_Dir_Node(NodeBase):
    title = 'compile_dir'
    type_ = 'compileall'
    doc = """Byte-compile all modules in the given directory tree.

    Arguments (only dir is required):

    dir:       the directory to byte-compile
    maxlevels: maximum recursion level (default 10)
    ddir:      the directory that will be prepended to the path to the
               file as it is compiled into each byte-code file.
    force:     if True, force compilation, even if timestamps are up-to-date
    quiet:     full output with False or 0, errors only with 1,
               no output with 2
    legacy:    if True, produce legacy pyc paths instead of PEP 3147 paths
    optimize:  optimization level or -1 for level of the interpreter
    workers:   maximum number of parallel workers
    invalidation_mode: how the up-to-dateness of the pyc will be checked
    """
    init_inputs = [
        NodeInputBP(label='dir'),
        NodeInputBP(label='maxlevels', dtype=dtypes.Data(default=10, size='s')),
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

    def update_event(self, input_called=-1):
        self.set_output_val(0, compileall.compile_dir(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7), self.input(8), self.input(9)))
        

class Compile_File_Node(NodeBase):
    title = 'compile_file'
    type_ = 'compileall'
    doc = """Byte-compile one file.

    Arguments (only fullname is required):

    fullname:  the file to byte-compile
    ddir:      if given, the directory name compiled in to the
               byte-code file.
    force:     if True, force compilation, even if timestamps are up-to-date
    quiet:     full output with False or 0, errors only with 1,
               no output with 2
    legacy:    if True, produce legacy pyc paths instead of PEP 3147 paths
    optimize:  optimization level or -1 for level of the interpreter
    invalidation_mode: how the up-to-dateness of the pyc will be checked
    """
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

    def update_event(self, input_called=-1):
        self.set_output_val(0, compileall.compile_file(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        

class Compile_Path_Node(NodeBase):
    title = 'compile_path'
    type_ = 'compileall'
    doc = """Byte-compile all module on sys.path.

    Arguments (all optional):

    skip_curdir: if true, skip current directory (default True)
    maxlevels:   max recursion level (default 0)
    force: as for compile_dir() (default False)
    quiet: as for compile_dir() (default 0)
    legacy: as for compile_dir() (default False)
    optimize: as for compile_dir() (default -1)
    invalidation_mode: as for compiler_dir()
    """
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

    def update_event(self, input_called=-1):
        self.set_output_val(0, compileall.compile_path(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        

class Main_Node(NodeBase):
    title = 'main'
    type_ = 'compileall'
    doc = """Script main program."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, compileall.main())
        


export_nodes(
    _Compile_File_Tuple_Node,
    _Walk_Dir_Node,
    Compile_Dir_Node,
    Compile_File_Node,
    Compile_Path_Node,
    Main_Node,
)
