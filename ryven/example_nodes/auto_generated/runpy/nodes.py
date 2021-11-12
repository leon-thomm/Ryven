
from ryven.NENV import *

import runpy


class NodeBase(Node):
    pass


class _Get_Code_From_File_Node(NodeBase):
    """
    """
    
    title = '_get_code_from_file'
    type_ = 'runpy'
    init_inputs = [
        NodeInputBP(label='run_name'),
        NodeInputBP(label='fname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, runpy._get_code_from_file(self.input(0), self.input(1)))
        

class _Get_Main_Module_Details_Node(NodeBase):
    """
    """
    
    title = '_get_main_module_details'
    type_ = 'runpy'
    init_inputs = [
        NodeInputBP(label='error', dtype=dtypes.Data(default=ImportError, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, runpy._get_main_module_details(self.input(0)))
        

class _Get_Module_Details_Node(NodeBase):
    """
    """
    
    title = '_get_module_details'
    type_ = 'runpy'
    init_inputs = [
        NodeInputBP(label='mod_name'),
        NodeInputBP(label='error', dtype=dtypes.Data(default=ImportError, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, runpy._get_module_details(self.input(0), self.input(1)))
        

class _Run_Code_Node(NodeBase):
    """
    Helper to run code in nominated namespace"""
    
    title = '_run_code'
    type_ = 'runpy'
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='run_globals'),
        NodeInputBP(label='init_globals', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='mod_name', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='mod_spec', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='pkg_name', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='script_name', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, runpy._run_code(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        

class _Run_Module_As_Main_Node(NodeBase):
    """
    Runs the designated module in the __main__ namespace

       Note that the executed module will have full access to the
       __main__ namespace. If this is not desirable, the run_module()
       function should be used to run the module code in a fresh namespace.

       At the very least, these variables in __main__ will be overwritten:
           __name__
           __file__
           __cached__
           __loader__
           __package__
    """
    
    title = '_run_module_as_main'
    type_ = 'runpy'
    init_inputs = [
        NodeInputBP(label='mod_name'),
        NodeInputBP(label='alter_argv', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, runpy._run_module_as_main(self.input(0), self.input(1)))
        

class _Run_Module_Code_Node(NodeBase):
    """
    Helper to run code in new namespace with sys modified"""
    
    title = '_run_module_code'
    type_ = 'runpy'
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='init_globals', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='mod_name', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='mod_spec', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='pkg_name', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='script_name', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, runpy._run_module_code(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class Get_Importer_Node(NodeBase):
    """
    Retrieve a finder for the given path item

    The returned finder is cached in sys.path_importer_cache
    if it was newly created by a path hook.

    The cache (or part of it) can be cleared manually if a
    rescan of sys.path_hooks is necessary.
    """
    
    title = 'get_importer'
    type_ = 'runpy'
    init_inputs = [
        NodeInputBP(label='path_item'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, runpy.get_importer(self.input(0)))
        

class Read_Code_Node(NodeBase):
    """
    """
    
    title = 'read_code'
    type_ = 'runpy'
    init_inputs = [
        NodeInputBP(label='stream'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, runpy.read_code(self.input(0)))
        

class Run_Module_Node(NodeBase):
    """
    Execute a module's code without importing it

       Returns the resulting top level namespace dictionary
    """
    
    title = 'run_module'
    type_ = 'runpy'
    init_inputs = [
        NodeInputBP(label='mod_name'),
        NodeInputBP(label='init_globals', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='run_name', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='alter_sys', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, runpy.run_module(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Run_Path_Node(NodeBase):
    """
    Execute code located at the specified filesystem location

       Returns the resulting top level namespace dictionary

       The file path may refer directly to a Python script (i.e.
       one that could be directly executed with execfile) or else
       it may refer to a zipfile or directory containing a top
       level __main__.py script.
    """
    
    title = 'run_path'
    type_ = 'runpy'
    init_inputs = [
        NodeInputBP(label='path_name'),
        NodeInputBP(label='init_globals', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='run_name', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, runpy.run_path(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _Get_Code_From_File_Node,
    _Get_Main_Module_Details_Node,
    _Get_Module_Details_Node,
    _Run_Code_Node,
    _Run_Module_As_Main_Node,
    _Run_Module_Code_Node,
    Get_Importer_Node,
    Read_Code_Node,
    Run_Module_Node,
    Run_Path_Node,
)
