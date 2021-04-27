
from NENV import *

import genericpath


class NodeBase(Node):
    pass


class _Check_Arg_Types_Node(NodeBase):
    title = '_check_arg_types'
    type_ = 'genericpath'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='funcname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, genericpath._check_arg_types(self.input(0)))
        

class _Splitext_Node(NodeBase):
    title = '_splitext'
    type_ = 'genericpath'
    doc = """Split the extension from a pathname.

    Extension is everything from the last dot to the end, ignoring
    leading dots.  Returns "(root, ext)"; ext may be empty."""
    init_inputs = [
        NodeInputBP(label='p'),
        NodeInputBP(label='sep'),
        NodeInputBP(label='altsep'),
        NodeInputBP(label='extsep'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, genericpath._splitext(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Commonprefix_Node(NodeBase):
    title = 'commonprefix'
    type_ = 'genericpath'
    doc = """Given a list of pathnames, returns the longest common leading component"""
    init_inputs = [
        NodeInputBP(label='m'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, genericpath.commonprefix(self.input(0)))
        

class Exists_Node(NodeBase):
    title = 'exists'
    type_ = 'genericpath'
    doc = """Test whether a path exists.  Returns False for broken symbolic links"""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, genericpath.exists(self.input(0)))
        

class Getatime_Node(NodeBase):
    title = 'getatime'
    type_ = 'genericpath'
    doc = """Return the last access time of a file, reported by os.stat()."""
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, genericpath.getatime(self.input(0)))
        

class Getctime_Node(NodeBase):
    title = 'getctime'
    type_ = 'genericpath'
    doc = """Return the metadata change time of a file, reported by os.stat()."""
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, genericpath.getctime(self.input(0)))
        

class Getmtime_Node(NodeBase):
    title = 'getmtime'
    type_ = 'genericpath'
    doc = """Return the last modification time of a file, reported by os.stat()."""
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, genericpath.getmtime(self.input(0)))
        

class Getsize_Node(NodeBase):
    title = 'getsize'
    type_ = 'genericpath'
    doc = """Return the size of a file, reported by os.stat()."""
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, genericpath.getsize(self.input(0)))
        

class Isdir_Node(NodeBase):
    title = 'isdir'
    type_ = 'genericpath'
    doc = """Return true if the pathname refers to an existing directory."""
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, genericpath.isdir(self.input(0)))
        

class Isfile_Node(NodeBase):
    title = 'isfile'
    type_ = 'genericpath'
    doc = """Test whether a path is a regular file"""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, genericpath.isfile(self.input(0)))
        

class Samefile_Node(NodeBase):
    title = 'samefile'
    type_ = 'genericpath'
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
        self.set_output_val(0, genericpath.samefile(self.input(0), self.input(1)))
        

class Sameopenfile_Node(NodeBase):
    title = 'sameopenfile'
    type_ = 'genericpath'
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
        self.set_output_val(0, genericpath.sameopenfile(self.input(0), self.input(1)))
        

class Samestat_Node(NodeBase):
    title = 'samestat'
    type_ = 'genericpath'
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
        self.set_output_val(0, genericpath.samestat(self.input(0), self.input(1)))
        


export_nodes(
    _Check_Arg_Types_Node,
    _Splitext_Node,
    Commonprefix_Node,
    Exists_Node,
    Getatime_Node,
    Getctime_Node,
    Getmtime_Node,
    Getsize_Node,
    Isdir_Node,
    Isfile_Node,
    Samefile_Node,
    Sameopenfile_Node,
    Samestat_Node,
)
