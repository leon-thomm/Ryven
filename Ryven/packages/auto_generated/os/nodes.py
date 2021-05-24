
from NENV import *

import os


class NodeBase(Node):
    pass


class _Check_Methods_Node(NodeBase):
    """
    """
    
    title = '_check_methods'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='C'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os._check_methods(self.input(0)))
        

class _Execvpe_Node(NodeBase):
    """
    """
    
    title = '_execvpe'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='file'),
        NodeInputBP(label='args'),
        NodeInputBP(label='env', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os._execvpe(self.input(0), self.input(1), self.input(2)))
        

class _Exists_Node(NodeBase):
    """
    """
    
    title = '_exists'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os._exists(self.input(0)))
        

class _Exit_Node(NodeBase):
    """
    Exit to the system with specified status, without normal exit processing."""
    
    title = '_exit'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='status'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os._exit(self.input(0)))
        

class _Fspath_Node(NodeBase):
    """
    Return the path representation of a path-like object.

    If str or bytes is passed in, it is returned unchanged. Otherwise the
    os.PathLike interface is used to get the path representation. If the
    path representation is not str or bytes, TypeError is raised. If the
    provided path is not str, bytes, or os.PathLike, TypeError is raised.
    """
    
    title = '_fspath'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os._fspath(self.input(0)))
        

class _Get_Exports_List_Node(NodeBase):
    """
    """
    
    title = '_get_exports_list'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='module'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os._get_exports_list(self.input(0)))
        

class _Walk_Node(NodeBase):
    """
    """
    
    title = '_walk'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='top'),
        NodeInputBP(label='topdown'),
        NodeInputBP(label='onerror'),
        NodeInputBP(label='followlinks'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os._walk(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Abort_Node(NodeBase):
    """
    Abort the interpreter immediately.

This function 'dumps core' or otherwise fails in the hardest way possible
on the hosting operating system.  This function never returns."""
    
    title = 'abort'
    type_ = 'os'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.abort())
        

class Access_Node(NodeBase):
    """
    Use the real uid/gid to test for access to a path.

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
  has the specified access to the path."""
    
    title = 'access'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='mode'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.access(self.input(0), self.input(1)))
        

class Add_Dll_Directory_Node(NodeBase):
    """
    Add a path to the DLL search path.

        This search path is used when resolving dependencies for imported
        extension modules (the module itself is resolved through sys.path),
        and also by ctypes.

        Remove the directory by calling close() on the returned object or
        using it in a with statement.
        """
    
    title = 'add_dll_directory'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.add_dll_directory(self.input(0)))
        

class Chdir_Node(NodeBase):
    """
    Change the current working directory to the specified path.

path may always be specified as a string.
On some platforms, path may also be specified as an open file descriptor.
  If this functionality is unavailable, using it raises an exception."""
    
    title = 'chdir'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.chdir(self.input(0)))
        

class Chmod_Node(NodeBase):
    """
    Change the access permissions of a file.

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
  If they are unavailable, using them will raise a NotImplementedError."""
    
    title = 'chmod'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='mode'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.chmod(self.input(0), self.input(1)))
        

class Close_Node(NodeBase):
    """
    Close a file descriptor."""
    
    title = 'close'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.close(self.input(0)))
        

class Closerange_Node(NodeBase):
    """
    Closes all file descriptors in [fd_low, fd_high), ignoring errors."""
    
    title = 'closerange'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd_low'),
        NodeInputBP(label='fd_high'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.closerange(self.input(0), self.input(1)))
        

class Cpu_Count_Node(NodeBase):
    """
    Return the number of CPUs in the system; return None if indeterminable.

This number is not equivalent to the number of CPUs the current process can
use.  The number of usable CPUs can be obtained with
``len(os.sched_getaffinity(0))``"""
    
    title = 'cpu_count'
    type_ = 'os'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.cpu_count())
        

class Device_Encoding_Node(NodeBase):
    """
    Return a string describing the encoding of a terminal's file descriptor.

The file descriptor must be attached to a terminal.
If the device is not a terminal, return None."""
    
    title = 'device_encoding'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.device_encoding(self.input(0)))
        

class Dup_Node(NodeBase):
    """
    Return a duplicate of a file descriptor."""
    
    title = 'dup'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.dup(self.input(0)))
        

