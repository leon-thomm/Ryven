import ryvencore_qt as rc
import os


class AutoNode_os__check_methods(rc.Node):
    title = '_check_methods'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='C'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os._check_methods(self.input(0)))
        


class AutoNode_os__execvpe(rc.Node):
    title = '_execvpe'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='file'),
rc.NodeInputBP(label='args'),
rc.NodeInputBP(label='env'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os._execvpe(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_os__exists(rc.Node):
    title = '_exists'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os._exists(self.input(0)))
        


class AutoNode_os__exit(rc.Node):
    title = '_exit'
    doc = '''Exit to the system with specified status, without normal exit processing.'''
    init_inputs = [
        rc.NodeInputBP(label='status'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os._exit(self.input(0)))
        


class AutoNode_os__fspath(rc.Node):
    title = '_fspath'
    doc = '''Return the path representation of a path-like object.

    If str or bytes is passed in, it is returned unchanged. Otherwise the
    os.PathLike interface is used to get the path representation. If the
    path representation is not str or bytes, TypeError is raised. If the
    provided path is not str, bytes, or os.PathLike, TypeError is raised.
    '''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os._fspath(self.input(0)))
        


class AutoNode_os__get_exports_list(rc.Node):
    title = '_get_exports_list'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='module'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os._get_exports_list(self.input(0)))
        


class AutoNode_os__putenv(rc.Node):
    title = '_putenv'
    doc = '''Change or add an environment variable.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os._putenv(self.input(0), self.input(1)))
        


class AutoNode_os__unsetenv(rc.Node):
    title = '_unsetenv'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os._unsetenv(self.input(0)))
        


class AutoNode_os_abort(rc.Node):
    title = 'abort'
    doc = '''Abort the interpreter immediately.

This function 'dumps core' or otherwise fails in the hardest way possible
on the hosting operating system.  This function never returns.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.abort())
        


class AutoNode_os_access(rc.Node):
    title = 'access'
    doc = '''Use the real uid/gid to test for access to a path.

  path
    Path to be tested; can be string, bytes, or a path-like object.
  mode
    Operating-system mode bitfield.  Can be F_OK to test existence,
    or the inclusive-OR of R_OK, W_OK, and X_OK.
  dir_fd
    If not None, it should be a file descriptor open to a directory,
    and path should be relative; path will then be relative to that
    directory.
  effective_ids
    If True, access will use the effective uid/gid instead of
    the real uid/gid.
  follow_symlinks
    If False, and the last element of the path is a symbolic link,
    access will examine the symbolic link itself instead of the file
    the link points to.

dir_fd, effective_ids, and follow_symlinks may not be implemented
  on your platform.  If they are unavailable, using them will raise a
  NotImplementedError.

Note that most operations will use the effective uid/gid, therefore this
  routine can be used in a suid/sgid environment to test if the invoking user
  has the specified access to the path.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='mode'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.access(self.input(0), self.input(1)))
        


class AutoNode_os_add_dll_directory(rc.Node):
    title = 'add_dll_directory'
    doc = '''Add a path to the DLL search path.

        This search path is used when resolving dependencies for imported
        extension modules (the module itself is resolved through sys.path),
        and also by ctypes.

        Remove the directory by calling close() on the returned object or
        using it in a with statement.
        '''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.add_dll_directory(self.input(0)))
        


class AutoNode_os_chdir(rc.Node):
    title = 'chdir'
    doc = '''Change the current working directory to the specified path.

path may always be specified as a string.
On some platforms, path may also be specified as an open file descriptor.
  If this functionality is unavailable, using it raises an exception.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.chdir(self.input(0)))
        


