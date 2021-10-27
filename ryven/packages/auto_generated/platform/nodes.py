
from NENV import *

import platform


class NodeBase(Node):
    pass


class _Comparable_Version_Node(NodeBase):
    """
    """
    
    title = '_comparable_version'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='version'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform._comparable_version(self.input(0)))
        

class _Follow_Symlinks_Node(NodeBase):
    """
     In case filepath is a symlink, follow it until a
        real file is reached.
    """
    
    title = '_follow_symlinks'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='filepath'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform._follow_symlinks(self.input(0)))
        

class _Get_Machine_Win32_Node(NodeBase):
    """
    """
    
    title = '_get_machine_win32'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform._get_machine_win32())
        

class _Java_Getprop_Node(NodeBase):
    """
    """
    
    title = '_java_getprop'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='default'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform._java_getprop(self.input(0), self.input(1)))
        

class _Mac_Ver_Xml_Node(NodeBase):
    """
    """
    
    title = '_mac_ver_xml'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform._mac_ver_xml())
        

class _Node_Node(NodeBase):
    """
     Helper to determine the node name of this machine.
    """
    
    title = '_node'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='default', dtype=dtypes.Data(default='', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform._node(self.input(0)))
        

class _Norm_Version_Node(NodeBase):
    """
     Normalize the version and build strings and return a single
        version string using the format major.minor.build (or patchlevel).
    """
    
    title = '_norm_version'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='version'),
        NodeInputBP(label='build', dtype=dtypes.Data(default='', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform._norm_version(self.input(0), self.input(1)))
        

class _Platform_Node(NodeBase):
    """
     Helper to format the platform string in a filename
        compatible format e.g. "system-version-machine".
    """
    
    title = '_platform'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform._platform())
        

class _Sys_Version_Node(NodeBase):
    """
     Returns a parsed version of Python's sys.version as tuple
        (name, version, branch, revision, buildno, builddate, compiler)
        referring to the Python implementation name, version, branch,
        revision, build number, build date/time as string and the compiler
        identification string.

        Note that unlike the Python sys.version, the returned value
        for the Python version will always include the patchlevel (it
        defaults to '.0').

        The function returns empty strings for tuple entries that
        cannot be determined.

        sys_version may be given to parse an alternative version
        string, e.g. if the version was read from a different Python
        interpreter.

    """
    
    title = '_sys_version'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='sys_version', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform._sys_version(self.input(0)))
        

