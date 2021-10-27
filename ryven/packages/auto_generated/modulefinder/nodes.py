
from NENV import *

import modulefinder


class NodeBase(Node):
    pass


class Addpackagepath_Node(NodeBase):
    """
    """
    
    title = 'AddPackagePath'
    type_ = 'modulefinder'
    init_inputs = [
        NodeInputBP(label='packagename'),
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, modulefinder.AddPackagePath(self.input(0), self.input(1)))
        

class Replacepackage_Node(NodeBase):
    """
    """
    
    title = 'ReplacePackage'
    type_ = 'modulefinder'
    init_inputs = [
        NodeInputBP(label='oldname'),
        NodeInputBP(label='newname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, modulefinder.ReplacePackage(self.input(0), self.input(1)))
        

class _Find_Module_Node(NodeBase):
    """
    An importlib reimplementation of imp.find_module (for our purposes)."""
    
    title = '_find_module'
    type_ = 'modulefinder'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='path', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, modulefinder._find_module(self.input(0), self.input(1)))
        

class Test_Node(NodeBase):
    """
    """
    
    title = 'test'
    type_ = 'modulefinder'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, modulefinder.test())
        


export_nodes(
    Addpackagepath_Node,
    Replacepackage_Node,
    _Find_Module_Node,
    Test_Node,
)
