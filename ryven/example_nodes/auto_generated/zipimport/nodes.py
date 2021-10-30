
from ryven.NENV import *

import zipimport


class NodeBase(Node):
    pass


class _Compile_Source_Node(NodeBase):
    """
    """
    
    title = '_compile_source'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='pathname'),
        NodeInputBP(label='source'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._compile_source(self.input(0), self.input(1)))
        

class _Eq_Mtime_Node(NodeBase):
    """
    """
    
    title = '_eq_mtime'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='t1'),
        NodeInputBP(label='t2'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._eq_mtime(self.input(0), self.input(1)))
        

class _Get_Data_Node(NodeBase):
    """
    """
    
    title = '_get_data'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='archive'),
        NodeInputBP(label='toc_entry'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._get_data(self.input(0), self.input(1)))
        

class _Get_Decompress_Func_Node(NodeBase):
    """
    """
    
    title = '_get_decompress_func'
    type_ = 'zipimport'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._get_decompress_func())
        

class _Get_Module_Code_Node(NodeBase):
    """
    """
    
    title = '_get_module_code'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='fullname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._get_module_code(self.input(0)))
        

class _Get_Module_Info_Node(NodeBase):
    """
    """
    
    title = '_get_module_info'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='fullname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._get_module_info(self.input(0)))
        

class _Get_Module_Path_Node(NodeBase):
    """
    """
    
    title = '_get_module_path'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='fullname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._get_module_path(self.input(0)))
        

class _Get_Mtime_And_Size_Of_Source_Node(NodeBase):
    """
    """
    
    title = '_get_mtime_and_size_of_source'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._get_mtime_and_size_of_source(self.input(0)))
        

class _Get_Pyc_Source_Node(NodeBase):
    """
    """
    
    title = '_get_pyc_source'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._get_pyc_source(self.input(0)))
        

class _Is_Dir_Node(NodeBase):
    """
    """
    
    title = '_is_dir'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._is_dir(self.input(0)))
        

class _Normalize_Line_Endings_Node(NodeBase):
    """
    """
    
    title = '_normalize_line_endings'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='source'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._normalize_line_endings(self.input(0)))
        

class _Parse_Dostime_Node(NodeBase):
    """
    """
    
    title = '_parse_dostime'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='d'),
        NodeInputBP(label='t'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._parse_dostime(self.input(0), self.input(1)))
        

class _Read_Directory_Node(NodeBase):
    """
    """
    
    title = '_read_directory'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='archive'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._read_directory(self.input(0)))
        

class _Unmarshal_Code_Node(NodeBase):
    """
    """
    
    title = '_unmarshal_code'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='pathname'),
        NodeInputBP(label='fullpath'),
        NodeInputBP(label='fullname'),
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._unmarshal_code(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Unpack_Uint16_Node(NodeBase):
    """
    Convert 2 bytes in little-endian to an integer."""
    
    title = '_unpack_uint16'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._unpack_uint16(self.input(0)))
        

class _Unpack_Uint32_Node(NodeBase):
    """
    Convert 4 bytes in little-endian to an integer."""
    
    title = '_unpack_uint32'
    type_ = 'zipimport'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, zipimport._unpack_uint32(self.input(0)))
        


export_nodes(
    _Compile_Source_Node,
    _Eq_Mtime_Node,
    _Get_Data_Node,
    _Get_Decompress_Func_Node,
    _Get_Module_Code_Node,
    _Get_Module_Info_Node,
    _Get_Module_Path_Node,
    _Get_Mtime_And_Size_Of_Source_Node,
    _Get_Pyc_Source_Node,
    _Is_Dir_Node,
    _Normalize_Line_Endings_Node,
    _Parse_Dostime_Node,
    _Read_Directory_Node,
    _Unmarshal_Code_Node,
    _Unpack_Uint16_Node,
    _Unpack_Uint32_Node,
)
