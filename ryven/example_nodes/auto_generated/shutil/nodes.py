
from ryven.NENV import *

import shutil


class NodeBase(Node):
    pass


class _Access_Check_Node(NodeBase):
    """
    """
    
    title = '_access_check'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='fn'),
        NodeInputBP(label='mode'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._access_check(self.input(0), self.input(1)))
        

class _Basename_Node(NodeBase):
    """
    A basename() variant which first strips the trailing slash, if present.
    Thus we always get the last component of the path, even for directories.

    path: Union[PathLike, str]

    e.g.
    >>> os.path.basename('/bar/foo')
    'foo'
    >>> os.path.basename('/bar/foo/')
    ''
    >>> _basename('/bar/foo/')
    'foo'
    """
    
    title = '_basename'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._basename(self.input(0)))
        

class _Check_Unpack_Options_Node(NodeBase):
    """
    Checks what gets registered as an unpacker."""
    
    title = '_check_unpack_options'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='extensions'),
        NodeInputBP(label='function'),
        NodeInputBP(label='extra_args'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._check_unpack_options(self.input(0), self.input(1), self.input(2)))
        

class _Copyfileobj_Readinto_Node(NodeBase):
    """
    readinto()/memoryview() based variant of copyfileobj().
    *fsrc* must support readinto() method and both files must be
    open in binary mode.
    """
    
    title = '_copyfileobj_readinto'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='fsrc'),
        NodeInputBP(label='fdst'),
        NodeInputBP(label='length', dtype=dtypes.Data(default=1048576, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._copyfileobj_readinto(self.input(0), self.input(1), self.input(2)))
        

class _Copytree_Node(NodeBase):
    """
    """
    
    title = '_copytree'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='entries'),
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
        NodeInputBP(label='symlinks'),
        NodeInputBP(label='ignore'),
        NodeInputBP(label='copy_function'),
        NodeInputBP(label='ignore_dangling_symlinks'),
        NodeInputBP(label='dirs_exist_ok', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._copytree(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        

class _Copyxattr_Node(NodeBase):
    """
    """
    
    title = '_copyxattr'
    type_ = 'shutil'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._copyxattr())
        

class _Destinsrc_Node(NodeBase):
    """
    """
    
    title = '_destinsrc'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._destinsrc(self.input(0), self.input(1)))
        

class _Ensure_Directory_Node(NodeBase):
    """
    Ensure that the parent directory of `path` exists"""
    
    title = '_ensure_directory'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._ensure_directory(self.input(0)))
        

class _Fastcopy_Fcopyfile_Node(NodeBase):
    """
    Copy a regular file content or metadata by using high-performance
    fcopyfile(3) syscall (macOS).
    """
    
    title = '_fastcopy_fcopyfile'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='fsrc'),
        NodeInputBP(label='fdst'),
        NodeInputBP(label='flags'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._fastcopy_fcopyfile(self.input(0), self.input(1), self.input(2)))
        

class _Fastcopy_Sendfile_Node(NodeBase):
    """
    Copy data from one regular mmap-like fd to another by using
    high-performance sendfile(2) syscall.
    This should work on Linux >= 2.6.33 only.
    """
    
    title = '_fastcopy_sendfile'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='fsrc'),
        NodeInputBP(label='fdst'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._fastcopy_sendfile(self.input(0), self.input(1)))
        

class _Find_Unpack_Format_Node(NodeBase):
    """
    """
    
    title = '_find_unpack_format'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._find_unpack_format(self.input(0)))
        

class _Get_Gid_Node(NodeBase):
    """
    Returns a gid, given a group name."""
    
    title = '_get_gid'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._get_gid(self.input(0)))
        

class _Get_Uid_Node(NodeBase):
    """
    Returns an uid, given a user name."""
    
    title = '_get_uid'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._get_uid(self.input(0)))
        

class _Is_Immutable_Node(NodeBase):
    """
    """
    
    title = '_is_immutable'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='src'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._is_immutable(self.input(0)))
        

