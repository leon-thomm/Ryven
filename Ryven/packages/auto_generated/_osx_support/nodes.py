
from NENV import *

import _osx_support


class NodeBase(Node):
    pass


class _Check_For_Unavailable_Sdk_Node(NodeBase):
    """
    Remove references to any SDKs not available"""
    
    title = '_check_for_unavailable_sdk'
    type_ = '_osx_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._check_for_unavailable_sdk())
        

class _Default_Sysroot_Node(NodeBase):
    """
     Returns the root of the default SDK for this system, or '/' """
    
    title = '_default_sysroot'
    type_ = '_osx_support'
    init_inputs = [
        NodeInputBP(label='cc'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._default_sysroot(self.input(0)))
        

class _Find_Appropriate_Compiler_Node(NodeBase):
    """
    Find appropriate C compiler for extension module builds"""
    
    title = '_find_appropriate_compiler'
    type_ = '_osx_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._find_appropriate_compiler())
        

class _Find_Build_Tool_Node(NodeBase):
    """
    Find a build tool on current path or using xcrun"""
    
    title = '_find_build_tool'
    type_ = '_osx_support'
    init_inputs = [
        NodeInputBP(label='toolname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._find_build_tool(self.input(0)))
        

class _Find_Executable_Node(NodeBase):
    """
    Tries to find 'executable' in the directories listed in 'path'.

    A string listing directories separated by 'os.pathsep'; defaults to
    os.environ['PATH'].  Returns the complete filename or None if not found.
    """
    
    title = '_find_executable'
    type_ = '_osx_support'
    init_inputs = [
        NodeInputBP(label='executable'),
        NodeInputBP(label='path', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._find_executable(self.input(0), self.input(1)))
        

class _Get_System_Version_Node(NodeBase):
    """
    Return the OS X system version as a string"""
    
    title = '_get_system_version'
    type_ = '_osx_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._get_system_version())
        

class _Get_System_Version_Tuple_Node(NodeBase):
    """
    
    Return the macOS system version as a tuple

    The return value is safe to use to compare
    two version numbers.
    """
    
    title = '_get_system_version_tuple'
    type_ = '_osx_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._get_system_version_tuple())
        

class _Override_All_Archs_Node(NodeBase):
    """
    Allow override of all archs with ARCHFLAGS env var"""
    
    title = '_override_all_archs'
    type_ = '_osx_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._override_all_archs())
        

class _Read_Output_Node(NodeBase):
    """
    Output from successful command execution or None"""
    
    title = '_read_output'
    type_ = '_osx_support'
    init_inputs = [
        NodeInputBP(label='commandstring'),
        NodeInputBP(label='capture_stderr', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._read_output(self.input(0), self.input(1)))
        

class _Remove_Original_Values_Node(NodeBase):
    """
    Remove original unmodified values for testing"""
    
    title = '_remove_original_values'
    type_ = '_osx_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._remove_original_values())
        

class _Remove_Universal_Flags_Node(NodeBase):
    """
    Remove all universal build arguments from config vars"""
    
    title = '_remove_universal_flags'
    type_ = '_osx_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._remove_universal_flags())
        

class _Remove_Unsupported_Archs_Node(NodeBase):
    """
    Remove any unsupported archs from config vars"""
    
    title = '_remove_unsupported_archs'
    type_ = '_osx_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._remove_unsupported_archs())
        

class _Save_Modified_Value_Node(NodeBase):
    """
    Save modified and original unmodified value of configuration var"""
    
    title = '_save_modified_value'
    type_ = '_osx_support'
    init_inputs = [
        NodeInputBP(label='cv'),
        NodeInputBP(label='newvalue'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._save_modified_value(self.input(0), self.input(1)))
        

class _Supports_Arm64_Builds_Node(NodeBase):
    """
    Returns True if arm64 builds are supported on this system"""
    
    title = '_supports_arm64_builds'
    type_ = '_osx_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._supports_arm64_builds())
        

class _Supports_Universal_Builds_Node(NodeBase):
    """
    Returns True if universal builds are supported on this system"""
    
    title = '_supports_universal_builds'
    type_ = '_osx_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support._supports_universal_builds())
        

class Compiler_Fixup_Node(NodeBase):
    """
    
    This function will strip '-isysroot PATH' and '-arch ARCH' from the
    compile flags if the user has specified one them in extra_compile_flags.

    This is needed because '-arch ARCH' adds another architecture to the
    build, without a way to remove an architecture. Furthermore GCC will
    barf if multiple '-isysroot' arguments are present.
    """
    
    title = 'compiler_fixup'
    type_ = '_osx_support'
    init_inputs = [
        NodeInputBP(label='compiler_so'),
        NodeInputBP(label='cc_args'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support.compiler_fixup(self.input(0), self.input(1)))
        

class Customize_Compiler_Node(NodeBase):
    """
    Customize compiler path and configuration variables.

    This customization is performed when the first
    extension module build is requested
    in distutils.sysconfig.customize_compiler).
    """
    
    title = 'customize_compiler'
    type_ = '_osx_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support.customize_compiler())
        

class Customize_Config_Vars_Node(NodeBase):
    """
    Customize Python build configuration variables.

    Called internally from sysconfig with a mutable mapping
    containing name/value pairs parsed from the configured
    makefile used to build this interpreter.  Returns
    the mapping updated as needed to reflect the environment
    in which the interpreter is running; in the case of
    a Python from a binary installer, the installed
    environment may be very different from the build
    environment, i.e. different OS levels, different
    built tools, different available CPU architectures.

    This customization is performed whenever
    distutils.sysconfig.get_config_vars() is first
    called.  It may be used in environments where no
    compilers are present, i.e. when installing pure
    Python dists.  Customization of compiler paths
    and detection of unavailable archs is deferred
    until the first extension module build is
    requested (in distutils.sysconfig.customize_compiler).

    Currently called from distutils.sysconfig
    """
    
    title = 'customize_config_vars'
    type_ = '_osx_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support.customize_config_vars())
        

class Get_Platform_Osx_Node(NodeBase):
    """
    Filter values for get_platform()"""
    
    title = 'get_platform_osx'
    type_ = '_osx_support'
    init_inputs = [
        NodeInputBP(label='osname'),
        NodeInputBP(label='release'),
        NodeInputBP(label='machine'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _osx_support.get_platform_osx(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _Check_For_Unavailable_Sdk_Node,
    _Default_Sysroot_Node,
    _Find_Appropriate_Compiler_Node,
    _Find_Build_Tool_Node,
    _Find_Executable_Node,
    _Get_System_Version_Node,
    _Get_System_Version_Tuple_Node,
    _Override_All_Archs_Node,
    _Read_Output_Node,
    _Remove_Original_Values_Node,
    _Remove_Universal_Flags_Node,
    _Remove_Unsupported_Archs_Node,
    _Save_Modified_Value_Node,
    _Supports_Arm64_Builds_Node,
    _Supports_Universal_Builds_Node,
    Compiler_Fixup_Node,
    Customize_Compiler_Node,
    Customize_Config_Vars_Node,
    Get_Platform_Osx_Node,
)
