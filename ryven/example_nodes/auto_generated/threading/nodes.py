
from ryven.NENV import *

import threading


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
    type_ = 'threading'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading.RLock())
        

class _After_Fork_Node(NodeBase):
    """
    
    Cleanup threading module state that should not exist after a fork.
    """
    
    title = '_after_fork'
    type_ = 'threading'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading._after_fork())
        

class _Enumerate_Node(NodeBase):
    """
    """
    
    title = '_enumerate'
    type_ = 'threading'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading._enumerate())
        

class _Make_Invoke_Excepthook_Node(NodeBase):
    """
    """
    
    title = '_make_invoke_excepthook'
    type_ = 'threading'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading._make_invoke_excepthook())
        

class _Newname_Node(NodeBase):
    """
    """
    
    title = '_newname'
    type_ = 'threading'
    init_inputs = [
        NodeInputBP(label='template', dtype=dtypes.Data(default='Thread-%d', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading._newname(self.input(0)))
        

class _Register_Atexit_Node(NodeBase):
    """
    CPython internal: register *func* to be called before joining threads.

    The registered *func* is called with its arguments just before all
    non-daemon threads are joined in `_shutdown()`. It provides a similar
    purpose to `atexit.register()`, but its functions are called prior to
    threading shutdown instead of interpreter shutdown.

    For similarity to atexit, the registered functions are called in reverse.
    """
    
    title = '_register_atexit'
    type_ = 'threading'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading._register_atexit(self.input(0)))
        

class _Shutdown_Node(NodeBase):
    """
    
    Wait until the Python thread state of all non-daemon threads get deleted.
    """
    
    title = '_shutdown'
    type_ = 'threading'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading._shutdown())
        

class Activecount_Node(NodeBase):
    """
    Return the number of Thread objects currently alive.

    The returned count is equal to the length of the list returned by
    enumerate().

    """
    
    title = 'activeCount'
    type_ = 'threading'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading.activeCount())
        

class Active_Count_Node(NodeBase):
    """
    Return the number of Thread objects currently alive.

    The returned count is equal to the length of the list returned by
    enumerate().

    """
    
    title = 'active_count'
    type_ = 'threading'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading.active_count())
        

class Currentthread_Node(NodeBase):
    """
    Return the current Thread object, corresponding to the caller's thread of control.

    If the caller's thread of control was not created through the threading
    module, a dummy thread object with limited functionality is returned.

    """
    
    title = 'currentThread'
    type_ = 'threading'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading.currentThread())
        

class Current_Thread_Node(NodeBase):
    """
    Return the current Thread object, corresponding to the caller's thread of control.

    If the caller's thread of control was not created through the threading
    module, a dummy thread object with limited functionality is returned.

    """
    
    title = 'current_thread'
    type_ = 'threading'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading.current_thread())
        

class Enumerate_Node(NodeBase):
    """
    Return a list of all Thread objects currently alive.

    The list includes daemonic threads, dummy thread objects created by
    current_thread(), and the main thread. It excludes terminated threads and
    threads that have not yet been started.

    """
    
    title = 'enumerate'
    type_ = 'threading'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading.enumerate())
        

class Main_Thread_Node(NodeBase):
    """
    Return the main thread object.

    In normal conditions, the main thread is the thread from which the
    Python interpreter was started.
    """
    
    title = 'main_thread'
    type_ = 'threading'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading.main_thread())
        

class Setprofile_Node(NodeBase):
    """
    Set a profile function for all threads started from the threading module.

    The func will be passed to sys.setprofile() for each thread, before its
    run() method is called.

    """
    
    title = 'setprofile'
    type_ = 'threading'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading.setprofile(self.input(0)))
        

class Settrace_Node(NodeBase):
    """
    Set a trace function for all threads started from the threading module.

    The func will be passed to sys.settrace() for each thread, before its run()
    method is called.

    """
    
    title = 'settrace'
    type_ = 'threading'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, threading.settrace(self.input(0)))
        


export_nodes(
    Rlock_Node,
    _After_Fork_Node,
    _Enumerate_Node,
    _Make_Invoke_Excepthook_Node,
    _Newname_Node,
    _Register_Atexit_Node,
    _Shutdown_Node,
    Activecount_Node,
    Active_Count_Node,
    Currentthread_Node,
    Current_Thread_Node,
    Enumerate_Node,
    Main_Thread_Node,
    Setprofile_Node,
    Settrace_Node,
)
