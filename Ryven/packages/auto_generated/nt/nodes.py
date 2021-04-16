import ryvencore_qt as rc
import nt


class AutoNode_nt__add_dll_directory(rc.Node):
    title = '_add_dll_directory'
    type_ = 'nt'
    doc = '''Add a path to the DLL search path.

This search path is used when resolving dependencies for imported
extension modules (the module itself is resolved through sys.path),
and also by ctypes.

Returns an opaque value that may be passed to os.remove_dll_directory
to remove this directory from the search path.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt._add_dll_directory(self.input(0)))
        


class AutoNode_nt__exit(rc.Node):
    title = '_exit'
    type_ = 'nt'
    doc = '''Exit to the system with specified status, without normal exit processing.'''
    init_inputs = [
        rc.NodeInputBP(label='status'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt._exit(self.input(0)))
        


class AutoNode_nt__getdiskusage(rc.Node):
    title = '_getdiskusage'
    type_ = 'nt'
    doc = '''Return disk usage statistics about the given path as a (total, free) tuple.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt._getdiskusage(self.input(0)))
        


class AutoNode_nt__getfinalpathname(rc.Node):
    title = '_getfinalpathname'
    type_ = 'nt'
    doc = '''A helper function for samepath on windows.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt._getfinalpathname(self.input(0)))
        


class AutoNode_nt__getfullpathname(rc.Node):
    title = '_getfullpathname'
    type_ = 'nt'
    doc = ''''''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt._getfullpathname(self.input(0)))
        


class AutoNode_nt__getvolumepathname(rc.Node):
    title = '_getvolumepathname'
    type_ = 'nt'
    doc = '''A helper function for ismount on Win32.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt._getvolumepathname(self.input(0)))
        


class AutoNode_nt__remove_dll_directory(rc.Node):
    title = '_remove_dll_directory'
    type_ = 'nt'
    doc = '''Removes a path from the DLL search path.

The parameter is an opaque value that was returned from
os.add_dll_directory. You can only remove directories that you added
yourself.'''
    init_inputs = [
        rc.NodeInputBP(label='cookie'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt._remove_dll_directory(self.input(0)))
        


class AutoNode_nt_abort(rc.Node):
    title = 'abort'
    type_ = 'nt'
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
        self.set_output_val(0, nt.abort())
        


class AutoNode_nt_access(rc.Node):
    title = 'access'
    type_ = 'nt'
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
        self.set_output_val(0, nt.access(self.input(0), self.input(1)))
        


class AutoNode_nt_chdir(rc.Node):
    title = 'chdir'
    type_ = 'nt'
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
        self.set_output_val(0, nt.chdir(self.input(0)))
        


class AutoNode_nt_chmod(rc.Node):
    title = 'chmod'
    type_ = 'nt'
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
        self.set_output_val(0, nt.chmod(self.input(0), self.input(1)))
        


class AutoNode_nt_close(rc.Node):
    title = 'close'
    type_ = 'nt'
    doc = '''Close a file descriptor.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt.close(self.input(0)))
        


class AutoNode_nt_closerange(rc.Node):
    title = 'closerange'
    type_ = 'nt'
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
        self.set_output_val(0, nt.closerange(self.input(0), self.input(1)))
        


class AutoNode_nt_cpu_count(rc.Node):
    title = 'cpu_count'
    type_ = 'nt'
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
        self.set_output_val(0, nt.cpu_count())
        


class AutoNode_nt_device_encoding(rc.Node):
    title = 'device_encoding'
    type_ = 'nt'
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
        self.set_output_val(0, nt.device_encoding(self.input(0)))
        


class AutoNode_nt_dup(rc.Node):
    title = 'dup'
    type_ = 'nt'
    doc = '''Return a duplicate of a file descriptor.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt.dup(self.input(0)))
        


