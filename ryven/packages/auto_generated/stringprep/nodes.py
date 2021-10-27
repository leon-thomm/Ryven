
from NENV import *

import stringprep


class NodeBase(Node):
    pass


class In_Table_A1_Node(NodeBase):
    """
    """
    
    title = 'in_table_a1'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_a1(self.input(0)))
        

class In_Table_B1_Node(NodeBase):
    """
    """
    
    title = 'in_table_b1'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_b1(self.input(0)))
        

class In_Table_C11_Node(NodeBase):
    """
    """
    
    title = 'in_table_c11'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_c11(self.input(0)))
        

class In_Table_C11_C12_Node(NodeBase):
    """
    """
    
    title = 'in_table_c11_c12'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_c11_c12(self.input(0)))
        

class In_Table_C12_Node(NodeBase):
    """
    """
    
    title = 'in_table_c12'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_c12(self.input(0)))
        

class In_Table_C21_Node(NodeBase):
    """
    """
    
    title = 'in_table_c21'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_c21(self.input(0)))
        

class In_Table_C21_C22_Node(NodeBase):
    """
    """
    
    title = 'in_table_c21_c22'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_c21_c22(self.input(0)))
        

class In_Table_C22_Node(NodeBase):
    """
    """
    
    title = 'in_table_c22'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_c22(self.input(0)))
        

class In_Table_C3_Node(NodeBase):
    """
    """
    
    title = 'in_table_c3'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_c3(self.input(0)))
        

class In_Table_C4_Node(NodeBase):
    """
    """
    
    title = 'in_table_c4'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_c4(self.input(0)))
        

class In_Table_C5_Node(NodeBase):
    """
    """
    
    title = 'in_table_c5'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_c5(self.input(0)))
        

class In_Table_C6_Node(NodeBase):
    """
    """
    
    title = 'in_table_c6'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_c6(self.input(0)))
        

class In_Table_C7_Node(NodeBase):
    """
    """
    
    title = 'in_table_c7'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_c7(self.input(0)))
        

class In_Table_C8_Node(NodeBase):
    """
    """
    
    title = 'in_table_c8'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_c8(self.input(0)))
        

class In_Table_C9_Node(NodeBase):
    """
    """
    
    title = 'in_table_c9'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_c9(self.input(0)))
        

class In_Table_D1_Node(NodeBase):
    """
    """
    
    title = 'in_table_d1'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_d1(self.input(0)))
        

class In_Table_D2_Node(NodeBase):
    """
    """
    
    title = 'in_table_d2'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.in_table_d2(self.input(0)))
        

class Map_Table_B2_Node(NodeBase):
    """
    """
    
    title = 'map_table_b2'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.map_table_b2(self.input(0)))
        

class Map_Table_B3_Node(NodeBase):
    """
    """
    
    title = 'map_table_b3'
    type_ = 'stringprep'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, stringprep.map_table_b3(self.input(0)))
        


export_nodes(
    In_Table_A1_Node,
    In_Table_B1_Node,
    In_Table_C11_Node,
    In_Table_C11_C12_Node,
    In_Table_C12_Node,
    In_Table_C21_Node,
    In_Table_C21_C22_Node,
    In_Table_C22_Node,
    In_Table_C3_Node,
    In_Table_C4_Node,
    In_Table_C5_Node,
    In_Table_C6_Node,
    In_Table_C7_Node,
    In_Table_C8_Node,
    In_Table_C9_Node,
    In_Table_D1_Node,
    In_Table_D2_Node,
    Map_Table_B2_Node,
    Map_Table_B3_Node,
)