class Dup2_Node(NodeBase):
    """
    Duplicate file descriptor."""
    
    title = 'dup2'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
        NodeInputBP(label='fd2'),
        NodeInputBP(label='inheritable', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.dup2(self.input(0), self.input(1), self.input(2)))
        

class Execl_Node(NodeBase):
    """
    execl(file, *args)

    Execute the executable file with argument list args, replacing the
    current process. """
    
    title = 'execl'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.execl(self.input(0)))
        

class Execle_Node(NodeBase):
    """
    execle(file, *args, env)

    Execute the executable file with argument list args and
    environment env, replacing the current process. """
    
    title = 'execle'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.execle(self.input(0)))
        

class Execlp_Node(NodeBase):
    """
    execlp(file, *args)

    Execute the executable file (which is searched for along $PATH)
    with argument list args, replacing the current process. """
    
    title = 'execlp'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.execlp(self.input(0)))
        

class Execlpe_Node(NodeBase):
    """
    execlpe(file, *args, env)

    Execute the executable file (which is searched for along $PATH)
    with argument list args and environment env, replacing the current
    process. """
    
    title = 'execlpe'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.execlpe(self.input(0)))
        

class Execv_Node(NodeBase):
    """
    Execute an executable path with arguments, replacing current process.

  path
    Path of executable file.
  argv
    Tuple or list of strings."""
    
    title = 'execv'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='argv'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.execv(self.input(0), self.input(1)))
        

class Execve_Node(NodeBase):
    """
    Execute an executable path with arguments, replacing current process.

  path
    Path of executable file.
  argv
    Tuple or list of strings.
  env
    Dictionary of strings mapping to strings."""
    
    title = 'execve'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='argv'),
        NodeInputBP(label='env'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.execve(self.input(0), self.input(1), self.input(2)))
        

class Execvp_Node(NodeBase):
    """
    execvp(file, args)

    Execute the executable file (which is searched for along $PATH)
    with argument list args, replacing the current process.
    args may be a list or tuple of strings. """
    
    title = 'execvp'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='file'),
        NodeInputBP(label='args'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.execvp(self.input(0), self.input(1)))
        

class Execvpe_Node(NodeBase):
    """
    execvpe(file, args, env)

    Execute the executable file (which is searched for along $PATH)
    with argument list args and environment env, replacing the
    current process.
    args may be a list or tuple of strings. """
    
    title = 'execvpe'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='file'),
        NodeInputBP(label='args'),
        NodeInputBP(label='env'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.execvpe(self.input(0), self.input(1), self.input(2)))
        

class Fdopen_Node(NodeBase):
    """
    """
    
    title = 'fdopen'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.fdopen(self.input(0)))
        

class Fsdecode_Node(NodeBase):
    """
    Decode filename (an os.PathLike, bytes, or str) from the filesystem
        encoding with 'surrogateescape' error handler, return str unchanged. On
        Windows, use 'strict' error handler if the file system encoding is
        'mbcs' (which is the default encoding).
        """
    
    title = 'fsdecode'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.fsdecode(self.input(0)))
        

class Fsencode_Node(NodeBase):
    """
    Encode filename (an os.PathLike, bytes, or str) to the filesystem
        encoding with 'surrogateescape' error handler, return bytes unchanged.
        On Windows, use 'strict' error handler if the file system encoding is
        'mbcs' (which is the default encoding).
        """
    
    title = 'fsencode'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.fsencode(self.input(0)))
        

class Fspath_Node(NodeBase):
    """
    Return the file system path representation of the object.

If the object is str or bytes, then allow it to pass through as-is. If the
object defines __fspath__(), then return the result of that method. All other
types raise a TypeError."""
    
    title = 'fspath'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.fspath(self.input(0)))
        

class Fstat_Node(NodeBase):
    """
    Perform a stat system call on the given file descriptor.

Like stat(), but for an open file descriptor.
Equivalent to os.stat(fd)."""
    
    title = 'fstat'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.fstat(self.input(0)))
        

class Fsync_Node(NodeBase):
    """
    Force write of fd to disk."""
    
    title = 'fsync'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.fsync(self.input(0)))
        

class Ftruncate_Node(NodeBase):
    """
    Truncate a file, specified by file descriptor, to a specific length."""
    
    title = 'ftruncate'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
        NodeInputBP(label='length'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.ftruncate(self.input(0), self.input(1)))
        