class _Syscmd_File_Node(NodeBase):
    """
     Interface to the system's file command.

        The function uses the -b option of the file command to have it
        omit the filename in its output. Follow the symlinks. It returns
        default in case the command should fail.

    """
    
    title = '_syscmd_file'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='target'),
        NodeInputBP(label='default', dtype=dtypes.Data(default='', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform._syscmd_file(self.input(0), self.input(1)))
        

class _Syscmd_Ver_Node(NodeBase):
    """
     Tries to figure out the OS version used and returns
        a tuple (system, release, version).

        It uses the "ver" shell command for this which is known
        to exists on Windows, DOS. XXX Others too ?

        In case this fails, the given parameters are used as
        defaults.

    """
    
    title = '_syscmd_ver'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='system', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='release', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='version', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='supported_platforms', dtype=dtypes.Data(default=('win32', 'win16', 'dos'), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform._syscmd_ver(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Unknown_As_Blank_Node(NodeBase):
    """
    """
    
    title = '_unknown_as_blank'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='val'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform._unknown_as_blank(self.input(0)))
        

class Architecture_Node(NodeBase):
    """
     Queries the given executable (defaults to the Python interpreter
        binary) for various architecture information.

        Returns a tuple (bits, linkage) which contains information about
        the bit architecture and the linkage format used for the
        executable. Both values are returned as strings.

        Values that cannot be determined are returned as given by the
        parameter presets. If bits is given as '', the sizeof(pointer)
        (or sizeof(long) on Python version < 1.5.2) is used as
        indicator for the supported pointer size.

        The function relies on the system's "file" command to do the
        actual work. This is available on most if not all Unix
        platforms. On some non-Unix platforms where the "file" command
        does not exist and the executable is set to the Python interpreter
        binary defaults from _default_architecture are used.

    """
    
    title = 'architecture'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='executable', dtype=dtypes.Data(default='C:\Users\nutri\projects\ryven projects\venv\Scripts\python.exe', size='s')),
        NodeInputBP(label='bits', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='linkage', dtype=dtypes.Data(default='', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.architecture(self.input(0), self.input(1), self.input(2)))
        

class Java_Ver_Node(NodeBase):
    """
     Version interface for Jython.

        Returns a tuple (release, vendor, vminfo, osinfo) with vminfo being
        a tuple (vm_name, vm_release, vm_vendor) and osinfo being a
        tuple (os_name, os_version, os_arch).

        Values which cannot be determined are set to the defaults
        given as parameters (which all default to '').

    """
    
    title = 'java_ver'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='release', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='vendor', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='vminfo', dtype=dtypes.Data(default=('', '', ''), size='s')),
        NodeInputBP(label='osinfo', dtype=dtypes.Data(default=('', '', ''), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.java_ver(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Libc_Ver_Node(NodeBase):
    """
     Tries to determine the libc version that the file executable
        (which defaults to the Python interpreter) is linked against.

        Returns a tuple of strings (lib,version) which default to the
        given parameters in case the lookup fails.

        Note that the function has intimate knowledge of how different
        libc versions add symbols to the executable and thus is probably
        only useable for executables compiled using gcc.

        The file is read and scanned in chunks of chunksize bytes.

    """
    
    title = 'libc_ver'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='executable', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='lib', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='version', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='chunksize', dtype=dtypes.Data(default=16384, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.libc_ver(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Mac_Ver_Node(NodeBase):
    """
     Get macOS version information and return it as tuple (release,
        versioninfo, machine) with versioninfo being a tuple (version,
        dev_stage, non_release_version).

        Entries which cannot be determined are set to the parameter values
        which default to ''. All tuple entries are strings.
    """
    
    title = 'mac_ver'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='release', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='versioninfo', dtype=dtypes.Data(default=('', '', ''), size='s')),
        NodeInputBP(label='machine', dtype=dtypes.Data(default='', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.mac_ver(self.input(0), self.input(1), self.input(2)))
        

class Machine_Node(NodeBase):
    """
     Returns the machine type, e.g. 'i386'

        An empty string is returned if the value cannot be determined.

    """
    
    title = 'machine'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.machine())
        

class Node_Node(NodeBase):
    """
     Returns the computer's network name (which may not be fully
        qualified)

        An empty string is returned if the value cannot be determined.

    """
    
    title = 'node'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.node())
        

class Platform_Node(NodeBase):
    """
     Returns a single string identifying the underlying platform
        with as much useful information as possible (but no more :).

        The output is intended to be human readable rather than
        machine parseable. It may look different on different
        platforms and this is intended.

        If "aliased" is true, the function will use aliases for
        various platforms that report system names which differ from
        their common names, e.g. SunOS will be reported as
        Solaris. The system_alias() function is used to implement
        this.

        Setting terse to true causes the function to return only the
        absolute minimum information needed to identify the platform.

    """
    
    title = 'platform'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='aliased', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='terse', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.platform(self.input(0), self.input(1)))
        

class Processor_Node(NodeBase):
    """
     Returns the (true) processor name, e.g. 'amdk6'

        An empty string is returned if the value cannot be
        determined. Note that many platforms do not provide this
        information or simply return the same value as for machine(),
        e.g.  NetBSD does this.

    """
    
    title = 'processor'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.processor())
        

class Python_Branch_Node(NodeBase):
    """
     Returns a string identifying the Python implementation
        branch.

        For CPython this is the SCM branch from which the
        Python binary was built.

        If not available, an empty string is returned.

    """
    
    title = 'python_branch'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.python_branch())
        

class Python_Build_Node(NodeBase):
    """
     Returns a tuple (buildno, builddate) stating the Python
        build number and date as strings.

    """
    
    title = 'python_build'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.python_build())
        

class Python_Compiler_Node(NodeBase):
    """
     Returns a string identifying the compiler used for compiling
        Python.

    """
    
    title = 'python_compiler'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.python_compiler())
        

