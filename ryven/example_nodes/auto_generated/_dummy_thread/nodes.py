
from ryven.NENV import *

import _dummy_thread


class NodeBase(Node):
    pass


class _Set_Sentinel_Node(NodeBase):
    title = '_set_sentinel'
    type_ = '_dummy_thread'
    doc = """Dummy implementation of _thread._set_sentinel()."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _dummy_thread._set_sentinel())
        

class Allocate_Lock_Node(NodeBase):
    title = 'allocate_lock'
    type_ = '_dummy_thread'
    doc = """Dummy implementation of _thread.allocate_lock()."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _dummy_thread.allocate_lock())
        

class Exit_Node(NodeBase):
    title = 'exit'
    type_ = '_dummy_thread'
    doc = """Dummy implementation of _thread.exit()."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _dummy_thread.exit())
        

class Get_Ident_Node(NodeBase):
    title = 'get_ident'
    type_ = '_dummy_thread'
    doc = """Dummy implementation of _thread.get_ident().

    Since this module should only be used when _threadmodule is not
    available, it is safe to assume that the current process is the
    only thread.  Thus a constant can be safely returned.
    """
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _dummy_thread.get_ident())
        

class Interrupt_Main_Node(NodeBase):
    title = 'interrupt_main'
    type_ = '_dummy_thread'
    doc = """Set _interrupt flag to True to have start_new_thread raise
    KeyboardInterrupt upon exiting."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _dummy_thread.interrupt_main())
        

class Stack_Size_Node(NodeBase):
    title = 'stack_size'
    type_ = '_dummy_thread'
    doc = """Dummy implementation of _thread.stack_size()."""
    init_inputs = [
        NodeInputBP(label='size', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _dummy_thread.stack_size(self.input(0)))
        

class Start_New_Thread_Node(NodeBase):
    title = 'start_new_thread'
    type_ = '_dummy_thread'
    doc = """Dummy implementation of _thread.start_new_thread().

    Compatibility is maintained by making sure that ``args`` is a
    tuple and ``kwargs`` is a dictionary.  If an exception is raised
    and it is SystemExit (which can be done by _thread.exit()) it is
    caught and nothing is done; all other exceptions are printed out
    by using traceback.print_exc().

    If the executed function calls interrupt_main the KeyboardInterrupt will be
    raised when the function returns.

    """
    init_inputs = [
        NodeInputBP(label='function'),
        NodeInputBP(label='args'),
        NodeInputBP(label='kwargs', dtype=dtypes.Data(default={}, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _dummy_thread.start_new_thread(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _Set_Sentinel_Node,
    Allocate_Lock_Node,
    Exit_Node,
    Get_Ident_Node,
    Interrupt_Main_Node,
    Stack_Size_Node,
    Start_New_Thread_Node,
)
