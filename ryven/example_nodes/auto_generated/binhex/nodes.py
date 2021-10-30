
from ryven.NENV import *

import binhex


class NodeBase(Node):
    pass


class _Ignore_Deprecation_Warning_Node(NodeBase):
    """
    """
    
    title = '_ignore_deprecation_warning'
    type_ = 'binhex'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, binhex._ignore_deprecation_warning())
        

class Binhex_Node(NodeBase):
    """
    binhex(infilename, outfilename): create binhex-encoded copy of a file"""
    
    title = 'binhex'
    type_ = 'binhex'
    init_inputs = [
        NodeInputBP(label='inp'),
        NodeInputBP(label='out'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, binhex.binhex(self.input(0), self.input(1)))
        

class Getfileinfo_Node(NodeBase):
    """
    """
    
    title = 'getfileinfo'
    type_ = 'binhex'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, binhex.getfileinfo(self.input(0)))
        

class Hexbin_Node(NodeBase):
    """
    hexbin(infilename, outfilename) - Decode binhexed file"""
    
    title = 'hexbin'
    type_ = 'binhex'
    init_inputs = [
        NodeInputBP(label='inp'),
        NodeInputBP(label='out'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, binhex.hexbin(self.input(0), self.input(1)))
        


export_nodes(
    _Ignore_Deprecation_Warning_Node,
    Binhex_Node,
    Getfileinfo_Node,
    Hexbin_Node,
)
