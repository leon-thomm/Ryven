import ryvencore_qt as rc
import multiprocessing


class AutoNode_multiprocessing_Array(rc.Node):
    title = 'Array'
    doc = '''Returns a synchronized shared array'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='typecode_or_type'),
rc.NodeInputBP(label='size_or_initializer'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.Array(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_multiprocessing_Barrier(rc.Node):
    title = 'Barrier'
    doc = '''Returns a barrier object'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='parties'),
rc.NodeInputBP(label='action'),
rc.NodeInputBP(label='timeout'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.Barrier(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_multiprocessing_BoundedSemaphore(rc.Node):
    title = 'BoundedSemaphore'
    doc = '''Returns a bounded semaphore object'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.BoundedSemaphore(self.input(0), self.input(1)))
        


class AutoNode_multiprocessing_Condition(rc.Node):
    title = 'Condition'
    doc = '''Returns a condition object'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='lock'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.Condition(self.input(0), self.input(1)))
        


class AutoNode_multiprocessing_Event(rc.Node):
    title = 'Event'
    doc = '''Returns an event object'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.Event(self.input(0)))
        


class AutoNode_multiprocessing_JoinableQueue(rc.Node):
    title = 'JoinableQueue'
    doc = '''Returns a queue object'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='maxsize'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.JoinableQueue(self.input(0), self.input(1)))
        


class AutoNode_multiprocessing_Lock(rc.Node):
    title = 'Lock'
    doc = '''Returns a non-recursive lock object'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.Lock(self.input(0)))
        


class AutoNode_multiprocessing_Manager(rc.Node):
    title = 'Manager'
    doc = '''Returns a manager associated with a running server process

        The managers methods such as `Lock()`, `Condition()` and `Queue()`
        can be used to create shared objects.
        '''
    init_inputs = [
        rc.NodeInputBP(label='self'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.Manager(self.input(0)))
        


class AutoNode_multiprocessing_Pipe(rc.Node):
    title = 'Pipe'
    doc = '''Returns two connection object connected by a pipe'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='duplex'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.Pipe(self.input(0), self.input(1)))
        


class AutoNode_multiprocessing_Pool(rc.Node):
    title = 'Pool'
    doc = '''Returns a process pool object'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='processes'),
rc.NodeInputBP(label='initializer'),
rc.NodeInputBP(label='initargs'),
rc.NodeInputBP(label='maxtasksperchild'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.Pool(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_multiprocessing_Queue(rc.Node):
    title = 'Queue'
    doc = '''Returns a queue object'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='maxsize'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.Queue(self.input(0), self.input(1)))
        


class AutoNode_multiprocessing_RLock(rc.Node):
    title = 'RLock'
    doc = '''Returns a recursive lock object'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.RLock(self.input(0)))
        


class AutoNode_multiprocessing_RawArray(rc.Node):
    title = 'RawArray'
    doc = '''Returns a shared array'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='typecode_or_type'),
rc.NodeInputBP(label='size_or_initializer'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.RawArray(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_multiprocessing_RawValue(rc.Node):
    title = 'RawValue'
    doc = '''Returns a shared object'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='typecode_or_type'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.RawValue(self.input(0), self.input(1)))
        


class AutoNode_multiprocessing_Semaphore(rc.Node):
    title = 'Semaphore'
    doc = '''Returns a semaphore object'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.Semaphore(self.input(0), self.input(1)))
        


class AutoNode_multiprocessing_SimpleQueue(rc.Node):
    title = 'SimpleQueue'
    doc = '''Returns a queue object'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.SimpleQueue(self.input(0)))
        


class AutoNode_multiprocessing_Value(rc.Node):
    title = 'Value'
    doc = '''Returns a synchronized shared object'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='typecode_or_type'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.Value(self.input(0), self.input(1)))
        


class AutoNode_multiprocessing_active_children(rc.Node):
    title = 'active_children'
    doc = '''
    Return list of process objects corresponding to live child processes
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.active_children())
        


class AutoNode_multiprocessing_allow_connection_pickling(rc.Node):
    title = 'allow_connection_pickling'
    doc = '''Install support for sending connections and sockets
        between processes
        '''
    init_inputs = [
        rc.NodeInputBP(label='self'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.allow_connection_pickling(self.input(0)))
        


class AutoNode_multiprocessing_cpu_count(rc.Node):
    title = 'cpu_count'
    doc = '''Returns the number of CPUs in the system'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.cpu_count(self.input(0)))
        


class AutoNode_multiprocessing_current_process(rc.Node):
    title = 'current_process'
    doc = '''
    Return process object representing the current process
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.current_process())
        


class AutoNode_multiprocessing_freeze_support(rc.Node):
    title = 'freeze_support'
    doc = '''Check whether this is a fake forked process in a frozen executable.
        If so then run code specified by commandline and exit.
        '''
    init_inputs = [
        rc.NodeInputBP(label='self'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.freeze_support(self.input(0)))
        


class AutoNode_multiprocessing_get_all_start_methods(rc.Node):
    title = 'get_all_start_methods'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.get_all_start_methods(self.input(0)))
        


class AutoNode_multiprocessing_get_context(rc.Node):
    title = 'get_context'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='method'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.get_context(self.input(0), self.input(1)))
        


class AutoNode_multiprocessing_get_logger(rc.Node):
    title = 'get_logger'
    doc = '''Return package logger -- if it does not already exist then
        it is created.
        '''
    init_inputs = [
        rc.NodeInputBP(label='self'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.get_logger(self.input(0)))
        


class AutoNode_multiprocessing_get_start_method(rc.Node):
    title = 'get_start_method'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='allow_none'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.get_start_method(self.input(0), self.input(1)))
        


class AutoNode_multiprocessing_log_to_stderr(rc.Node):
    title = 'log_to_stderr'
    doc = '''Turn on logging and add a handler which prints to stderr'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='level'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.log_to_stderr(self.input(0), self.input(1)))
        


class AutoNode_multiprocessing_parent_process(rc.Node):
    title = 'parent_process'
    doc = '''
    Return process object representing the parent process
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.parent_process())
        


class AutoNode_multiprocessing_set_executable(rc.Node):
    title = 'set_executable'
    doc = '''Sets the path to a python.exe or pythonw.exe binary used to run
        child processes instead of sys.executable when using the 'spawn'
        start method.  Useful for people embedding Python.
        '''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='executable'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.set_executable(self.input(0), self.input(1)))
        


class AutoNode_multiprocessing_set_forkserver_preload(rc.Node):
    title = 'set_forkserver_preload'
    doc = '''Set list of module names to try to load in forkserver process.
        This is really just a hint.
        '''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='module_names'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.set_forkserver_preload(self.input(0), self.input(1)))
        


class AutoNode_multiprocessing_set_start_method(rc.Node):
    title = 'set_start_method'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='method'),
rc.NodeInputBP(label='force'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, multiprocessing.set_start_method(self.input(0), self.input(1), self.input(2)))
        