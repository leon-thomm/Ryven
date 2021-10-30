
from ryven.NENV import *

import smtpd


class NodeBase(Node):
    pass


class Get_Addr_Spec_Node(NodeBase):
    """
     addr-spec = local-part "@" domain

    """
    
    title = 'get_addr_spec'
    type_ = 'smtpd'
    init_inputs = [
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, smtpd.get_addr_spec(self.input(0)))
        

class Get_Angle_Addr_Node(NodeBase):
    """
     angle-addr = [CFWS] "<" addr-spec ">" [CFWS] / obs-angle-addr
        obs-angle-addr = [CFWS] "<" obs-route addr-spec ">" [CFWS]

    """
    
    title = 'get_angle_addr'
    type_ = 'smtpd'
    init_inputs = [
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, smtpd.get_angle_addr(self.input(0)))
        

class Parseargs_Node(NodeBase):
    """
    """
    
    title = 'parseargs'
    type_ = 'smtpd'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, smtpd.parseargs())
        

class Usage_Node(NodeBase):
    """
    """
    
    title = 'usage'
    type_ = 'smtpd'
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='msg', dtype=dtypes.Data(default='', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, smtpd.usage(self.input(0), self.input(1)))
        

class Warn_Node(NodeBase):
    """
    Issue a warning, or maybe ignore it or raise an exception."""
    
    title = 'warn'
    type_ = 'smtpd'
    init_inputs = [
        NodeInputBP(label='message'),
        NodeInputBP(label='category', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='stacklevel', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='source', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, smtpd.warn(self.input(0), self.input(1), self.input(2), self.input(3)))
        


export_nodes(
    Get_Addr_Spec_Node,
    Get_Angle_Addr_Node,
    Parseargs_Node,
    Usage_Node,
    Warn_Node,
)
