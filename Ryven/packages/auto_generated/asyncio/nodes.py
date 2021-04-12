import ryvencore_qt as rc
import asyncio


class AutoNode_asyncio__all_tasks_compat(rc.Node):
    title = '_all_tasks_compat'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='loop'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio._all_tasks_compat(self.input(0)))
        


class AutoNode_asyncio__enter_task(rc.Node):
    title = '_enter_task'
    description = '''Enter into task execution or resume suspended task.

Task belongs to loop.

Returns None.'''
    init_inputs = [
        rc.NodeInputBP(label='loop'),
rc.NodeInputBP(label='task'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio._enter_task(self.input(0), self.input(1)))
        


class AutoNode_asyncio__get_running_loop(rc.Node):
    title = '_get_running_loop'
    description = '''Return the running event loop or None.

This is a low-level function intended to be used by event loops.
This function is thread-specific.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio._get_running_loop())
        


class AutoNode_asyncio__leave_task(rc.Node):
    title = '_leave_task'
    description = '''Leave task execution or suspend a task.

Task belongs to loop.

Returns None.'''
    init_inputs = [
        rc.NodeInputBP(label='loop'),
rc.NodeInputBP(label='task'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio._leave_task(self.input(0), self.input(1)))
        


class AutoNode_asyncio__register_task(rc.Node):
    title = '_register_task'
    description = '''Register a new task in asyncio as executed by loop.

Returns None.'''
    init_inputs = [
        rc.NodeInputBP(label='task'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio._register_task(self.input(0)))
        


class AutoNode_asyncio__set_running_loop(rc.Node):
    title = '_set_running_loop'
    description = '''Set the running event loop.

This is a low-level function intended to be used by event loops.
This function is thread-specific.'''
    init_inputs = [
        rc.NodeInputBP(label='loop'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio._set_running_loop(self.input(0)))
        


class AutoNode_asyncio__unregister_task(rc.Node):
    title = '_unregister_task'
    description = '''Unregister a task.

Returns None.'''
    init_inputs = [
        rc.NodeInputBP(label='task'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio._unregister_task(self.input(0)))
        


class AutoNode_asyncio_all_tasks(rc.Node):
    title = 'all_tasks'
    description = '''Return a set of all tasks for the loop.'''
    init_inputs = [
        rc.NodeInputBP(label='loop'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.all_tasks(self.input(0)))
        


class AutoNode_asyncio_as_completed(rc.Node):
    title = 'as_completed'
    description = '''Return an iterator whose values are coroutines.

    When waiting for the yielded coroutines you'll get the results (or
    exceptions!) of the original Futures (or coroutines), in the order
    in which and as soon as they complete.

    This differs from PEP 3148; the proper way to use this is:

        for f in as_completed(fs):
            result = await f  # The 'await' may raise.
            # Use result.

    If a timeout is specified, the 'await' will raise
    TimeoutError when the timeout occurs before all Futures are done.

    Note: The futures 'f' are not necessarily members of fs.
    '''
    init_inputs = [
        rc.NodeInputBP(label='fs'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.as_completed(self.input(0)))
        


class AutoNode_asyncio_coroutine(rc.Node):
    title = 'coroutine'
    description = '''Decorator to mark coroutines.

    If the coroutine is not yielded from before it is destroyed,
    an error message is logged.
    '''
    init_inputs = [
        rc.NodeInputBP(label='func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.coroutine(self.input(0)))
        


class AutoNode_asyncio_create_subprocess_exec(rc.Node):
    title = 'create_subprocess_exec'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='program'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.create_subprocess_exec(self.input(0)))
        


class AutoNode_asyncio_create_subprocess_shell(rc.Node):
    title = 'create_subprocess_shell'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='cmd'),
rc.NodeInputBP(label='stdin'),
rc.NodeInputBP(label='stdout'),
rc.NodeInputBP(label='stderr'),
rc.NodeInputBP(label='loop'),
rc.NodeInputBP(label='limit'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.create_subprocess_shell(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode_asyncio_create_task(rc.Node):
    title = 'create_task'
    description = '''Schedule the execution of a coroutine object in a spawn task.

    Return a Task object.
    '''
    init_inputs = [
        rc.NodeInputBP(label='coro'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.create_task(self.input(0)))
        


class AutoNode_asyncio_current_task(rc.Node):
    title = 'current_task'
    description = '''Return a currently executed task.'''
    init_inputs = [
        rc.NodeInputBP(label='loop'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.current_task(self.input(0)))
        


class AutoNode_asyncio_ensure_future(rc.Node):
    title = 'ensure_future'
    description = '''Wrap a coroutine or an awaitable in a future.

    If the argument is a Future, it is returned directly.
    '''
    init_inputs = [
        rc.NodeInputBP(label='coro_or_future'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.ensure_future(self.input(0)))
        


class AutoNode_asyncio_gather(rc.Node):
    title = 'gather'
    description = '''Return a future aggregating results from the given coroutines/futures.

    Coroutines will be wrapped in a future and scheduled in the event
    loop. They will not necessarily be scheduled in the same order as
    passed in.

    All futures must share the same event loop.  If all the tasks are
    done successfully, the returned future's result is the list of
    results (in the order of the original sequence, not necessarily
    the order of results arrival).  If *return_exceptions* is True,
    exceptions in the tasks are treated the same as successful
    results, and gathered in the result list; otherwise, the first
    raised exception will be immediately propagated to the returned
    future.

    Cancellation: if the outer Future is cancelled, all children (that
    have not completed yet) are also cancelled.  If any child is
    cancelled, this is treated as if it raised CancelledError --
    the outer Future is *not* cancelled in this case.  (This is to
    prevent the cancellation of one child to cause other children to
    be cancelled.)

    If *return_exceptions* is False, cancelling gather() after it
    has been marked done won't cancel any submitted awaitables.
    For instance, gather can be marked done after propagating an
    exception to the caller, therefore, calling ``gather.cancel()``
    after catching an exception (raised by one of the awaitables) from
    gather won't cancel any other awaitables.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.gather())
        