class _Islink_Node(NodeBase):
    """
    """
    
    title = '_islink'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='fn'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._islink(self.input(0)))
        

class _Make_Tarball_Node(NodeBase):
    """
    Create a (possibly compressed) tar file from all the files under
    'base_dir'.

    'compress' must be "gzip" (the default), "bzip2", "xz", or None.

    'owner' and 'group' can be used to define an owner and a group for the
    archive that is being built. If not provided, the current owner and group
    will be used.

    The output tar file will be named 'base_name' +  ".tar", possibly plus
    the appropriate compression extension (".gz", ".bz2", or ".xz").

    Returns the output filename.
    """
    
    title = '_make_tarball'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='base_name'),
        NodeInputBP(label='base_dir'),
        NodeInputBP(label='compress', dtype=dtypes.Data(default='gzip', size='s')),
        NodeInputBP(label='verbose', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='dry_run', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='owner', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='group', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='logger', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._make_tarball(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        

class _Make_Zipfile_Node(NodeBase):
    """
    Create a zip file from all the files under 'base_dir'.

    The output zip file will be named 'base_name' + ".zip".  Returns the
    name of the output zip file.
    """
    
    title = '_make_zipfile'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='base_name'),
        NodeInputBP(label='base_dir'),
        NodeInputBP(label='verbose', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='dry_run', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='logger', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._make_zipfile(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class _Rmtree_Isdir_Node(NodeBase):
    """
    """
    
    title = '_rmtree_isdir'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='entry'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._rmtree_isdir(self.input(0)))
        

class _Rmtree_Islink_Node(NodeBase):
    """
    """
    
    title = '_rmtree_islink'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._rmtree_islink(self.input(0)))
        

class _Rmtree_Safe_Fd_Node(NodeBase):
    """
    """
    
    title = '_rmtree_safe_fd'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='topfd'),
        NodeInputBP(label='path'),
        NodeInputBP(label='onerror'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._rmtree_safe_fd(self.input(0), self.input(1), self.input(2)))
        

class _Rmtree_Unsafe_Node(NodeBase):
    """
    """
    
    title = '_rmtree_unsafe'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='onerror'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._rmtree_unsafe(self.input(0), self.input(1)))
        

class _Samefile_Node(NodeBase):
    """
    """
    
    title = '_samefile'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._samefile(self.input(0), self.input(1)))
        

class _Stat_Node(NodeBase):
    """
    """
    
    title = '_stat'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='fn'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._stat(self.input(0)))
        

class _Unpack_Tarfile_Node(NodeBase):
    """
    Unpack tar/tar.gz/tar.bz2/tar.xz `filename` to `extract_dir`
    """
    
    title = '_unpack_tarfile'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='extract_dir'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._unpack_tarfile(self.input(0), self.input(1)))
        

class _Unpack_Zipfile_Node(NodeBase):
    """
    Unpack zip `filename` to `extract_dir`
    """
    
    title = '_unpack_zipfile'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='extract_dir'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil._unpack_zipfile(self.input(0), self.input(1)))
        

class Chown_Node(NodeBase):
    """
    Change owner user and group of the given path.

    user and group can be the uid/gid or the user/group names, and in that case,
    they are converted to their respective uid/gid.
    """
    
    title = 'chown'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='user', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='group', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.chown(self.input(0), self.input(1), self.input(2)))
        

class Copy_Node(NodeBase):
    """
    Copy data and mode bits ("cp src dst"). Return the file's destination.

    The destination may be a directory.

    If follow_symlinks is false, symlinks won't be followed. This
    resembles GNU's "cp -P src dst".

    If source and destination are the same file, a SameFileError will be
    raised.

    """
    
    title = 'copy'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.copy(self.input(0), self.input(1)))
        

class Copy2_Node(NodeBase):
    """
    Copy data and metadata. Return the file's destination.

    Metadata is copied with copystat(). Please see the copystat function
    for more information.

    The destination may be a directory.

    If follow_symlinks is false, symlinks won't be followed. This
    resembles GNU's "cp -P src dst".
    """
    
    title = 'copy2'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.copy2(self.input(0), self.input(1)))
        

