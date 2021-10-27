
from NENV import *

import sre_parse


class NodeBase(Node):
    pass


class _Class_Escape_Node(NodeBase):
    """
    """
    
    title = '_class_escape'
    type_ = 'sre_parse'
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='escape'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_parse._class_escape(self.input(0), self.input(1)))
        

class _Escape_Node(NodeBase):
    """
    """
    
    title = '_escape'
    type_ = 'sre_parse'
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='escape'),
        NodeInputBP(label='state'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_parse._escape(self.input(0), self.input(1), self.input(2)))
        

class _Parse_Node(NodeBase):
    """
    """
    
    title = '_parse'
    type_ = 'sre_parse'
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='state'),
        NodeInputBP(label='verbose'),
        NodeInputBP(label='nested'),
        NodeInputBP(label='first', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_parse._parse(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class _Parse_Flags_Node(NodeBase):
    """
    """
    
    title = '_parse_flags'
    type_ = 'sre_parse'
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='state'),
        NodeInputBP(label='char'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_parse._parse_flags(self.input(0), self.input(1), self.input(2)))
        

class _Parse_Sub_Node(NodeBase):
    """
    """
    
    title = '_parse_sub'
    type_ = 'sre_parse'
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='state'),
        NodeInputBP(label='verbose'),
        NodeInputBP(label='nested'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_parse._parse_sub(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Uniq_Node(NodeBase):
    """
    """
    
    title = '_uniq'
    type_ = 'sre_parse'
    init_inputs = [
        NodeInputBP(label='items'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_parse._uniq(self.input(0)))
        

class Expand_Template_Node(NodeBase):
    """
    """
    
    title = 'expand_template'
    type_ = 'sre_parse'
    init_inputs = [
        NodeInputBP(label='template'),
        NodeInputBP(label='match'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_parse.expand_template(self.input(0), self.input(1)))
        

class Fix_Flags_Node(NodeBase):
    """
    """
    
    title = 'fix_flags'
    type_ = 'sre_parse'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='flags'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_parse.fix_flags(self.input(0), self.input(1)))
        

class Parse_Node(NodeBase):
    """
    """
    
    title = 'parse'
    type_ = 'sre_parse'
    init_inputs = [
        NodeInputBP(label='str'),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='state', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_parse.parse(self.input(0), self.input(1), self.input(2)))
        

class Parse_Template_Node(NodeBase):
    """
    """
    
    title = 'parse_template'
    type_ = 'sre_parse'
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='state'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, sre_parse.parse_template(self.input(0), self.input(1)))
        


export_nodes(
    _Class_Escape_Node,
    _Escape_Node,
    _Parse_Node,
    _Parse_Flags_Node,
    _Parse_Sub_Node,
    _Uniq_Node,
    Expand_Template_Node,
    Fix_Flags_Node,
    Parse_Node,
    Parse_Template_Node,
)
