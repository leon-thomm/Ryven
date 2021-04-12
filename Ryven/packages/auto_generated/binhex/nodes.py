import ryvencore_qt as rc
import binhex


class AutoNode_binhex_binhex(rc.Node):
    title = 'binhex'
    description = '''binhex(infilename, outfilename): create binhex-encoded copy of a file'''
    init_inputs = [
        rc.NodeInputBP(label='inp'),
rc.NodeInputBP(label='out'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binhex.binhex(self.input(0), self.input(1)))
        


class AutoNode_binhex_getfileinfo(rc.Node):
    title = 'getfileinfo'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binhex.getfileinfo(self.input(0)))
        


class AutoNode_binhex_hexbin(rc.Node):
    title = 'hexbin'
    description = '''hexbin(infilename, outfilename) - Decode binhexed file'''
    init_inputs = [
        rc.NodeInputBP(label='inp'),
rc.NodeInputBP(label='out'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, binhex.hexbin(self.input(0), self.input(1)))
        