class Copyfile_Node(NodeBase):
    """
    Copy data from src to dst in the most efficient way possible.

    If follow_symlinks is not set and src is a symbolic link, a new
    symlink will be created instead of copying the file it points to.

    """
    
    title = 'copyfile'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.copyfile(self.input(0), self.input(1)))
        

class Copyfileobj_Node(NodeBase):
    """
    copy data from file-like object fsrc to file-like object fdst"""
    
    title = 'copyfileobj'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='fsrc'),
        NodeInputBP(label='fdst'),
        NodeInputBP(label='length', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.copyfileobj(self.input(0), self.input(1), self.input(2)))
        

class Copymode_Node(NodeBase):
    """
    Copy mode bits from src to dst.

    If follow_symlinks is not set, symlinks aren't followed if and only
    if both `src` and `dst` are symlinks.  If `lchmod` isn't available
    (e.g. Linux) this method does nothing.

    """
    
    title = 'copymode'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.copymode(self.input(0), self.input(1)))
        

class Copystat_Node(NodeBase):
    """
    Copy file metadata

    Copy the permission bits, last access time, last modification time, and
    flags from `src` to `dst`. On Linux, copystat() also copies the "extended
    attributes" where possible. The file contents, owner, and group are
    unaffected. `src` and `dst` are path-like objects or path names given as
    strings.

    If the optional flag `follow_symlinks` is not set, symlinks aren't
    followed if and only if both `src` and `dst` are symlinks.
    """
    
    title = 'copystat'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.copystat(self.input(0), self.input(1)))
        

class Copytree_Node(NodeBase):
    """
    Recursively copy a directory tree and return the destination directory.

    dirs_exist_ok dictates whether to raise an exception in case dst or any
    missing parent directory already exists.

    If exception(s) occur, an Error is raised with a list of reasons.

    If the optional symlinks flag is true, symbolic links in the
    source tree result in symbolic links in the destination tree; if
    it is false, the contents of the files pointed to by symbolic
    links are copied. If the file pointed by the symlink doesn't
    exist, an exception will be added in the list of errors raised in
    an Error exception at the end of the copy process.

    You can set the optional ignore_dangling_symlinks flag to true if you
    want to silence this exception. Notice that this has no effect on
    platforms that don't support os.symlink.

    The optional ignore argument is a callable. If given, it
    is called with the `src` parameter, which is the directory
    being visited by copytree(), and `names` which is the list of
    `src` contents, as returned by os.listdir():

        callable(src, names) -> ignored_names

    Since copytree() is called recursively, the callable will be
    called once for each directory that is copied. It returns a
    list of names relative to the `src` directory that should
    not be copied.

    The optional copy_function argument is a callable that will be used
    to copy each file. It will be called with the source path and the
    destination path as arguments. By default, copy2() is used, but any
    function that supports the same signature (like copy()) can be used.

    """
    
    title = 'copytree'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
        NodeInputBP(label='symlinks', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='ignore', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='copy_function', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='ignore_dangling_symlinks', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='dirs_exist_ok', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.copytree(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        

class Disk_Usage_Node(NodeBase):
    """
    Return disk usage statistics about the given path.

        Returned values is a named tuple with attributes 'total', 'used' and
        'free', which are the amount of total, used and free space, in bytes.
        """
    
    title = 'disk_usage'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.disk_usage(self.input(0)))
        

class Get_Archive_Formats_Node(NodeBase):
    """
    Returns a list of supported formats for archiving and unarchiving.

    Each element of the returned sequence is a tuple (name, description)
    """
    
    title = 'get_archive_formats'
    type_ = 'shutil'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.get_archive_formats())
        

