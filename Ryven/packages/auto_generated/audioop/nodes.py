import ryvencore_qt as rc
import audioop


class AutoNode_audioop_add(rc.Node):
    title = 'add'
    type_ = 'audioop'
    doc = '''Return a fragment which is the addition of the two samples passed as parameters.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment1'),
rc.NodeInputBP(label='fragment2'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.add(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_audioop_adpcm2lin(rc.Node):
    title = 'adpcm2lin'
    type_ = 'audioop'
    doc = '''Decode an Intel/DVI ADPCM coded fragment to a linear fragment.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
rc.NodeInputBP(label='state'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.adpcm2lin(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_audioop_alaw2lin(rc.Node):
    title = 'alaw2lin'
    type_ = 'audioop'
    doc = '''Convert sound fragments in a-LAW encoding to linearly encoded sound fragments.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.alaw2lin(self.input(0), self.input(1)))
        


class AutoNode_audioop_avg(rc.Node):
    title = 'avg'
    type_ = 'audioop'
    doc = '''Return the average over all samples in the fragment.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.avg(self.input(0), self.input(1)))
        


class AutoNode_audioop_avgpp(rc.Node):
    title = 'avgpp'
    type_ = 'audioop'
    doc = '''Return the average peak-peak value over all samples in the fragment.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.avgpp(self.input(0), self.input(1)))
        


class AutoNode_audioop_bias(rc.Node):
    title = 'bias'
    type_ = 'audioop'
    doc = '''Return a fragment that is the original fragment with a bias added to each sample.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
rc.NodeInputBP(label='bias'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.bias(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_audioop_byteswap(rc.Node):
    title = 'byteswap'
    type_ = 'audioop'
    doc = '''Convert big-endian samples to little-endian and vice versa.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.byteswap(self.input(0), self.input(1)))
        


class AutoNode_audioop_cross(rc.Node):
    title = 'cross'
    type_ = 'audioop'
    doc = '''Return the number of zero crossings in the fragment passed as an argument.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.cross(self.input(0), self.input(1)))
        


class AutoNode_audioop_findfactor(rc.Node):
    title = 'findfactor'
    type_ = 'audioop'
    doc = '''Return a factor F such that rms(add(fragment, mul(reference, -F))) is minimal.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='reference'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.findfactor(self.input(0), self.input(1)))
        


class AutoNode_audioop_findfit(rc.Node):
    title = 'findfit'
    type_ = 'audioop'
    doc = '''Try to match reference as well as possible to a portion of fragment.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='reference'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.findfit(self.input(0), self.input(1)))
        


class AutoNode_audioop_findmax(rc.Node):
    title = 'findmax'
    type_ = 'audioop'
    doc = '''Search fragment for a slice of specified number of samples with maximum energy.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='length'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.findmax(self.input(0), self.input(1)))
        


class AutoNode_audioop_getsample(rc.Node):
    title = 'getsample'
    type_ = 'audioop'
    doc = '''Return the value of sample index from the fragment.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
rc.NodeInputBP(label='index'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.getsample(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_audioop_lin2adpcm(rc.Node):
    title = 'lin2adpcm'
    type_ = 'audioop'
    doc = '''Convert samples to 4 bit Intel/DVI ADPCM encoding.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
rc.NodeInputBP(label='state'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.lin2adpcm(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_audioop_lin2alaw(rc.Node):
    title = 'lin2alaw'
    type_ = 'audioop'
    doc = '''Convert samples in the audio fragment to a-LAW encoding.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.lin2alaw(self.input(0), self.input(1)))
        


class AutoNode_audioop_lin2lin(rc.Node):
    title = 'lin2lin'
    type_ = 'audioop'
    doc = '''Convert samples between 1-, 2-, 3- and 4-byte formats.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
rc.NodeInputBP(label='newwidth'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.lin2lin(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_audioop_lin2ulaw(rc.Node):
    title = 'lin2ulaw'
    type_ = 'audioop'
    doc = '''Convert samples in the audio fragment to u-LAW encoding.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.lin2ulaw(self.input(0), self.input(1)))
        


class AutoNode_audioop_max(rc.Node):
    title = 'max'
    type_ = 'audioop'
    doc = '''Return the maximum of the absolute value of all samples in a fragment.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.max(self.input(0), self.input(1)))
        


class AutoNode_audioop_maxpp(rc.Node):
    title = 'maxpp'
    type_ = 'audioop'
    doc = '''Return the maximum peak-peak value in the sound fragment.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.maxpp(self.input(0), self.input(1)))
        


class AutoNode_audioop_minmax(rc.Node):
    title = 'minmax'
    type_ = 'audioop'
    doc = '''Return the minimum and maximum values of all samples in the sound fragment.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.minmax(self.input(0), self.input(1)))
        


class AutoNode_audioop_mul(rc.Node):
    title = 'mul'
    type_ = 'audioop'
    doc = '''Return a fragment that has all samples in the original fragment multiplied by the floating-point value factor.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
rc.NodeInputBP(label='factor'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.mul(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_audioop_ratecv(rc.Node):
    title = 'ratecv'
    type_ = 'audioop'
    doc = '''Convert the frame rate of the input fragment.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
rc.NodeInputBP(label='nchannels'),
rc.NodeInputBP(label='inrate'),
rc.NodeInputBP(label='outrate'),
rc.NodeInputBP(label='state'),
rc.NodeInputBP(label='weightA'),
rc.NodeInputBP(label='weightB'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.ratecv(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        


class AutoNode_audioop_reverse(rc.Node):
    title = 'reverse'
    type_ = 'audioop'
    doc = '''Reverse the samples in a fragment and returns the modified fragment.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.reverse(self.input(0), self.input(1)))
        


class AutoNode_audioop_rms(rc.Node):
    title = 'rms'
    type_ = 'audioop'
    doc = '''Return the root-mean-square of the fragment, i.e. sqrt(sum(S_i^2)/n).'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.rms(self.input(0), self.input(1)))
        


class AutoNode_audioop_tomono(rc.Node):
    title = 'tomono'
    type_ = 'audioop'
    doc = '''Convert a stereo fragment to a mono fragment.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
rc.NodeInputBP(label='lfactor'),
rc.NodeInputBP(label='rfactor'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.tomono(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_audioop_tostereo(rc.Node):
    title = 'tostereo'
    type_ = 'audioop'
    doc = '''Generate a stereo fragment from a mono fragment.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
rc.NodeInputBP(label='lfactor'),
rc.NodeInputBP(label='rfactor'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.tostereo(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_audioop_ulaw2lin(rc.Node):
    title = 'ulaw2lin'
    type_ = 'audioop'
    doc = '''Convert sound fragments in u-LAW encoding to linearly encoded sound fragments.'''
    init_inputs = [
        rc.NodeInputBP(label='fragment'),
rc.NodeInputBP(label='width'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.ulaw2lin(self.input(0), self.input(1)))
        