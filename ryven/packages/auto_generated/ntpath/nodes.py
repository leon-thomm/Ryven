
from NENV import *

import ntpath


class NodeBase(Node):
    pass


class _Abspath_Fallback_Node(NodeBase):
    """
    Return the absolute version of a path as a fallback function in case
    `nt._getfullpathname` is not available or raises OSError. See bpo-31047 for
    more.

    """
    
    title = '_abspath_fallback'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath._abspath_fallback(self.input(0)))
        

class _Get_Bothseps_Node(NodeBase):
    """
    """
    
    title = '_get_bothseps'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath._get_bothseps(self.input(0)))
        

class _Getfinalpathname_Node(NodeBase):
    """
    A helper function for samepath on windows."""
    
    title = '_getfinalpathname'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath._getfinalpathname(self.input(0)))
        

class _Getfinalpathname_Nonstrict_Node(NodeBase):
    """
    """
    
    title = '_getfinalpathname_nonstrict'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath._getfinalpathname_nonstrict(self.input(0)))
        

class _Getfullpathname_Node(NodeBase):
    """
    """
    
    title = '_getfullpathname'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath._getfullpathname(self.input(0)))
        

class _Getvolumepathname_Node(NodeBase):
    """
    A helper function for ismount on Win32."""
    
    title = '_getvolumepathname'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath._getvolumepathname(self.input(0)))
        

class _Nt_Readlink_Node(NodeBase):
    """
    Return a string representing the path to which the symbolic link points.

If dir_fd is not None, it should be a file descriptor open to a directory,
and path should be relative; path will then be relative to that directory.

dir_fd may not be implemented on your platform.  If it is unavailable,
using it will raise a NotImplementedError."""
    
    title = '_nt_readlink'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath._nt_readlink(self.input(0)))
        

class _Readlink_Deep_Node(NodeBase):
    """
    """
    
    title = '_readlink_deep'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath._readlink_deep(self.input(0)))
        

class Abspath_Node(NodeBase):
    """
    Return the absolute version of a path."""
    
    title = 'abspath'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.abspath(self.input(0)))
        

class Basename_Node(NodeBase):
    """
    Returns the final component of a pathname"""
    
    title = 'basename'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.basename(self.input(0)))
        

class Commonpath_Node(NodeBase):
    """
    Given a sequence of path names, returns the longest common sub-path."""
    
    title = 'commonpath'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='paths'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.commonpath(self.input(0)))
        

class Commonprefix_Node(NodeBase):
    """
    Given a list of pathnames, returns the longest common leading component"""
    
    title = 'commonprefix'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='m'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.commonprefix(self.input(0)))
        

class Dirname_Node(NodeBase):
    """
    Returns the directory component of a pathname"""
    
    title = 'dirname'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.dirname(self.input(0)))
        

class Exists_Node(NodeBase):
    """
    Test whether a path exists.  Returns False for broken symbolic links"""
    
    title = 'exists'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.exists(self.input(0)))
        

class Expanduser_Node(NodeBase):
    """
    Expand ~ and ~user constructs.

    If user or $HOME is unknown, do nothing."""
    
    title = 'expanduser'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.expanduser(self.input(0)))
        

class Expandvars_Node(NodeBase):
    """
    Expand shell variables of the forms $var, ${var} and %var%.

    Unknown variables are left unchanged."""
    
    title = 'expandvars'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.expandvars(self.input(0)))
        

class Getatime_Node(NodeBase):
    """
    Return the last access time of a file, reported by os.stat()."""
    
    title = 'getatime'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.getatime(self.input(0)))
        

class Getctime_Node(NodeBase):
    """
    Return the metadata change time of a file, reported by os.stat()."""
    
    title = 'getctime'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.getctime(self.input(0)))
        

class Getmtime_Node(NodeBase):
    """
    Return the last modification time of a file, reported by os.stat()."""
    
    title = 'getmtime'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.getmtime(self.input(0)))
        

class Getsize_Node(NodeBase):
    """
    Return the size of a file, reported by os.stat()."""
    
    title = 'getsize'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.getsize(self.input(0)))
        

class Isabs_Node(NodeBase):
    """
    Test whether a path is absolute"""
    
    title = 'isabs'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.isabs(self.input(0)))
        

class Isdir_Node(NodeBase):
    """
    Return true if the pathname refers to an existing directory."""
    
    title = 'isdir'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.isdir(self.input(0)))
        

class Isfile_Node(NodeBase):
    """
    Test whether a path is a regular file"""
    
    title = 'isfile'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.isfile(self.input(0)))
        

