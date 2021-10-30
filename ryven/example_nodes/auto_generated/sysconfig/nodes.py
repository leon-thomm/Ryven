
from ryven.NENV import *

import sysconfig


class NodeBase(Node):
    pass


class _Expand_Vars_Node(NodeBase):
    """
    """
    
    title = '_expand_vars'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='scheme'),
        NodeInputBP(label='vars'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._expand_vars(self.input(0), self.input(1)))
        

class _Extend_Dict_Node(NodeBase):
    """
    """
    
    title = '_extend_dict'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='target_dict'),
        NodeInputBP(label='other_dict'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._extend_dict(self.input(0), self.input(1)))
        

class _Fix_Pcbuild_Node(NodeBase):
    """
    """
    
    title = '_fix_pcbuild'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='d'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._fix_pcbuild(self.input(0)))
        

class _Generate_Posix_Vars_Node(NodeBase):
    """
    Generate the Python module containing build-time variables."""
    
    title = '_generate_posix_vars'
    type_ = 'sysconfig'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._generate_posix_vars())
        

class _Get_Default_Scheme_Node(NodeBase):
    """
    """
    
    title = '_get_default_scheme'
    type_ = 'sysconfig'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._get_default_scheme())
        

class _Get_Sysconfigdata_Name_Node(NodeBase):
    """
    """
    
    title = '_get_sysconfigdata_name'
    type_ = 'sysconfig'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._get_sysconfigdata_name())
        

class _Getuserbase_Node(NodeBase):
    """
    """
    
    title = '_getuserbase'
    type_ = 'sysconfig'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._getuserbase())
        

class _Init_Non_Posix_Node(NodeBase):
    """
    Initialize the module as appropriate for NT"""
    
    title = '_init_non_posix'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='vars'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._init_non_posix(self.input(0)))
        

class _Init_Posix_Node(NodeBase):
    """
    Initialize the module as appropriate for POSIX systems."""
    
    title = '_init_posix'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='vars'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._init_posix(self.input(0)))
        

class _Is_Python_Source_Dir_Node(NodeBase):
    """
    """
    
    title = '_is_python_source_dir'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='d'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._is_python_source_dir(self.input(0)))
        

class _Main_Node(NodeBase):
    """
    Display all information sysconfig detains."""
    
    title = '_main'
    type_ = 'sysconfig'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._main())
        

class _Parse_Makefile_Node(NodeBase):
    """
    Parse a Makefile-style file.

    A dictionary containing name/value pairs is returned.  If an
    optional dictionary is passed in as the second argument, it is
    used instead of a new dictionary.
    """
    
    title = '_parse_makefile'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='vars', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._parse_makefile(self.input(0), self.input(1)))
        

class _Print_Dict_Node(NodeBase):
    """
    """
    
    title = '_print_dict'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='title'),
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._print_dict(self.input(0), self.input(1)))
        

class _Safe_Realpath_Node(NodeBase):
    """
    """
    
    title = '_safe_realpath'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._safe_realpath(self.input(0)))
        

class _Subst_Vars_Node(NodeBase):
    """
    """
    
    title = '_subst_vars'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='local_vars'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig._subst_vars(self.input(0), self.input(1)))
        

class Get_Config_H_Filename_Node(NodeBase):
    """
    Return the path of pyconfig.h."""
    
    title = 'get_config_h_filename'
    type_ = 'sysconfig'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig.get_config_h_filename())
        

class Get_Config_Var_Node(NodeBase):
    """
    Return the value of a single variable using the dictionary returned by
    'get_config_vars()'.

    Equivalent to get_config_vars().get(name)
    """
    
    title = 'get_config_var'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig.get_config_var(self.input(0)))
        

class Get_Config_Vars_Node(NodeBase):
    """
    With no arguments, return a dictionary of all configuration
    variables relevant for the current platform.

    On Unix, this means every variable defined in Python's installed Makefile;
    On Windows it's a much smaller set.

    With arguments, return a list of values that result from looking up
    each argument in the configuration variable dictionary.
    """
    
    title = 'get_config_vars'
    type_ = 'sysconfig'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig.get_config_vars())
        

