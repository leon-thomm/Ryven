
from ryven.NENV import *

import tempfile


class NodeBase(Node):
    pass


class Namedtemporaryfile_Node(NodeBase):
    """
    Create and return a temporary file.
    Arguments:
    'prefix', 'suffix', 'dir' -- as for mkstemp.
    'mode' -- the mode argument to io.open (default "w+b").
    'buffering' -- the buffer size argument to io.open (default -1).
    'encoding' -- the encoding argument to io.open (default None)
    'newline' -- the newline argument to io.open (default None)
    'delete' -- whether the file is deleted on close (default True).
    'errors' -- the errors argument to io.open (default None)
    The file is created as mkstemp() would do it.

    Returns an object with a file-like interface; the name of the file
    is accessible as its 'name' attribute.  The file will be automatically
    deleted when it is closed unless the 'delete' argument is set to False.
    """
    
    title = 'NamedTemporaryFile'
    type_ = 'tempfile'
    init_inputs = [
        NodeInputBP(label='mode', dtype=dtypes.Data(default='w+b', size='s')),
        NodeInputBP(label='buffering', dtype=dtypes.Data(default=-1, size='s')),
        NodeInputBP(label='encoding', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='newline', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='suffix', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='prefix', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='dir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='delete', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile.NamedTemporaryFile(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        

class Temporaryfile_Node(NodeBase):
    """
    Create and return a temporary file.
    Arguments:
    'prefix', 'suffix', 'dir' -- as for mkstemp.
    'mode' -- the mode argument to io.open (default "w+b").
    'buffering' -- the buffer size argument to io.open (default -1).
    'encoding' -- the encoding argument to io.open (default None)
    'newline' -- the newline argument to io.open (default None)
    'delete' -- whether the file is deleted on close (default True).
    'errors' -- the errors argument to io.open (default None)
    The file is created as mkstemp() would do it.

    Returns an object with a file-like interface; the name of the file
    is accessible as its 'name' attribute.  The file will be automatically
    deleted when it is closed unless the 'delete' argument is set to False.
    """
    
    title = 'TemporaryFile'
    type_ = 'tempfile'
    init_inputs = [
        NodeInputBP(label='mode', dtype=dtypes.Data(default='w+b', size='s')),
        NodeInputBP(label='buffering', dtype=dtypes.Data(default=-1, size='s')),
        NodeInputBP(label='encoding', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='newline', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='suffix', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='prefix', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='dir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='delete', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile.TemporaryFile(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        

class _Candidate_Tempdir_List_Node(NodeBase):
    """
    Generate a list of candidate temporary directories which
    _get_default_tempdir will try."""
    
    title = '_candidate_tempdir_list'
    type_ = 'tempfile'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile._candidate_tempdir_list())
        

class _Exists_Node(NodeBase):
    """
    """
    
    title = '_exists'
    type_ = 'tempfile'
    init_inputs = [
        NodeInputBP(label='fn'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile._exists(self.input(0)))
        

class _Get_Candidate_Names_Node(NodeBase):
    """
    Common setup sequence for all user-callable interfaces."""
    
    title = '_get_candidate_names'
    type_ = 'tempfile'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile._get_candidate_names())
        

class _Get_Default_Tempdir_Node(NodeBase):
    """
    Calculate the default directory to use for temporary files.
    This routine should be called exactly once.

    We determine whether or not a candidate temp dir is usable by
    trying to create and write to a file in that directory.  If this
    is successful, the test file is deleted.  To prevent denial of
    service, the name of the test file must be randomized."""
    
    title = '_get_default_tempdir'
    type_ = 'tempfile'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile._get_default_tempdir())
        

class _Infer_Return_Type_Node(NodeBase):
    """
    Look at the type of all args and divine their implied return type."""
    
    title = '_infer_return_type'
    type_ = 'tempfile'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile._infer_return_type())
        

class _Mkstemp_Inner_Node(NodeBase):
    """
    Code common to mkstemp, TemporaryFile, and NamedTemporaryFile."""
    
    title = '_mkstemp_inner'
    type_ = 'tempfile'
    init_inputs = [
        NodeInputBP(label='dir'),
        NodeInputBP(label='pre'),
        NodeInputBP(label='suf'),
        NodeInputBP(label='flags'),
        NodeInputBP(label='output_type'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile._mkstemp_inner(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class _Sanitize_Params_Node(NodeBase):
    """
    Common parameter processing for most APIs in this module."""
    
    title = '_sanitize_params'
    type_ = 'tempfile'
    init_inputs = [
        NodeInputBP(label='prefix'),
        NodeInputBP(label='suffix'),
        NodeInputBP(label='dir'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile._sanitize_params(self.input(0), self.input(1), self.input(2)))
        

class Gettempdir_Node(NodeBase):
    """
    Accessor for tempfile.tempdir."""
    
    title = 'gettempdir'
    type_ = 'tempfile'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile.gettempdir())
        

class Gettempdirb_Node(NodeBase):
    """
    A bytes version of tempfile.gettempdir()."""
    
    title = 'gettempdirb'
    type_ = 'tempfile'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile.gettempdirb())
        

class Gettempprefix_Node(NodeBase):
    """
    The default prefix for temporary directories."""
    
    title = 'gettempprefix'
    type_ = 'tempfile'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile.gettempprefix())
        

class Gettempprefixb_Node(NodeBase):
    """
    The default prefix for temporary directories as bytes."""
    
    title = 'gettempprefixb'
    type_ = 'tempfile'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile.gettempprefixb())
        

class Mkdtemp_Node(NodeBase):
    """
    User-callable function to create and return a unique temporary
    directory.  The return value is the pathname of the directory.

    Arguments are as for mkstemp, except that the 'text' argument is
    not accepted.

    The directory is readable, writable, and searchable only by the
    creating user.

    Caller is responsible for deleting the directory when done with it.
    """
    
    title = 'mkdtemp'
    type_ = 'tempfile'
    init_inputs = [
        NodeInputBP(label='suffix', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='prefix', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='dir', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile.mkdtemp(self.input(0), self.input(1), self.input(2)))
        

class Mkstemp_Node(NodeBase):
    """
    User-callable function to create and return a unique temporary
    file.  The return value is a pair (fd, name) where fd is the
    file descriptor returned by os.open, and name is the filename.

    If 'suffix' is not None, the file name will end with that suffix,
    otherwise there will be no suffix.

    If 'prefix' is not None, the file name will begin with that prefix,
    otherwise a default prefix is used.

    If 'dir' is not None, the file will be created in that directory,
    otherwise a default directory is used.

    If 'text' is specified and true, the file is opened in text
    mode.  Else (the default) the file is opened in binary mode.

    If any of 'suffix', 'prefix' and 'dir' are not None, they must be the
    same type.  If they are bytes, the returned name will be bytes; str
    otherwise.

    The file is readable and writable only by the creating user ID.
    If the operating system uses permission bits to indicate whether a
    file is executable, the file is executable by no one. The file
    descriptor is not inherited by children of this process.

    Caller is responsible for deleting the file when done with it.
    """
    
    title = 'mkstemp'
    type_ = 'tempfile'
    init_inputs = [
        NodeInputBP(label='suffix', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='prefix', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='dir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='text', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile.mkstemp(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Mktemp_Node(NodeBase):
    """
    User-callable function to return a unique temporary file name.  The
    file is not created.

    Arguments are similar to mkstemp, except that the 'text' argument is
    not accepted, and suffix=None, prefix=None and bytes file names are not
    supported.

    THIS FUNCTION IS UNSAFE AND SHOULD NOT BE USED.  The file name may
    refer to a file that did not exist at some point, but by the time
    you get around to creating it, someone else may have beaten you to
    the punch.
    """
    
    title = 'mktemp'
    type_ = 'tempfile'
    init_inputs = [
        NodeInputBP(label='suffix', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='prefix', dtype=dtypes.Data(default='tmp', size='s')),
        NodeInputBP(label='dir', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tempfile.mktemp(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    Namedtemporaryfile_Node,
    Temporaryfile_Node,
    _Candidate_Tempdir_List_Node,
    _Exists_Node,
    _Get_Candidate_Names_Node,
    _Get_Default_Tempdir_Node,
    _Infer_Return_Type_Node,
    _Mkstemp_Inner_Node,
    _Sanitize_Params_Node,
    Gettempdir_Node,
    Gettempdirb_Node,
    Gettempprefix_Node,
    Gettempprefixb_Node,
    Mkdtemp_Node,
    Mkstemp_Node,
    Mktemp_Node,
)