class Python_Implementation_Node(NodeBase):
    """
     Returns a string identifying the Python implementation.

        Currently, the following implementations are identified:
          'CPython' (C implementation of Python),
          'IronPython' (.NET implementation of Python),
          'Jython' (Java implementation of Python),
          'PyPy' (Python implementation of Python).

    """
    
    title = 'python_implementation'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.python_implementation())
        

class Python_Revision_Node(NodeBase):
    """
     Returns a string identifying the Python implementation
        revision.

        For CPython this is the SCM revision from which the
        Python binary was built.

        If not available, an empty string is returned.

    """
    
    title = 'python_revision'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.python_revision())
        

class Python_Version_Node(NodeBase):
    """
     Returns the Python version as string 'major.minor.patchlevel'

        Note that unlike the Python sys.version, the returned value
        will always include the patchlevel (it defaults to 0).

    """
    
    title = 'python_version'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.python_version())
        

class Python_Version_Tuple_Node(NodeBase):
    """
     Returns the Python version as tuple (major, minor, patchlevel)
        of strings.

        Note that unlike the Python sys.version, the returned value
        will always include the patchlevel (it defaults to 0).

    """
    
    title = 'python_version_tuple'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.python_version_tuple())
        

class Release_Node(NodeBase):
    """
     Returns the system's release, e.g. '2.2.0' or 'NT'

        An empty string is returned if the value cannot be determined.

    """
    
    title = 'release'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.release())
        

class System_Node(NodeBase):
    """
     Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.

        An empty string is returned if the value cannot be determined.

    """
    
    title = 'system'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.system())
        

class System_Alias_Node(NodeBase):
    """
     Returns (system, release, version) aliased to common
        marketing names used for some systems.

        It also does some reordering of the information in some cases
        where it would otherwise cause confusion.

    """
    
    title = 'system_alias'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='system'),
        NodeInputBP(label='release'),
        NodeInputBP(label='version'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.system_alias(self.input(0), self.input(1), self.input(2)))
        

class Uname_Node(NodeBase):
    """
     Fairly portable uname interface. Returns a tuple
        of strings (system, node, release, version, machine, processor)
        identifying the underlying platform.

        Note that unlike the os.uname function this also returns
        possible processor information as an additional tuple entry.

        Entries which cannot be determined are set to ''.

    """
    
    title = 'uname'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.uname())
        

class Version_Node(NodeBase):
    """
     Returns the system's release version, e.g. '#3 on degas'

        An empty string is returned if the value cannot be determined.

    """
    
    title = 'version'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.version())
        

class Win32_Edition_Node(NodeBase):
    """
    """
    
    title = 'win32_edition'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.win32_edition())
        

class Win32_Is_Iot_Node(NodeBase):
    """
    """
    
    title = 'win32_is_iot'
    type_ = 'platform'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.win32_is_iot())
        

class Win32_Ver_Node(NodeBase):
    """
    """
    
    title = 'win32_ver'
    type_ = 'platform'
    init_inputs = [
        NodeInputBP(label='release', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='version', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='csd', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='ptype', dtype=dtypes.Data(default='', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, platform.win32_ver(self.input(0), self.input(1), self.input(2), self.input(3)))
        


export_nodes(
    _Comparable_Version_Node,
    _Follow_Symlinks_Node,
    _Get_Machine_Win32_Node,
    _Java_Getprop_Node,
    _Mac_Ver_Xml_Node,
    _Node_Node,
    _Norm_Version_Node,
    _Platform_Node,
    _Sys_Version_Node,
    _Syscmd_File_Node,
    _Syscmd_Ver_Node,
    _Unknown_As_Blank_Node,
    Architecture_Node,
    Java_Ver_Node,
    Libc_Ver_Node,
    Mac_Ver_Node,
    Machine_Node,
    Node_Node,
    Platform_Node,
    Processor_Node,
    Python_Branch_Node,
    Python_Build_Node,
    Python_Compiler_Node,
    Python_Implementation_Node,
    Python_Revision_Node,
    Python_Version_Node,
    Python_Version_Tuple_Node,
    Release_Node,
    System_Node,
    System_Alias_Node,
    Uname_Node,
    Version_Node,
    Win32_Edition_Node,
    Win32_Is_Iot_Node,
    Win32_Ver_Node,
)
