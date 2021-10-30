
from ryven.NENV import *

import _threading_local


class NodeBase(Node):
    pass


class Rlock_Node(NodeBase):
    """
    Factory function that returns a new reentrant lock.

    A reentrant lock must be released by the thread that acquired it. Once a
    thread has acquired a reentrant lock, the same thread may acquire it again
    without blocking; the thread must release it once for each time it has
    acquired it.

    """
    
    title = 'RLock'
    type_ = '_threading_local'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _threading_local.RLock())
        

class _Patch_Node(NodeBase):
    """
    """
    
    title = '_patch'
    type_ = '_threading_local'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _threading_local._patch())
        

class Contextmanager_Node(NodeBase):
    """
    @contextmanager decorator.

    Typical usage:

        @contextmanager
        def some_generator(<arguments>):
            <setup>
            try:
                yield <value>
            finally:
                <cleanup>

    This makes this:

        with some_generator(<arguments>) as <variable>:
            <body>

    equivalent to this:

        <setup>
        try:
            <variable> = <value>
            <body>
        finally:
            <cleanup>
    """
    
    title = 'contextmanager'
    type_ = '_threading_local'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _threading_local.contextmanager(self.input(0)))
        

class Current_Thread_Node(NodeBase):
    """
    Return the current Thread object, corresponding to the caller's thread of control.

    If the caller's thread of control was not created through the threading
    module, a dummy thread object with limited functionality is returned.

    """
    
    title = 'current_thread'
    type_ = '_threading_local'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _threading_local.current_thread())
        


export_nodes(
    Rlock_Node,
    _Patch_Node,
    Contextmanager_Node,
    Current_Thread_Node,
)
