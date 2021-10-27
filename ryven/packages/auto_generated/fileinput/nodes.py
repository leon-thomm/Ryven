
from NENV import *

import fileinput


class NodeBase(Node):
    pass


class _Test_Node(NodeBase):
    """
    """
    
    title = '_test'
    type_ = 'fileinput'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fileinput._test())
        

class Close_Node(NodeBase):
    """
    Close the sequence."""
    
    title = 'close'
    type_ = 'fileinput'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fileinput.close())
        

class Filelineno_Node(NodeBase):
    """
    
    Return the line number in the current file. Before the first line
    has been read, returns 0. After the last line of the last file has
    been read, returns the line number of that line within the file.
    """
    
    title = 'filelineno'
    type_ = 'fileinput'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fileinput.filelineno())
        

class Filename_Node(NodeBase):
    """
    
    Return the name of the file currently being read.
    Before the first line has been read, returns None.
    """
    
    title = 'filename'
    type_ = 'fileinput'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fileinput.filename())
        

class Fileno_Node(NodeBase):
    """
    
    Return the file number of the current file. When no file is currently
    opened, returns -1.
    """
    
    title = 'fileno'
    type_ = 'fileinput'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fileinput.fileno())
        

class Hook_Compressed_Node(NodeBase):
    """
    """
    
    title = 'hook_compressed'
    type_ = 'fileinput'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='mode'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fileinput.hook_compressed(self.input(0), self.input(1)))
        

class Hook_Encoded_Node(NodeBase):
    """
    """
    
    title = 'hook_encoded'
    type_ = 'fileinput'
    init_inputs = [
        NodeInputBP(label='encoding'),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fileinput.hook_encoded(self.input(0), self.input(1)))
        

class Input_Node(NodeBase):
    """
    Return an instance of the FileInput class, which can be iterated.

    The parameters are passed to the constructor of the FileInput class.
    The returned instance, in addition to being an iterator,
    keeps global state for the functions of this module,.
    """
    
    title = 'input'
    type_ = 'fileinput'
    init_inputs = [
        NodeInputBP(label='files', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='inplace', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='backup', dtype=dtypes.Data(default='', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fileinput.input(self.input(0), self.input(1), self.input(2)))
        

class Isfirstline_Node(NodeBase):
    """
    
    Returns true the line just read is the first line of its file,
    otherwise returns false.
    """
    
    title = 'isfirstline'
    type_ = 'fileinput'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fileinput.isfirstline())
        

class Isstdin_Node(NodeBase):
    """
    
    Returns true if the last line was read from sys.stdin,
    otherwise returns false.
    """
    
    title = 'isstdin'
    type_ = 'fileinput'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fileinput.isstdin())
        

class Lineno_Node(NodeBase):
    """
    
    Return the cumulative line number of the line that has just been read.
    Before the first line has been read, returns 0. After the last line
    of the last file has been read, returns the line number of that line.
    """
    
    title = 'lineno'
    type_ = 'fileinput'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fileinput.lineno())
        

class Nextfile_Node(NodeBase):
    """
    
    Close the current file so that the next iteration will read the first
    line from the next file (if any); lines not read from the file will
    not count towards the cumulative line count. The filename is not
    changed until after the first line of the next file has been read.
    Before the first line has been read, this function has no effect;
    it cannot be used to skip the first file. After the last line of the
    last file has been read, this function has no effect.
    """
    
    title = 'nextfile'
    type_ = 'fileinput'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fileinput.nextfile())
        


export_nodes(
    _Test_Node,
    Close_Node,
    Filelineno_Node,
    Filename_Node,
    Fileno_Node,
    Hook_Compressed_Node,
    Hook_Encoded_Node,
    Input_Node,
    Isfirstline_Node,
    Isstdin_Node,
    Lineno_Node,
    Nextfile_Node,
)
