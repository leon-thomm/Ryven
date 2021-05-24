
from NENV import *

import filecmp


class NodeBase(Node):
    pass


class _Cmp_Node(NodeBase):
    """
    """
    
    title = '_cmp'
    type_ = 'filecmp'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
        NodeInputBP(label='sh'),
        NodeInputBP(label='abs', dtype=dtypes.Data(default=<built-in function abs>, size='s')),
        NodeInputBP(label='cmp', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, filecmp._cmp(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class _Do_Cmp_Node(NodeBase):
    """
    """
    
    title = '_do_cmp'
    type_ = 'filecmp'
    init_inputs = [
        NodeInputBP(label='f1'),
        NodeInputBP(label='f2'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, filecmp._do_cmp(self.input(0), self.input(1)))
        

class _Filter_Node(NodeBase):
    """
    """
    
    title = '_filter'
    type_ = 'filecmp'
    init_inputs = [
        NodeInputBP(label='flist'),
        NodeInputBP(label='skip'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, filecmp._filter(self.input(0), self.input(1)))
        

class _Sig_Node(NodeBase):
    """
    """
    
    title = '_sig'
    type_ = 'filecmp'
    init_inputs = [
        NodeInputBP(label='st'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, filecmp._sig(self.input(0)))
        

class Clear_Cache_Node(NodeBase):
    """
    Clear the filecmp cache."""
    
    title = 'clear_cache'
    type_ = 'filecmp'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, filecmp.clear_cache())
        

class Cmp_Node(NodeBase):
    """
    Compare two files.

    Arguments:

    f1 -- First file name

    f2 -- Second file name

    shallow -- Just check stat signature (do not read the files).
               defaults to True.

    Return value:

    True if the files are the same, False otherwise.

    This function uses a cache for past comparisons and the results,
    with cache entries invalidated if their stat information
    changes.  The cache may be cleared by calling clear_cache().

    """
    
    title = 'cmp'
    type_ = 'filecmp'
    init_inputs = [
        NodeInputBP(label='f1'),
        NodeInputBP(label='f2'),
        NodeInputBP(label='shallow', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, filecmp.cmp(self.input(0), self.input(1), self.input(2)))
        

class Cmpfiles_Node(NodeBase):
    """
    Compare common files in two directories.

    a, b -- directory names
    common -- list of file names found in both directories
    shallow -- if true, do comparison based solely on stat() information

    Returns a tuple of three lists:
      files that compare equal
      files that are different
      filenames that aren't regular files.

    """
    
    title = 'cmpfiles'
    type_ = 'filecmp'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
        NodeInputBP(label='common'),
        NodeInputBP(label='shallow', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, filecmp.cmpfiles(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Demo_Node(NodeBase):
    """
    """
    
    title = 'demo'
    type_ = 'filecmp'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, filecmp.demo())
        


export_nodes(
    _Cmp_Node,
    _Do_Cmp_Node,
    _Filter_Node,
    _Sig_Node,
    Clear_Cache_Node,
    Cmp_Node,
    Cmpfiles_Node,
    Demo_Node,
)