class Get_Exec_Path_Node(NodeBase):
    """
    Returns the sequence of directories that will be searched for the
    named executable (similar to a shell) when launching a process.

    *env* must be an environment variable dict or None.  If *env* is None,
    os.environ will be used.
    """
    
    title = 'get_exec_path'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='env', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.get_exec_path(self.input(0)))
        

class Get_Handle_Inheritable_Node(NodeBase):
    """
    Get the close-on-exe flag of the specified file descriptor."""
    
    title = 'get_handle_inheritable'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='handle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.get_handle_inheritable(self.input(0)))
        

class Get_Inheritable_Node(NodeBase):
    """
    Get the close-on-exe flag of the specified file descriptor."""
    
    title = 'get_inheritable'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.get_inheritable(self.input(0)))
        

class Getcwd_Node(NodeBase):
    """
    Return a unicode string representing the current working directory."""
    
    title = 'getcwd'
    type_ = 'os'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.getcwd())
        

class Getcwdb_Node(NodeBase):
    """
    Return a bytes string representing the current working directory."""
    
    title = 'getcwdb'
    type_ = 'os'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.getcwdb())
        

class Getenv_Node(NodeBase):
    """
    Get an environment variable, return None if it doesn't exist.
    The optional second argument can specify an alternate default.
    key, default and the result are str."""
    
    title = 'getenv'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='key'),
        NodeInputBP(label='default', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.getenv(self.input(0), self.input(1)))
        

class Getlogin_Node(NodeBase):
    """
    Return the actual login name."""
    
    title = 'getlogin'
    type_ = 'os'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.getlogin())
        

class Getpid_Node(NodeBase):
    """
    Return the current process id."""
    
    title = 'getpid'
    type_ = 'os'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.getpid())
        

class Getppid_Node(NodeBase):
    """
    Return the parent's process id.

If the parent process has already exited, Windows machines will still
return its id; others systems will return the id of the 'init' process (1)."""
    
    title = 'getppid'
    type_ = 'os'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.getppid())
        

class Isatty_Node(NodeBase):
    """
    Return True if the fd is connected to a terminal.

Return True if the file descriptor is an open file descriptor
connected to the slave end of a terminal."""
    
    title = 'isatty'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.isatty(self.input(0)))
        

class Kill_Node(NodeBase):
    """
    Kill a process with a signal."""
    
    title = 'kill'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='pid'),
        NodeInputBP(label='signal'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.kill(self.input(0), self.input(1)))
        

class Link_Node(NodeBase):
    """
    Create a hard link to a file.

If either src_dir_fd or dst_dir_fd is not None, it should be a file
  descriptor open to a directory, and the respective path string (src or dst)
  should be relative; the path will then be relative to that directory.
If follow_symlinks is False, and the last element of src is a symbolic
  link, link will create a link to the symbolic link itself instead of the
  file the link points to.
src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your
  platform.  If they are unavailable, using them will raise a
  NotImplementedError."""
    
    title = 'link'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.link(self.input(0), self.input(1)))
        

class Listdir_Node(NodeBase):
    """
    Return a list containing the names of the files in the directory.

path can be specified as either str, bytes, or a path-like object.  If path is bytes,
  the filenames returned will also be bytes; in all other circumstances
  the filenames returned will be str.
If path is None, uses the path='.'.
On some platforms, path may also be specified as an open file descriptor;\
  the file descriptor must refer to a directory.
  If this functionality is unavailable, using it raises NotImplementedError.

The list is in arbitrary order.  It does not include the special
entries '.' and '..' even if they are present in the directory."""
    
    title = 'listdir'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.listdir(self.input(0)))
        

class Lseek_Node(NodeBase):
    """
    Set the position of a file descriptor.  Return the new position.

Return the new cursor position in number of bytes
relative to the beginning of the file."""
    
    title = 'lseek'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
        NodeInputBP(label='position'),
        NodeInputBP(label='how'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.lseek(self.input(0), self.input(1), self.input(2)))
        

class Lstat_Node(NodeBase):
    """
    Perform a stat system call on the given path, without following symbolic links.

Like stat(), but do not follow symbolic links.
Equivalent to stat(path, follow_symlinks=False)."""
    
    title = 'lstat'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.lstat(self.input(0)))
        

