import ryvencore_qt as rc
import fractions


class AutoNode_fractions__gcd(rc.Node):
    title = '_gcd'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fractions._gcd(self.input(0), self.input(1)))
        


class AutoNode_fractions_gcd(rc.Node):
    title = 'gcd'
    doc = '''Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    '''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fractions.gcd(self.input(0), self.input(1)))
        