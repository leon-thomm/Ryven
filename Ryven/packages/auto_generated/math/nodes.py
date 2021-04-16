import ryvencore_qt as rc
import math


class AutoNode_math_acos(rc.Node):
    title = 'acos'
    type_ = 'math'
    doc = '''Return the arc cosine (measured in radians) of x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.acos(self.input(0)))
        


class AutoNode_math_acosh(rc.Node):
    title = 'acosh'
    type_ = 'math'
    doc = '''Return the inverse hyperbolic cosine of x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.acosh(self.input(0)))
        


class AutoNode_math_asin(rc.Node):
    title = 'asin'
    type_ = 'math'
    doc = '''Return the arc sine (measured in radians) of x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.asin(self.input(0)))
        


class AutoNode_math_asinh(rc.Node):
    title = 'asinh'
    type_ = 'math'
    doc = '''Return the inverse hyperbolic sine of x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.asinh(self.input(0)))
        


class AutoNode_math_atan(rc.Node):
    title = 'atan'
    type_ = 'math'
    doc = '''Return the arc tangent (measured in radians) of x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.atan(self.input(0)))
        


class AutoNode_math_atan2(rc.Node):
    title = 'atan2'
    type_ = 'math'
    doc = '''Return the arc tangent (measured in radians) of y/x.

Unlike atan(y/x), the signs of both x and y are considered.'''
    init_inputs = [
        rc.NodeInputBP(label='y'),
rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.atan2(self.input(0), self.input(1)))
        


class AutoNode_math_atanh(rc.Node):
    title = 'atanh'
    type_ = 'math'
    doc = '''Return the inverse hyperbolic tangent of x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.atanh(self.input(0)))
        


class AutoNode_math_ceil(rc.Node):
    title = 'ceil'
    type_ = 'math'
    doc = '''Return the ceiling of x as an Integral.

This is the smallest integer >= x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.ceil(self.input(0)))
        


class AutoNode_math_comb(rc.Node):
    title = 'comb'
    type_ = 'math'
    doc = '''Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.'''
    init_inputs = [
        rc.NodeInputBP(label='n'),
rc.NodeInputBP(label='k'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.comb(self.input(0), self.input(1)))
        


class AutoNode_math_copysign(rc.Node):
    title = 'copysign'
    type_ = 'math'
    doc = '''Return a float with the magnitude (absolute value) of x but the sign of y.

On platforms that support signed zeros, copysign(1.0, -0.0)
returns -1.0.
'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='y'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.copysign(self.input(0), self.input(1)))
        


class AutoNode_math_cos(rc.Node):
    title = 'cos'
    type_ = 'math'
    doc = '''Return the cosine of x (measured in radians).'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.cos(self.input(0)))
        


class AutoNode_math_cosh(rc.Node):
    title = 'cosh'
    type_ = 'math'
    doc = '''Return the hyperbolic cosine of x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.cosh(self.input(0)))
        


class AutoNode_math_degrees(rc.Node):
    title = 'degrees'
    type_ = 'math'
    doc = '''Convert angle x from radians to degrees.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.degrees(self.input(0)))
        


class AutoNode_math_dist(rc.Node):
    title = 'dist'
    type_ = 'math'
    doc = '''Return the Euclidean distance between two points p and q.

The points should be specified as sequences (or iterables) of
coordinates.  Both inputs must have the same dimension.

Roughly equivalent to:
    sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))'''
    init_inputs = [
        rc.NodeInputBP(label='p'),
rc.NodeInputBP(label='q'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.dist(self.input(0), self.input(1)))
        


class AutoNode_math_erf(rc.Node):
    title = 'erf'
    type_ = 'math'
    doc = '''Error function at x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.erf(self.input(0)))
        


class AutoNode_math_erfc(rc.Node):
    title = 'erfc'
    type_ = 'math'
    doc = '''Complementary error function at x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.erfc(self.input(0)))
        


class AutoNode_math_exp(rc.Node):
    title = 'exp'
    type_ = 'math'
    doc = '''Return e raised to the power of x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.exp(self.input(0)))
        


