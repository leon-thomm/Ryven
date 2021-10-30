
from ryven.NENV import *

import asyncore


class NodeBase(Node):
    pass


class _Exception_Node(NodeBase):
    """
    """
    
    title = '_exception'
    type_ = 'asyncore'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, asyncore._exception(self.input(0)))
        

class _Strerror_Node(NodeBase):
    """
    """
    
    title = '_strerror'
    type_ = 'asyncore'
    init_inputs = [
        NodeInputBP(label='err'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, asyncore._strerror(self.input(0)))
        

class Close_All_Node(NodeBase):
    """
    """
    
    title = 'close_all'
    type_ = 'asyncore'
    init_inputs = [
        NodeInputBP(label='map', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='ignore_all', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, asyncore.close_all(self.input(0), self.input(1)))
        

class Compact_Traceback_Node(NodeBase):
    """
    """
    
    title = 'compact_traceback'
    type_ = 'asyncore'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, asyncore.compact_traceback())
        

class Loop_Node(NodeBase):
    """
    """
    
    title = 'loop'
    type_ = 'asyncore'
    init_inputs = [
        NodeInputBP(label='timeout', dtype=dtypes.Data(default=30.0, size='s')),
        NodeInputBP(label='use_poll', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='map', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='count', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, asyncore.loop(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Poll_Node(NodeBase):
    """
    """
    
    title = 'poll'
    type_ = 'asyncore'
    init_inputs = [
        NodeInputBP(label='timeout', dtype=dtypes.Data(default=0.0, size='s')),
        NodeInputBP(label='map', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, asyncore.poll(self.input(0), self.input(1)))
        

class Poll2_Node(NodeBase):
    """
    """
    
    title = 'poll2'
    type_ = 'asyncore'
    init_inputs = [
        NodeInputBP(label='timeout', dtype=dtypes.Data(default=0.0, size='s')),
        NodeInputBP(label='map', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, asyncore.poll2(self.input(0), self.input(1)))
        

class Poll3_Node(NodeBase):
    """
    """
    
    title = 'poll3'
    type_ = 'asyncore'
    init_inputs = [
        NodeInputBP(label='timeout', dtype=dtypes.Data(default=0.0, size='s')),
        NodeInputBP(label='map', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, asyncore.poll3(self.input(0), self.input(1)))
        

class Read_Node(NodeBase):
    """
    """
    
    title = 'read'
    type_ = 'asyncore'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, asyncore.read(self.input(0)))
        

class Readwrite_Node(NodeBase):
    """
    """
    
    title = 'readwrite'
    type_ = 'asyncore'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='flags'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, asyncore.readwrite(self.input(0), self.input(1)))
        

class Write_Node(NodeBase):
    """
    """
    
    title = 'write'
    type_ = 'asyncore'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, asyncore.write(self.input(0)))
        


export_nodes(
    _Exception_Node,
    _Strerror_Node,
    Close_All_Node,
    Compact_Traceback_Node,
    Loop_Node,
    Poll_Node,
    Poll2_Node,
    Poll3_Node,
    Read_Node,
    Readwrite_Node,
    Write_Node,
)
