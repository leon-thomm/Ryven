import ryvencore_qt as rc
import py_compile


class AutoNode_py_compile__get_default_invalidation_mode(rc.Node):
    title = '_get_default_invalidation_mode'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, py_compile._get_default_invalidation_mode())
        


class AutoNode_py_compile_compile(rc.Node):
    title = 'compile'
    description = '''Byte-compile one Python source file to Python bytecode.

    :param file: The source file name.
    :param cfile: The target byte compiled file name.  When not given, this
        defaults to the PEP 3147/PEP 488 location.
    :param dfile: Purported file name, i.e. the file name that shows up in
        error messages.  Defaults to the source file name.
    :param doraise: Flag indicating whether or not an exception should be
        raised when a compile error is found.  If an exception occurs and this
        flag is set to False, a string indicating the nature of the exception
        will be printed, and the function will return to the caller. If an
        exception occurs and this flag is set to True, a PyCompileError
        exception will be raised.
    :param optimize: The optimization level for the compiler.  Valid values
        are -1, 0, 1 and 2.  A value of -1 means to use the optimization
        level of the current interpreter, as given by -O command line options.
    :param invalidation_mode:
    :param quiet: Return full output with False or 0, errors only with 1,
        and no output with 2.

    :return: Path to the resulting byte compiled file.

    Note that it isn't necessary to byte-compile Python modules for
    execution efficiency -- Python itself byte-compiles a module when
    it is loaded, and if it can, writes out the bytecode to the
    corresponding .pyc file.

    However, if a Python installation is shared between users, it is a
    good idea to byte-compile all modules upon installation, since
    other users may not be able to write in the source directories,
    and thus they won't be able to write the .pyc file, and then
    they would be byte-compiling every module each time it is loaded.
    This can slow down program start-up considerably.

    See compileall.py for a script/module that uses this module to
    byte-compile all installed files (or all files in selected
    directories).

    Do note that FileExistsError is raised if cfile ends up pointing at a
    non-regular file or symlink. Because the compilation uses a file renaming,
    the resulting file would be regular and thus not the same type of file as
    it was previously.
    '''
    init_inputs = [
        rc.NodeInputBP(label='file'),
rc.NodeInputBP(label='cfile'),
rc.NodeInputBP(label='dfile'),
rc.NodeInputBP(label='doraise'),
rc.NodeInputBP(label='optimize'),
rc.NodeInputBP(label='invalidation_mode'),
rc.NodeInputBP(label='quiet'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, py_compile.compile(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        


class AutoNode_py_compile_main(rc.Node):
    title = 'main'
    description = '''Compile several source files.

    The files named in 'args' (or on the command line, if 'args' is
    not specified) are compiled and the resulting bytecode is cached
    in the normal manner.  This function does not search a directory
    structure to locate source files; it only compiles files named
    explicitly.  If '-' is the only parameter in args, the list of
    files is taken from standard input.

    '''
    init_inputs = [
        rc.NodeInputBP(label='args'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, py_compile.main(self.input(0)))
        