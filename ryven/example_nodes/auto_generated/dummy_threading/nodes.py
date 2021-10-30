
from ryven.NENV import *

import dummy_threading


class NodeBase(Node):
    pass


class Excepthookargs_Node(NodeBase):
    title = 'ExceptHookArgs'
    type_ = 'dummy_threading'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='args'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dummy_threading.ExceptHookArgs(self.input(0)))
        

class Lock_Node(NodeBase):
    title = 'Lock'
    type_ = 'dummy_threading'
    doc = """Dummy implementation of _thread.allocate_lock()."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dummy_threading.Lock())
        

class Rlock_Node(NodeBase):
    title = 'RLock'
    type_ = 'dummy_threading'
    doc = """Factory function that returns a new reentrant lock.

    A reentrant lock must be released by the thread that acquired it. Once a
    thread has acquired a reentrant lock, the same thread may acquire it again
    without blocking; the thread must release it once for each time it has
    acquired it.

    """
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dummy_threading.RLock())
        

class Active_Count_Node(NodeBase):
    title = 'active_count'
    type_ = 'dummy_threading'
    doc = """Return the number of Thread objects currently alive.

    The returned count is equal to the length of the list returned by
    enumerate().

    """
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dummy_threading.active_count())
        

class Current_Thread_Node(NodeBase):
    title = 'current_thread'
    type_ = 'dummy_threading'
    doc = """Return the current Thread object, corresponding to the caller's thread of control.

    If the caller's thread of control was not created through the threading
    module, a dummy thread object with limited functionality is returned.

    """
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dummy_threading.current_thread())
        

class Enumerate_Node(NodeBase):
    title = 'enumerate'
    type_ = 'dummy_threading'
    doc = """Return a list of all Thread objects currently alive.

    The list includes daemonic threads, dummy thread objects created by
    current_thread(), and the main thread. It excludes terminated threads and
    threads that have not yet been started.

    """
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dummy_threading.enumerate())
        

class Excepthook_Node(NodeBase):
    title = 'excepthook'
    type_ = 'dummy_threading'
    doc = """
        Handle uncaught Thread.run() exception.
        """
    init_inputs = [
        NodeInputBP(label='args'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dummy_threading.excepthook(self.input(0)))
        

class Get_Ident_Node(NodeBase):
    title = 'get_ident'
    type_ = 'dummy_threading'
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
        self.set_output_val(0, dummy_threading.get_ident())
        

class Main_Thread_Node(NodeBase):
    title = 'main_thread'
    type_ = 'dummy_threading'
    doc = """Return the main thread object.

    In normal conditions, the main thread is the thread from which the
    Python interpreter was started.
    """
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dummy_threading.main_thread())
        

class Setprofile_Node(NodeBase):
    title = 'setprofile'
    type_ = 'dummy_threading'
    doc = """Set a profile function for all threads started from the threading module.

    The func will be passed to sys.setprofile() for each thread, before its
    run() method is called.

    """
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dummy_threading.setprofile(self.input(0)))
        

class Settrace_Node(NodeBase):
    title = 'settrace'
    type_ = 'dummy_threading'
    doc = """Set a trace function for all threads started from the threading module.

    The func will be passed to sys.settrace() for each thread, before its run()
    method is called.

    """
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dummy_threading.settrace(self.input(0)))
        

class Stack_Size_Node(NodeBase):
    title = 'stack_size'
    type_ = 'dummy_threading'
    doc = """Dummy implementation of _thread.stack_size()."""
    init_inputs = [
        NodeInputBP(label='size', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dummy_threading.stack_size(self.input(0)))
        


export_nodes(
    Excepthookargs_Node,
    Lock_Node,
    Rlock_Node,
    Active_Count_Node,
    Current_Thread_Node,
    Enumerate_Node,
    Excepthook_Node,
    Get_Ident_Node,
    Main_Thread_Node,
    Setprofile_Node,
    Settrace_Node,
    Stack_Size_Node,
)