class AutoNode_asyncio_get_child_watcher(rc.Node):
    title = 'get_child_watcher'
    description = '''Equivalent to calling get_event_loop_policy().get_child_watcher().'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.get_child_watcher())
        


class AutoNode_asyncio_get_event_loop(rc.Node):
    title = 'get_event_loop'
    description = '''Return an asyncio event loop.

When called from a coroutine or a callback (e.g. scheduled with
call_soon or similar API), this function will always return the
running event loop.

If there is no running event loop set, the function will return
the result of `get_event_loop_policy().get_event_loop()` call.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.get_event_loop())
        


class AutoNode_asyncio_get_event_loop_policy(rc.Node):
    title = 'get_event_loop_policy'
    description = '''Get the current event loop policy.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.get_event_loop_policy())
        


class AutoNode_asyncio_get_running_loop(rc.Node):
    title = 'get_running_loop'
    description = '''Return the running event loop.  Raise a RuntimeError if there is none.

This function is thread-specific.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.get_running_loop())
        


class AutoNode_asyncio_iscoroutine(rc.Node):
    title = 'iscoroutine'
    description = '''Return True if obj is a coroutine object.'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.iscoroutine(self.input(0)))
        


class AutoNode_asyncio_iscoroutinefunction(rc.Node):
    title = 'iscoroutinefunction'
    description = '''Return True if func is a decorated coroutine function.'''
    init_inputs = [
        rc.NodeInputBP(label='func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.iscoroutinefunction(self.input(0)))
        


class AutoNode_asyncio_isfuture(rc.Node):
    title = 'isfuture'
    description = '''Check for a Future.

    This returns True when obj is a Future instance or is advertising
    itself as duck-type compatible by setting _asyncio_future_blocking.
    See comment in Future for more details.
    '''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.isfuture(self.input(0)))
        


class AutoNode_asyncio_new_event_loop(rc.Node):
    title = 'new_event_loop'
    description = '''Equivalent to calling get_event_loop_policy().new_event_loop().'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.new_event_loop())
        