class AutoNode_nt_dup2(rc.Node):
    title = 'dup2'
    type_ = 'nt'
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
        self.set_output_val(0, nt.dup2(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_nt_execv(rc.Node):
    title = 'execv'
    type_ = 'nt'
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
        self.set_output_val(0, nt.execv(self.input(0), self.input(1)))
        


class AutoNode_nt_execve(rc.Node):
    title = 'execve'
    type_ = 'nt'
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
        self.set_output_val(0, nt.execve(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_nt_fspath(rc.Node):
    title = 'fspath'
    type_ = 'nt'
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
        self.set_output_val(0, nt.fspath(self.input(0)))
        


class AutoNode_nt_fstat(rc.Node):
    title = 'fstat'
    type_ = 'nt'
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
        self.set_output_val(0, nt.fstat(self.input(0)))
        


class AutoNode_nt_fsync(rc.Node):
    title = 'fsync'
    type_ = 'nt'
    doc = '''Force write of fd to disk.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt.fsync(self.input(0)))
        


class AutoNode_nt_ftruncate(rc.Node):
    title = 'ftruncate'
    type_ = 'nt'
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
        self.set_output_val(0, nt.ftruncate(self.input(0), self.input(1)))
        


class AutoNode_nt_get_handle_inheritable(rc.Node):
    title = 'get_handle_inheritable'
    type_ = 'nt'
    doc = '''Get the close-on-exe flag of the specified file descriptor.'''
    init_inputs = [
        rc.NodeInputBP(label='handle'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt.get_handle_inheritable(self.input(0)))
        


class AutoNode_nt_get_inheritable(rc.Node):
    title = 'get_inheritable'
    type_ = 'nt'
    doc = '''Get the close-on-exe flag of the specified file descriptor.'''
    init_inputs = [
        rc.NodeInputBP(label='fd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt.get_inheritable(self.input(0)))
        


class AutoNode_nt_getcwd(rc.Node):
    title = 'getcwd'
    type_ = 'nt'
    doc = '''Return a unicode string representing the current working directory.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt.getcwd())
        


class AutoNode_nt_getcwdb(rc.Node):
    title = 'getcwdb'
    type_ = 'nt'
    doc = '''Return a bytes string representing the current working directory.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt.getcwdb())
        


class AutoNode_nt_getlogin(rc.Node):
    title = 'getlogin'
    type_ = 'nt'
    doc = '''Return the actual login name.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt.getlogin())
        


class AutoNode_nt_getpid(rc.Node):
    title = 'getpid'
    type_ = 'nt'
    doc = '''Return the current process id.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt.getpid())
        


class AutoNode_nt_getppid(rc.Node):
    title = 'getppid'
    type_ = 'nt'
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
        self.set_output_val(0, nt.getppid())
        


class AutoNode_nt_isatty(rc.Node):
    title = 'isatty'
    type_ = 'nt'
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
        self.set_output_val(0, nt.isatty(self.input(0)))
        


class AutoNode_nt_kill(rc.Node):
    title = 'kill'
    type_ = 'nt'
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
        self.set_output_val(0, nt.kill(self.input(0), self.input(1)))
        


class AutoNode_nt_link(rc.Node):
    title = 'link'
    type_ = 'nt'
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
        self.set_output_val(0, nt.link(self.input(0), self.input(1)))
        


class AutoNode_nt_listdir(rc.Node):
    title = 'listdir'
    type_ = 'nt'
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
        self.set_output_val(0, nt.listdir(self.input(0)))
        


class AutoNode_nt_lseek(rc.Node):
    title = 'lseek'
    type_ = 'nt'
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
        self.set_output_val(0, nt.lseek(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_nt_lstat(rc.Node):
    title = 'lstat'
    type_ = 'nt'
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
        self.set_output_val(0, nt.lstat(self.input(0)))
        


class AutoNode_nt_mkdir(rc.Node):
    title = 'mkdir'
    type_ = 'nt'
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
        self.set_output_val(0, nt.mkdir(self.input(0), self.input(1)))
        


class AutoNode_nt_open(rc.Node):
    title = 'open'
    type_ = 'nt'
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
        self.set_output_val(0, nt.open(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_nt_pipe(rc.Node):
    title = 'pipe'
    type_ = 'nt'
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
        self.set_output_val(0, nt.pipe())
        


class AutoNode_nt_putenv(rc.Node):
    title = 'putenv'
    type_ = 'nt'
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
        self.set_output_val(0, nt.putenv(self.input(0), self.input(1)))
        


class AutoNode_nt_read(rc.Node):
    title = 'read'
    type_ = 'nt'
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
        self.set_output_val(0, nt.read(self.input(0), self.input(1)))
        


class AutoNode_nt_readlink(rc.Node):
    title = 'readlink'
    type_ = 'nt'
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
        self.set_output_val(0, nt.readlink(self.input(0)))
        


class AutoNode_nt_remove(rc.Node):
    title = 'remove'
    type_ = 'nt'
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
        self.set_output_val(0, nt.remove(self.input(0)))
        


class AutoNode_nt_rename(rc.Node):
    title = 'rename'
    type_ = 'nt'
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
        self.set_output_val(0, nt.rename(self.input(0), self.input(1)))
        


class AutoNode_nt_replace(rc.Node):
    title = 'replace'
    type_ = 'nt'
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
        self.set_output_val(0, nt.replace(self.input(0), self.input(1)))
        


class AutoNode_nt_rmdir(rc.Node):
    title = 'rmdir'
    type_ = 'nt'
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
        self.set_output_val(0, nt.rmdir(self.input(0)))
        


class AutoNode_nt_scandir(rc.Node):
    title = 'scandir'
    type_ = 'nt'
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
        self.set_output_val(0, nt.scandir(self.input(0)))
        


class AutoNode_nt_set_handle_inheritable(rc.Node):
    title = 'set_handle_inheritable'
    type_ = 'nt'
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
        self.set_output_val(0, nt.set_handle_inheritable(self.input(0), self.input(1)))
        


class AutoNode_nt_set_inheritable(rc.Node):
    title = 'set_inheritable'
    type_ = 'nt'
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
        self.set_output_val(0, nt.set_inheritable(self.input(0), self.input(1)))
        


class AutoNode_nt_spawnv(rc.Node):
    title = 'spawnv'
    type_ = 'nt'
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
        self.set_output_val(0, nt.spawnv(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_nt_spawnve(rc.Node):
    title = 'spawnve'
    type_ = 'nt'
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
        self.set_output_val(0, nt.spawnve(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_nt_stat(rc.Node):
    title = 'stat'
    type_ = 'nt'
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
        self.set_output_val(0, nt.stat(self.input(0)))
        


class AutoNode_nt_strerror(rc.Node):
    title = 'strerror'
    type_ = 'nt'
    doc = '''Translate an error code to a message string.'''
    init_inputs = [
        rc.NodeInputBP(label='code'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt.strerror(self.input(0)))
        


class AutoNode_nt_symlink(rc.Node):
    title = 'symlink'
    type_ = 'nt'
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
        self.set_output_val(0, nt.symlink(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_nt_system(rc.Node):
    title = 'system'
    type_ = 'nt'
    doc = '''Execute the command in a subshell.'''
    init_inputs = [
        rc.NodeInputBP(label='command'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt.system(self.input(0)))
        


class AutoNode_nt_times(rc.Node):
    title = 'times'
    type_ = 'nt'
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
        self.set_output_val(0, nt.times())
        


class AutoNode_nt_truncate(rc.Node):
    title = 'truncate'
    type_ = 'nt'
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
        self.set_output_val(0, nt.truncate(self.input(0), self.input(1)))
        


class AutoNode_nt_umask(rc.Node):
    title = 'umask'
    type_ = 'nt'
    doc = '''Set the current numeric umask and return the previous umask.'''
    init_inputs = [
        rc.NodeInputBP(label='mask'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt.umask(self.input(0)))
        


class AutoNode_nt_unlink(rc.Node):
    title = 'unlink'
    type_ = 'nt'
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
        self.set_output_val(0, nt.unlink(self.input(0)))
        


class AutoNode_nt_urandom(rc.Node):
    title = 'urandom'
    type_ = 'nt'
    doc = '''Return a bytes object containing random bytes suitable for cryptographic use.'''
    init_inputs = [
        rc.NodeInputBP(label='size'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, nt.urandom(self.input(0)))
        


class AutoNode_nt_waitpid(rc.Node):
    title = 'waitpid'
    type_ = 'nt'
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
        self.set_output_val(0, nt.waitpid(self.input(0), self.input(1)))
        


class AutoNode_nt_write(rc.Node):
    title = 'write'
    type_ = 'nt'
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
        self.set_output_val(0, nt.write(self.input(0), self.input(1)))
        