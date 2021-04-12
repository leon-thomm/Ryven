import ryvencore_qt as rc
import _winapi


class AutoNode__winapi_CloseHandle(rc.Node):
    title = 'CloseHandle'
    type_ = '_winapi'
    description = '''Close handle.'''
    init_inputs = [
        rc.NodeInputBP(label='handle'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CloseHandle(self.input(0)))
        


class AutoNode__winapi_ConnectNamedPipe(rc.Node):
    title = 'ConnectNamedPipe'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='handle'),
rc.NodeInputBP(label='overlapped'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.ConnectNamedPipe(self.input(0), self.input(1)))
        


class AutoNode__winapi_CreateFile(rc.Node):
    title = 'CreateFile'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='file_name'),
rc.NodeInputBP(label='desired_access'),
rc.NodeInputBP(label='share_mode'),
rc.NodeInputBP(label='security_attributes'),
rc.NodeInputBP(label='creation_disposition'),
rc.NodeInputBP(label='flags_and_attributes'),
rc.NodeInputBP(label='template_file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CreateFile(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        


class AutoNode__winapi_CreateFileMapping(rc.Node):
    title = 'CreateFileMapping'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='file_handle'),
rc.NodeInputBP(label='security_attributes'),
rc.NodeInputBP(label='protect'),
rc.NodeInputBP(label='max_size_high'),
rc.NodeInputBP(label='max_size_low'),
rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CreateFileMapping(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode__winapi_CreateJunction(rc.Node):
    title = 'CreateJunction'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='src_path'),
rc.NodeInputBP(label='dst_path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CreateJunction(self.input(0), self.input(1)))
        


class AutoNode__winapi_CreateNamedPipe(rc.Node):
    title = 'CreateNamedPipe'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='open_mode'),