class AutoNode_math_expm1(rc.Node):
    title = 'expm1'
    type_ = 'math'
    doc = '''Return exp(x)-1.

This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.expm1(self.input(0)))
        


class AutoNode_math_fabs(rc.Node):
    title = 'fabs'
    type_ = 'math'
    doc = '''Return the absolute value of the float x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.fabs(self.input(0)))
        


class AutoNode_math_factorial(rc.Node):
    title = 'factorial'
    type_ = 'math'
    doc = '''Find x!.

Raise a ValueError if x is negative or non-integral.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.factorial(self.input(0)))
        


class AutoNode_math_floor(rc.Node):
    title = 'floor'
    type_ = 'math'
    doc = '''Return the floor of x as an Integral.

This is the largest integer <= x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.floor(self.input(0)))
        


class AutoNode_math_fmod(rc.Node):
    title = 'fmod'
    type_ = 'math'
    doc = '''Return fmod(x, y), according to platform C.

x % y may differ.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='y'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.fmod(self.input(0), self.input(1)))
        


class AutoNode_math_frexp(rc.Node):
    title = 'frexp'
    type_ = 'math'
    doc = '''Return the mantissa and exponent of x, as pair (m, e).

m is a float and e is an int, such that x = m * 2.**e.
If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.frexp(self.input(0)))
        


class AutoNode_math_fsum(rc.Node):
    title = 'fsum'
    type_ = 'math'
    doc = '''Return an accurate floating point sum of values in the iterable seq.

Assumes IEEE-754 floating point arithmetic.'''
    init_inputs = [
        rc.NodeInputBP(label='seq'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.fsum(self.input(0)))
        


class AutoNode_math_gamma(rc.Node):
    title = 'gamma'
    type_ = 'math'
    doc = '''Gamma function at x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.gamma(self.input(0)))
        


class AutoNode_math_gcd(rc.Node):
    title = 'gcd'
    type_ = 'math'
    doc = '''greatest common divisor of x and y'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='y'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.gcd(self.input(0), self.input(1)))
        


class AutoNode_math_isclose(rc.Node):
    title = 'isclose'
    type_ = 'math'
    doc = '''Determine whether two floating point numbers are close in value.

  rel_tol
    maximum difference for being considered "close", relative to the
    magnitude of the input values
  abs_tol
    maximum difference for being considered "close", regardless of the
    magnitude of the input values

Return True if a is close in value to b, and False otherwise.

For the values to be considered close, the difference between them
must be smaller than at least one of the tolerances.

-inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
is, NaN is not close to anything, even itself.  inf and -inf are
only close to themselves.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.isclose(self.input(0), self.input(1)))
        


class AutoNode_math_isfinite(rc.Node):
    title = 'isfinite'
    type_ = 'math'
    doc = '''Return True if x is neither an infinity nor a NaN, and False otherwise.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.isfinite(self.input(0)))
        


class AutoNode_math_isinf(rc.Node):
    title = 'isinf'
    type_ = 'math'
    doc = '''Return True if x is a positive or negative infinity, and False otherwise.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.isinf(self.input(0)))
        


class AutoNode_math_isnan(rc.Node):
    title = 'isnan'
    type_ = 'math'
    doc = '''Return True if x is a NaN (not a number), and False otherwise.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.isnan(self.input(0)))
        


class AutoNode_math_isqrt(rc.Node):
    title = 'isqrt'
    type_ = 'math'
    doc = '''Return the integer part of the square root of the input.'''
    init_inputs = [
        rc.NodeInputBP(label='n'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.isqrt(self.input(0)))
        


class AutoNode_math_ldexp(rc.Node):
    title = 'ldexp'
    type_ = 'math'
    doc = '''Return x * (2**i).

This is essentially the inverse of frexp().'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='i'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.ldexp(self.input(0), self.input(1)))
        


class AutoNode_math_lgamma(rc.Node):
    title = 'lgamma'
    type_ = 'math'
    doc = '''Natural logarithm of absolute value of Gamma function at x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.lgamma(self.input(0)))
        


