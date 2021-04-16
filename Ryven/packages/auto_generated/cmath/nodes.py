import ryvencore_qt as rc
import cmath


class AutoNode_cmath_acos(rc.Node):
    title = 'acos'
    type_ = 'cmath'
    doc = '''Return the arc cosine of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.acos(self.input(0)))
        


class AutoNode_cmath_acosh(rc.Node):
    title = 'acosh'
    type_ = 'cmath'
    doc = '''Return the inverse hyperbolic cosine of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.acosh(self.input(0)))
        


class AutoNode_cmath_asin(rc.Node):
    title = 'asin'
    type_ = 'cmath'
    doc = '''Return the arc sine of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.asin(self.input(0)))
        


class AutoNode_cmath_asinh(rc.Node):
    title = 'asinh'
    type_ = 'cmath'
    doc = '''Return the inverse hyperbolic sine of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.asinh(self.input(0)))
        


class AutoNode_cmath_atan(rc.Node):
    title = 'atan'
    type_ = 'cmath'
    doc = '''Return the arc tangent of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.atan(self.input(0)))
        


class AutoNode_cmath_atanh(rc.Node):
    title = 'atanh'
    type_ = 'cmath'
    doc = '''Return the inverse hyperbolic tangent of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.atanh(self.input(0)))
        


class AutoNode_cmath_cos(rc.Node):
    title = 'cos'
    type_ = 'cmath'
    doc = '''Return the cosine of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.cos(self.input(0)))
        


class AutoNode_cmath_cosh(rc.Node):
    title = 'cosh'
    type_ = 'cmath'
    doc = '''Return the hyperbolic cosine of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.cosh(self.input(0)))
        


class AutoNode_cmath_exp(rc.Node):
    title = 'exp'
    type_ = 'cmath'
    doc = '''Return the exponential value e**z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.exp(self.input(0)))
        


class AutoNode_cmath_isclose(rc.Node):
    title = 'isclose'
    type_ = 'cmath'
    doc = '''Determine whether two complex numbers are close in value.

  rel_tol
    maximum difference for being considered "close", relative to the
    magnitude of the input values
  abs_tol
    maximum difference for being considered "close", regardless of the
    magnitude of the input values

Return True if a is close in value to b, and False otherwise.

For the values to be considered close, the difference between them must be
smaller than at least one of the tolerances.

-inf, inf and NaN behave similarly to the IEEE 754 Standard. That is, NaN is
not close to anything, even itself. inf and -inf are only close to themselves.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.isclose(self.input(0), self.input(1)))
        


class AutoNode_cmath_isfinite(rc.Node):
    title = 'isfinite'
    type_ = 'cmath'
    doc = '''Return True if both the real and imaginary parts of z are finite, else False.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.isfinite(self.input(0)))
        


class AutoNode_cmath_isinf(rc.Node):
    title = 'isinf'
    type_ = 'cmath'
    doc = '''Checks if the real or imaginary part of z is infinite.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.isinf(self.input(0)))
        


class AutoNode_cmath_isnan(rc.Node):
    title = 'isnan'
    type_ = 'cmath'
    doc = '''Checks if the real or imaginary part of z not a number (NaN).'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.isnan(self.input(0)))
        


class AutoNode_cmath_log10(rc.Node):
    title = 'log10'
    type_ = 'cmath'
    doc = '''Return the base-10 logarithm of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.log10(self.input(0)))
        


class AutoNode_cmath_phase(rc.Node):
    title = 'phase'
    type_ = 'cmath'
    doc = '''Return argument, also known as the phase angle, of a complex.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.phase(self.input(0)))
        


class AutoNode_cmath_polar(rc.Node):
    title = 'polar'
    type_ = 'cmath'
    doc = '''Convert a complex from rectangular coordinates to polar coordinates.

r is the distance from 0 and phi the phase angle.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.polar(self.input(0)))
        


class AutoNode_cmath_rect(rc.Node):
    title = 'rect'
    type_ = 'cmath'
    doc = '''Convert from polar coordinates to rectangular coordinates.'''
    init_inputs = [
        rc.NodeInputBP(label='r'),
rc.NodeInputBP(label='phi'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.rect(self.input(0), self.input(1)))
        


class AutoNode_cmath_sin(rc.Node):
    title = 'sin'
    type_ = 'cmath'
    doc = '''Return the sine of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.sin(self.input(0)))
        


class AutoNode_cmath_sinh(rc.Node):
    title = 'sinh'
    type_ = 'cmath'
    doc = '''Return the hyperbolic sine of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.sinh(self.input(0)))
        


class AutoNode_cmath_sqrt(rc.Node):
    title = 'sqrt'
    type_ = 'cmath'
    doc = '''Return the square root of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.sqrt(self.input(0)))
        


class AutoNode_cmath_tan(rc.Node):
    title = 'tan'
    type_ = 'cmath'
    doc = '''Return the tangent of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.tan(self.input(0)))
        


class AutoNode_cmath_tanh(rc.Node):
    title = 'tanh'
    type_ = 'cmath'
    doc = '''Return the hyperbolic tangent of z.'''
    init_inputs = [
        rc.NodeInputBP(label='z'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cmath.tanh(self.input(0)))
        