class Get_Terminal_Size_Node(NodeBase):
    """
    Get the size of the terminal window.

    For each of the two dimensions, the environment variable, COLUMNS
    and LINES respectively, is checked. If the variable is defined and
    the value is a positive integer, it is used.

    When COLUMNS or LINES is not defined, which is the common case,
    the terminal connected to sys.__stdout__ is queried
    by invoking os.get_terminal_size.

    If the terminal size cannot be successfully queried, either because
    the system doesn't support querying, or because we are not
    connected to a terminal, the value given in fallback parameter
    is used. Fallback defaults to (80, 24) which is the default
    size used by many terminal emulators.

    The value returned is a named tuple of type os.terminal_size.
    """
    
    title = 'get_terminal_size'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='fallback', dtype=dtypes.Data(default=(80, 24), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.get_terminal_size(self.input(0)))
        

class Get_Unpack_Formats_Node(NodeBase):
    """
    Returns a list of supported formats for unpacking.

    Each element of the returned sequence is a tuple
    (name, extensions, description)
    """
    
    title = 'get_unpack_formats'
    type_ = 'shutil'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.get_unpack_formats())
        

class Ignore_Patterns_Node(NodeBase):
    """
    Function that can be used as copytree() ignore parameter.

    Patterns is a sequence of glob-style patterns
    that are used to exclude files"""
    
    title = 'ignore_patterns'
    type_ = 'shutil'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.ignore_patterns())
        

class Make_Archive_Node(NodeBase):
    """
    Create an archive file (eg. zip or tar).

    'base_name' is the name of the file to create, minus any format-specific
    extension; 'format' is the archive format: one of "zip", "tar", "gztar",
    "bztar", or "xztar".  Or any other registered format.

    'root_dir' is a directory that will be the root directory of the
    archive; ie. we typically chdir into 'root_dir' before creating the
    archive.  'base_dir' is the directory where we start archiving from;
    ie. 'base_dir' will be the common prefix of all files and
    directories in the archive.  'root_dir' and 'base_dir' both default
    to the current directory.  Returns the name of the archive file.

    'owner' and 'group' are used when creating a tar archive. By default,
    uses the current owner and group.
    """
    
    title = 'make_archive'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='base_name'),
        NodeInputBP(label='format'),
        NodeInputBP(label='root_dir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='base_dir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='verbose', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='dry_run', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='owner', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='group', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='logger', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.make_archive(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7), self.input(8)))
        

class Move_Node(NodeBase):
    """
    Recursively move a file or directory to another location. This is
    similar to the Unix "mv" command. Return the file or directory's
    destination.

    If the destination is a directory or a symlink to a directory, the source
    is moved inside the directory. The destination path must not already
    exist.

    If the destination already exists but is not a directory, it may be
    overwritten depending on os.rename() semantics.

    If the destination is on our current filesystem, then rename() is used.
    Otherwise, src is copied to the destination and then removed. Symlinks are
    recreated under the new name if os.rename() fails because of cross
    filesystem renames.

    The optional `copy_function` argument is a callable that will be used
    to copy the source or it will be delegated to `copytree`.
    By default, copy2() is used, but any function that supports the same
    signature (like copy()) can be used.

    A lot more could be done here...  A look at a mv.c shows a lot of
    the issues this implementation glosses over.

    """
    
    title = 'move'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
        NodeInputBP(label='copy_function', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.move(self.input(0), self.input(1), self.input(2)))
        