rc.NodeInputBP(label='pipe_mode'),
rc.NodeInputBP(label='max_instances'),
rc.NodeInputBP(label='out_buffer_size'),
rc.NodeInputBP(label='in_buffer_size'),
rc.NodeInputBP(label='default_timeout'),
rc.NodeInputBP(label='security_attributes'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CreateNamedPipe(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        


class AutoNode__winapi_CreatePipe(rc.Node):
    title = 'CreatePipe'
    type_ = '_winapi'
    description = '''Create an anonymous pipe.

  pipe_attrs
    Ignored internally, can be None.

Returns a 2-tuple of handles, to the read and write ends of the pipe.'''
    init_inputs = [
        rc.NodeInputBP(label='pipe_attrs'),
rc.NodeInputBP(label='size'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CreatePipe(self.input(0), self.input(1)))
        


class AutoNode__winapi_CreateProcess(rc.Node):
    title = 'CreateProcess'
    type_ = '_winapi'
    description = '''Create a new process and its primary thread.

  command_line
    Can be str or None
  proc_attrs
    Ignored internally, can be None.
  thread_attrs
    Ignored internally, can be None.

The return value is a tuple of the process handle, thread handle,
process ID, and thread ID.'''
    init_inputs = [
        rc.NodeInputBP(label='application_name'),
rc.NodeInputBP(label='command_line'),
rc.NodeInputBP(label='proc_attrs'),
rc.NodeInputBP(label='thread_attrs'),
rc.NodeInputBP(label='inherit_handles'),
rc.NodeInputBP(label='creation_flags'),
rc.NodeInputBP(label='env_mapping'),
rc.NodeInputBP(label='current_directory'),
rc.NodeInputBP(label='startup_info'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CreateProcess(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7), self.input(8)))
        


class AutoNode__winapi_DuplicateHandle(rc.Node):
    title = 'DuplicateHandle'
    type_ = '_winapi'
    description = '''Return a duplicate handle object.

The duplicate handle refers to the same object as the original
handle. Therefore, any changes to the object are reflected
through both handles.'''
    init_inputs = [
        rc.NodeInputBP(label='source_process_handle'),
rc.NodeInputBP(label='source_handle'),
rc.NodeInputBP(label='target_process_handle'),
rc.NodeInputBP(label='desired_access'),
rc.NodeInputBP(label='inherit_handle'),
rc.NodeInputBP(label='options'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.DuplicateHandle(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode__winapi_ExitProcess(rc.Node):
    title = 'ExitProcess'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='ExitCode'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.ExitProcess(self.input(0)))
        


class AutoNode__winapi_GetACP(rc.Node):
    title = 'GetACP'
    type_ = '_winapi'
    description = '''Get the current Windows ANSI code page identifier.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetACP())
        


class AutoNode__winapi_GetCurrentProcess(rc.Node):
    title = 'GetCurrentProcess'
    type_ = '_winapi'
    description = '''Return a handle object for the current process.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetCurrentProcess())
        


class AutoNode__winapi_GetExitCodeProcess(rc.Node):
    title = 'GetExitCodeProcess'
    type_ = '_winapi'
    description = '''Return the termination status of the specified process.'''
    init_inputs = [
        rc.NodeInputBP(label='process'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetExitCodeProcess(self.input(0)))
        


class AutoNode__winapi_GetFileType(rc.Node):
    title = 'GetFileType'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='handle'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetFileType(self.input(0)))
        


class AutoNode__winapi_GetLastError(rc.Node):
    title = 'GetLastError'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetLastError())
        


class AutoNode__winapi_GetModuleFileName(rc.Node):
    title = 'GetModuleFileName'
    type_ = '_winapi'
    description = '''Return the fully-qualified path for the file that contains module.

The module must have been loaded by the current process.

The module parameter should be a handle to the loaded module
whose path is being requested. If this parameter is 0,
GetModuleFileName retrieves the path of the executable file
of the current process.'''
    init_inputs = [
        rc.NodeInputBP(label='module_handle'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetModuleFileName(self.input(0)))
        


class AutoNode__winapi_GetStdHandle(rc.Node):
    title = 'GetStdHandle'
    type_ = '_winapi'
    description = '''Return a handle to the specified standard device.

  std_handle
    One of STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, or STD_ERROR_HANDLE.

The integer associated with the handle object is returned.'''
    init_inputs = [
        rc.NodeInputBP(label='std_handle'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetStdHandle(self.input(0)))
        


class AutoNode__winapi_GetVersion(rc.Node):
    title = 'GetVersion'
    type_ = '_winapi'
    description = '''Return the version number of the current operating system.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetVersion())
        


class AutoNode__winapi_MapViewOfFile(rc.Node):
    title = 'MapViewOfFile'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='file_map'),
rc.NodeInputBP(label='desired_access'),
rc.NodeInputBP(label='file_offset_high'),
rc.NodeInputBP(label='file_offset_low'),
rc.NodeInputBP(label='number_bytes'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.MapViewOfFile(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode__winapi_OpenFileMapping(rc.Node):
    title = 'OpenFileMapping'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='desired_access'),
rc.NodeInputBP(label='inherit_handle'),
rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.OpenFileMapping(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__winapi_OpenProcess(rc.Node):
    title = 'OpenProcess'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='desired_access'),
rc.NodeInputBP(label='inherit_handle'),
rc.NodeInputBP(label='process_id'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.OpenProcess(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__winapi_PeekNamedPipe(rc.Node):
    title = 'PeekNamedPipe'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='handle'),
rc.NodeInputBP(label='size'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.PeekNamedPipe(self.input(0), self.input(1)))
        


class AutoNode__winapi_ReadFile(rc.Node):
    title = 'ReadFile'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='handle'),
rc.NodeInputBP(label='size'),
rc.NodeInputBP(label='overlapped'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.ReadFile(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__winapi_SetNamedPipeHandleState(rc.Node):
    title = 'SetNamedPipeHandleState'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='named_pipe'),
rc.NodeInputBP(label='mode'),
rc.NodeInputBP(label='max_collection_count'),
rc.NodeInputBP(label='collect_data_timeout'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.SetNamedPipeHandleState(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode__winapi_TerminateProcess(rc.Node):
    title = 'TerminateProcess'
    type_ = '_winapi'
    description = '''Terminate the specified process and all of its threads.'''
    init_inputs = [
        rc.NodeInputBP(label='handle'),
rc.NodeInputBP(label='exit_code'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.TerminateProcess(self.input(0), self.input(1)))
        


class AutoNode__winapi_VirtualQuerySize(rc.Node):
    title = 'VirtualQuerySize'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='address'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.VirtualQuerySize(self.input(0)))
        


class AutoNode__winapi_WaitForMultipleObjects(rc.Node):
    title = 'WaitForMultipleObjects'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='handle_seq'),
rc.NodeInputBP(label='wait_flag'),
rc.NodeInputBP(label='milliseconds'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.WaitForMultipleObjects(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__winapi_WaitForSingleObject(rc.Node):
    title = 'WaitForSingleObject'
    type_ = '_winapi'
    description = '''Wait for a single object.

Wait until the specified object is in the signaled state or
the time-out interval elapses. The timeout value is specified
in milliseconds.'''
    init_inputs = [
        rc.NodeInputBP(label='handle'),
rc.NodeInputBP(label='milliseconds'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.WaitForSingleObject(self.input(0), self.input(1)))
        


class AutoNode__winapi_WaitNamedPipe(rc.Node):
    title = 'WaitNamedPipe'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='timeout'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.WaitNamedPipe(self.input(0), self.input(1)))
        


class AutoNode__winapi_WriteFile(rc.Node):
    title = 'WriteFile'
    type_ = '_winapi'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='handle'),
rc.NodeInputBP(label='buffer'),
rc.NodeInputBP(label='overlapped'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.WriteFile(self.input(0), self.input(1), self.input(2)))
        