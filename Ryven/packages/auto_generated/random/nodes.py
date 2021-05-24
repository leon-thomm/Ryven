
from NENV import *

import random


class NodeBase(Node):
    pass


class _Acos_Node(NodeBase):
    """
    Return the arc cosine (measured in radians) of x.

The result is between 0 and pi."""
    
    title = '_acos'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random._acos(self.input(0)))
        

class _Bisect_Node(NodeBase):
    """
    Return the index where to insert item x in list a, assuming a is sorted.

The return value i is such that all e in a[:i] have e <= x, and all e in
a[i:] have e > x.  So if x already appears in the list, i points just
beyond the rightmost x already there

Optional args lo (default 0) and hi (default len(a)) bound the
slice of a to be searched."""
    
    title = '_bisect'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='x'),
        NodeInputBP(label='lo', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='hi', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random._bisect(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Ceil_Node(NodeBase):
    """
    Return the ceiling of x as an Integral.

This is the smallest integer >= x."""
    
    title = '_ceil'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random._ceil(self.input(0)))
        

class _Cos_Node(NodeBase):
    """
    Return the cosine of x (measured in radians)."""
    
    title = '_cos'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random._cos(self.input(0)))
        

class _Exp_Node(NodeBase):
    """
    Return e raised to the power of x."""
    
    title = '_exp'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random._exp(self.input(0)))
        

class _Floor_Node(NodeBase):
    """
    Return the floor of x as an Integral.

This is the largest integer <= x."""
    
    title = '_floor'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random._floor(self.input(0)))
        

class _Sha512_Node(NodeBase):
    """
    Return a new SHA-512 hash object; optionally initialized with a string."""
    
    title = '_sha512'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='string', dtype=dtypes.Data(default=b'', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random._sha512(self.input(0)))
        

class _Sin_Node(NodeBase):
    """
    Return the sine of x (measured in radians)."""
    
    title = '_sin'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random._sin(self.input(0)))
        

class _Sqrt_Node(NodeBase):
    """
    Return the square root of x."""
    
    title = '_sqrt'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random._sqrt(self.input(0)))
        

class _Test_Node(NodeBase):
    """
    """
    
    title = '_test'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='N', dtype=dtypes.Data(default=2000, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random._test(self.input(0)))
        

class _Test_Generator_Node(NodeBase):
    """
    """
    
    title = '_test_generator'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='n'),
        NodeInputBP(label='func'),
        NodeInputBP(label='args'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random._test_generator(self.input(0), self.input(1), self.input(2)))
        

class _Urandom_Node(NodeBase):
    """
    Return a bytes object containing random bytes suitable for cryptographic use."""
    
    title = '_urandom'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='size'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random._urandom(self.input(0)))
        

class _Warn_Node(NodeBase):
    """
    Issue a warning, or maybe ignore it or raise an exception."""
    
    title = '_warn'
    type_ = 'random'
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

    def update_event(self, inp=-1):
        self.set_output_val(0, random._warn(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Betavariate_Node(NodeBase):
    """
    Beta distribution.

        Conditions on the parameters are alpha > 0 and beta > 0.
        Returned values range between 0 and 1.

        """
    
    title = 'betavariate'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='alpha'),
        NodeInputBP(label='beta'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.betavariate(self.input(0), self.input(1)))
        

class Choice_Node(NodeBase):
    """
    Choose a random element from a non-empty sequence."""
    
    title = 'choice'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='seq'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.choice(self.input(0)))
        

class Choices_Node(NodeBase):
    """
    Return a k sized list of population elements chosen with replacement.

        If the relative weights or cumulative weights are not specified,
        the selections are made with equal probability.

        """
    
    title = 'choices'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='population'),
        NodeInputBP(label='weights', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.choices(self.input(0), self.input(1)))
        

class Expovariate_Node(NodeBase):
    """
    Exponential distribution.

        lambd is 1.0 divided by the desired mean.  It should be
        nonzero.  (The parameter would be called "lambda", but that is
        a reserved word in Python.)  Returned values range from 0 to
        positive infinity if lambd is positive, and from negative
        infinity to 0 if lambd is negative.

        """
    
    title = 'expovariate'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='lambd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.expovariate(self.input(0)))
        

class Gammavariate_Node(NodeBase):
    """
    Gamma distribution.  Not the gamma function!

        Conditions on the parameters are alpha > 0 and beta > 0.

        The probability distribution function is:

                    x ** (alpha - 1) * math.exp(-x / beta)
          pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha

        """
    
    title = 'gammavariate'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='alpha'),
        NodeInputBP(label='beta'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.gammavariate(self.input(0), self.input(1)))
        

class Gauss_Node(NodeBase):
    """
    Gaussian distribution.

        mu is the mean, and sigma is the standard deviation.  This is
        slightly faster than the normalvariate() function.

        Not thread-safe without a lock around calls.

        """
    
    title = 'gauss'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='mu'),
        NodeInputBP(label='sigma'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.gauss(self.input(0), self.input(1)))
        

class Getrandbits_Node(NodeBase):
    """
    getrandbits(k) -> x.  Generates an int with k random bits."""
    
    title = 'getrandbits'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='k'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.getrandbits(self.input(0)))
        

class Getstate_Node(NodeBase):
    """
    Return internal state; can be passed to setstate() later."""
    
    title = 'getstate'
    type_ = 'random'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.getstate())
        

