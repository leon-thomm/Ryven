
from NENV import *

import random


class NodeBase(Node):
    pass


class _Acos_Node(NodeBase):
    title = '_acos'
    type_ = 'random'
    doc = """Return the arc cosine (measured in radians) of x."""
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random._acos(self.input(0)))
        

class _Ceil_Node(NodeBase):
    title = '_ceil'
    type_ = 'random'
    doc = """Return the ceiling of x as an Integral.

This is the smallest integer >= x."""
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random._ceil(self.input(0)))
        

class _Cos_Node(NodeBase):
    title = '_cos'
    type_ = 'random'
    doc = """Return the cosine of x (measured in radians)."""
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random._cos(self.input(0)))
        

class _Exp_Node(NodeBase):
    title = '_exp'
    type_ = 'random'
    doc = """Return e raised to the power of x."""
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random._exp(self.input(0)))
        

class _Sha512_Node(NodeBase):
    title = '_sha512'
    type_ = 'random'
    doc = """Return a new SHA-512 hash object; optionally initialized with a string."""
    init_inputs = [
        NodeInputBP(label='string', dtype=dtypes.Data(default=b'', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random._sha512(self.input(0)))
        

class _Sin_Node(NodeBase):
    title = '_sin'
    type_ = 'random'
    doc = """Return the sine of x (measured in radians)."""
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random._sin(self.input(0)))
        

class _Sqrt_Node(NodeBase):
    title = '_sqrt'
    type_ = 'random'
    doc = """Return the square root of x."""
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random._sqrt(self.input(0)))
        

class _Test_Node(NodeBase):
    title = '_test'
    type_ = 'random'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='N', dtype=dtypes.Data(default=2000, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random._test(self.input(0)))
        

class _Test_Generator_Node(NodeBase):
    title = '_test_generator'
    type_ = 'random'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='n'),
        NodeInputBP(label='func'),
        NodeInputBP(label='args'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random._test_generator(self.input(0), self.input(1), self.input(2)))
        