class Makedirs_Node(NodeBase):
    """
    makedirs(name [, mode=0o777][, exist_ok=False])

    Super-mkdir; create a leaf directory and all intermediate ones.  Works like
    mkdir, except that any intermediate path segment (not just the rightmost)
    will be created if it does not exist. If the target directory already
    exists, raise an OSError if exist_ok is False. Otherwise no exception is
    raised.  This is recursive.

    """
    
    title = 'makedirs'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='mode', dtype=dtypes.Data(default=511, size='s')),
        NodeInputBP(label='exist_ok', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.makedirs(self.input(0), self.input(1), self.input(2)))
        

class Mkdir_Node(NodeBase):
    """
    Create a directory.

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError.

The mode argument is ignored on Windows."""
    
    title = 'mkdir'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='mode', dtype=dtypes.Data(default=511, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.mkdir(self.input(0), self.input(1)))
        

class Open_Node(NodeBase):
    """
    Open a file for low level IO.  Returns a file descriptor (integer).

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError."""
    
    title = 'open'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='flags'),
        NodeInputBP(label='mode', dtype=dtypes.Data(default=511, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.open(self.input(0), self.input(1), self.input(2)))
        

class Pipe_Node(NodeBase):
    """
    Create a pipe.

Returns a tuple of two file descriptors:
  (read_fd, write_fd)"""
    
    title = 'pipe'
    type_ = 'os'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.pipe())
        

class Popen_Node(NodeBase):
    """
    """
    
    title = 'popen'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='cmd'),
        NodeInputBP(label='mode', dtype=dtypes.Data(default='r', size='s')),
        NodeInputBP(label='buffering', dtype=dtypes.Data(default=-1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.popen(self.input(0), self.input(1), self.input(2)))
        

class Putenv_Node(NodeBase):
    """
    Change or add an environment variable."""
    
    title = 'putenv'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.putenv(self.input(0), self.input(1)))
        

class Read_Node(NodeBase):
    """
    Read from a file descriptor.  Returns a bytes object."""
    
    title = 'read'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
        NodeInputBP(label='length'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.read(self.input(0), self.input(1)))
        

class Readlink_Node(NodeBase):
    """
    Return a string representing the path to which the symbolic link points.

If dir_fd is not None, it should be a file descriptor open to a directory,
and path should be relative; path will then be relative to that directory.

dir_fd may not be implemented on your platform.  If it is unavailable,
using it will raise a NotImplementedError."""
    
    title = 'readlink'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.readlink(self.input(0)))
        

class Remove_Node(NodeBase):
    """
    Remove a file (same as unlink()).

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError."""
    
    title = 'remove'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.remove(self.input(0)))
        

class Removedirs_Node(NodeBase):
    """
    removedirs(name)

    Super-rmdir; remove a leaf directory and all empty intermediate
    ones.  Works like rmdir except that, if the leaf directory is
    successfully removed, directories corresponding to rightmost path
    segments will be pruned away until either the whole path is
    consumed or an error occurs.  Errors during this latter phase are
    ignored -- they generally mean that a directory was not empty.

    """
    
    title = 'removedirs'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.removedirs(self.input(0)))
        

class Rename_Node(NodeBase):
    """
    Rename a file or directory.

If either src_dir_fd or dst_dir_fd is not None, it should be a file
  descriptor open to a directory, and the respective path string (src or dst)
  should be relative; the path will then be relative to that directory.
src_dir_fd and dst_dir_fd, may not be implemented on your platform.
  If they are unavailable, using them will raise a NotImplementedError."""
    
    title = 'rename'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.rename(self.input(0), self.input(1)))
        

class Renames_Node(NodeBase):
    """
    renames(old, new)

    Super-rename; create directories as necessary and delete any left
    empty.  Works like rename, except creation of any intermediate
    directories needed to make the new pathname good is attempted
    first.  After the rename, directories corresponding to rightmost
    path segments of the old name will be pruned until either the
    whole path is consumed or a nonempty directory is found.

    Note: this function can fail with the new directory structure made
    if you lack permissions needed to unlink the leaf directory or
    file.

    """
    
    title = 'renames'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='old'),
        NodeInputBP(label='new'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.renames(self.input(0), self.input(1)))
        

class Replace_Node(NodeBase):
    """
    Rename a file or directory, overwriting the destination.

If either src_dir_fd or dst_dir_fd is not None, it should be a file
  descriptor open to a directory, and the respective path string (src or dst)
  should be relative; the path will then be relative to that directory.
src_dir_fd and dst_dir_fd, may not be implemented on your platform.
  If they are unavailable, using them will raise a NotImplementedError."""
    
    title = 'replace'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.replace(self.input(0), self.input(1)))
        

