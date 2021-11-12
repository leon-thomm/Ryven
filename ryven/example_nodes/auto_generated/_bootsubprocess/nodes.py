
from ryven.NENV import *

import _bootsubprocess


class NodeBase(Node):
    pass


class _Check_Cmd_Node(NodeBase):
    """
    """
    
    title = '_check_cmd'
    type_ = '_bootsubprocess'
    init_inputs = [
        NodeInputBP(label='cmd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _bootsubprocess._check_cmd(self.input(0)))
        

class Check_Output_Node(NodeBase):
    """
    """
    
    title = 'check_output'
    type_ = '_bootsubprocess'
    init_inputs = [
        NodeInputBP(label='cmd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _bootsubprocess.check_output(self.input(0)))
        


export_nodes(
    _Check_Cmd_Node,
    Check_Output_Node,
)