class _Urandom_Node(NodeBase):
    title = '_urandom'
    type_ = 'random'
    doc = """Return a bytes object containing random bytes suitable for cryptographic use."""
    init_inputs = [
        NodeInputBP(label='size'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random._urandom(self.input(0)))
        

class _Warn_Node(NodeBase):
    title = '_warn'
    type_ = 'random'
    doc = """Issue a warning, or maybe ignore it or raise an exception."""
    init_inputs = [
        NodeInputBP(label='message'),
        NodeInputBP(label='category', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='stacklevel', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='source', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random._warn(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Betavariate_Node(NodeBase):
    title = 'betavariate'
    type_ = 'random'
    doc = """Beta distribution.

        Conditions on the parameters are alpha > 0 and beta > 0.
        Returned values range between 0 and 1.

        """
    init_inputs = [
        NodeInputBP(label='alpha'),
        NodeInputBP(label='beta'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.betavariate(self.input(0), self.input(1)))
        

class Choice_Node(NodeBase):
    title = 'choice'
    type_ = 'random'
    doc = """Choose a random element from a non-empty sequence."""
    init_inputs = [
        NodeInputBP(label='seq'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.choice(self.input(0)))
        

class Choices_Node(NodeBase):
    title = 'choices'
    type_ = 'random'
    doc = """Return a k sized list of population elements chosen with replacement.

        If the relative weights or cumulative weights are not specified,
        the selections are made with equal probability.

        """
    init_inputs = [
        NodeInputBP(label='population'),
        NodeInputBP(label='weights', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.choices(self.input(0), self.input(1)))
        

class Expovariate_Node(NodeBase):
    title = 'expovariate'
    type_ = 'random'
    doc = """Exponential distribution.

        lambd is 1.0 divided by the desired mean.  It should be
        nonzero.  (The parameter would be called "lambda", but that is
        a reserved word in Python.)  Returned values range from 0 to
        positive infinity if lambd is positive, and from negative
        infinity to 0 if lambd is negative.

        """
    init_inputs = [
        NodeInputBP(label='lambd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.expovariate(self.input(0)))
        

class Gammavariate_Node(NodeBase):
    title = 'gammavariate'
    type_ = 'random'
    doc = """Gamma distribution.  Not the gamma function!

        Conditions on the parameters are alpha > 0 and beta > 0.

        The probability distribution function is:

                    x ** (alpha - 1) * math.exp(-x / beta)
          pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha

        """
    init_inputs = [
        NodeInputBP(label='alpha'),
        NodeInputBP(label='beta'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.gammavariate(self.input(0), self.input(1)))
        

class Gauss_Node(NodeBase):
    title = 'gauss'
    type_ = 'random'
    doc = """Gaussian distribution.

        mu is the mean, and sigma is the standard deviation.  This is
        slightly faster than the normalvariate() function.

        Not thread-safe without a lock around calls.

        """
    init_inputs = [
        NodeInputBP(label='mu'),
        NodeInputBP(label='sigma'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.gauss(self.input(0), self.input(1)))
        

class Getrandbits_Node(NodeBase):
    title = 'getrandbits'
    type_ = 'random'
    doc = """getrandbits(k) -> x.  Generates an int with k random bits."""
    init_inputs = [
        NodeInputBP(label='k'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.getrandbits(self.input(0)))
        

class Getstate_Node(NodeBase):
    title = 'getstate'
    type_ = 'random'
    doc = """Return internal state; can be passed to setstate() later."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.getstate())
        

class Lognormvariate_Node(NodeBase):
    title = 'lognormvariate'
    type_ = 'random'
    doc = """Log normal distribution.

        If you take the natural logarithm of this distribution, you'll get a
        normal distribution with mean mu and standard deviation sigma.
        mu can have any value, and sigma must be greater than zero.

        """
    init_inputs = [
        NodeInputBP(label='mu'),
        NodeInputBP(label='sigma'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.lognormvariate(self.input(0), self.input(1)))
        

class Normalvariate_Node(NodeBase):
    title = 'normalvariate'
    type_ = 'random'
    doc = """Normal distribution.

        mu is the mean, and sigma is the standard deviation.

        """
    init_inputs = [
        NodeInputBP(label='mu'),
        NodeInputBP(label='sigma'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.normalvariate(self.input(0), self.input(1)))
        

class Paretovariate_Node(NodeBase):
    title = 'paretovariate'
    type_ = 'random'
    doc = """Pareto distribution.  alpha is the shape parameter."""
    init_inputs = [
        NodeInputBP(label='alpha'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.paretovariate(self.input(0)))
        

class Randint_Node(NodeBase):
    title = 'randint'
    type_ = 'random'
    doc = """Return random integer in range [a, b], including both end points.
        """
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.randint(self.input(0), self.input(1)))
        

class Random_Node(NodeBase):
    title = 'random'
    type_ = 'random'
    doc = """random() -> x in the interval [0, 1)."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.random())
        

class Randrange_Node(NodeBase):
    title = 'randrange'
    type_ = 'random'
    doc = """Choose a random item from range(start, stop[, step]).

        This fixes the problem with randint() which includes the
        endpoint; in Python this is usually not what you want.

        """
    init_inputs = [
        NodeInputBP(label='start'),
        NodeInputBP(label='stop', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='step', dtype=dtypes.Data(default=1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.randrange(self.input(0), self.input(1), self.input(2)))
        

class Sample_Node(NodeBase):
    title = 'sample'
    type_ = 'random'
    doc = """Chooses k unique random elements from a population sequence or set.

        Returns a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).

        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.

        To choose a sample in a range of integers, use range as an argument.
        This is especially fast and space efficient for sampling from a
        large population:   sample(range(10000000), 60)
        """
    init_inputs = [
        NodeInputBP(label='population'),
        NodeInputBP(label='k'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.sample(self.input(0), self.input(1)))
        

class Seed_Node(NodeBase):
    title = 'seed'
    type_ = 'random'
    doc = """Initialize internal state from hashable object.

        None or no argument seeds from current time or from an operating
        system specific randomness source if available.

        If *a* is an int, all bits are used.

        For version 2 (the default), all of the bits are used if *a* is a str,
        bytes, or bytearray.  For version 1 (provided for reproducing random
        sequences from older versions of Python), the algorithm for str and
        bytes generates a narrower range of seeds.

        """
    init_inputs = [
        NodeInputBP(label='a', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='version', dtype=dtypes.Data(default=2, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.seed(self.input(0), self.input(1)))
        

class Setstate_Node(NodeBase):
    title = 'setstate'
    type_ = 'random'
    doc = """Restore internal state from object returned by getstate()."""
    init_inputs = [
        NodeInputBP(label='state'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.setstate(self.input(0)))
        

class Shuffle_Node(NodeBase):
    title = 'shuffle'
    type_ = 'random'
    doc = """Shuffle list x in place, and return None.

        Optional argument random is a 0-argument function returning a
        random float in [0.0, 1.0); if it is the default None, the
        standard random.random will be used.

        """
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='random', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.shuffle(self.input(0), self.input(1)))
        

class Triangular_Node(NodeBase):
    title = 'triangular'
    type_ = 'random'
    doc = """Triangular distribution.

        Continuous distribution bounded by given lower and upper limits,
        and having a given mode value in-between.

        http://en.wikipedia.org/wiki/Triangular_distribution

        """
    init_inputs = [
        NodeInputBP(label='low', dtype=dtypes.Data(default=0.0, size='s')),
        NodeInputBP(label='high', dtype=dtypes.Data(default=1.0, size='s')),
        NodeInputBP(label='mode', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.triangular(self.input(0), self.input(1), self.input(2)))
        

class Uniform_Node(NodeBase):
    title = 'uniform'
    type_ = 'random'
    doc = """Get a random number in the range [a, b) or [a, b] depending on rounding."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.uniform(self.input(0), self.input(1)))
        

class Vonmisesvariate_Node(NodeBase):
    title = 'vonmisesvariate'
    type_ = 'random'
    doc = """Circular data distribution.

        mu is the mean angle, expressed in radians between 0 and 2*pi, and
        kappa is the concentration parameter, which must be greater than or
        equal to zero.  If kappa is equal to zero, this distribution reduces
        to a uniform random angle over the range 0 to 2*pi.

        """
    init_inputs = [
        NodeInputBP(label='mu'),
        NodeInputBP(label='kappa'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.vonmisesvariate(self.input(0), self.input(1)))
        

class Weibullvariate_Node(NodeBase):
    title = 'weibullvariate'
    type_ = 'random'
    doc = """Weibull distribution.

        alpha is the scale parameter and beta is the shape parameter.

        """
    init_inputs = [
        NodeInputBP(label='alpha'),
        NodeInputBP(label='beta'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, random.weibullvariate(self.input(0), self.input(1)))
        


export_nodes(
    _Acos_Node,
    _Ceil_Node,
    _Cos_Node,
    _Exp_Node,
    _Sha512_Node,
    _Sin_Node,
    _Sqrt_Node,
    _Test_Node,
    _Test_Generator_Node,
    _Urandom_Node,
    _Warn_Node,
    Betavariate_Node,
    Choice_Node,
    Choices_Node,
    Expovariate_Node,
    Gammavariate_Node,
    Gauss_Node,
    Getrandbits_Node,
    Getstate_Node,
    Lognormvariate_Node,
    Normalvariate_Node,
    Paretovariate_Node,
    Randint_Node,
    Random_Node,
    Randrange_Node,
    Sample_Node,
    Seed_Node,
    Setstate_Node,
    Shuffle_Node,
    Triangular_Node,
    Uniform_Node,
    Vonmisesvariate_Node,
    Weibullvariate_Node,
)
