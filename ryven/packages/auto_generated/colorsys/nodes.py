
from NENV import *

import colorsys


class NodeBase(Node):
    pass


class _V_Node(NodeBase):
    """
    """
    
    title = '_v'
    type_ = 'colorsys'
    init_inputs = [
        NodeInputBP(label='m1'),
        NodeInputBP(label='m2'),
        NodeInputBP(label='hue'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, colorsys._v(self.input(0), self.input(1), self.input(2)))
        

class Hls_To_Rgb_Node(NodeBase):
    """
    """
    
    title = 'hls_to_rgb'
    type_ = 'colorsys'
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='l'),
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, colorsys.hls_to_rgb(self.input(0), self.input(1), self.input(2)))
        

class Hsv_To_Rgb_Node(NodeBase):
    """
    """
    
    title = 'hsv_to_rgb'
    type_ = 'colorsys'
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='s'),
        NodeInputBP(label='v'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, colorsys.hsv_to_rgb(self.input(0), self.input(1), self.input(2)))
        

class Rgb_To_Hls_Node(NodeBase):
    """
    """
    
    title = 'rgb_to_hls'
    type_ = 'colorsys'
    init_inputs = [
        NodeInputBP(label='r'),
        NodeInputBP(label='g'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, colorsys.rgb_to_hls(self.input(0), self.input(1), self.input(2)))
        

class Rgb_To_Hsv_Node(NodeBase):
    """
    """
    
    title = 'rgb_to_hsv'
    type_ = 'colorsys'
    init_inputs = [
        NodeInputBP(label='r'),
        NodeInputBP(label='g'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, colorsys.rgb_to_hsv(self.input(0), self.input(1), self.input(2)))
        

class Rgb_To_Yiq_Node(NodeBase):
    """
    """
    
    title = 'rgb_to_yiq'
    type_ = 'colorsys'
    init_inputs = [
        NodeInputBP(label='r'),
        NodeInputBP(label='g'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, colorsys.rgb_to_yiq(self.input(0), self.input(1), self.input(2)))
        

class Yiq_To_Rgb_Node(NodeBase):
    """
    """
    
    title = 'yiq_to_rgb'
    type_ = 'colorsys'
    init_inputs = [
        NodeInputBP(label='y'),
        NodeInputBP(label='i'),
        NodeInputBP(label='q'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, colorsys.yiq_to_rgb(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _V_Node,
    Hls_To_Rgb_Node,
    Hsv_To_Rgb_Node,
    Rgb_To_Hls_Node,
    Rgb_To_Hsv_Node,
    Rgb_To_Yiq_Node,
    Yiq_To_Rgb_Node,
)