class AutoNode_os_chmod(rc.Node):
    title = 'chmod'
    doc = '''Change the access permissions of a file.

  path
    Path to be modified.  May always be specified as a str, bytes, or a path-like object.
    On some platforms, path may also be specified as an open file descriptor.
    If this functionality is unavailable, using it raises an exception.
  mode
    Operating-system mode bitfield.
  dir_fd
    If not None, it should be a file descriptor open to a directory,
    and path should be relative; path will then be relative to that
    directory.
  follow_symlinks
    If False, and the last element of the path is a symbolic link,
    chmod will modify the symbolic link itself instead of the file
    the link points to.

It is an error to use dir_fd or follow_symlinks when specifying path as
  an open file descriptor.
dir_fd and follow_symlinks may not be implemented on your platform.
  If they are unavailable, using them will raise a NotImplementedError.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='mode'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.chmod(self.input(0), self.input(1)))
        


class AutoNode_os_close(rc.Node):
    title = 'close'
    doc = '''Close a file descriptor.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.close(self.input(0)))
        


class AutoNode_os_closerange(rc.Node):
    title = 'closerange'
    doc = '''Closes all file descriptors in [fd_low, fd_high), ignoring errors.'''
    init_inputs = [
        rc.NodeInputBP(label='fd_low'),
rc.NodeInputBP(label='fd_high'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.closerange(self.input(0), self.input(1)))
        


class AutoNode_os_cpu_count(rc.Node):
    title = 'cpu_count'
    doc = '''Return the number of CPUs in the system; return None if indeterminable.

This number is not equivalent to the number of CPUs the current process can
use.  The number of usable CPUs can be obtained with
``len(os.sched_getaffinity(0))``'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.cpu_count())
        


class AutoNode_os_device_encoding(rc.Node):
    title = 'device_encoding'
    doc = '''Return a string describing the encoding of a terminal's file descriptor.

The file descriptor must be attached to a terminal.
If the device is not a terminal, return None.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.device_encoding(self.input(0)))
        


class AutoNode_os_dup(rc.Node):
    title = 'dup'
    doc = '''Return a duplicate of a file descriptor.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.dup(self.input(0)))
        


class AutoNode_os_dup2(rc.Node):
    title = 'dup2'
    doc = '''Duplicate file descriptor.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
