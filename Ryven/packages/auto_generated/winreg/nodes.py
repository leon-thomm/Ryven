import ryvencore_qt as rc
import winreg


class AutoNode_winreg_CloseKey(rc.Node):
    title = 'CloseKey'
    type_ = 'winreg'
    description = '''Closes a previously opened registry key.

  hkey
    A previously opened key.

Note that if the key is not closed using this method, it will be
closed when the hkey object is destroyed by Python.'''
    init_inputs = [
        rc.NodeInputBP(label='hkey'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.CloseKey(self.input(0)))
        


class AutoNode_winreg_ConnectRegistry(rc.Node):
    title = 'ConnectRegistry'
    type_ = 'winreg'
    description = '''Establishes a connection to the registry on another computer.

  computer_name
    The name of the remote computer, of the form r"\\computername".  If
    None, the local computer is used.
  key
    The predefined key to connect to.

The return value is the handle of the opened key.
If the function fails, an OSError exception is raised.'''
    init_inputs = [
        rc.NodeInputBP(label='computer_name'),
rc.NodeInputBP(label='key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.ConnectRegistry(self.input(0), self.input(1)))
        


class AutoNode_winreg_CreateKey(rc.Node):
    title = 'CreateKey'
    type_ = 'winreg'
    description = '''Creates or opens the specified key.

  key
    An already open key, or one of the predefined HKEY_* constants.
  sub_key
    The name of the key this method opens or creates.

If key is one of the predefined keys, sub_key may be None. In that case,
the handle returned is the same key handle passed in to the function.

If the key already exists, this function opens the existing key.

The return value is the handle of the opened key.
If the function fails, an OSError exception is raised.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='sub_key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.CreateKey(self.input(0), self.input(1)))
        


class AutoNode_winreg_CreateKeyEx(rc.Node):
    title = 'CreateKeyEx'
    type_ = 'winreg'
    description = '''Creates or opens the specified key.

  key
    An already open key, or one of the predefined HKEY_* constants.
  sub_key
    The name of the key this method opens or creates.
  reserved
    A reserved integer, and must be zero.  Default is zero.
  access
    An integer that specifies an access mask that describes the
    desired security access for the key. Default is KEY_WRITE.

If key is one of the predefined keys, sub_key may be None. In that case,
the handle returned is the same key handle passed in to the function.

If the key already exists, this function opens the existing key

The return value is the handle of the opened key.
If the function fails, an OSError exception is raised.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='sub_key'),
rc.NodeInputBP(label='reserved'),
rc.NodeInputBP(label='access'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.CreateKeyEx(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_winreg_DeleteKey(rc.Node):
    title = 'DeleteKey'
    type_ = 'winreg'
    description = '''Deletes the specified key.

  key
    An already open key, or any one of the predefined HKEY_* constants.
  sub_key
    A string that must be the name of a subkey of the key identified by
    the key parameter. This value must not be None, and the key may not
    have subkeys.

This method can not delete keys with subkeys.

If the function succeeds, the entire key, including all of its values,
is removed.  If the function fails, an OSError exception is raised.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='sub_key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.DeleteKey(self.input(0), self.input(1)))
        


class AutoNode_winreg_DeleteKeyEx(rc.Node):
    title = 'DeleteKeyEx'
    type_ = 'winreg'
    description = '''Deletes the specified key (64-bit OS only).

  key
    An already open key, or any one of the predefined HKEY_* constants.
  sub_key
    A string that must be the name of a subkey of the key identified by
    the key parameter. This value must not be None, and the key may not
    have subkeys.
  access
    An integer that specifies an access mask that describes the
    desired security access for the key. Default is KEY_WOW64_64KEY.
  reserved
    A reserved integer, and must be zero.  Default is zero.

This method can not delete keys with subkeys.

If the function succeeds, the entire key, including all of its values,
is removed.  If the function fails, an OSError exception is raised.
On unsupported Windows versions, NotImplementedError is raised.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='sub_key'),
rc.NodeInputBP(label='access'),
rc.NodeInputBP(label='reserved'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.DeleteKeyEx(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_winreg_DeleteValue(rc.Node):
    title = 'DeleteValue'
    type_ = 'winreg'
    description = '''Removes a named value from a registry key.

  key
    An already open key, or any one of the predefined HKEY_* constants.
  value
    A string that identifies the value to remove.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.DeleteValue(self.input(0), self.input(1)))
        


class AutoNode_winreg_DisableReflectionKey(rc.Node):
    title = 'DisableReflectionKey'
    type_ = 'winreg'
    description = '''Disables registry reflection for 32bit processes running on a 64bit OS.

  key
    An already open key, or any one of the predefined HKEY_* constants.

Will generally raise NotImplementedError if executed on a 32bit OS.

If the key is not on the reflection list, the function succeeds but has
no effect.  Disabling reflection for a key does not affect reflection
of any subkeys.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.DisableReflectionKey(self.input(0)))
        


class AutoNode_winreg_EnableReflectionKey(rc.Node):
    title = 'EnableReflectionKey'
    type_ = 'winreg'
    description = '''Restores registry reflection for the specified disabled key.

  key
    An already open key, or any one of the predefined HKEY_* constants.

Will generally raise NotImplementedError if executed on a 32bit OS.
Restoring reflection for a key does not affect reflection of any
subkeys.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.EnableReflectionKey(self.input(0)))
        


class AutoNode_winreg_EnumKey(rc.Node):
    title = 'EnumKey'
    type_ = 'winreg'
    description = '''Enumerates subkeys of an open registry key.

  key
    An already open key, or any one of the predefined HKEY_* constants.
  index
    An integer that identifies the index of the key to retrieve.

The function retrieves the name of one subkey each time it is called.
It is typically called repeatedly until an OSError exception is
raised, indicating no more values are available.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='index'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.EnumKey(self.input(0), self.input(1)))
        


class AutoNode_winreg_EnumValue(rc.Node):
    title = 'EnumValue'
    type_ = 'winreg'
    description = '''Enumerates values of an open registry key.

  key
    An already open key, or any one of the predefined HKEY_* constants.
  index
    An integer that identifies the index of the value to retrieve.

The function retrieves the name of one subkey each time it is called.
It is typically called repeatedly, until an OSError exception
is raised, indicating no more values.

The result is a tuple of 3 items:
  value_name
    A string that identifies the value.
  value_data
    An object that holds the value data, and whose type depends
    on the underlying registry type.
  data_type
    An integer that identifies the type of the value data.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='index'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.EnumValue(self.input(0), self.input(1)))
        


class AutoNode_winreg_ExpandEnvironmentStrings(rc.Node):
    title = 'ExpandEnvironmentStrings'
    type_ = 'winreg'
    description = '''Expand environment vars.'''
    init_inputs = [
        rc.NodeInputBP(label='string'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.ExpandEnvironmentStrings(self.input(0)))
        


class AutoNode_winreg_FlushKey(rc.Node):
    title = 'FlushKey'
    type_ = 'winreg'
    description = '''Writes all the attributes of a key to the registry.

  key
    An already open key, or any one of the predefined HKEY_* constants.

It is not necessary to call FlushKey to change a key.  Registry changes
are flushed to disk by the registry using its lazy flusher.  Registry
changes are also flushed to disk at system shutdown.  Unlike
CloseKey(), the FlushKey() method returns only when all the data has
been written to the registry.

An application should only call FlushKey() if it requires absolute
certainty that registry changes are on disk.  If you don't know whether
a FlushKey() call is required, it probably isn't.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.FlushKey(self.input(0)))
        


class AutoNode_winreg_LoadKey(rc.Node):
    title = 'LoadKey'
    type_ = 'winreg'
    description = '''Insert data into the registry from a file.

  key
    An already open key, or any one of the predefined HKEY_* constants.
  sub_key
    A string that identifies the sub-key to load.
  file_name
    The name of the file to load registry data from.  This file must
    have been created with the SaveKey() function.  Under the file
    allocation table (FAT) file system, the filename may not have an
    extension.

Creates a subkey under the specified key and stores registration
information from a specified file into that subkey.

A call to LoadKey() fails if the calling process does not have the
SE_RESTORE_PRIVILEGE privilege.

If key is a handle returned by ConnectRegistry(), then the path
specified in fileName is relative to the remote computer.

The MSDN docs imply key must be in the HKEY_USER or HKEY_LOCAL_MACHINE
tree.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='sub_key'),
rc.NodeInputBP(label='file_name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.LoadKey(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_winreg_OpenKey(rc.Node):
    title = 'OpenKey'
    type_ = 'winreg'
    description = '''Opens the specified key.

  key
    An already open key, or any one of the predefined HKEY_* constants.
  sub_key
    A string that identifies the sub_key to open.
  reserved
    A reserved integer that must be zero.  Default is zero.
  access
    An integer that specifies an access mask that describes the desired
    security access for the key.  Default is KEY_READ.

The result is a new handle to the specified key.
If the function fails, an OSError exception is raised.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='sub_key'),
rc.NodeInputBP(label='reserved'),
rc.NodeInputBP(label='access'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.OpenKey(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_winreg_OpenKeyEx(rc.Node):
    title = 'OpenKeyEx'
    type_ = 'winreg'
    description = '''Opens the specified key.

  key
    An already open key, or any one of the predefined HKEY_* constants.
  sub_key
    A string that identifies the sub_key to open.
  reserved
    A reserved integer that must be zero.  Default is zero.
  access
    An integer that specifies an access mask that describes the desired
    security access for the key.  Default is KEY_READ.

The result is a new handle to the specified key.
If the function fails, an OSError exception is raised.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='sub_key'),
rc.NodeInputBP(label='reserved'),
rc.NodeInputBP(label='access'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.OpenKeyEx(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_winreg_QueryInfoKey(rc.Node):
    title = 'QueryInfoKey'
    type_ = 'winreg'
    description = '''Returns information about a key.

  key
    An already open key, or any one of the predefined HKEY_* constants.

The result is a tuple of 3 items:
An integer that identifies the number of sub keys this key has.
An integer that identifies the number of values this key has.
An integer that identifies when the key was last modified (if available)
as 100's of nanoseconds since Jan 1, 1600.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.QueryInfoKey(self.input(0)))
        


class AutoNode_winreg_QueryReflectionKey(rc.Node):
    title = 'QueryReflectionKey'
    type_ = 'winreg'
    description = '''Returns the reflection state for the specified key as a bool.

  key
    An already open key, or any one of the predefined HKEY_* constants.

Will generally raise NotImplementedError if executed on a 32bit OS.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.QueryReflectionKey(self.input(0)))
        


class AutoNode_winreg_QueryValue(rc.Node):
    title = 'QueryValue'
    type_ = 'winreg'
    description = '''Retrieves the unnamed value for a key.

  key
    An already open key, or any one of the predefined HKEY_* constants.
  sub_key
    A string that holds the name of the subkey with which the value
    is associated.  If this parameter is None or empty, the function
    retrieves the value set by the SetValue() method for the key
    identified by key.

Values in the registry have name, type, and data components. This method
retrieves the data for a key's first value that has a NULL name.
But since the underlying API call doesn't return the type, you'll
probably be happier using QueryValueEx; this function is just here for
completeness.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='sub_key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.QueryValue(self.input(0), self.input(1)))
        


class AutoNode_winreg_QueryValueEx(rc.Node):
    title = 'QueryValueEx'
    type_ = 'winreg'
    description = '''Retrieves the type and value of a specified sub-key.

  key
    An already open key, or any one of the predefined HKEY_* constants.
  name
    A string indicating the value to query.

Behaves mostly like QueryValue(), but also returns the type of the
specified value name associated with the given open registry key.

The return value is a tuple of the value and the type_id.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.QueryValueEx(self.input(0), self.input(1)))
        


class AutoNode_winreg_SaveKey(rc.Node):
    title = 'SaveKey'
    type_ = 'winreg'
    description = '''Saves the specified key, and all its subkeys to the specified file.

  key
    An already open key, or any one of the predefined HKEY_* constants.
  file_name
    The name of the file to save registry data to.  This file cannot
    already exist. If this filename includes an extension, it cannot be
    used on file allocation table (FAT) file systems by the LoadKey(),
    ReplaceKey() or RestoreKey() methods.

If key represents a key on a remote computer, the path described by
file_name is relative to the remote computer.

The caller of this method must possess the SeBackupPrivilege
security privilege.  This function passes NULL for security_attributes
to the API.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='file_name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.SaveKey(self.input(0), self.input(1)))
        


class AutoNode_winreg_SetValue(rc.Node):
    title = 'SetValue'
    type_ = 'winreg'
    description = '''Associates a value with a specified key.

  key
    An already open key, or any one of the predefined HKEY_* constants.
  sub_key
    A string that names the subkey with which the value is associated.
  type
    An integer that specifies the type of the data.  Currently this must
    be REG_SZ, meaning only strings are supported.
  value
    A string that specifies the new value.

If the key specified by the sub_key parameter does not exist, the
SetValue function creates it.

Value lengths are limited by available memory. Long values (more than
2048 bytes) should be stored as files with the filenames stored in
the configuration registry to help the registry perform efficiently.

The key identified by the key parameter must have been opened with
KEY_SET_VALUE access.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='sub_key'),
rc.NodeInputBP(label='type'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.SetValue(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_winreg_SetValueEx(rc.Node):
    title = 'SetValueEx'
    type_ = 'winreg'
    description = '''Stores data in the value field of an open registry key.

  key
    An already open key, or any one of the predefined HKEY_* constants.
  value_name
    A string containing the name of the value to set, or None.
  reserved
    Can be anything - zero is always passed to the API.
  type
    An integer that specifies the type of the data, one of:
    REG_BINARY -- Binary data in any form.
    REG_DWORD -- A 32-bit number.
    REG_DWORD_LITTLE_ENDIAN -- A 32-bit number in little-endian format. Equivalent to REG_DWORD
    REG_DWORD_BIG_ENDIAN -- A 32-bit number in big-endian format.
    REG_EXPAND_SZ -- A null-terminated string that contains unexpanded
                     references to environment variables (for example,
                     %PATH%).
    REG_LINK -- A Unicode symbolic link.
    REG_MULTI_SZ -- A sequence of null-terminated strings, terminated
                    by two null characters.  Note that Python handles
                    this termination automatically.
    REG_NONE -- No defined value type.
    REG_QWORD -- A 64-bit number.
    REG_QWORD_LITTLE_ENDIAN -- A 64-bit number in little-endian format. Equivalent to REG_QWORD.
    REG_RESOURCE_LIST -- A device-driver resource list.
    REG_SZ -- A null-terminated string.
  value
    A string that specifies the new value.

This method can also set additional value and type information for the
specified key.  The key identified by the key parameter must have been
opened with KEY_SET_VALUE access.

To open the key, use the CreateKeyEx() or OpenKeyEx() methods.

Value lengths are limited by available memory. Long values (more than
2048 bytes) should be stored as files with the filenames stored in
the configuration registry to help the registry perform efficiently.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='value_name'),
rc.NodeInputBP(label='reserved'),
rc.NodeInputBP(label='type'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, winreg.SetValueEx(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        