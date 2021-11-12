
from ryven.NENV import *

import rlcompleter


class NodeBase(Node):
    pass


class Get_Class_Members_Node(NodeBase):
    """
    """
    
    title = 'get_class_members'
    type_ = 'rlcompleter'
    init_inputs = [
        NodeInputBP(label='klass'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, rlcompleter.get_class_members(self.input(0)))
        


export_nodes(
    Get_Class_Members_Node,
)
