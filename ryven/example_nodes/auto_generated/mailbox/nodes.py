
from ryven.NENV import *

import mailbox


class NodeBase(Node):
    pass


class _Create_Carefully_Node(NodeBase):
    """
    Create a file if it doesn't exist and open for reading and writing."""
    
    title = '_create_carefully'
    type_ = 'mailbox'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailbox._create_carefully(self.input(0)))
        

class _Create_Temporary_Node(NodeBase):
    """
    Create a temp file based on path and open for reading and writing."""
    
    title = '_create_temporary'
    type_ = 'mailbox'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailbox._create_temporary(self.input(0)))
        

class _Lock_File_Node(NodeBase):
    """
    Lock file f using lockf and dot locking."""
    
    title = '_lock_file'
    type_ = 'mailbox'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='dotlock', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailbox._lock_file(self.input(0), self.input(1)))
        

class _Sync_Close_Node(NodeBase):
    """
    Close file f, ensuring all changes are physically on disk."""
    
    title = '_sync_close'
    type_ = 'mailbox'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailbox._sync_close(self.input(0)))
        

class _Sync_Flush_Node(NodeBase):
    """
    Ensure changes to file f are physically on disk."""
    
    title = '_sync_flush'
    type_ = 'mailbox'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailbox._sync_flush(self.input(0)))
        

class _Unlock_File_Node(NodeBase):
    """
    Unlock file f using lockf and dot locking."""
    
    title = '_unlock_file'
    type_ = 'mailbox'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailbox._unlock_file(self.input(0)))
        


export_nodes(
    _Create_Carefully_Node,
    _Create_Temporary_Node,
    _Lock_File_Node,
    _Sync_Close_Node,
    _Sync_Flush_Node,
    _Unlock_File_Node,
)
