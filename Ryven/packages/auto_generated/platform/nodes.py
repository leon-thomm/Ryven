import ryvencore_qt as rc
import platform


class AutoNode_platform__comparable_version(rc.Node):
    title = '_comparable_version'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='version'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform._comparable_version(self.input(0)))
        


class AutoNode_platform__follow_symlinks(rc.Node):
    title = '_follow_symlinks'
    doc = ''' In case filepath is a symlink, follow it until a
        real file is reached.
    '''
    init_inputs = [
        rc.NodeInputBP(label='filepath'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform._follow_symlinks(self.input(0)))
        


class AutoNode_platform__java_getprop(rc.Node):
    title = '_java_getprop'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='default'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform._java_getprop(self.input(0), self.input(1)))
        


class AutoNode_platform__mac_ver_xml(rc.Node):
    title = '_mac_ver_xml'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform._mac_ver_xml())
        


class AutoNode_platform__node(rc.Node):
    title = '_node'
    doc = ''' Helper to determine the node name of this machine.
    '''
    init_inputs = [
        rc.NodeInputBP(label='default'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform._node(self.input(0)))
        


class AutoNode_platform__norm_version(rc.Node):
    title = '_norm_version'
    doc = ''' Normalize the version and build strings and return a single
        version string using the format major.minor.build (or patchlevel).
    '''
    init_inputs = [
        rc.NodeInputBP(label='version'),
rc.NodeInputBP(label='build'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform._norm_version(self.input(0), self.input(1)))
        


class AutoNode_platform__platform(rc.Node):
    title = '_platform'
    doc = ''' Helper to format the platform string in a filename
        compatible format e.g. "system-version-machine".
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform._platform())
        


class AutoNode_platform__sys_version(rc.Node):
    title = '_sys_version'
    doc = ''' Returns a parsed version of Python's sys.version as tuple
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

    '''
    init_inputs = [
        rc.NodeInputBP(label='sys_version'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform._sys_version(self.input(0)))
        


class AutoNode_platform__syscmd_file(rc.Node):
    title = '_syscmd_file'
    doc = ''' Interface to the system's file command.

        The function uses the -b option of the file command to have it
        omit the filename in its output. Follow the symlinks. It returns
        default in case the command should fail.

    '''
    init_inputs = [
        rc.NodeInputBP(label='target'),
rc.NodeInputBP(label='default'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform._syscmd_file(self.input(0), self.input(1)))
        


class AutoNode_platform__syscmd_uname(rc.Node):
    title = '_syscmd_uname'
    doc = ''' Interface to the system's uname command.
    '''
    init_inputs = [
        rc.NodeInputBP(label='option'),
rc.NodeInputBP(label='default'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform._syscmd_uname(self.input(0), self.input(1)))
        


class AutoNode_platform__syscmd_ver(rc.Node):
    title = '_syscmd_ver'
    doc = ''' Tries to figure out the OS version used and returns
        a tuple (system, release, version).

        It uses the "ver" shell command for this which is known
        to exists on Windows, DOS. XXX Others too ?

        In case this fails, the given parameters are used as
        defaults.

    '''
    init_inputs = [
        rc.NodeInputBP(label='system'),
rc.NodeInputBP(label='release'),
rc.NodeInputBP(label='version'),
rc.NodeInputBP(label='supported_platforms'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform._syscmd_ver(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_platform_architecture(rc.Node):
    title = 'architecture'
    doc = ''' Queries the given executable (defaults to the Python interpreter
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

    '''
    init_inputs = [
        rc.NodeInputBP(label='executable'),
rc.NodeInputBP(label='bits'),
rc.NodeInputBP(label='linkage'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.architecture(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_platform_java_ver(rc.Node):
    title = 'java_ver'
    doc = ''' Version interface for Jython.

        Returns a tuple (release, vendor, vminfo, osinfo) with vminfo being
        a tuple (vm_name, vm_release, vm_vendor) and osinfo being a
        tuple (os_name, os_version, os_arch).

        Values which cannot be determined are set to the defaults
        given as parameters (which all default to '').

    '''
    init_inputs = [
        rc.NodeInputBP(label='release'),
rc.NodeInputBP(label='vendor'),
rc.NodeInputBP(label='vminfo'),
rc.NodeInputBP(label='osinfo'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.java_ver(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_platform_libc_ver(rc.Node):
    title = 'libc_ver'
    doc = ''' Tries to determine the libc version that the file executable
        (which defaults to the Python interpreter) is linked against.

        Returns a tuple of strings (lib,version) which default to the
        given parameters in case the lookup fails.

        Note that the function has intimate knowledge of how different
        libc versions add symbols to the executable and thus is probably
        only useable for executables compiled using gcc.

        The file is read and scanned in chunks of chunksize bytes.

    '''
    init_inputs = [
        rc.NodeInputBP(label='executable'),
rc.NodeInputBP(label='lib'),
rc.NodeInputBP(label='version'),
rc.NodeInputBP(label='chunksize'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.libc_ver(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_platform_mac_ver(rc.Node):
    title = 'mac_ver'
    doc = ''' Get macOS version information and return it as tuple (release,
        versioninfo, machine) with versioninfo being a tuple (version,
        dev_stage, non_release_version).

        Entries which cannot be determined are set to the parameter values
        which default to ''. All tuple entries are strings.
    '''
    init_inputs = [
        rc.NodeInputBP(label='release'),
rc.NodeInputBP(label='versioninfo'),
rc.NodeInputBP(label='machine'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.mac_ver(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_platform_machine(rc.Node):
    title = 'machine'
    doc = ''' Returns the machine type, e.g. 'i386'

        An empty string is returned if the value cannot be determined.

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.machine())
        


class AutoNode_platform_node(rc.Node):
    title = 'node'
    doc = ''' Returns the computer's network name (which may not be fully
        qualified)

        An empty string is returned if the value cannot be determined.

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.node())
        


class AutoNode_platform_platform(rc.Node):
    title = 'platform'
    doc = ''' Returns a single string identifying the underlying platform
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

    '''
    init_inputs = [
        rc.NodeInputBP(label='aliased'),
rc.NodeInputBP(label='terse'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.platform(self.input(0), self.input(1)))
        


class AutoNode_platform_processor(rc.Node):
    title = 'processor'
    doc = ''' Returns the (true) processor name, e.g. 'amdk6'

        An empty string is returned if the value cannot be
        determined. Note that many platforms do not provide this
        information or simply return the same value as for machine(),
        e.g.  NetBSD does this.

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.processor())
        


class AutoNode_platform_python_branch(rc.Node):
    title = 'python_branch'
    doc = ''' Returns a string identifying the Python implementation
        branch.

        For CPython this is the SCM branch from which the
        Python binary was built.

        If not available, an empty string is returned.

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.python_branch())
        


class AutoNode_platform_python_build(rc.Node):
    title = 'python_build'
    doc = ''' Returns a tuple (buildno, builddate) stating the Python
        build number and date as strings.

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.python_build())
        


