
from NENV import *

import posixpath


class NodeBase(Node):
    pass


class _Get_Sep_Node(NodeBase):
    title = '_get_sep'
    type_ = 'posixpath'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath._get_sep(self.input(0)))
        

class _Joinrealpath_Node(NodeBase):
    title = '_joinrealpath'
    type_ = 'posixpath'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='rest'),
        NodeInputBP(label='seen'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath._joinrealpath(self.input(0), self.input(1), self.input(2)))
        

class Abspath_Node(NodeBase):
    title = 'abspath'
    type_ = 'posixpath'
    doc = """Return an absolute path."""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.abspath(self.input(0)))
        

class Basename_Node(NodeBase):
    title = 'basename'
    type_ = 'posixpath'
    doc = """Returns the final component of a pathname"""
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.basename(self.input(0)))
        

class Commonpath_Node(NodeBase):
    title = 'commonpath'
    type_ = 'posixpath'
    doc = """Given a sequence of path names, returns the longest common sub-path."""
    init_inputs = [
        NodeInputBP(label='paths'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.commonpath(self.input(0)))
        

class Commonprefix_Node(NodeBase):
    title = 'commonprefix'
    type_ = 'posixpath'
    doc = """Given a list of pathnames, returns the longest common leading component"""
    init_inputs = [
        NodeInputBP(label='m'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.commonprefix(self.input(0)))
        

class Dirname_Node(NodeBase):
    title = 'dirname'
    type_ = 'posixpath'
    doc = """Returns the directory component of a pathname"""
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.dirname(self.input(0)))
        

class Exists_Node(NodeBase):
    title = 'exists'
    type_ = 'posixpath'
    doc = """Test whether a path exists.  Returns False for broken symbolic links"""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.exists(self.input(0)))
        

class Expanduser_Node(NodeBase):
    title = 'expanduser'
    type_ = 'posixpath'
    doc = """Expand ~ and ~user constructions.  If user or $HOME is unknown,
    do nothing."""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.expanduser(self.input(0)))
        

class Expandvars_Node(NodeBase):
    title = 'expandvars'
    type_ = 'posixpath'
    doc = """Expand shell variables of form $var and ${var}.  Unknown variables
    are left unchanged."""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.expandvars(self.input(0)))
        

class Getatime_Node(NodeBase):
    title = 'getatime'
    type_ = 'posixpath'
    doc = """Return the last access time of a file, reported by os.stat()."""
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.getatime(self.input(0)))
        

class Getctime_Node(NodeBase):
    title = 'getctime'
    type_ = 'posixpath'
    doc = """Return the metadata change time of a file, reported by os.stat()."""
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.getctime(self.input(0)))
        

class Getmtime_Node(NodeBase):
    title = 'getmtime'
    type_ = 'posixpath'
    doc = """Return the last modification time of a file, reported by os.stat()."""
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.getmtime(self.input(0)))
        

class Getsize_Node(NodeBase):
    title = 'getsize'
    type_ = 'posixpath'
    doc = """Return the size of a file, reported by os.stat()."""
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.getsize(self.input(0)))
        

class Isabs_Node(NodeBase):
    title = 'isabs'
    type_ = 'posixpath'
    doc = """Test whether a path is absolute"""
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.isabs(self.input(0)))
        

class Isdir_Node(NodeBase):
    title = 'isdir'
    type_ = 'posixpath'
    doc = """Return true if the pathname refers to an existing directory."""
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.isdir(self.input(0)))
        

class Isfile_Node(NodeBase):
    title = 'isfile'
    type_ = 'posixpath'
    doc = """Test whether a path is a regular file"""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.isfile(self.input(0)))
        

class Islink_Node(NodeBase):
    title = 'islink'
    type_ = 'posixpath'
    doc = """Test whether a path is a symbolic link"""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.islink(self.input(0)))
        

class Ismount_Node(NodeBase):
    title = 'ismount'
    type_ = 'posixpath'
    doc = """Test whether a path is a mount point"""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.ismount(self.input(0)))
        

class Join_Node(NodeBase):
    title = 'join'
    type_ = 'posixpath'
    doc = """Join two or more pathname components, inserting '/' as needed.
    If any component is an absolute path, all previous path components
    will be discarded.  An empty last part will result in a path that
    ends with a separator."""
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.join(self.input(0)))
        

class Lexists_Node(NodeBase):
    title = 'lexists'
    type_ = 'posixpath'
    doc = """Test whether a path exists.  Returns True for broken symbolic links"""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.lexists(self.input(0)))
        

class Normcase_Node(NodeBase):
    title = 'normcase'
    type_ = 'posixpath'
    doc = """Normalize case of pathname.  Has no effect under Posix"""
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.normcase(self.input(0)))
        

class Normpath_Node(NodeBase):
    title = 'normpath'
    type_ = 'posixpath'
    doc = """Normalize path, eliminating double slashes, etc."""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.normpath(self.input(0)))
        

class Realpath_Node(NodeBase):
    title = 'realpath'
    type_ = 'posixpath'
    doc = """Return the canonical path of the specified filename, eliminating any
symbolic links encountered in the path."""
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.realpath(self.input(0)))
        

class Relpath_Node(NodeBase):
    title = 'relpath'
    type_ = 'posixpath'
    doc = """Return a relative version of a path"""
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='start', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.relpath(self.input(0), self.input(1)))
        

class Samefile_Node(NodeBase):
    title = 'samefile'
    type_ = 'posixpath'
    doc = """Test whether two pathnames reference the same actual file or directory

    This is determined by the device number and i-node number and
    raises an exception if an os.stat() call on either pathname fails.
    """
    init_inputs = [
        NodeInputBP(label='f1'),
        NodeInputBP(label='f2'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.samefile(self.input(0), self.input(1)))
        

class Sameopenfile_Node(NodeBase):
    title = 'sameopenfile'
    type_ = 'posixpath'
    doc = """Test whether two open file objects reference the same file"""
    init_inputs = [
        NodeInputBP(label='fp1'),
        NodeInputBP(label='fp2'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.sameopenfile(self.input(0), self.input(1)))
        

class Samestat_Node(NodeBase):
    title = 'samestat'
    type_ = 'posixpath'
    doc = """Test whether two stat buffers reference the same file"""
    init_inputs = [
        NodeInputBP(label='s1'),
        NodeInputBP(label='s2'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.samestat(self.input(0), self.input(1)))
        

class Split_Node(NodeBase):
    title = 'split'
    type_ = 'posixpath'
    doc = """Split a pathname.  Returns tuple "(head, tail)" where "tail" is
    everything after the final slash.  Either part may be empty."""
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.split(self.input(0)))
        

class Splitdrive_Node(NodeBase):
    title = 'splitdrive'
    type_ = 'posixpath'
    doc = """Split a pathname into drive and path. On Posix, drive is always
    empty."""
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.splitdrive(self.input(0)))
        

class Splitext_Node(NodeBase):
    title = 'splitext'
    type_ = 'posixpath'
    doc = """Split the extension from a pathname.

    Extension is everything from the last dot to the end, ignoring
    leading dots.  Returns "(root, ext)"; ext may be empty."""
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, posixpath.splitext(self.input(0)))
        


export_nodes(
    _Get_Sep_Node,
    _Joinrealpath_Node,
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