class Get_Makefile_Filename_Node(NodeBase):
    """
    Return the path of the Makefile."""
    
    title = 'get_makefile_filename'
    type_ = 'sysconfig'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig.get_makefile_filename())
        

class Get_Path_Node(NodeBase):
    """
    Return a path corresponding to the scheme.

    ``scheme`` is the install scheme name.
    """
    
    title = 'get_path'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='scheme', dtype=dtypes.Data(default='nt', size='s')),
        NodeInputBP(label='vars', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='expand', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig.get_path(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Get_Path_Names_Node(NodeBase):
    """
    Return a tuple containing the paths names."""
    
    title = 'get_path_names'
    type_ = 'sysconfig'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig.get_path_names())
        

class Get_Paths_Node(NodeBase):
    """
    Return a mapping containing an install scheme.

    ``scheme`` is the install scheme name. If not provided, it will
    return the default scheme for the current platform.
    """
    
    title = 'get_paths'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='scheme', dtype=dtypes.Data(default='nt', size='s')),
        NodeInputBP(label='vars', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='expand', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig.get_paths(self.input(0), self.input(1), self.input(2)))
        

class Get_Platform_Node(NodeBase):
    """
    Return a string that identifies the current platform.

    This is used mainly to distinguish platform-specific build directories and
    platform-specific built distributions.  Typically includes the OS name and
    version and the architecture (as supplied by 'os.uname()'), although the
    exact information included depends on the OS; on Linux, the kernel version
    isn't particularly important.

    Examples of returned values:
       linux-i586
       linux-alpha (?)
       solaris-2.6-sun4u

    Windows will return one of:
       win-amd64 (64bit Windows on AMD64 (aka x86_64, Intel64, EM64T, etc)
       win32 (all others - specifically, sys.platform is returned)

    For other non-POSIX platforms, currently just returns 'sys.platform'.

    """
    
    title = 'get_platform'
    type_ = 'sysconfig'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig.get_platform())
        

class Get_Python_Version_Node(NodeBase):
    """
    """
    
    title = 'get_python_version'
    type_ = 'sysconfig'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig.get_python_version())
        

class Get_Scheme_Names_Node(NodeBase):
    """
    Return a tuple containing the schemes names."""
    
    title = 'get_scheme_names'
    type_ = 'sysconfig'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig.get_scheme_names())
        

class Is_Python_Build_Node(NodeBase):
    """
    """
    
    title = 'is_python_build'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='check_home', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig.is_python_build(self.input(0)))
        

class Parse_Config_H_Node(NodeBase):
    """
    Parse a config.h-style file.

    A dictionary containing name/value pairs is returned.  If an
    optional dictionary is passed in as the second argument, it is
    used instead of a new dictionary.
    """
    
    title = 'parse_config_h'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='fp'),
        NodeInputBP(label='vars', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig.parse_config_h(self.input(0), self.input(1)))
        

class Realpath_Node(NodeBase):
    """
    """
    
    title = 'realpath'
    type_ = 'sysconfig'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sysconfig.realpath(self.input(0)))
        


export_nodes(
    _Expand_Vars_Node,
    _Extend_Dict_Node,
    _Fix_Pcbuild_Node,
    _Generate_Posix_Vars_Node,
    _Get_Default_Scheme_Node,
    _Get_Sysconfigdata_Name_Node,
    _Getuserbase_Node,
    _Init_Non_Posix_Node,
    _Init_Posix_Node,
    _Is_Python_Source_Dir_Node,
    _Main_Node,
    _Parse_Makefile_Node,
    _Print_Dict_Node,
    _Safe_Realpath_Node,
    _Subst_Vars_Node,
    Get_Config_H_Filename_Node,
    Get_Config_Var_Node,
    Get_Config_Vars_Node,
    Get_Makefile_Filename_Node,
    Get_Path_Node,
    Get_Path_Names_Node,
    Get_Paths_Node,
    Get_Platform_Node,
    Get_Python_Version_Node,
    Get_Scheme_Names_Node,
    Is_Python_Build_Node,
    Parse_Config_H_Node,
    Realpath_Node,
)
