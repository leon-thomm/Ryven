
from ryven.NENV import *

import site


class NodeBase(Node):
    pass


class _Get_Path_Node(NodeBase):
    """
    """
    
    title = '_get_path'
    type_ = 'site'
    init_inputs = [
        NodeInputBP(label='userbase'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site._get_path(self.input(0)))
        

class _Getuserbase_Node(NodeBase):
    """
    """
    
    title = '_getuserbase'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site._getuserbase())
        

class _Init_Pathinfo_Node(NodeBase):
    """
    Return a set containing all existing file system items from sys.path."""
    
    title = '_init_pathinfo'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site._init_pathinfo())
        

class _Script_Node(NodeBase):
    """
    """
    
    title = '_script'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site._script())
        

class Abs_Paths_Node(NodeBase):
    """
    Set all module __file__ and __cached__ attributes to an absolute path"""
    
    title = 'abs_paths'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.abs_paths())
        

class Addpackage_Node(NodeBase):
    """
    Process a .pth file within the site-packages directory:
       For each line in the file, either combine it with sitedir to a path
       and add that to known_paths, or execute it if it starts with 'import '.
    """
    
    title = 'addpackage'
    type_ = 'site'
    init_inputs = [
        NodeInputBP(label='sitedir'),
        NodeInputBP(label='name'),
        NodeInputBP(label='known_paths'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.addpackage(self.input(0), self.input(1), self.input(2)))
        

class Addsitedir_Node(NodeBase):
    """
    Add 'sitedir' argument to sys.path if missing and handle .pth files in
    'sitedir'"""
    
    title = 'addsitedir'
    type_ = 'site'
    init_inputs = [
        NodeInputBP(label='sitedir'),
        NodeInputBP(label='known_paths', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.addsitedir(self.input(0), self.input(1)))
        

class Addsitepackages_Node(NodeBase):
    """
    Add site-packages to sys.path"""
    
    title = 'addsitepackages'
    type_ = 'site'
    init_inputs = [
        NodeInputBP(label='known_paths'),
        NodeInputBP(label='prefixes', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.addsitepackages(self.input(0), self.input(1)))
        

class Addusersitepackages_Node(NodeBase):
    """
    Add a per user site-package to sys.path

    Each user has its own python directory with site-packages in the
    home directory.
    """
    
    title = 'addusersitepackages'
    type_ = 'site'
    init_inputs = [
        NodeInputBP(label='known_paths'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.addusersitepackages(self.input(0)))
        

class Check_Enableusersite_Node(NodeBase):
    """
    Check if user site directory is safe for inclusion

    The function tests for the command line flag (including environment var),
    process uid/gid equal to effective uid/gid.

    None: Disabled for security reasons
    False: Disabled by user (command line option)
    True: Safe and enabled
    """
    
    title = 'check_enableusersite'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.check_enableusersite())
        

class Enablerlcompleter_Node(NodeBase):
    """
    Enable default readline configuration on interactive prompts, by
    registering a sys.__interactivehook__.

    If the readline module can be imported, the hook will set the Tab key
    as completion key and register ~/.python_history as history file.
    This can be overridden in the sitecustomize or usercustomize module,
    or in a PYTHONSTARTUP file.
    """
    
    title = 'enablerlcompleter'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.enablerlcompleter())
        

class Execsitecustomize_Node(NodeBase):
    """
    Run custom site specific code, if available."""
    
    title = 'execsitecustomize'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.execsitecustomize())
        

class Execusercustomize_Node(NodeBase):
    """
    Run custom user specific code, if available."""
    
    title = 'execusercustomize'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.execusercustomize())
        

class Getsitepackages_Node(NodeBase):
    """
    Returns a list containing all global site-packages directories.

    For each directory present in ``prefixes`` (or the global ``PREFIXES``),
    this function will find its `site-packages` subdirectory depending on the
    system environment, and will return a list of full paths.
    """
    
    title = 'getsitepackages'
    type_ = 'site'
    init_inputs = [
        NodeInputBP(label='prefixes', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.getsitepackages(self.input(0)))
        

class Getuserbase_Node(NodeBase):
    """
    Returns the `user base` directory path.

    The `user base` directory can be used to store data. If the global
    variable ``USER_BASE`` is not initialized yet, this function will also set
    it.
    """
    
    title = 'getuserbase'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.getuserbase())
        

class Getusersitepackages_Node(NodeBase):
    """
    Returns the user-specific site-packages directory path.

    If the global variable ``USER_SITE`` is not initialized yet, this
    function will also set it.
    """
    
    title = 'getusersitepackages'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.getusersitepackages())
        

class Main_Node(NodeBase):
    """
    Add standard site-specific directories to the module search path.

    This function is called automatically when this module is imported,
    unless the python interpreter was started with the -S flag.
    """
    
    title = 'main'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.main())
        

class Makepath_Node(NodeBase):
    """
    """
    
    title = 'makepath'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.makepath())
        

class Removeduppaths_Node(NodeBase):
    """
     Remove duplicate entries from sys.path along with making them
    absolute"""
    
    title = 'removeduppaths'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.removeduppaths())
        

class Setcopyright_Node(NodeBase):
    """
    Set 'copyright' and 'credits' in builtins"""
    
    title = 'setcopyright'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.setcopyright())
        

class Sethelper_Node(NodeBase):
    """
    """
    
    title = 'sethelper'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.sethelper())
        

class Setquit_Node(NodeBase):
    """
    Define new builtins 'quit' and 'exit'.

    These are objects which make the interpreter exit when called.
    The repr of each object contains a hint at how it works.

    """
    
    title = 'setquit'
    type_ = 'site'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.setquit())
        

class Venv_Node(NodeBase):
    """
    """
    
    title = 'venv'
    type_ = 'site'
    init_inputs = [
        NodeInputBP(label='known_paths'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, site.venv(self.input(0)))
        


export_nodes(
    _Get_Path_Node,
    _Getuserbase_Node,
    _Init_Pathinfo_Node,
    _Script_Node,
    Abs_Paths_Node,
    Addpackage_Node,
    Addsitedir_Node,
    Addsitepackages_Node,
    Addusersitepackages_Node,
    Check_Enableusersite_Node,
    Enablerlcompleter_Node,
    Execsitecustomize_Node,
    Execusercustomize_Node,
    Getsitepackages_Node,
    Getuserbase_Node,
    Getusersitepackages_Node,
    Main_Node,
    Makepath_Node,
    Removeduppaths_Node,
    Setcopyright_Node,
    Sethelper_Node,
    Setquit_Node,
    Venv_Node,
)
