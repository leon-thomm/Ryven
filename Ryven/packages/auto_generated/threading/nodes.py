
from NENV import *

import threading


class NodeBase(Node):
    pass


class Rlock_Node(NodeBase):
    title = 'RLock'
    type_ = 'threading'
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

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading.RLock())
        

class _After_Fork_Node(NodeBase):
    title = '_after_fork'
    type_ = 'threading'
    doc = """
    Cleanup threading module state that should not exist after a fork.
    """
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading._after_fork())
        

class _Enumerate_Node(NodeBase):
    title = '_enumerate'
    type_ = 'threading'
    doc = """"""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading._enumerate())
        

class _Make_Invoke_Excepthook_Node(NodeBase):
    title = '_make_invoke_excepthook'
    type_ = 'threading'
    doc = """"""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading._make_invoke_excepthook())
        

class _Newname_Node(NodeBase):
    title = '_newname'
    type_ = 'threading'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='template', dtype=dtypes.Data(default='Thread-%d', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading._newname(self.input(0)))
        

class _Shutdown_Node(NodeBase):
    title = '_shutdown'
    type_ = 'threading'
    doc = """
    Wait until the Python thread state of all non-daemon threads get deleted.
    """
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading._shutdown())
        

class Activecount_Node(NodeBase):
    title = 'activeCount'
    type_ = 'threading'
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

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading.activeCount())
        

class Active_Count_Node(NodeBase):
    title = 'active_count'
    type_ = 'threading'
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

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading.active_count())
        

class Currentthread_Node(NodeBase):
    title = 'currentThread'
    type_ = 'threading'
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

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading.currentThread())
        

class Current_Thread_Node(NodeBase):
    title = 'current_thread'
    type_ = 'threading'
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

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading.current_thread())
        

class Enumerate_Node(NodeBase):
    title = 'enumerate'
    type_ = 'threading'
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

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading.enumerate())
        

class Main_Thread_Node(NodeBase):
    title = 'main_thread'
    type_ = 'threading'
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

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading.main_thread())
        

class Setprofile_Node(NodeBase):
    title = 'setprofile'
    type_ = 'threading'
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

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading.setprofile(self.input(0)))
        

class Settrace_Node(NodeBase):
    title = 'settrace'
    type_ = 'threading'
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

    def update_event(self, input_called=-1):
        self.set_output_val(0, threading.settrace(self.input(0)))
        


export_nodes(
    Rlock_Node,
    _After_Fork_Node,
    _Enumerate_Node,
    _Make_Invoke_Excepthook_Node,
    _Newname_Node,
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