class Register_Archive_Format_Node(NodeBase):
    """
    Registers an archive format.

    name is the name of the format. function is the callable that will be
    used to create archives. If provided, extra_args is a sequence of
    (name, value) tuples that will be passed as arguments to the callable.
    description can be provided to describe the format, and will be returned
    by the get_archive_formats() function.
    """
    
    title = 'register_archive_format'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='function'),
        NodeInputBP(label='extra_args', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='description', dtype=dtypes.Data(default='', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.register_archive_format(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Register_Unpack_Format_Node(NodeBase):
    """
    Registers an unpack format.

    `name` is the name of the format. `extensions` is a list of extensions
    corresponding to the format.

    `function` is the callable that will be
    used to unpack archives. The callable will receive archives to unpack.
    If it's unable to handle an archive, it needs to raise a ReadError
    exception.

    If provided, `extra_args` is a sequence of
    (name, value) tuples that will be passed as arguments to the callable.
    description can be provided to describe the format, and will be returned
    by the get_unpack_formats() function.
    """
    
    title = 'register_unpack_format'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='extensions'),
        NodeInputBP(label='function'),
        NodeInputBP(label='extra_args', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='description', dtype=dtypes.Data(default='', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.register_unpack_format(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Rmtree_Node(NodeBase):
    """
    Recursively delete a directory tree.

    If ignore_errors is set, errors are ignored; otherwise, if onerror
    is set, it is called to handle the error with arguments (func,
    path, exc_info) where func is platform and implementation dependent;
    path is the argument to that function that caused it to fail; and
    exc_info is a tuple returned by sys.exc_info().  If ignore_errors
    is false and onerror is None, an exception is raised.

    """
    
    title = 'rmtree'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='ignore_errors', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='onerror', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.rmtree(self.input(0), self.input(1), self.input(2)))
        

class Unpack_Archive_Node(NodeBase):
    """
    Unpack an archive.

    `filename` is the name of the archive.

    `extract_dir` is the name of the target directory, where the archive
    is unpacked. If not provided, the current working directory is used.

    `format` is the archive format: one of "zip", "tar", "gztar", "bztar",
    or "xztar".  Or any other registered format.  If not provided,
    unpack_archive will use the filename extension and see if an unpacker
    was registered for that extension.

    In case none is found, a ValueError is raised.
    """
    
    title = 'unpack_archive'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='extract_dir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='format', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.unpack_archive(self.input(0), self.input(1), self.input(2)))
        

class Unregister_Archive_Format_Node(NodeBase):
    """
    """
    
    title = 'unregister_archive_format'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.unregister_archive_format(self.input(0)))
        

class Unregister_Unpack_Format_Node(NodeBase):
    """
    Removes the pack format from the registry."""
    
    title = 'unregister_unpack_format'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.unregister_unpack_format(self.input(0)))
        

class Which_Node(NodeBase):
    """
    Given a command, mode, and a PATH string, return the path which
    conforms to the given mode on the PATH, or None if there is no such
    file.

    `mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
    of os.environ.get("PATH"), or can be overridden with a custom search
    path.

    """
    
    title = 'which'
    type_ = 'shutil'
    init_inputs = [
        NodeInputBP(label='cmd'),
        NodeInputBP(label='mode', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='path', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shutil.which(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _Access_Check_Node,
    _Basename_Node,
    _Check_Unpack_Options_Node,
    _Copyfileobj_Readinto_Node,
    _Copytree_Node,
    _Copyxattr_Node,
    _Destinsrc_Node,
    _Ensure_Directory_Node,
    _Fastcopy_Fcopyfile_Node,
    _Fastcopy_Sendfile_Node,
    _Find_Unpack_Format_Node,
    _Get_Gid_Node,
    _Get_Uid_Node,
    _Is_Immutable_Node,
    _Islink_Node,
    _Make_Tarball_Node,
    _Make_Zipfile_Node,
    _Rmtree_Isdir_Node,
    _Rmtree_Islink_Node,
    _Rmtree_Safe_Fd_Node,
    _Rmtree_Unsafe_Node,
    _Samefile_Node,
    _Stat_Node,
    _Unpack_Tarfile_Node,
    _Unpack_Zipfile_Node,
    Chown_Node,
    Copy_Node,
    Copy2_Node,
    Copyfile_Node,
    Copyfileobj_Node,
    Copymode_Node,
    Copystat_Node,
    Copytree_Node,
    Disk_Usage_Node,
    Get_Archive_Formats_Node,
    Get_Terminal_Size_Node,
    Get_Unpack_Formats_Node,
    Ignore_Patterns_Node,
    Make_Archive_Node,
    Move_Node,
    Register_Archive_Format_Node,
    Register_Unpack_Format_Node,
    Rmtree_Node,
    Unpack_Archive_Node,
    Unregister_Archive_Format_Node,
    Unregister_Unpack_Format_Node,
    Which_Node,
)
