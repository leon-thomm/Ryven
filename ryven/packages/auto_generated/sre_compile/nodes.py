
from NENV import *

import sre_compile


class NodeBase(Node):
    pass


class _Bytes_To_Codes_Node(NodeBase):
    """
    """
    
    title = '_bytes_to_codes'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._bytes_to_codes(self.input(0)))
        

class _Code_Node(NodeBase):
    """
    """
    
    title = '_code'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='p'),
        NodeInputBP(label='flags'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._code(self.input(0), self.input(1)))
        

class _Combine_Flags_Node(NodeBase):
    """
    """
    
    title = '_combine_flags'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='flags'),
        NodeInputBP(label='add_flags'),
        NodeInputBP(label='del_flags'),
        NodeInputBP(label='TYPE_FLAGS', dtype=dtypes.Data(default=292, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._combine_flags(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Compile_Node(NodeBase):
    """
    """
    
    title = '_compile'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='pattern'),
        NodeInputBP(label='flags'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._compile(self.input(0), self.input(1), self.input(2)))
        

class _Compile_Charset_Node(NodeBase):
    """
    """
    
    title = '_compile_charset'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='charset'),
        NodeInputBP(label='flags'),
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._compile_charset(self.input(0), self.input(1), self.input(2)))
        

class _Compile_Info_Node(NodeBase):
    """
    """
    
    title = '_compile_info'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='pattern'),
        NodeInputBP(label='flags'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._compile_info(self.input(0), self.input(1), self.input(2)))
        

class _Generate_Overlap_Table_Node(NodeBase):
    """
    
    Generate an overlap table for the following prefix.
    An overlap table is a table of the same size as the prefix which
    informs about the potential self-overlap for each index in the prefix:
    - if overlap[i] == 0, prefix[i:] can't overlap prefix[0:...]
    - if overlap[i] == k with 0 < k <= i, prefix[i-k+1:i+1] overlaps with
      prefix[0:k]
    """
    
    title = '_generate_overlap_table'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='prefix'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._generate_overlap_table(self.input(0)))
        

class _Get_Charset_Prefix_Node(NodeBase):
    """
    """
    
    title = '_get_charset_prefix'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='flags'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._get_charset_prefix(self.input(0), self.input(1)))
        

class _Get_Iscased_Node(NodeBase):
    """
    """
    
    title = '_get_iscased'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='flags'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._get_iscased(self.input(0)))
        

class _Get_Literal_Prefix_Node(NodeBase):
    """
    """
    
    title = '_get_literal_prefix'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='flags'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._get_literal_prefix(self.input(0), self.input(1)))
        

class _Hex_Code_Node(NodeBase):
    """
    """
    
    title = '_hex_code'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._hex_code(self.input(0)))
        

class _Mk_Bitmap_Node(NodeBase):
    """
    """
    
    title = '_mk_bitmap'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='bits'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._mk_bitmap(self.input(0)))
        

class _Optimize_Charset_Node(NodeBase):
    """
    """
    
    title = '_optimize_charset'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='charset'),
        NodeInputBP(label='iscased', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='fixup', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='fixes', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._optimize_charset(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Simple_Node(NodeBase):
    """
    """
    
    title = '_simple'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile._simple(self.input(0)))
        

class Compile_Node(NodeBase):
    """
    """
    
    title = 'compile'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='p'),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile.compile(self.input(0), self.input(1)))
        

class Dis_Node(NodeBase):
    """
    """
    
    title = 'dis'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile.dis(self.input(0)))
        

class Isstring_Node(NodeBase):
    """
    """
    
    title = 'isstring'
    type_ = 'sre_compile'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_compile.isstring(self.input(0)))
        


export_nodes(
    _Bytes_To_Codes_Node,
    _Code_Node,
    _Combine_Flags_Node,
    _Compile_Node,
    _Compile_Charset_Node,
    _Compile_Info_Node,
    _Generate_Overlap_Table_Node,
    _Get_Charset_Prefix_Node,
    _Get_Iscased_Node,
    _Get_Literal_Prefix_Node,
    _Hex_Code_Node,
    _Mk_Bitmap_Node,
    _Optimize_Charset_Node,
    _Simple_Node,
    Compile_Node,
    Dis_Node,
    Isstring_Node,
)