rc.NodeInputBP(label='fd2'),
rc.NodeInputBP(label='inheritable'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.dup2(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_os_execl(rc.Node):
    title = 'execl'
    doc = '''execl(file, *args)

    Execute the executable file with argument list args, replacing the
    current process. '''
    init_inputs = [
        rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.execl(self.input(0)))
        


class AutoNode_os_execle(rc.Node):
    title = 'execle'
    doc = '''execle(file, *args, env)

    Execute the executable file with argument list args and
    environment env, replacing the current process. '''
    init_inputs = [
        rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.execle(self.input(0)))
        


class AutoNode_os_execlp(rc.Node):
    title = 'execlp'
    doc = '''execlp(file, *args)

    Execute the executable file (which is searched for along $PATH)
    with argument list args, replacing the current process. '''
    init_inputs = [
        rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.execlp(self.input(0)))
        


class AutoNode_os_execlpe(rc.Node):
    title = 'execlpe'
    doc = '''execlpe(file, *args, env)

    Execute the executable file (which is searched for along $PATH)
    with argument list args and environment env, replacing the current
    process. '''
    init_inputs = [
        rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.execlpe(self.input(0)))
        


class AutoNode_os_execv(rc.Node):
    title = 'execv'
    doc = '''Execute an executable path with arguments, replacing current process.

  path
    Path of executable file.
  argv
    Tuple or list of strings.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='argv'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.execv(self.input(0), self.input(1)))
        


class AutoNode_os_execve(rc.Node):
    title = 'execve'
    doc = '''Execute an executable path with arguments, replacing current process.

  path
    Path of executable file.
  argv
    Tuple or list of strings.
  env
    Dictionary of strings mapping to strings.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='argv'),
rc.NodeInputBP(label='env'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.execve(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_os_execvp(rc.Node):
    title = 'execvp'
    doc = '''execvp(file, args)

    Execute the executable file (which is searched for along $PATH)
    with argument list args, replacing the current process.
    args may be a list or tuple of strings. '''
    init_inputs = [
        rc.NodeInputBP(label='file'),
rc.NodeInputBP(label='args'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.execvp(self.input(0), self.input(1)))
        


class AutoNode_os_execvpe(rc.Node):
    title = 'execvpe'
    doc = '''execvpe(file, args, env)

    Execute the executable file (which is searched for along $PATH)
    with argument list args and environment env, replacing the
    current process.
    args may be a list or tuple of strings. '''
    init_inputs = [
        rc.NodeInputBP(label='file'),
rc.NodeInputBP(label='args'),
rc.NodeInputBP(label='env'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.execvpe(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_os_fdopen(rc.Node):
    title = 'fdopen'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.fdopen(self.input(0)))
        


class AutoNode_os_fsdecode(rc.Node):
    title = 'fsdecode'
    doc = '''Decode filename (an os.PathLike, bytes, or str) from the filesystem
        encoding with 'surrogateescape' error handler, return str unchanged. On
        Windows, use 'strict' error handler if the file system encoding is
        'mbcs' (which is the default encoding).
        '''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.fsdecode(self.input(0)))
        


class AutoNode_os_fsencode(rc.Node):
    title = 'fsencode'
    doc = '''Encode filename (an os.PathLike, bytes, or str) to the filesystem
        encoding with 'surrogateescape' error handler, return bytes unchanged.
        On Windows, use 'strict' error handler if the file system encoding is
        'mbcs' (which is the default encoding).
        '''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.fsencode(self.input(0)))
        


class AutoNode_os_fspath(rc.Node):
    title = 'fspath'
    doc = '''Return the file system path representation of the object.

If the object is str or bytes, then allow it to pass through as-is. If the
object defines __fspath__(), then return the result of that method. All other
types raise a TypeError.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.fspath(self.input(0)))
        


class AutoNode_os_fstat(rc.Node):
    title = 'fstat'
    doc = '''Perform a stat system call on the given file descriptor.

Like stat(), but for an open file descriptor.
Equivalent to os.stat(fd).'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.fstat(self.input(0)))
        


class AutoNode_os_fsync(rc.Node):
    title = 'fsync'
    doc = '''Force write of fd to disk.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.fsync(self.input(0)))
        


class AutoNode_os_ftruncate(rc.Node):
    title = 'ftruncate'
    doc = '''Truncate a file, specified by file descriptor, to a specific length.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
rc.NodeInputBP(label='length'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.ftruncate(self.input(0), self.input(1)))
        


class AutoNode_os_get_exec_path(rc.Node):
    title = 'get_exec_path'
    doc = '''Returns the sequence of directories that will be searched for the
    named executable (similar to a shell) when launching a process.

    *env* must be an environment variable dict or None.  If *env* is None,
    os.environ will be used.
    '''
    init_inputs = [
        rc.NodeInputBP(label='env'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.get_exec_path(self.input(0)))
        


class AutoNode_os_get_handle_inheritable(rc.Node):
    title = 'get_handle_inheritable'
    doc = '''Get the close-on-exe flag of the specified file descriptor.'''
    init_inputs = [
        rc.NodeInputBP(label='handle'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.get_handle_inheritable(self.input(0)))
        


class AutoNode_os_get_inheritable(rc.Node):
    title = 'get_inheritable'
    doc = '''Get the close-on-exe flag of the specified file descriptor.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.get_inheritable(self.input(0)))
        


class AutoNode_os_getcwd(rc.Node):
    title = 'getcwd'
    doc = '''Return a unicode string representing the current working directory.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.getcwd())
        


class AutoNode_os_getcwdb(rc.Node):
    title = 'getcwdb'
    doc = '''Return a bytes string representing the current working directory.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.getcwdb())
        


class AutoNode_os_getenv(rc.Node):
    title = 'getenv'
    doc = '''Get an environment variable, return None if it doesn't exist.
    The optional second argument can specify an alternate default.
    key, default and the result are str.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='default'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.getenv(self.input(0), self.input(1)))
        


class AutoNode_os_getlogin(rc.Node):
    title = 'getlogin'
    doc = '''Return the actual login name.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.getlogin())
        


class AutoNode_os_getpid(rc.Node):
    title = 'getpid'
    doc = '''Return the current process id.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.getpid())
        


class AutoNode_os_getppid(rc.Node):
    title = 'getppid'
    doc = '''Return the parent's process id.

If the parent process has already exited, Windows machines will still
return its id; others systems will return the id of the 'init' process (1).'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.getppid())
        


class AutoNode_os_isatty(rc.Node):
    title = 'isatty'
    doc = '''Return True if the fd is connected to a terminal.

Return True if the file descriptor is an open file descriptor
connected to the slave end of a terminal.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.isatty(self.input(0)))
        


class AutoNode_os_kill(rc.Node):
    title = 'kill'
    doc = '''Kill a process with a signal.'''
    init_inputs = [
        rc.NodeInputBP(label='pid'),
rc.NodeInputBP(label='signal'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.kill(self.input(0), self.input(1)))
        


class AutoNode_os_link(rc.Node):
    title = 'link'
    doc = '''Create a hard link to a file.

If either src_dir_fd or dst_dir_fd is not None, it should be a file
  descriptor open to a directory, and the respective path string (src or dst)
  should be relative; the path will then be relative to that directory.
If follow_symlinks is False, and the last element of src is a symbolic
  link, link will create a link to the symbolic link itself instead of the
  file the link points to.
src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your
  platform.  If they are unavailable, using them will raise a
  NotImplementedError.'''
    init_inputs = [
        rc.NodeInputBP(label='src'),
rc.NodeInputBP(label='dst'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.link(self.input(0), self.input(1)))
        


class AutoNode_os_listdir(rc.Node):
    title = 'listdir'
    doc = '''Return a list containing the names of the files in the directory.

path can be specified as either str, bytes, or a path-like object.  If path is bytes,
  the filenames returned will also be bytes; in all other circumstances
  the filenames returned will be str.
If path is None, uses the path='.'.
On some platforms, path may also be specified as an open file descriptor;\
  the file descriptor must refer to a directory.
  If this functionality is unavailable, using it raises NotImplementedError.

The list is in arbitrary order.  It does not include the special
entries '.' and '..' even if they are present in the directory.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.listdir(self.input(0)))
        


class AutoNode_os_lseek(rc.Node):
    title = 'lseek'
    doc = '''Set the position of a file descriptor.  Return the new position.

Return the new cursor position in number of bytes
relative to the beginning of the file.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
rc.NodeInputBP(label='position'),
rc.NodeInputBP(label='how'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.lseek(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_os_lstat(rc.Node):
    title = 'lstat'
    doc = '''Perform a stat system call on the given path, without following symbolic links.

Like stat(), but do not follow symbolic links.
Equivalent to stat(path, follow_symlinks=False).'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.lstat(self.input(0)))
        


class AutoNode_os_makedirs(rc.Node):
    title = 'makedirs'
    doc = '''makedirs(name [, mode=0o777][, exist_ok=False])

    Super-mkdir; create a leaf directory and all intermediate ones.  Works like
    mkdir, except that any intermediate path segment (not just the rightmost)
    will be created if it does not exist. If the target directory already
    exists, raise an OSError if exist_ok is False. Otherwise no exception is
    raised.  This is recursive.

    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='mode'),
rc.NodeInputBP(label='exist_ok'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.makedirs(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_os_mkdir(rc.Node):
    title = 'mkdir'
    doc = '''Create a directory.

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError.

The mode argument is ignored on Windows.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='mode'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.mkdir(self.input(0), self.input(1)))
        


class AutoNode_os_open(rc.Node):
    title = 'open'
    doc = '''Open a file for low level IO.  Returns a file descriptor (integer).

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='flags'),
rc.NodeInputBP(label='mode'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.open(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_os_pipe(rc.Node):
    title = 'pipe'
    doc = '''Create a pipe.

Returns a tuple of two file descriptors:
  (read_fd, write_fd)'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.pipe())
        


class AutoNode_os_popen(rc.Node):
    title = 'popen'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='cmd'),
rc.NodeInputBP(label='mode'),
rc.NodeInputBP(label='buffering'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.popen(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_os_putenv(rc.Node):
    title = 'putenv'
    doc = '''Change or add an environment variable.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.putenv(self.input(0), self.input(1)))
        


class AutoNode_os_read(rc.Node):
    title = 'read'
    doc = '''Read from a file descriptor.  Returns a bytes object.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
rc.NodeInputBP(label='length'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.read(self.input(0), self.input(1)))
        


class AutoNode_os_readlink(rc.Node):
    title = 'readlink'
    doc = '''Return a string representing the path to which the symbolic link points.

If dir_fd is not None, it should be a file descriptor open to a directory,
and path should be relative; path will then be relative to that directory.

dir_fd may not be implemented on your platform.  If it is unavailable,
using it will raise a NotImplementedError.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.readlink(self.input(0)))
        


class AutoNode_os_remove(rc.Node):
    title = 'remove'
    doc = '''Remove a file (same as unlink()).

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.remove(self.input(0)))
        


class AutoNode_os_removedirs(rc.Node):
    title = 'removedirs'
    doc = '''removedirs(name)

    Super-rmdir; remove a leaf directory and all empty intermediate
    ones.  Works like rmdir except that, if the leaf directory is
    successfully removed, directories corresponding to rightmost path
    segments will be pruned away until either the whole path is
    consumed or an error occurs.  Errors during this latter phase are
    ignored -- they generally mean that a directory was not empty.

    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.removedirs(self.input(0)))
        


class AutoNode_os_rename(rc.Node):
    title = 'rename'
    doc = '''Rename a file or directory.

If either src_dir_fd or dst_dir_fd is not None, it should be a file
  descriptor open to a directory, and the respective path string (src or dst)
  should be relative; the path will then be relative to that directory.
src_dir_fd and dst_dir_fd, may not be implemented on your platform.
  If they are unavailable, using them will raise a NotImplementedError.'''
    init_inputs = [
        rc.NodeInputBP(label='src'),
rc.NodeInputBP(label='dst'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.rename(self.input(0), self.input(1)))
        


class AutoNode_os_renames(rc.Node):
    title = 'renames'
    doc = '''renames(old, new)

    Super-rename; create directories as necessary and delete any left
    empty.  Works like rename, except creation of any intermediate
    directories needed to make the new pathname good is attempted
    first.  After the rename, directories corresponding to rightmost
    path segments of the old name will be pruned until either the
    whole path is consumed or a nonempty directory is found.

    Note: this function can fail with the new directory structure made
    if you lack permissions needed to unlink the leaf directory or
    file.

    '''
    init_inputs = [
        rc.NodeInputBP(label='old'),
rc.NodeInputBP(label='new'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.renames(self.input(0), self.input(1)))
        


class AutoNode_os_replace(rc.Node):
    title = 'replace'
    doc = '''Rename a file or directory, overwriting the destination.

If either src_dir_fd or dst_dir_fd is not None, it should be a file
  descriptor open to a directory, and the respective path string (src or dst)
  should be relative; the path will then be relative to that directory.
src_dir_fd and dst_dir_fd, may not be implemented on your platform.
  If they are unavailable, using them will raise a NotImplementedError.'''
    init_inputs = [
        rc.NodeInputBP(label='src'),
rc.NodeInputBP(label='dst'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.replace(self.input(0), self.input(1)))
        


class AutoNode_os_rmdir(rc.Node):
    title = 'rmdir'
    doc = '''Remove a directory.

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.rmdir(self.input(0)))
        


class AutoNode_os_scandir(rc.Node):
    title = 'scandir'
    doc = '''Return an iterator of DirEntry objects for given path.

path can be specified as either str, bytes, or a path-like object.  If path
is bytes, the names of yielded DirEntry objects will also be bytes; in
all other circumstances they will be str.

If path is None, uses the path='.'.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.scandir(self.input(0)))
        


class AutoNode_os_set_handle_inheritable(rc.Node):
    title = 'set_handle_inheritable'
    doc = '''Set the inheritable flag of the specified handle.'''
    init_inputs = [
        rc.NodeInputBP(label='handle'),
rc.NodeInputBP(label='inheritable'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.set_handle_inheritable(self.input(0), self.input(1)))
        


class AutoNode_os_set_inheritable(rc.Node):
    title = 'set_inheritable'
    doc = '''Set the inheritable flag of the specified file descriptor.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
rc.NodeInputBP(label='inheritable'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.set_inheritable(self.input(0), self.input(1)))
        


class AutoNode_os_spawnl(rc.Node):
    title = 'spawnl'
    doc = '''spawnl(mode, file, *args) -> integer

Execute file with arguments from args in a subprocess.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. '''
    init_inputs = [
        rc.NodeInputBP(label='mode'),
rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.spawnl(self.input(0), self.input(1)))
        


class AutoNode_os_spawnle(rc.Node):
    title = 'spawnle'
    doc = '''spawnle(mode, file, *args, env) -> integer

Execute file with arguments from args in a subprocess with the
supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. '''
    init_inputs = [
        rc.NodeInputBP(label='mode'),
rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.spawnle(self.input(0), self.input(1)))
        


class AutoNode_os_spawnv(rc.Node):
    title = 'spawnv'
    doc = '''Execute the program specified by path in a new process.

  mode
    Mode of process creation.
  path
    Path of executable file.
  argv
    Tuple or list of strings.'''
    init_inputs = [
        rc.NodeInputBP(label='mode'),
rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='argv'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.spawnv(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_os_spawnve(rc.Node):
    title = 'spawnve'
    doc = '''Execute the program specified by path in a new process.

  mode
    Mode of process creation.
  path
    Path of executable file.
  argv
    Tuple or list of strings.
  env
    Dictionary of strings mapping to strings.'''
    init_inputs = [
        rc.NodeInputBP(label='mode'),
rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='argv'),
rc.NodeInputBP(label='env'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.spawnve(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_os_stat(rc.Node):
    title = 'stat'
    doc = '''Perform a stat system call on the given path.

  path
    Path to be examined; can be string, bytes, a path-like object or
    open-file-descriptor int.
  dir_fd
    If not None, it should be a file descriptor open to a directory,
    and path should be a relative string; path will then be relative to
    that directory.
  follow_symlinks
    If False, and the last element of the path is a symbolic link,
    stat will examine the symbolic link itself instead of the file
    the link points to.

dir_fd and follow_symlinks may not be implemented
  on your platform.  If they are unavailable, using them will raise a
  NotImplementedError.

It's an error to use dir_fd or follow_symlinks when specifying path as
  an open file descriptor.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.stat(self.input(0)))
        


class AutoNode_os_strerror(rc.Node):
    title = 'strerror'
    doc = '''Translate an error code to a message string.'''
    init_inputs = [
        rc.NodeInputBP(label='code'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.strerror(self.input(0)))
        


class AutoNode_os_symlink(rc.Node):
    title = 'symlink'
    doc = '''Create a symbolic link pointing to src named dst.

target_is_directory is required on Windows if the target is to be
  interpreted as a directory.  (On Windows, symlink requires
  Windows 6.0 or greater, and raises a NotImplementedError otherwise.)
  target_is_directory is ignored on non-Windows platforms.

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError.'''
    init_inputs = [
        rc.NodeInputBP(label='src'),
rc.NodeInputBP(label='dst'),
rc.NodeInputBP(label='target_is_directory'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.symlink(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_os_system(rc.Node):
    title = 'system'
    doc = '''Execute the command in a subshell.'''
    init_inputs = [
        rc.NodeInputBP(label='command'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.system(self.input(0)))
        


class AutoNode_os_times(rc.Node):
    title = 'times'
    doc = '''Return a collection containing process timing information.

The object returned behaves like a named tuple with these fields:
  (utime, stime, cutime, cstime, elapsed_time)
All fields are floating point numbers.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.times())
        


class AutoNode_os_truncate(rc.Node):
    title = 'truncate'
    doc = '''Truncate a file, specified by path, to a specific length.

On some platforms, path may also be specified as an open file descriptor.
  If this functionality is unavailable, using it raises an exception.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='length'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.truncate(self.input(0), self.input(1)))
        


class AutoNode_os_umask(rc.Node):
    title = 'umask'
    doc = '''Set the current numeric umask and return the previous umask.'''
    init_inputs = [
        rc.NodeInputBP(label='mask'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.umask(self.input(0)))
        


class AutoNode_os_unlink(rc.Node):
    title = 'unlink'
    doc = '''Remove a file (same as remove()).

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.unlink(self.input(0)))
        


class AutoNode_os_urandom(rc.Node):
    title = 'urandom'
    doc = '''Return a bytes object containing random bytes suitable for cryptographic use.'''
    init_inputs = [
        rc.NodeInputBP(label='size'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.urandom(self.input(0)))
        


class AutoNode_os_waitpid(rc.Node):
    title = 'waitpid'
    doc = '''Wait for completion of a given process.

Returns a tuple of information regarding the process:
    (pid, status << 8)

The options argument is ignored on Windows.'''
    init_inputs = [
        rc.NodeInputBP(label='pid'),
rc.NodeInputBP(label='options'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.waitpid(self.input(0), self.input(1)))
        


class AutoNode_os_walk(rc.Node):
    title = 'walk'
    doc = '''Directory tree generator.

    For each directory in the directory tree rooted at top (including top
    itself, but excluding '.' and '..'), yields a 3-tuple

        dirpath, dirnames, filenames

    dirpath is a string, the path to the directory.  dirnames is a list of
    the names of the subdirectories in dirpath (excluding '.' and '..').
    filenames is a list of the names of the non-directory files in dirpath.
    Note that the names in the lists are just names, with no path components.
    To get a full path (which begins with top) to a file or directory in
    dirpath, do os.path.join(dirpath, name).

    If optional arg 'topdown' is true or not specified, the triple for a
    directory is generated before the triples for any of its subdirectories
    (directories are generated top down).  If topdown is false, the triple
    for a directory is generated after the triples for all of its
    subdirectories (directories are generated bottom up).

    When topdown is true, the caller can modify the dirnames list in-place
    (e.g., via del or slice assignment), and walk will only recurse into the
    subdirectories whose names remain in dirnames; this can be used to prune the
    search, or to impose a specific order of visiting.  Modifying dirnames when
    topdown is false has no effect on the behavior of os.walk(), since the
    directories in dirnames have already been generated by the time dirnames
    itself is generated. No matter the value of topdown, the list of
    subdirectories is retrieved before the tuples for the directory and its
    subdirectories are generated.

    By default errors from the os.scandir() call are ignored.  If
    optional arg 'onerror' is specified, it should be a function; it
    will be called with one argument, an OSError instance.  It can
    report the error to continue with the walk, or raise the exception
    to abort the walk.  Note that the filename is available as the
    filename attribute of the exception object.

    By default, os.walk does not follow symbolic links to subdirectories on
    systems that support them.  In order to get this functionality, set the
    optional argument 'followlinks' to true.

    Caution:  if you pass a relative pathname for top, don't change the
    current working directory between resumptions of walk.  walk never
    changes the current directory, and assumes that the client doesn't
    either.

    Example:

    import os
    from os.path import join, getsize
    for root, dirs, files in os.walk('python/Lib/email'):
        print(root, "consumes", end="")
        print(sum(getsize(join(root, name)) for name in files), end="")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories

    '''
    init_inputs = [
        rc.NodeInputBP(label='top'),
rc.NodeInputBP(label='topdown'),
rc.NodeInputBP(label='onerror'),
rc.NodeInputBP(label='followlinks'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.walk(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_os_write(rc.Node):
    title = 'write'
    doc = '''Write a bytes object to a file descriptor.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, os.write(self.input(0), self.input(1)))
        