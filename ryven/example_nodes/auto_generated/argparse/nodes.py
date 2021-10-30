
from ryven.NENV import *

import argparse


class NodeBase(Node):
    pass


class __Node(NodeBase):
    """
    """
    
    title = '_'
    type_ = 'argparse'
    init_inputs = [
        NodeInputBP(label='message'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, argparse._(self.input(0)))
        

class _Copy_Items_Node(NodeBase):
    """
    """
    
    title = '_copy_items'
    type_ = 'argparse'
    init_inputs = [
        NodeInputBP(label='items'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, argparse._copy_items(self.input(0)))
        

class _Get_Action_Name_Node(NodeBase):
    """
    """
    
    title = '_get_action_name'
    type_ = 'argparse'
    init_inputs = [
        NodeInputBP(label='argument'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, argparse._get_action_name(self.input(0)))
        

class Ngettext_Node(NodeBase):
    """
    """
    
    title = 'ngettext'
    type_ = 'argparse'
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
        self.set_output_val(0, argparse.ngettext(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    __Node,
    _Copy_Items_Node,
    _Get_Action_Name_Node,
    Ngettext_Node,
)
