
from NENV import *

import audioop


class NodeBase(Node):
    pass


class AutoNode_audioop_add(NodeBase):
    title = 'add'
    type_ = 'audioop'
    doc = """Return a fragment which is the addition of the two samples passed as parameters."""
    init_inputs = [
        NodeInputBP(label='fragment1'),
        NodeInputBP(label='fragment2'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.add(self.input(0), self.input(1), self.input(2)))
        

class AutoNode_audioop_adpcm2lin(NodeBase):
    title = 'adpcm2lin'
    type_ = 'audioop'
    doc = """Decode an Intel/DVI ADPCM coded fragment to a linear fragment."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
        NodeInputBP(label='state'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.adpcm2lin(self.input(0), self.input(1), self.input(2)))
        

class AutoNode_audioop_alaw2lin(NodeBase):
    title = 'alaw2lin'
    type_ = 'audioop'
    doc = """Convert sound fragments in a-LAW encoding to linearly encoded sound fragments."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.alaw2lin(self.input(0), self.input(1)))
        

class AutoNode_audioop_avg(NodeBase):
    title = 'avg'
    type_ = 'audioop'
    doc = """Return the average over all samples in the fragment."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.avg(self.input(0), self.input(1)))
        

class AutoNode_audioop_avgpp(NodeBase):
    title = 'avgpp'
    type_ = 'audioop'
    doc = """Return the average peak-peak value over all samples in the fragment."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.avgpp(self.input(0), self.input(1)))
        

class AutoNode_audioop_bias(NodeBase):
    title = 'bias'
    type_ = 'audioop'
    doc = """Return a fragment that is the original fragment with a bias added to each sample."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
        NodeInputBP(label='bias'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.bias(self.input(0), self.input(1), self.input(2)))
        

class AutoNode_audioop_byteswap(NodeBase):
    title = 'byteswap'
    type_ = 'audioop'
    doc = """Convert big-endian samples to little-endian and vice versa."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.byteswap(self.input(0), self.input(1)))
        

class AutoNode_audioop_cross(NodeBase):
    title = 'cross'
    type_ = 'audioop'
    doc = """Return the number of zero crossings in the fragment passed as an argument."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.cross(self.input(0), self.input(1)))
        

class AutoNode_audioop_findfactor(NodeBase):
    title = 'findfactor'
    type_ = 'audioop'
    doc = """Return a factor F such that rms(add(fragment, mul(reference, -F))) is minimal."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='reference'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.findfactor(self.input(0), self.input(1)))
        

class AutoNode_audioop_findfit(NodeBase):
    title = 'findfit'
    type_ = 'audioop'
    doc = """Try to match reference as well as possible to a portion of fragment."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='reference'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.findfit(self.input(0), self.input(1)))
        

class AutoNode_audioop_findmax(NodeBase):
    title = 'findmax'
    type_ = 'audioop'
    doc = """Search fragment for a slice of specified number of samples with maximum energy."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='length'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.findmax(self.input(0), self.input(1)))
        

class AutoNode_audioop_getsample(NodeBase):
    title = 'getsample'
    type_ = 'audioop'
    doc = """Return the value of sample index from the fragment."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
        NodeInputBP(label='index'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.getsample(self.input(0), self.input(1), self.input(2)))
        

class AutoNode_audioop_lin2adpcm(NodeBase):
    title = 'lin2adpcm'
    type_ = 'audioop'
    doc = """Convert samples to 4 bit Intel/DVI ADPCM encoding."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
        NodeInputBP(label='state'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.lin2adpcm(self.input(0), self.input(1), self.input(2)))
        

class AutoNode_audioop_lin2alaw(NodeBase):
    title = 'lin2alaw'
    type_ = 'audioop'
    doc = """Convert samples in the audio fragment to a-LAW encoding."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.lin2alaw(self.input(0), self.input(1)))
        

class AutoNode_audioop_lin2lin(NodeBase):
    title = 'lin2lin'
    type_ = 'audioop'
    doc = """Convert samples between 1-, 2-, 3- and 4-byte formats."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
        NodeInputBP(label='newwidth'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.lin2lin(self.input(0), self.input(1), self.input(2)))
        

class AutoNode_audioop_lin2ulaw(NodeBase):
    title = 'lin2ulaw'
    type_ = 'audioop'
    doc = """Convert samples in the audio fragment to u-LAW encoding."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.lin2ulaw(self.input(0), self.input(1)))
        

class AutoNode_audioop_max(NodeBase):
    title = 'max'
    type_ = 'audioop'
    doc = """Return the maximum of the absolute value of all samples in a fragment."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.max(self.input(0), self.input(1)))
        

class AutoNode_audioop_maxpp(NodeBase):
    title = 'maxpp'
    type_ = 'audioop'
    doc = """Return the maximum peak-peak value in the sound fragment."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.maxpp(self.input(0), self.input(1)))
        

class AutoNode_audioop_minmax(NodeBase):
    title = 'minmax'
    type_ = 'audioop'
    doc = """Return the minimum and maximum values of all samples in the sound fragment."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.minmax(self.input(0), self.input(1)))
        

class AutoNode_audioop_mul(NodeBase):
    title = 'mul'
    type_ = 'audioop'
    doc = """Return a fragment that has all samples in the original fragment multiplied by the floating-point value factor."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
        NodeInputBP(label='factor'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.mul(self.input(0), self.input(1), self.input(2)))
        

class AutoNode_audioop_ratecv(NodeBase):
    title = 'ratecv'
    type_ = 'audioop'
    doc = """Convert the frame rate of the input fragment."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
        NodeInputBP(label='nchannels'),
        NodeInputBP(label='inrate'),
        NodeInputBP(label='outrate'),
        NodeInputBP(label='state'),
        NodeInputBP(label='weightA'),
        NodeInputBP(label='weightB'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.ratecv(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        

class AutoNode_audioop_reverse(NodeBase):
    title = 'reverse'
    type_ = 'audioop'
    doc = """Reverse the samples in a fragment and returns the modified fragment."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.reverse(self.input(0), self.input(1)))
        

class AutoNode_audioop_rms(NodeBase):
    title = 'rms'
    type_ = 'audioop'
    doc = """Return the root-mean-square of the fragment, i.e. sqrt(sum(S_i^2)/n)."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.rms(self.input(0), self.input(1)))
        

class AutoNode_audioop_tomono(NodeBase):
    title = 'tomono'
    type_ = 'audioop'
    doc = """Convert a stereo fragment to a mono fragment."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
        NodeInputBP(label='lfactor'),
        NodeInputBP(label='rfactor'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.tomono(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class AutoNode_audioop_tostereo(NodeBase):
    title = 'tostereo'
    type_ = 'audioop'
    doc = """Generate a stereo fragment from a mono fragment."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
        NodeInputBP(label='lfactor'),
        NodeInputBP(label='rfactor'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.tostereo(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class AutoNode_audioop_ulaw2lin(NodeBase):
    title = 'ulaw2lin'
    type_ = 'audioop'
    doc = """Convert sound fragments in u-LAW encoding to linearly encoded sound fragments."""
    init_inputs = [
        NodeInputBP(label='fragment'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, audioop.ulaw2lin(self.input(0), self.input(1)))
        


export_nodes(
    AutoNode_audioop_add,
    AutoNode_audioop_adpcm2lin,
    AutoNode_audioop_alaw2lin,
    AutoNode_audioop_avg,
    AutoNode_audioop_avgpp,
    AutoNode_audioop_bias,
    AutoNode_audioop_byteswap,
    AutoNode_audioop_cross,
    AutoNode_audioop_findfactor,
    AutoNode_audioop_findfit,
    AutoNode_audioop_findmax,
    AutoNode_audioop_getsample,
    AutoNode_audioop_lin2adpcm,
    AutoNode_audioop_lin2alaw,
    AutoNode_audioop_lin2lin,
    AutoNode_audioop_lin2ulaw,
    AutoNode_audioop_max,
    AutoNode_audioop_maxpp,
    AutoNode_audioop_minmax,
    AutoNode_audioop_mul,
    AutoNode_audioop_ratecv,
    AutoNode_audioop_reverse,
    AutoNode_audioop_rms,
    AutoNode_audioop_tomono,
    AutoNode_audioop_tostereo,
    AutoNode_audioop_ulaw2lin,
)
