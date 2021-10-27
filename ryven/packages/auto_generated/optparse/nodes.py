
from NENV import *

import optparse


class NodeBase(Node):
    pass


class __Node(NodeBase):
    """
    """
    
    title = '_'
    type_ = 'optparse'
    init_inputs = [
        NodeInputBP(label='message'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, optparse._(self.input(0)))
        

class _Match_Abbrev_Node(NodeBase):
    """
    _match_abbrev(s : string, wordmap : {string : Option}) -> string

    Return the string key in 'wordmap' for which 's' is an unambiguous
    abbreviation.  If 's' is found to be ambiguous or doesn't match any of
    'words', raise BadOptionError.
    """
    
    title = '_match_abbrev'
    type_ = 'optparse'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='wordmap'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, optparse._match_abbrev(self.input(0), self.input(1)))
        

class _Parse_Int_Node(NodeBase):
    """
    """
    
    title = '_parse_int'
    type_ = 'optparse'
    init_inputs = [
        NodeInputBP(label='val'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, optparse._parse_int(self.input(0)))
        

class _Parse_Num_Node(NodeBase):
    """
    """
    
    title = '_parse_num'
    type_ = 'optparse'
    init_inputs = [
        NodeInputBP(label='val'),
        NodeInputBP(label='type'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, optparse._parse_num(self.input(0), self.input(1)))
        

class _Repr_Node(NodeBase):
    """
    """
    
    title = '_repr'
    type_ = 'optparse'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, optparse._repr())
        

class Check_Builtin_Node(NodeBase):
    """
    """
    
    title = 'check_builtin'
    type_ = 'optparse'
    init_inputs = [
        NodeInputBP(label='option'),
        NodeInputBP(label='opt'),
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, optparse.check_builtin(self.input(0), self.input(1), self.input(2)))
        

class Check_Choice_Node(NodeBase):
    """
    """
    
    title = 'check_choice'
    type_ = 'optparse'
    init_inputs = [
        NodeInputBP(label='option'),
        NodeInputBP(label='opt'),
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, optparse.check_choice(self.input(0), self.input(1), self.input(2)))
        

class Gettext_Node(NodeBase):
    """
    """
    
    title = 'gettext'
    type_ = 'optparse'
    init_inputs = [
        NodeInputBP(label='message'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, optparse.gettext(self.input(0)))
        

class Ngettext_Node(NodeBase):
    """
    """
    
    title = 'ngettext'
    type_ = 'optparse'
    init_inputs = [
        NodeInputBP(label='msgid1'),
        NodeInputBP(label='msgid2'),
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, optparse.ngettext(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    __Node,
    _Match_Abbrev_Node,
    _Parse_Int_Node,
    _Parse_Num_Node,
    _Repr_Node,
    Check_Builtin_Node,
    Check_Choice_Node,
    Gettext_Node,
    Ngettext_Node,
)