class AutoNode_platform_python_compiler(rc.Node):
    title = 'python_compiler'
    doc = ''' Returns a string identifying the compiler used for compiling
        Python.

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.python_compiler())
        


class AutoNode_platform_python_implementation(rc.Node):
    title = 'python_implementation'
    doc = ''' Returns a string identifying the Python implementation.

        Currently, the following implementations are identified:
          'CPython' (C implementation of Python),
          'IronPython' (.NET implementation of Python),
          'Jython' (Java implementation of Python),
          'PyPy' (Python implementation of Python).

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.python_implementation())
        


class AutoNode_platform_python_revision(rc.Node):
    title = 'python_revision'
    doc = ''' Returns a string identifying the Python implementation
        revision.

        For CPython this is the SCM revision from which the
        Python binary was built.

        If not available, an empty string is returned.

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.python_revision())
        


class AutoNode_platform_python_version(rc.Node):
    title = 'python_version'
    doc = ''' Returns the Python version as string 'major.minor.patchlevel'

        Note that unlike the Python sys.version, the returned value
        will always include the patchlevel (it defaults to 0).

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.python_version())
        


class AutoNode_platform_python_version_tuple(rc.Node):
    title = 'python_version_tuple'
    doc = ''' Returns the Python version as tuple (major, minor, patchlevel)
        of strings.

        Note that unlike the Python sys.version, the returned value
        will always include the patchlevel (it defaults to 0).

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.python_version_tuple())
        


class AutoNode_platform_release(rc.Node):
    title = 'release'
    doc = ''' Returns the system's release, e.g. '2.2.0' or 'NT'

        An empty string is returned if the value cannot be determined.

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.release())
        


class AutoNode_platform_system(rc.Node):
    title = 'system'
    doc = ''' Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.

        An empty string is returned if the value cannot be determined.

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.system())
        


class AutoNode_platform_system_alias(rc.Node):
    title = 'system_alias'
    doc = ''' Returns (system, release, version) aliased to common
        marketing names used for some systems.

        It also does some reordering of the information in some cases
        where it would otherwise cause confusion.

    '''
    init_inputs = [
        rc.NodeInputBP(label='system'),
rc.NodeInputBP(label='release'),
rc.NodeInputBP(label='version'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.system_alias(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_platform_uname(rc.Node):
    title = 'uname'
    doc = ''' Fairly portable uname interface. Returns a tuple
        of strings (system, node, release, version, machine, processor)
        identifying the underlying platform.

        Note that unlike the os.uname function this also returns
        possible processor information as an additional tuple entry.

        Entries which cannot be determined are set to ''.

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.uname())
        


class AutoNode_platform_version(rc.Node):
    title = 'version'
    doc = ''' Returns the system's release version, e.g. '#3 on degas'

        An empty string is returned if the value cannot be determined.

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.version())
        


class AutoNode_platform_win32_edition(rc.Node):
    title = 'win32_edition'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.win32_edition())
        


class AutoNode_platform_win32_is_iot(rc.Node):
    title = 'win32_is_iot'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.win32_is_iot())
        


class AutoNode_platform_win32_ver(rc.Node):
    title = 'win32_ver'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='release'),
rc.NodeInputBP(label='version'),
rc.NodeInputBP(label='csd'),
rc.NodeInputBP(label='ptype'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, platform.win32_ver(self.input(0), self.input(1), self.input(2), self.input(3)))
        