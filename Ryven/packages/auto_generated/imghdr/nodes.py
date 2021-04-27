
from NENV import *

import imghdr


class NodeBase(Node):
    pass


class Test_Node(NodeBase):
    title = 'test'
    type_ = 'imghdr'
    doc = """"""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test())
        

class Test_Bmp_Node(NodeBase):
    title = 'test_bmp'
    type_ = 'imghdr'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_bmp(self.input(0), self.input(1)))
        

class Test_Exr_Node(NodeBase):
    title = 'test_exr'
    type_ = 'imghdr'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_exr(self.input(0), self.input(1)))
        

class Test_Gif_Node(NodeBase):
    title = 'test_gif'
    type_ = 'imghdr'
    doc = """GIF ('87 and '89 variants)"""
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_gif(self.input(0), self.input(1)))
        

class Test_Jpeg_Node(NodeBase):
    title = 'test_jpeg'
    type_ = 'imghdr'
    doc = """JPEG data in JFIF or Exif format"""
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_jpeg(self.input(0), self.input(1)))
        

class Test_Pbm_Node(NodeBase):
    title = 'test_pbm'
    type_ = 'imghdr'
    doc = """PBM (portable bitmap)"""
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_pbm(self.input(0), self.input(1)))
        

class Test_Pgm_Node(NodeBase):
    title = 'test_pgm'
    type_ = 'imghdr'
    doc = """PGM (portable graymap)"""
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_pgm(self.input(0), self.input(1)))
        

class Test_Png_Node(NodeBase):
    title = 'test_png'
    type_ = 'imghdr'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_png(self.input(0), self.input(1)))
        

class Test_Ppm_Node(NodeBase):
    title = 'test_ppm'
    type_ = 'imghdr'
    doc = """PPM (portable pixmap)"""
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_ppm(self.input(0), self.input(1)))
        

class Test_Rast_Node(NodeBase):
    title = 'test_rast'
    type_ = 'imghdr'
    doc = """Sun raster file"""
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_rast(self.input(0), self.input(1)))
        

class Test_Rgb_Node(NodeBase):
    title = 'test_rgb'
    type_ = 'imghdr'
    doc = """SGI image library"""
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_rgb(self.input(0), self.input(1)))
        

class Test_Tiff_Node(NodeBase):
    title = 'test_tiff'
    type_ = 'imghdr'
    doc = """TIFF (can be in Motorola or Intel byte order)"""
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_tiff(self.input(0), self.input(1)))
        

class Test_Webp_Node(NodeBase):
    title = 'test_webp'
    type_ = 'imghdr'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_webp(self.input(0), self.input(1)))
        

class Test_Xbm_Node(NodeBase):
    title = 'test_xbm'
    type_ = 'imghdr'
    doc = """X bitmap (X10 or X11)"""
    init_inputs = [
        NodeInputBP(label='h'),
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_xbm(self.input(0), self.input(1)))
        

class Testall_Node(NodeBase):
    title = 'testall'
    type_ = 'imghdr'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='list'),
        NodeInputBP(label='recursive'),
        NodeInputBP(label='toplevel'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.testall(self.input(0), self.input(1), self.input(2)))
        

class What_Node(NodeBase):
    title = 'what'
    type_ = 'imghdr'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='file'),
        NodeInputBP(label='h', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.what(self.input(0), self.input(1)))
        


export_nodes(
    Test_Node,
    Test_Bmp_Node,
    Test_Exr_Node,
    Test_Gif_Node,
    Test_Jpeg_Node,
    Test_Pbm_Node,
    Test_Pgm_Node,
    Test_Png_Node,
    Test_Ppm_Node,
    Test_Rast_Node,
    Test_Rgb_Node,
    Test_Tiff_Node,
    Test_Webp_Node,
    Test_Xbm_Node,
    Testall_Node,
    What_Node,
)
