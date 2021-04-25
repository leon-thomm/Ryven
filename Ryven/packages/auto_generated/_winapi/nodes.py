
from NENV import *

import _winapi


class NodeBase(Node):
    pass


class AutoNode__winapi_CloseHandle(NodeBase):
    title = 'CloseHandle'
    type_ = '_winapi'
    doc = """Close handle."""
    init_inputs = [
        NodeInputBP(label='handle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CloseHandle(self.input(0)))
        

class AutoNode__winapi_ConnectNamedPipe(NodeBase):
    title = 'ConnectNamedPipe'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='handle'),
        NodeInputBP(label='overlapped'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.ConnectNamedPipe(self.input(0), self.input(1)))
        

class AutoNode__winapi_CreateFile(NodeBase):
    title = 'CreateFile'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='file_name'),
        NodeInputBP(label='desired_access'),
        NodeInputBP(label='share_mode'),
        NodeInputBP(label='security_attributes'),
        NodeInputBP(label='creation_disposition'),
        NodeInputBP(label='flags_and_attributes'),
        NodeInputBP(label='template_file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CreateFile(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        

class AutoNode__winapi_CreateFileMapping(NodeBase):
    title = 'CreateFileMapping'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='file_handle'),
        NodeInputBP(label='security_attributes'),
        NodeInputBP(label='protect'),
        NodeInputBP(label='max_size_high'),
        NodeInputBP(label='max_size_low'),
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CreateFileMapping(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class AutoNode__winapi_CreateJunction(NodeBase):
    title = 'CreateJunction'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='src_path'),
        NodeInputBP(label='dst_path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CreateJunction(self.input(0), self.input(1)))
        

class AutoNode__winapi_CreateNamedPipe(NodeBase):
    title = 'CreateNamedPipe'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='open_mode'),
        NodeInputBP(label='pipe_mode'),
        NodeInputBP(label='max_instances'),
        NodeInputBP(label='out_buffer_size'),
        NodeInputBP(label='in_buffer_size'),
        NodeInputBP(label='default_timeout'),
        NodeInputBP(label='security_attributes'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CreateNamedPipe(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        

class AutoNode__winapi_CreatePipe(NodeBase):
    title = 'CreatePipe'
    type_ = '_winapi'
    doc = """Create an anonymous pipe.

  pipe_attrs
    Ignored internally, can be None.

Returns a 2-tuple of handles, to the read and write ends of the pipe."""
    init_inputs = [
        NodeInputBP(label='pipe_attrs'),
        NodeInputBP(label='size'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CreatePipe(self.input(0), self.input(1)))
        

class AutoNode__winapi_CreateProcess(NodeBase):
    title = 'CreateProcess'
    type_ = '_winapi'
    doc = """Create a new process and its primary thread.

  command_line
    Can be str or None
  proc_attrs
    Ignored internally, can be None.
  thread_attrs
    Ignored internally, can be None.

The return value is a tuple of the process handle, thread handle,
process ID, and thread ID."""
    init_inputs = [
        NodeInputBP(label='application_name'),
        NodeInputBP(label='command_line'),
        NodeInputBP(label='proc_attrs'),
        NodeInputBP(label='thread_attrs'),
        NodeInputBP(label='inherit_handles'),
        NodeInputBP(label='creation_flags'),
        NodeInputBP(label='env_mapping'),
        NodeInputBP(label='current_directory'),
        NodeInputBP(label='startup_info'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.CreateProcess(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7), self.input(8)))
        

class AutoNode__winapi_DuplicateHandle(NodeBase):
    title = 'DuplicateHandle'
    type_ = '_winapi'
    doc = """Return a duplicate handle object.

The duplicate handle refers to the same object as the original
handle. Therefore, any changes to the object are reflected
through both handles."""
    init_inputs = [
        NodeInputBP(label='source_process_handle'),
        NodeInputBP(label='source_handle'),
        NodeInputBP(label='target_process_handle'),
        NodeInputBP(label='desired_access'),
        NodeInputBP(label='inherit_handle'),
        NodeInputBP(label='options'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.DuplicateHandle(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class AutoNode__winapi_ExitProcess(NodeBase):
    title = 'ExitProcess'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='ExitCode'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.ExitProcess(self.input(0)))
        

class AutoNode__winapi_GetACP(NodeBase):
    title = 'GetACP'
    type_ = '_winapi'
    doc = """Get the current Windows ANSI code page identifier."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetACP())
        

class AutoNode__winapi_GetCurrentProcess(NodeBase):
    title = 'GetCurrentProcess'
    type_ = '_winapi'
    doc = """Return a handle object for the current process."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetCurrentProcess())
        

class AutoNode__winapi_GetExitCodeProcess(NodeBase):
    title = 'GetExitCodeProcess'
    type_ = '_winapi'
    doc = """Return the termination status of the specified process."""
    init_inputs = [
        NodeInputBP(label='process'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetExitCodeProcess(self.input(0)))
        

class AutoNode__winapi_GetFileType(NodeBase):
    title = 'GetFileType'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='handle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetFileType(self.input(0)))
        

class AutoNode__winapi_GetLastError(NodeBase):
    title = 'GetLastError'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetLastError())
        

class AutoNode__winapi_GetModuleFileName(NodeBase):
    title = 'GetModuleFileName'
    type_ = '_winapi'
    doc = """Return the fully-qualified path for the file that contains module.

The module must have been loaded by the current process.

The module parameter should be a handle to the loaded module
whose path is being requested. If this parameter is 0,
GetModuleFileName retrieves the path of the executable file
of the current process."""
    init_inputs = [
        NodeInputBP(label='module_handle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetModuleFileName(self.input(0)))
        

class AutoNode__winapi_GetStdHandle(NodeBase):
    title = 'GetStdHandle'
    type_ = '_winapi'
    doc = """Return a handle to the specified standard device.

  std_handle
    One of STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, or STD_ERROR_HANDLE.

The integer associated with the handle object is returned."""
    init_inputs = [
        NodeInputBP(label='std_handle'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetStdHandle(self.input(0)))
        

class AutoNode__winapi_GetVersion(NodeBase):
    title = 'GetVersion'
    type_ = '_winapi'
    doc = """Return the version number of the current operating system."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.GetVersion())
        

class AutoNode__winapi_MapViewOfFile(NodeBase):
    title = 'MapViewOfFile'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='file_map'),
        NodeInputBP(label='desired_access'),
        NodeInputBP(label='file_offset_high'),
        NodeInputBP(label='file_offset_low'),
        NodeInputBP(label='number_bytes'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.MapViewOfFile(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class AutoNode__winapi_OpenFileMapping(NodeBase):
    title = 'OpenFileMapping'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='desired_access'),
        NodeInputBP(label='inherit_handle'),
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.OpenFileMapping(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__winapi_OpenProcess(NodeBase):
    title = 'OpenProcess'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='desired_access'),
        NodeInputBP(label='inherit_handle'),
        NodeInputBP(label='process_id'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.OpenProcess(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__winapi_PeekNamedPipe(NodeBase):
    title = 'PeekNamedPipe'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='handle'),
        NodeInputBP(label='size'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.PeekNamedPipe(self.input(0), self.input(1)))
        

class AutoNode__winapi_ReadFile(NodeBase):
    title = 'ReadFile'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='handle'),
        NodeInputBP(label='size'),
        NodeInputBP(label='overlapped'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.ReadFile(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__winapi_SetNamedPipeHandleState(NodeBase):
    title = 'SetNamedPipeHandleState'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='named_pipe'),
        NodeInputBP(label='mode'),
        NodeInputBP(label='max_collection_count'),
        NodeInputBP(label='collect_data_timeout'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.SetNamedPipeHandleState(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class AutoNode__winapi_TerminateProcess(NodeBase):
    title = 'TerminateProcess'
    type_ = '_winapi'
    doc = """Terminate the specified process and all of its threads."""
    init_inputs = [
        NodeInputBP(label='handle'),
        NodeInputBP(label='exit_code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.TerminateProcess(self.input(0), self.input(1)))
        

class AutoNode__winapi_VirtualQuerySize(NodeBase):
    title = 'VirtualQuerySize'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='address'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.VirtualQuerySize(self.input(0)))
        

class AutoNode__winapi_WaitForMultipleObjects(NodeBase):
    title = 'WaitForMultipleObjects'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='handle_seq'),
        NodeInputBP(label='wait_flag'),
        NodeInputBP(label='milliseconds'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.WaitForMultipleObjects(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__winapi_WaitForSingleObject(NodeBase):
    title = 'WaitForSingleObject'
    type_ = '_winapi'
    doc = """Wait for a single object.

Wait until the specified object is in the signaled state or
the time-out interval elapses. The timeout value is specified
in milliseconds."""
    init_inputs = [
        NodeInputBP(label='handle'),
        NodeInputBP(label='milliseconds'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.WaitForSingleObject(self.input(0), self.input(1)))
        

class AutoNode__winapi_WaitNamedPipe(NodeBase):
    title = 'WaitNamedPipe'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='timeout'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.WaitNamedPipe(self.input(0), self.input(1)))
        

class AutoNode__winapi_WriteFile(NodeBase):
    title = 'WriteFile'
    type_ = '_winapi'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='handle'),
        NodeInputBP(label='buffer'),
        NodeInputBP(label='overlapped'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _winapi.WriteFile(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    AutoNode__winapi_CloseHandle,
    AutoNode__winapi_ConnectNamedPipe,
    AutoNode__winapi_CreateFile,
    AutoNode__winapi_CreateFileMapping,
    AutoNode__winapi_CreateJunction,
    AutoNode__winapi_CreateNamedPipe,
    AutoNode__winapi_CreatePipe,
    AutoNode__winapi_CreateProcess,
    AutoNode__winapi_DuplicateHandle,
    AutoNode__winapi_ExitProcess,
    AutoNode__winapi_GetACP,
    AutoNode__winapi_GetCurrentProcess,
    AutoNode__winapi_GetExitCodeProcess,
    AutoNode__winapi_GetFileType,
    AutoNode__winapi_GetLastError,
    AutoNode__winapi_GetModuleFileName,
    AutoNode__winapi_GetStdHandle,
    AutoNode__winapi_GetVersion,
    AutoNode__winapi_MapViewOfFile,
    AutoNode__winapi_OpenFileMapping,
    AutoNode__winapi_OpenProcess,
    AutoNode__winapi_PeekNamedPipe,
    AutoNode__winapi_ReadFile,
    AutoNode__winapi_SetNamedPipeHandleState,
    AutoNode__winapi_TerminateProcess,
    AutoNode__winapi_VirtualQuerySize,
    AutoNode__winapi_WaitForMultipleObjects,
    AutoNode__winapi_WaitForSingleObject,
    AutoNode__winapi_WaitNamedPipe,
    AutoNode__winapi_WriteFile,
)