class AutoNode_math_log10(rc.Node):
    title = 'log10'
    type_ = 'math'
    doc = '''Return the base 10 logarithm of x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.log10(self.input(0)))
        


class AutoNode_math_log1p(rc.Node):
    title = 'log1p'
    type_ = 'math'
    doc = '''Return the natural logarithm of 1+x (base e).

The result is computed in a way which is accurate for x near zero.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.log1p(self.input(0)))
        


class AutoNode_math_log2(rc.Node):
    title = 'log2'
    type_ = 'math'
    doc = '''Return the base 2 logarithm of x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.log2(self.input(0)))
        


class AutoNode_math_modf(rc.Node):
    title = 'modf'
    type_ = 'math'
    doc = '''Return the fractional and integer parts of x.

Both results carry the sign of x and are floats.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.modf(self.input(0)))
        


class AutoNode_math_perm(rc.Node):
    title = 'perm'
    type_ = 'math'
    doc = '''Number of ways to choose k items from n items without repetition and with order.

Evaluates to n! / (n - k)! when k <= n and evaluates
to zero when k > n.

If k is not specified or is None, then k defaults to n
and the function returns n!.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.'''
    init_inputs = [
        rc.NodeInputBP(label='n'),
rc.NodeInputBP(label='k'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.perm(self.input(0), self.input(1)))
        


class AutoNode_math_pow(rc.Node):
    title = 'pow'
    type_ = 'math'
    doc = '''Return x**y (x to the power of y).'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='y'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.pow(self.input(0), self.input(1)))
        


class AutoNode_math_prod(rc.Node):
    title = 'prod'
    type_ = 'math'
    doc = '''Calculate the product of all the elements in the input iterable.

The default start value for the product is 1.

When the iterable is empty, return the start value.  This function is
intended specifically for use with numeric values and may reject
non-numeric types.'''
    init_inputs = [
        rc.NodeInputBP(label='iterable'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.prod(self.input(0)))
        


class AutoNode_math_radians(rc.Node):
    title = 'radians'
    type_ = 'math'
    doc = '''Convert angle x from degrees to radians.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.radians(self.input(0)))
        


class AutoNode_math_remainder(rc.Node):
    title = 'remainder'
    type_ = 'math'
    doc = '''Difference between x and the closest integer multiple of y.

Return x - n*y where n*y is the closest integer multiple of y.
In the case where x is exactly halfway between two multiples of
y, the nearest even value of n is used. The result is always exact.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='y'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.remainder(self.input(0), self.input(1)))
        


class AutoNode_math_sin(rc.Node):
    title = 'sin'
    type_ = 'math'
    doc = '''Return the sine of x (measured in radians).'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.sin(self.input(0)))
        


class AutoNode_math_sinh(rc.Node):
    title = 'sinh'
    type_ = 'math'
    doc = '''Return the hyperbolic sine of x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.sinh(self.input(0)))
        


class AutoNode_math_sqrt(rc.Node):
    title = 'sqrt'
    type_ = 'math'
    doc = '''Return the square root of x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.sqrt(self.input(0)))
        


class AutoNode_math_tan(rc.Node):
    title = 'tan'
    type_ = 'math'
    doc = '''Return the tangent of x (measured in radians).'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.tan(self.input(0)))
        


class AutoNode_math_tanh(rc.Node):
    title = 'tanh'
    type_ = 'math'
    doc = '''Return the hyperbolic tangent of x.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.tanh(self.input(0)))
        


class AutoNode_math_trunc(rc.Node):
    title = 'trunc'
    type_ = 'math'
    doc = '''Truncates the Real x to the nearest Integral toward 0.

Uses the __trunc__ magic method.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, math.trunc(self.input(0)))
        