class Rmdir_Node(NodeBase):
    """
    Remove a directory.

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError."""
    
    title = 'rmdir'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.rmdir(self.input(0)))
        

class Scandir_Node(NodeBase):
    """
    Return an iterator of DirEntry objects for given path.

path can be specified as either str, bytes, or a path-like object.  If path
is bytes, the names of yielded DirEntry objects will also be bytes; in
all other circumstances they will be str.

If path is None, uses the path='.'."""
    
    title = 'scandir'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.scandir(self.input(0)))
        

class Set_Handle_Inheritable_Node(NodeBase):
    """
    Set the inheritable flag of the specified handle."""
    
    title = 'set_handle_inheritable'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='handle'),
        NodeInputBP(label='inheritable'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.set_handle_inheritable(self.input(0), self.input(1)))
        

class Set_Inheritable_Node(NodeBase):
    """
    Set the inheritable flag of the specified file descriptor."""
    
    title = 'set_inheritable'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
        NodeInputBP(label='inheritable'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.set_inheritable(self.input(0), self.input(1)))
        

class Spawnl_Node(NodeBase):
    """
    spawnl(mode, file, *args) -> integer

Execute file with arguments from args in a subprocess.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
    
    title = 'spawnl'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='mode'),
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.spawnl(self.input(0), self.input(1)))
        

class Spawnle_Node(NodeBase):
    """
    spawnle(mode, file, *args, env) -> integer

Execute file with arguments from args in a subprocess with the
supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
    
    title = 'spawnle'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='mode'),
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.spawnle(self.input(0), self.input(1)))
        

class Spawnv_Node(NodeBase):
    """
    Execute the program specified by path in a new process.

  mode
    Mode of process creation.
  path
    Path of executable file.
  argv
    Tuple or list of strings."""
    
    title = 'spawnv'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='mode'),
        NodeInputBP(label='path'),
        NodeInputBP(label='argv'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.spawnv(self.input(0), self.input(1), self.input(2)))
        

class Spawnve_Node(NodeBase):
    """
    Execute the program specified by path in a new process.

  mode
    Mode of process creation.
  path
    Path of executable file.
  argv
    Tuple or list of strings.
  env
    Dictionary of strings mapping to strings."""
    
    title = 'spawnve'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='mode'),
        NodeInputBP(label='path'),
        NodeInputBP(label='argv'),
        NodeInputBP(label='env'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.spawnve(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Stat_Node(NodeBase):
    """
    Perform a stat system call on the given path.

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
  an open file descriptor."""
    
    title = 'stat'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.stat(self.input(0)))
        

class Strerror_Node(NodeBase):
    """
    Translate an error code to a message string."""
    
    title = 'strerror'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.strerror(self.input(0)))
        

class Symlink_Node(NodeBase):
    """
    Create a symbolic link pointing to src named dst.

target_is_directory is required on Windows if the target is to be
  interpreted as a directory.  (On Windows, symlink requires
  Windows 6.0 or greater, and raises a NotImplementedError otherwise.)
  target_is_directory is ignored on non-Windows platforms.

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError."""
    
    title = 'symlink'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
        NodeInputBP(label='target_is_directory', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.symlink(self.input(0), self.input(1), self.input(2)))
        

class System_Node(NodeBase):
    """
    Execute the command in a subshell."""
    
    title = 'system'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='command'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.system(self.input(0)))
        

class Times_Node(NodeBase):
    """
    Return a collection containing process timing information.

The object returned behaves like a named tuple with these fields:
  (utime, stime, cutime, cstime, elapsed_time)
All fields are floating point numbers."""
    
    title = 'times'
    type_ = 'os'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.times())
        

class Truncate_Node(NodeBase):
    """
    Truncate a file, specified by path, to a specific length.

On some platforms, path may also be specified as an open file descriptor.
  If this functionality is unavailable, using it raises an exception."""
    
    title = 'truncate'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='length'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.truncate(self.input(0), self.input(1)))
        

class Umask_Node(NodeBase):
    """
    Set the current numeric umask and return the previous umask."""
    
    title = 'umask'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='mask'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.umask(self.input(0)))
        

