import ryvencore_qt as rc
import colorsys


class AutoNode_colorsys__v(rc.Node):
    title = '_v'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='m1'),
rc.NodeInputBP(label='m2'),
rc.NodeInputBP(label='hue'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, colorsys._v(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_colorsys_hls_to_rgb(rc.Node):
    title = 'hls_to_rgb'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='l'),
rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, colorsys.hls_to_rgb(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_colorsys_hsv_to_rgb(rc.Node):
    title = 'hsv_to_rgb'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='h'),
rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='v'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, colorsys.hsv_to_rgb(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_colorsys_rgb_to_hls(rc.Node):
    title = 'rgb_to_hls'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='r'),
rc.NodeInputBP(label='g'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, colorsys.rgb_to_hls(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_colorsys_rgb_to_hsv(rc.Node):
    title = 'rgb_to_hsv'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='r'),
rc.NodeInputBP(label='g'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, colorsys.rgb_to_hsv(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_colorsys_rgb_to_yiq(rc.Node):
    title = 'rgb_to_yiq'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='r'),
rc.NodeInputBP(label='g'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, colorsys.rgb_to_yiq(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_colorsys_yiq_to_rgb(rc.Node):
    title = 'yiq_to_rgb'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='y'),
rc.NodeInputBP(label='i'),
rc.NodeInputBP(label='q'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, colorsys.yiq_to_rgb(self.input(0), self.input(1), self.input(2)))
        