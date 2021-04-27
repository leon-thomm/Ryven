
from NENV import *

import binhex


class NodeBase(Node):
    pass


class Binhex_Node(NodeBase):
    title = 'binhex'
    type_ = 'binhex'
    doc = """binhex(infilename, outfilename): create binhex-encoded copy of a file"""
    init_inputs = [
        NodeInputBP(label='inp'),
        NodeInputBP(label='out'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binhex.binhex(self.input(0), self.input(1)))
        

class Getfileinfo_Node(NodeBase):
    title = 'getfileinfo'
    type_ = 'binhex'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binhex.getfileinfo(self.input(0)))
        

class Hexbin_Node(NodeBase):
    title = 'hexbin'
    type_ = 'binhex'
    doc = """hexbin(infilename, outfilename) - Decode binhexed file"""
    init_inputs = [
        NodeInputBP(label='inp'),
        NodeInputBP(label='out'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binhex.hexbin(self.input(0), self.input(1)))
        


export_nodes(
    Binhex_Node,
    Getfileinfo_Node,
    Hexbin_Node,
)