class Unlink_Node(NodeBase):
    """
    Remove a file (same as remove()).

If dir_fd is not None, it should be a file descriptor open to a directory,
  and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
  If it is unavailable, using it will raise a NotImplementedError."""
    
    title = 'unlink'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.unlink(self.input(0)))
        

class Unsetenv_Node(NodeBase):
    """
    Delete an environment variable."""
    
    title = 'unsetenv'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.unsetenv(self.input(0)))
        

class Urandom_Node(NodeBase):
    """
    Return a bytes object containing random bytes suitable for cryptographic use."""
    
    title = 'urandom'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='size'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.urandom(self.input(0)))
        

class Waitpid_Node(NodeBase):
    """
    Wait for completion of a given process.

Returns a tuple of information regarding the process:
    (pid, status << 8)

The options argument is ignored on Windows."""
    
    title = 'waitpid'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='pid'),
        NodeInputBP(label='options'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.waitpid(self.input(0), self.input(1)))
        

class Waitstatus_To_Exitcode_Node(NodeBase):
    """
    Convert a wait status to an exit code.

On Unix:

* If WIFEXITED(status) is true, return WEXITSTATUS(status).
* If WIFSIGNALED(status) is true, return -WTERMSIG(status).
* Otherwise, raise a ValueError.

On Windows, return status shifted right by 8 bits.

On Unix, if the process is being traced or if waitpid() was called with
WUNTRACED option, the caller must first check if WIFSTOPPED(status) is true.
This function must not be called if WIFSTOPPED(status) is true."""
    
    title = 'waitstatus_to_exitcode'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='status'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.waitstatus_to_exitcode(self.input(0)))
        

class Walk_Node(NodeBase):
    """
    Directory tree generator.

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

    """
    
    title = 'walk'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='top'),
        NodeInputBP(label='topdown', dtype=dtypes.Data(default=True, size='s')),
        NodeInputBP(label='onerror', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='followlinks', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.walk(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Write_Node(NodeBase):
    """
    Write a bytes object to a file descriptor."""
    
    title = 'write'
    type_ = 'os'
    init_inputs = [
        NodeInputBP(label='fd'),
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, os.write(self.input(0), self.input(1)))
        


export_nodes(
    _Check_Methods_Node,
    _Execvpe_Node,
    _Exists_Node,
    _Exit_Node,
    _Fspath_Node,
    _Get_Exports_List_Node,
    _Walk_Node,
    Abort_Node,
    Access_Node,
    Add_Dll_Directory_Node,
    Chdir_Node,
    Chmod_Node,
    Close_Node,
    Closerange_Node,
    Cpu_Count_Node,
    Device_Encoding_Node,
    Dup_Node,
    Dup2_Node,
    Execl_Node,
    Execle_Node,
    Execlp_Node,
    Execlpe_Node,
    Execv_Node,
    Execve_Node,
    Execvp_Node,
    Execvpe_Node,
    Fdopen_Node,
    Fsdecode_Node,
    Fsencode_Node,
    Fspath_Node,
    Fstat_Node,
    Fsync_Node,
    Ftruncate_Node,
    Get_Exec_Path_Node,
    Get_Handle_Inheritable_Node,
    Get_Inheritable_Node,
    Getcwd_Node,
    Getcwdb_Node,
    Getenv_Node,
    Getlogin_Node,
    Getpid_Node,
    Getppid_Node,
    Isatty_Node,
    Kill_Node,
    Link_Node,
    Listdir_Node,
    Lseek_Node,
    Lstat_Node,
    Makedirs_Node,
    Mkdir_Node,
    Open_Node,
    Pipe_Node,
    Popen_Node,
    Putenv_Node,
    Read_Node,
    Readlink_Node,
    Remove_Node,
    Removedirs_Node,
    Rename_Node,
    Renames_Node,
    Replace_Node,
    Rmdir_Node,
    Scandir_Node,
    Set_Handle_Inheritable_Node,
    Set_Inheritable_Node,
    Spawnl_Node,
    Spawnle_Node,
    Spawnv_Node,
    Spawnve_Node,
    Stat_Node,
    Strerror_Node,
    Symlink_Node,
    System_Node,
    Times_Node,
    Truncate_Node,
    Umask_Node,
    Unlink_Node,
    Unsetenv_Node,
    Urandom_Node,
    Waitpid_Node,
    Waitstatus_To_Exitcode_Node,
    Walk_Node,
    Write_Node,
)