class Lognormvariate_Node(NodeBase):
    """
    Log normal distribution.

        If you take the natural logarithm of this distribution, you'll get a
        normal distribution with mean mu and standard deviation sigma.
        mu can have any value, and sigma must be greater than zero.

        """
    
    title = 'lognormvariate'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='mu'),
        NodeInputBP(label='sigma'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.lognormvariate(self.input(0), self.input(1)))
        

class Normalvariate_Node(NodeBase):
    """
    Normal distribution.

        mu is the mean, and sigma is the standard deviation.

        """
    
    title = 'normalvariate'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='mu'),
        NodeInputBP(label='sigma'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.normalvariate(self.input(0), self.input(1)))
        

class Paretovariate_Node(NodeBase):
    """
    Pareto distribution.  alpha is the shape parameter."""
    
    title = 'paretovariate'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='alpha'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.paretovariate(self.input(0)))
        

class Randbytes_Node(NodeBase):
    """
    Generate n random bytes."""
    
    title = 'randbytes'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.randbytes(self.input(0)))
        

class Randint_Node(NodeBase):
    """
    Return random integer in range [a, b], including both end points.
        """
    
    title = 'randint'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.randint(self.input(0), self.input(1)))
        

class Random_Node(NodeBase):
    """
    random() -> x in the interval [0, 1)."""
    
    title = 'random'
    type_ = 'random'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.random())
        

class Randrange_Node(NodeBase):
    """
    Choose a random item from range(start, stop[, step]).

        This fixes the problem with randint() which includes the
        endpoint; in Python this is usually not what you want.

        """
    
    title = 'randrange'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='start'),
        NodeInputBP(label='stop', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='step', dtype=dtypes.Data(default=1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.randrange(self.input(0), self.input(1), self.input(2)))
        

class Sample_Node(NodeBase):
    """
    Chooses k unique random elements from a population sequence or set.

        Returns a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).

        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.

        Repeated elements can be specified one at a time or with the optional
        counts parameter.  For example:

            sample(['red', 'blue'], counts=[4, 2], k=5)

        is equivalent to:

            sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)

        To choose a sample from a range of integers, use range() for the
        population argument.  This is especially fast and space efficient
        for sampling from a large population:

            sample(range(10000000), 60)

        """
    
    title = 'sample'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='population'),
        NodeInputBP(label='k'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.sample(self.input(0), self.input(1)))
        

class Seed_Node(NodeBase):
    """
    Initialize internal state from a seed.

        The only supported seed types are None, int, float,
        str, bytes, and bytearray.

        None or no argument seeds from current time or from an operating
        system specific randomness source if available.

        If *a* is an int, all bits are used.

        For version 2 (the default), all of the bits are used if *a* is a str,
        bytes, or bytearray.  For version 1 (provided for reproducing random
        sequences from older versions of Python), the algorithm for str and
        bytes generates a narrower range of seeds.

        """
    
    title = 'seed'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='a', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='version', dtype=dtypes.Data(default=2, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.seed(self.input(0), self.input(1)))
        

class Setstate_Node(NodeBase):
    """
    Restore internal state from object returned by getstate()."""
    
    title = 'setstate'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='state'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.setstate(self.input(0)))
        

class Shuffle_Node(NodeBase):
    """
    Shuffle list x in place, and return None.

        Optional argument random is a 0-argument function returning a
        random float in [0.0, 1.0); if it is the default None, the
        standard random.random will be used.

        """
    
    title = 'shuffle'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='random', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.shuffle(self.input(0), self.input(1)))
        

class Triangular_Node(NodeBase):
    """
    Triangular distribution.

        Continuous distribution bounded by given lower and upper limits,
        and having a given mode value in-between.

        http://en.wikipedia.org/wiki/Triangular_distribution

        """
    
    title = 'triangular'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='low', dtype=dtypes.Data(default=0.0, size='s')),
        NodeInputBP(label='high', dtype=dtypes.Data(default=1.0, size='s')),
        NodeInputBP(label='mode', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.triangular(self.input(0), self.input(1), self.input(2)))
        

class Uniform_Node(NodeBase):
    """
    Get a random number in the range [a, b) or [a, b] depending on rounding."""
    
    title = 'uniform'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.uniform(self.input(0), self.input(1)))
        

class Vonmisesvariate_Node(NodeBase):
    """
    Circular data distribution.

        mu is the mean angle, expressed in radians between 0 and 2*pi, and
        kappa is the concentration parameter, which must be greater than or
        equal to zero.  If kappa is equal to zero, this distribution reduces
        to a uniform random angle over the range 0 to 2*pi.

        """
    
    title = 'vonmisesvariate'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='mu'),
        NodeInputBP(label='kappa'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.vonmisesvariate(self.input(0), self.input(1)))
        

class Weibullvariate_Node(NodeBase):
    """
    Weibull distribution.

        alpha is the scale parameter and beta is the shape parameter.

        """
    
    title = 'weibullvariate'
    type_ = 'random'
    init_inputs = [
        NodeInputBP(label='alpha'),
        NodeInputBP(label='beta'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, random.weibullvariate(self.input(0), self.input(1)))
        


export_nodes(
    _Acos_Node,
    _Bisect_Node,
    _Ceil_Node,
    _Cos_Node,
    _Exp_Node,
    _Floor_Node,
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
    Randbytes_Node,
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
