
from NENV import *

import zipapp


class NodeBase(Node):
    pass


class _Copy_Archive_Node(NodeBase):
    """
    Copy an application archive, modifying the shebang line."""
    
    title = '_copy_archive'
    type_ = 'zipapp'
    init_inputs = [
        NodeInputBP(label='archive'),
        NodeInputBP(label='new_archive'),
        NodeInputBP(label='interpreter', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipapp._copy_archive(self.input(0), self.input(1), self.input(2)))
        

class _Maybe_Open_Node(NodeBase):
    """
    """
    
    title = '_maybe_open'
    type_ = 'zipapp'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipapp._maybe_open())
        

class _Write_File_Prefix_Node(NodeBase):
    """
    Write a shebang line."""
    
    title = '_write_file_prefix'
    type_ = 'zipapp'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='interpreter'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipapp._write_file_prefix(self.input(0), self.input(1)))
        

class Create_Archive_Node(NodeBase):
    """
    Create an application archive from SOURCE.

    The SOURCE can be the name of a directory, or a filename or a file-like
    object referring to an existing archive.

    The content of SOURCE is packed into an application archive in TARGET,
    which can be a filename or a file-like object.  If SOURCE is a directory,
    TARGET can be omitted and will default to the name of SOURCE with .pyz
    appended.

    The created application archive will have a shebang line specifying
    that it should run with INTERPRETER (there will be no shebang line if
    INTERPRETER is None), and a __main__.py which runs MAIN (if MAIN is
    not specified, an existing __main__.py will be used).  It is an error
    to specify MAIN for anything other than a directory source with no
    __main__.py, and it is an error to omit MAIN if the directory has no
    __main__.py.
    """
    
    title = 'create_archive'
    type_ = 'zipapp'
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='target', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='interpreter', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='main', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='filter', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='compressed', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipapp.create_archive(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class Get_Interpreter_Node(NodeBase):
    """
    """
    
    title = 'get_interpreter'
    type_ = 'zipapp'
    init_inputs = [
        NodeInputBP(label='archive'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipapp.get_interpreter(self.input(0)))
        

class Main_Node(NodeBase):
    """
    Run the zipapp command line interface.

    The ARGS parameter lets you specify the argument list directly.
    Omitting ARGS (or setting it to None) works as for argparse, using
    sys.argv[1:] as the argument list.
    """
    
    title = 'main'
    type_ = 'zipapp'
    init_inputs = [
        NodeInputBP(label='args', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipapp.main(self.input(0)))
        


export_nodes(
    _Copy_Archive_Node,
    _Maybe_Open_Node,
    _Write_File_Prefix_Node,
    Create_Archive_Node,
    Get_Interpreter_Node,
    Main_Node,
)
