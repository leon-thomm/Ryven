import ryvencore_qt as rc
import _sre


class AutoNode__sre_ascii_iscased(rc.Node):
    title = 'ascii_iscased'
    type_ = '_sre'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='character'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sre.ascii_iscased(self.input(0)))
        


class AutoNode__sre_ascii_tolower(rc.Node):
    title = 'ascii_tolower'
    type_ = '_sre'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='character'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sre.ascii_tolower(self.input(0)))
        


class AutoNode__sre_compile(rc.Node):
    title = 'compile'
    type_ = '_sre'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='pattern'),
rc.NodeInputBP(label='flags'),
rc.NodeInputBP(label='code'),
rc.NodeInputBP(label='groups'),
rc.NodeInputBP(label='groupindex'),
rc.NodeInputBP(label='indexgroup'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sre.compile(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode__sre_getcodesize(rc.Node):
    title = 'getcodesize'
    type_ = '_sre'
    description = ''''''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sre.getcodesize())
        


class AutoNode__sre_unicode_iscased(rc.Node):
    title = 'unicode_iscased'
    type_ = '_sre'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='character'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sre.unicode_iscased(self.input(0)))
        


class AutoNode__sre_unicode_tolower(rc.Node):
    title = 'unicode_tolower'
    type_ = '_sre'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='character'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sre.unicode_tolower(self.input(0)))
        