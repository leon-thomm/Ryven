
from ryven.NENV import *

import tabnanny


class NodeBase(Node):
    pass


class Check_Node(NodeBase):
    """
    check(file_or_dir)

    If file_or_dir is a directory and not a symbolic link, then recursively
    descend the directory tree named by file_or_dir, checking all .py files
    along the way. If file_or_dir is an ordinary Python source file, it is
    checked for whitespace related problems. The diagnostic messages are
    written to standard output using the print statement.
    """
    
    title = 'check'
    type_ = 'tabnanny'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tabnanny.check(self.input(0)))
        

class Errprint_Node(NodeBase):
    """
    """
    
    title = 'errprint'
    type_ = 'tabnanny'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tabnanny.errprint())
        

class Format_Witnesses_Node(NodeBase):
    """
    """
    
    title = 'format_witnesses'
    type_ = 'tabnanny'
    init_inputs = [
        NodeInputBP(label='w'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tabnanny.format_witnesses(self.input(0)))
        

class Main_Node(NodeBase):
    """
    """
    
    title = 'main'
    type_ = 'tabnanny'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tabnanny.main())
        

class Process_Tokens_Node(NodeBase):
    """
    """
    
    title = 'process_tokens'
    type_ = 'tabnanny'
    init_inputs = [
        NodeInputBP(label='tokens'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tabnanny.process_tokens(self.input(0)))
        


export_nodes(
    Check_Node,
    Errprint_Node,
    Format_Witnesses_Node,
    Main_Node,
    Process_Tokens_Node,
)
