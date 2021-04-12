import ryvencore_qt as rc
import imghdr


class AutoNode_imghdr_test(rc.Node):
    title = 'test'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test())
        


class AutoNode_imghdr_test_bmp(rc.Node):
    title = 'test_bmp'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_bmp(self.input(0), self.input(1)))
        


class AutoNode_imghdr_test_exr(rc.Node):
    title = 'test_exr'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_exr(self.input(0), self.input(1)))
        


class AutoNode_imghdr_test_gif(rc.Node):
    title = 'test_gif'
    description = '''GIF ('87 and '89 variants)'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_gif(self.input(0), self.input(1)))
        


class AutoNode_imghdr_test_jpeg(rc.Node):
    title = 'test_jpeg'
    description = '''JPEG data in JFIF or Exif format'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_jpeg(self.input(0), self.input(1)))
        


class AutoNode_imghdr_test_pbm(rc.Node):
    title = 'test_pbm'
    description = '''PBM (portable bitmap)'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_pbm(self.input(0), self.input(1)))
        


class AutoNode_imghdr_test_pgm(rc.Node):
    title = 'test_pgm'
    description = '''PGM (portable graymap)'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_pgm(self.input(0), self.input(1)))
        


class AutoNode_imghdr_test_png(rc.Node):
    title = 'test_png'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_png(self.input(0), self.input(1)))
        


class AutoNode_imghdr_test_ppm(rc.Node):
    title = 'test_ppm'
    description = '''PPM (portable pixmap)'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_ppm(self.input(0), self.input(1)))
        


class AutoNode_imghdr_test_rast(rc.Node):
    title = 'test_rast'
    description = '''Sun raster file'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_rast(self.input(0), self.input(1)))
        


class AutoNode_imghdr_test_rgb(rc.Node):
    title = 'test_rgb'
    description = '''SGI image library'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_rgb(self.input(0), self.input(1)))
        


class AutoNode_imghdr_test_tiff(rc.Node):
    title = 'test_tiff'
    description = '''TIFF (can be in Motorola or Intel byte order)'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_tiff(self.input(0), self.input(1)))
        


class AutoNode_imghdr_test_webp(rc.Node):
    title = 'test_webp'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_webp(self.input(0), self.input(1)))
        


class AutoNode_imghdr_test_xbm(rc.Node):
    title = 'test_xbm'
    description = '''X bitmap (X10 or X11)'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.test_xbm(self.input(0), self.input(1)))
        


class AutoNode_imghdr_testall(rc.Node):
    title = 'testall'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='list'),
rc.NodeInputBP(label='recursive'),
rc.NodeInputBP(label='toplevel'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.testall(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_imghdr_what(rc.Node):
    title = 'what'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='file'),
rc.NodeInputBP(label='h'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imghdr.what(self.input(0), self.input(1)))
        