class AutoNode_asyncio_open_connection(rc.Node):
    title = 'open_connection'
    description = '''A wrapper for create_connection() returning a (reader, writer) pair.

    The reader returned is a StreamReader instance; the writer is a
    StreamWriter instance.

    The arguments are all the usual arguments to create_connection()
    except protocol_factory; most common are positional host and port,
    with various optional keyword arguments following.

    Additional optional keyword arguments are loop (to set the event loop
    instance to use) and limit (to set the buffer limit passed to the
    StreamReader).

    (If you want to customize the StreamReader and/or
    StreamReaderProtocol classes, just copy the code -- there's
    really nothing special here except some convenience.)
    '''
    init_inputs = [
        rc.NodeInputBP(label='host'),
rc.NodeInputBP(label='port'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.open_connection(self.input(0), self.input(1)))
        


class AutoNode_asyncio_run(rc.Node):
    title = 'run'
    description = '''Execute the coroutine and return the result.

    This function runs the passed coroutine, taking care of
    managing the asyncio event loop and finalizing asynchronous
    generators.

    This function cannot be called when another asyncio event loop is
    running in the same thread.

    If debug is True, the event loop will be run in debug mode.

    This function always creates a new event loop and closes it at the end.
    It should be used as a main entry point for asyncio programs, and should
    ideally only be called once.

    Example:

        async def main():
            await asyncio.sleep(1)
            print('hello')

        asyncio.run(main())
    '''
    init_inputs = [
        rc.NodeInputBP(label='main'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.run(self.input(0)))
        


class AutoNode_asyncio_run_coroutine_threadsafe(rc.Node):
    title = 'run_coroutine_threadsafe'
    description = '''Submit a coroutine object to a given event loop.

    Return a concurrent.futures.Future to access the result.
    '''
    init_inputs = [
        rc.NodeInputBP(label='coro'),
rc.NodeInputBP(label='loop'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.run_coroutine_threadsafe(self.input(0), self.input(1)))
        


class AutoNode_asyncio_set_child_watcher(rc.Node):
    title = 'set_child_watcher'
    description = '''Equivalent to calling
    get_event_loop_policy().set_child_watcher(watcher).'''
    init_inputs = [
        rc.NodeInputBP(label='watcher'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.set_child_watcher(self.input(0)))
        


class AutoNode_asyncio_set_event_loop(rc.Node):
    title = 'set_event_loop'
    description = '''Equivalent to calling get_event_loop_policy().set_event_loop(loop).'''
    init_inputs = [
        rc.NodeInputBP(label='loop'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.set_event_loop(self.input(0)))
        


class AutoNode_asyncio_set_event_loop_policy(rc.Node):
    title = 'set_event_loop_policy'
    description = '''Set the current event loop policy.

    If policy is None, the default policy is restored.'''
    init_inputs = [
        rc.NodeInputBP(label='policy'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.set_event_loop_policy(self.input(0)))
        


class AutoNode_asyncio_shield(rc.Node):
    title = 'shield'
    description = '''Wait for a future, shielding it from cancellation.

    The statement

        res = await shield(something())

    is exactly equivalent to the statement

        res = await something()

    *except* that if the coroutine containing it is cancelled, the
    task running in something() is not cancelled.  From the POV of
    something(), the cancellation did not happen.  But its caller is
    still cancelled, so the yield-from expression still raises
    CancelledError.  Note: If something() is cancelled by other means
    this will still cancel shield().

    If you want to completely ignore cancellation (not recommended)
    you can combine shield() with a try/except clause, as follows:

        try:
            res = await shield(something())
        except CancelledError:
            res = None
    '''
    init_inputs = [
        rc.NodeInputBP(label='arg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.shield(self.input(0)))
        


class AutoNode_asyncio_sleep(rc.Node):
    title = 'sleep'
    description = '''Coroutine that completes after a given time (in seconds).'''
    init_inputs = [
        rc.NodeInputBP(label='delay'),
rc.NodeInputBP(label='result'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.sleep(self.input(0), self.input(1)))
        


class AutoNode_asyncio_start_server(rc.Node):
    title = 'start_server'
    description = '''Start a socket server, call back for each client connected.

    The first parameter, `client_connected_cb`, takes two parameters:
    client_reader, client_writer.  client_reader is a StreamReader
    object, while client_writer is a StreamWriter object.  This
    parameter can either be a plain callback function or a coroutine;
    if it is a coroutine, it will be automatically converted into a
    Task.

    The rest of the arguments are all the usual arguments to
    loop.create_server() except protocol_factory; most common are
    positional host and port, with various optional keyword arguments
    following.  The return value is the same as loop.create_server().

    Additional optional keyword arguments are loop (to set the event loop
    instance to use) and limit (to set the buffer limit passed to the
    StreamReader).

    The return value is the same as loop.create_server(), i.e. a
    Server object which can be used to stop the service.
    '''
    init_inputs = [
        rc.NodeInputBP(label='client_connected_cb'),
rc.NodeInputBP(label='host'),
rc.NodeInputBP(label='port'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.start_server(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_asyncio_wait(rc.Node):
    title = 'wait'
    description = '''Wait for the Futures and coroutines given by fs to complete.

    The fs iterable must not be empty.

    Coroutines will be wrapped in Tasks.

    Returns two sets of Future: (done, pending).

    Usage:

        done, pending = await asyncio.wait(fs)

    Note: This does not raise TimeoutError! Futures that aren't done
    when the timeout occurs are returned in the second set.
    '''
    init_inputs = [
        rc.NodeInputBP(label='fs'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.wait(self.input(0)))
        


class AutoNode_asyncio_wait_for(rc.Node):
    title = 'wait_for'
    description = '''Wait for the single Future or coroutine to complete, with timeout.

    Coroutine will be wrapped in Task.

    Returns result of the Future or coroutine.  When a timeout occurs,
    it cancels the task and raises TimeoutError.  To avoid the task
    cancellation, wrap it in shield().

    If the wait is cancelled, the task is also cancelled.

    This function is a coroutine.
    '''
    init_inputs = [
        rc.NodeInputBP(label='fut'),
rc.NodeInputBP(label='timeout'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.wait_for(self.input(0), self.input(1)))
        


class AutoNode_asyncio_wrap_future(rc.Node):
    title = 'wrap_future'
    description = '''Wrap concurrent.futures.Future object.'''
    init_inputs = [
        rc.NodeInputBP(label='future'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncio.wrap_future(self.input(0)))
        