class Islink_Node(NodeBase):
    """
    Test whether a path is a symbolic link.
    This will always return false for Windows prior to 6.0.
    """
    
    title = 'islink'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.islink(self.input(0)))
        

class Ismount_Node(NodeBase):
    """
    Test whether a path is a mount point (a drive root, the root of a
    share, or a mounted volume)"""
    
    title = 'ismount'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.ismount(self.input(0)))
        

class Join_Node(NodeBase):
    """
    """
    
    title = 'join'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.join(self.input(0)))
        

class Lexists_Node(NodeBase):
    """
    Test whether a path exists.  Returns True for broken symbolic links"""
    
    title = 'lexists'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.lexists(self.input(0)))
        

class Normcase_Node(NodeBase):
    """
    Normalize case of pathname.

    Makes all characters lowercase and all slashes into backslashes."""
    
    title = 'normcase'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.normcase(self.input(0)))
        

class Normpath_Node(NodeBase):
    """
    Normalize path, eliminating double slashes, etc."""
    
    title = 'normpath'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.normpath(self.input(0)))
        

class Realpath_Node(NodeBase):
    """
    """
    
    title = 'realpath'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.realpath(self.input(0)))
        

class Relpath_Node(NodeBase):
    """
    Return a relative version of a path"""
    
    title = 'relpath'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='start', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.relpath(self.input(0), self.input(1)))
        

class Samefile_Node(NodeBase):
    """
    Test whether two pathnames reference the same actual file or directory

    This is determined by the device number and i-node number and
    raises an exception if an os.stat() call on either pathname fails.
    """
    
    title = 'samefile'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='f1'),
        NodeInputBP(label='f2'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.samefile(self.input(0), self.input(1)))
        

class Sameopenfile_Node(NodeBase):
    """
    Test whether two open file objects reference the same file"""
    
    title = 'sameopenfile'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='fp1'),
        NodeInputBP(label='fp2'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.sameopenfile(self.input(0), self.input(1)))
        

class Samestat_Node(NodeBase):
    """
    Test whether two stat buffers reference the same file"""
    
    title = 'samestat'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='s1'),
        NodeInputBP(label='s2'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.samestat(self.input(0), self.input(1)))
        

class Split_Node(NodeBase):
    """
    Split a pathname.

    Return tuple (head, tail) where tail is everything after the final slash.
    Either part may be empty."""
    
    title = 'split'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.split(self.input(0)))
        

class Splitdrive_Node(NodeBase):
    """
    Split a pathname into drive/UNC sharepoint and relative path specifiers.
    Returns a 2-tuple (drive_or_unc, path); either part may be empty.

    If you assign
        result = splitdrive(p)
    It is always true that:
        result[0] + result[1] == p

    If the path contained a drive letter, drive_or_unc will contain everything
    up to and including the colon.  e.g. splitdrive("c:/dir") returns ("c:", "/dir")

    If the path contained a UNC path, the drive_or_unc will contain the host name
    and share up to but not including the fourth directory separator character.
    e.g. splitdrive("//host/computer/dir") returns ("//host/computer", "/dir")

    Paths cannot contain both a drive letter and a UNC path.

    """
    
    title = 'splitdrive'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.splitdrive(self.input(0)))
        

class Splitext_Node(NodeBase):
    """
    Split the extension from a pathname.

    Extension is everything from the last dot to the end, ignoring
    leading dots.  Returns "(root, ext)"; ext may be empty."""
    
    title = 'splitext'
    type_ = 'ntpath'
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ntpath.splitext(self.input(0)))
        


export_nodes(
    _Abspath_Fallback_Node,
    _Get_Bothseps_Node,
    _Getfinalpathname_Node,
    _Getfinalpathname_Nonstrict_Node,
    _Getfullpathname_Node,
    _Getvolumepathname_Node,
    _Nt_Readlink_Node,
    _Readlink_Deep_Node,
    Abspath_Node,
    Basename_Node,
    Commonpath_Node,
    Commonprefix_Node,
    Dirname_Node,
    Exists_Node,
    Expanduser_Node,
    Expandvars_Node,
    Getatime_Node,
    Getctime_Node,
    Getmtime_Node,
    Getsize_Node,
    Isabs_Node,
    Isdir_Node,
    Isfile_Node,
    Islink_Node,
    Ismount_Node,
    Join_Node,
    Lexists_Node,
    Normcase_Node,
    Normpath_Node,
    Realpath_Node,
    Relpath_Node,
    Samefile_Node,
    Sameopenfile_Node,
    Samestat_Node,
    Split_Node,
    Splitdrive_Node,
    Splitext_Node,
)
