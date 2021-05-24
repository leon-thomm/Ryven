
from NENV import *

import statistics


class NodeBase(Node):
    pass


class _Coerce_Node(NodeBase):
    """
    Coerce types T and S to a common type, or raise TypeError.

    Coercion rules are currently an implementation detail. See the CoerceTest
    test class in test_statistics for details.
    """
    
    title = '_coerce'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='T'),
        NodeInputBP(label='S'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics._coerce(self.input(0), self.input(1)))
        

class _Convert_Node(NodeBase):
    """
    Convert value to given numeric type T."""
    
    title = '_convert'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='value'),
        NodeInputBP(label='T'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics._convert(self.input(0), self.input(1)))
        

class _Exact_Ratio_Node(NodeBase):
    """
    Return Real number x to exact (numerator, denominator) pair.

    >>> _exact_ratio(0.25)
    (1, 4)

    x is expected to be an int, Fraction, Decimal or float.
    """
    
    title = '_exact_ratio'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics._exact_ratio(self.input(0)))
        

class _Fail_Neg_Node(NodeBase):
    """
    Iterate over values, failing if any are less than zero."""
    
    title = '_fail_neg'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='values'),
        NodeInputBP(label='errmsg', dtype=dtypes.Data(default='negative value', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics._fail_neg(self.input(0), self.input(1)))
        

class _Find_Lteq_Node(NodeBase):
    """
    Locate the leftmost value exactly equal to x"""
    
    title = '_find_lteq'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics._find_lteq(self.input(0), self.input(1)))
        

class _Find_Rteq_Node(NodeBase):
    """
    Locate the rightmost value exactly equal to x"""
    
    title = '_find_rteq'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='l'),
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics._find_rteq(self.input(0), self.input(1), self.input(2)))
        

class _Isfinite_Node(NodeBase):
    """
    """
    
    title = '_isfinite'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics._isfinite(self.input(0)))
        

class _Normal_Dist_Inv_Cdf_Node(NodeBase):
    """
    """
    
    title = '_normal_dist_inv_cdf'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='p'),
        NodeInputBP(label='mu'),
        NodeInputBP(label='sigma'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics._normal_dist_inv_cdf(self.input(0), self.input(1), self.input(2)))
        

class _Ss_Node(NodeBase):
    """
    Return sum of square deviations of sequence data.

    If ``c`` is None, the mean is calculated in one pass, and the deviations
    from the mean are calculated in a second pass. Otherwise, deviations are
    calculated from ``c`` as given. Use the second case with care, as it can
    lead to garbage results.
    """
    
    title = '_ss'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='c', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics._ss(self.input(0), self.input(1)))
        

class _Sum_Node(NodeBase):
    """
    _sum(data [, start]) -> (type, sum, count)

    Return a high-precision sum of the given numeric data as a fraction,
    together with the type to be converted to and the count of items.

    If optional argument ``start`` is given, it is added to the total.
    If ``data`` is empty, ``start`` (defaulting to 0) is returned.


    Examples
    --------

    >>> _sum([3, 2.25, 4.5, -0.5, 1.0], 0.75)
    (<class 'float'>, Fraction(11, 1), 5)

    Some sources of round-off error will be avoided:

    # Built-in sum returns zero.
    >>> _sum([1e50, 1, -1e50] * 1000)
    (<class 'float'>, Fraction(1000, 1), 3000)

    Fractions and Decimals are also supported:

    >>> from fractions import Fraction as F
    >>> _sum([F(2, 3), F(7, 5), F(1, 4), F(5, 6)])
    (<class 'fractions.Fraction'>, Fraction(63, 20), 4)

    >>> from decimal import Decimal as D
    >>> data = [D("0.1375"), D("0.2108"), D("0.3061"), D("0.0419")]
    >>> _sum(data)
    (<class 'decimal.Decimal'>, Fraction(6963, 10000), 4)

    Mixed types are currently treated as an error, except that int is
    allowed.
    """
    
    title = '_sum'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='start', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics._sum(self.input(0), self.input(1)))
        

class Bisect_Left_Node(NodeBase):
    """
    Return the index where to insert item x in list a, assuming a is sorted.

The return value i is such that all e in a[:i] have e < x, and all e in
a[i:] have e >= x.  So if x already appears in the list, i points just
before the leftmost x already there.

Optional args lo (default 0) and hi (default len(a)) bound the
slice of a to be searched."""
    
    title = 'bisect_left'
    type_ = 'statistics'
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
        self.set_output_val(0, statistics.bisect_left(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Bisect_Right_Node(NodeBase):
    """
    Return the index where to insert item x in list a, assuming a is sorted.

The return value i is such that all e in a[:i] have e <= x, and all e in
a[i:] have e > x.  So if x already appears in the list, i points just
beyond the rightmost x already there

Optional args lo (default 0) and hi (default len(a)) bound the
slice of a to be searched."""
    
    title = 'bisect_right'
    type_ = 'statistics'
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
        self.set_output_val(0, statistics.bisect_right(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Erf_Node(NodeBase):
    """
    Error function at x."""
    
    title = 'erf'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.erf(self.input(0)))
        

class Exp_Node(NodeBase):
    """
    Return e raised to the power of x."""
    
    title = 'exp'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.exp(self.input(0)))
        

class Fabs_Node(NodeBase):
    """
    Return the absolute value of the float x."""
    
    title = 'fabs'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.fabs(self.input(0)))
        

class Fmean_Node(NodeBase):
    """
    Convert data to floats and compute the arithmetic mean.

    This runs faster than the mean() function and it always returns a float.
    If the input dataset is empty, it raises a StatisticsError.

    >>> fmean([3.5, 4.0, 5.25])
    4.25
    """
    
    title = 'fmean'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.fmean(self.input(0)))
        

class Fsum_Node(NodeBase):
    """
    Return an accurate floating point sum of values in the iterable seq.

Assumes IEEE-754 floating point arithmetic."""
    
    title = 'fsum'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='seq'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.fsum(self.input(0)))
        

class Geometric_Mean_Node(NodeBase):
    """
    Convert data to floats and compute the geometric mean.

    Raises a StatisticsError if the input dataset is empty,
    if it contains a zero, or if it contains a negative value.

    No special efforts are made to achieve exact results.
    (However, this may change in the future.)

    >>> round(geometric_mean([54, 24, 36]), 9)
    36.0
    """
    
    title = 'geometric_mean'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.geometric_mean(self.input(0)))
        

class Harmonic_Mean_Node(NodeBase):
    """
    Return the harmonic mean of data.

    The harmonic mean, sometimes called the subcontrary mean, is the
    reciprocal of the arithmetic mean of the reciprocals of the data,
    and is often appropriate when averaging quantities which are rates
    or ratios, for example speeds. Example:

    Suppose an investor purchases an equal value of shares in each of
    three companies, with P/E (price/earning) ratios of 2.5, 3 and 10.
    What is the average P/E ratio for the investor's portfolio?

    >>> harmonic_mean([2.5, 3, 10])  # For an equal investment portfolio.
    3.6

    Using the arithmetic mean would give an average of about 5.167, which
    is too high.

    If ``data`` is empty, or any element is less than zero,
    ``harmonic_mean`` will raise ``StatisticsError``.
    """
    
    title = 'harmonic_mean'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.harmonic_mean(self.input(0)))
        

class Mean_Node(NodeBase):
    """
    Return the sample arithmetic mean of data.

    >>> mean([1, 2, 3, 4, 4])
    2.8

    >>> from fractions import Fraction as F
    >>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
    Fraction(13, 21)

    >>> from decimal import Decimal as D
    >>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
    Decimal('0.5625')

    If ``data`` is empty, StatisticsError will be raised.
    """
    
    title = 'mean'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.mean(self.input(0)))
        

class Median_Node(NodeBase):
    """
    Return the median (middle value) of numeric data.

    When the number of data points is odd, return the middle data point.
    When the number of data points is even, the median is interpolated by
    taking the average of the two middle values:

    >>> median([1, 3, 5])
    3
    >>> median([1, 3, 5, 7])
    4.0

    """
    
    title = 'median'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.median(self.input(0)))
        

class Median_Grouped_Node(NodeBase):
    """
    Return the 50th percentile (median) of grouped continuous data.

    >>> median_grouped([1, 2, 2, 3, 4, 4, 4, 4, 4, 5])
    3.7
    >>> median_grouped([52, 52, 53, 54])
    52.5

    This calculates the median as the 50th percentile, and should be
    used when your data is continuous and grouped. In the above example,
    the values 1, 2, 3, etc. actually represent the midpoint of classes
    0.5-1.5, 1.5-2.5, 2.5-3.5, etc. The middle value falls somewhere in
    class 3.5-4.5, and interpolation is used to estimate it.

    Optional argument ``interval`` represents the class interval, and
    defaults to 1. Changing the class interval naturally will change the
    interpolated 50th percentile value:

    >>> median_grouped([1, 3, 3, 5, 7], interval=1)
    3.25
    >>> median_grouped([1, 3, 3, 5, 7], interval=2)
    3.5

    This function does not check whether the data points are at least
    ``interval`` apart.
    """
    
    title = 'median_grouped'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='interval', dtype=dtypes.Data(default=1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.median_grouped(self.input(0), self.input(1)))
        

class Median_High_Node(NodeBase):
    """
    Return the high median of data.

    When the number of data points is odd, the middle value is returned.
    When it is even, the larger of the two middle values is returned.

    >>> median_high([1, 3, 5])
    3
    >>> median_high([1, 3, 5, 7])
    5

    """
    
    title = 'median_high'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.median_high(self.input(0)))
        

class Median_Low_Node(NodeBase):
    """
    Return the low median of numeric data.

    When the number of data points is odd, the middle value is returned.
    When it is even, the smaller of the two middle values is returned.

    >>> median_low([1, 3, 5])
    3
    >>> median_low([1, 3, 5, 7])
    3

    """
    
    title = 'median_low'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.median_low(self.input(0)))
        

class Mode_Node(NodeBase):
    """
    Return the most common data point from discrete or nominal data.

    ``mode`` assumes discrete data, and returns a single value. This is the
    standard treatment of the mode as commonly taught in schools:

        >>> mode([1, 1, 2, 3, 3, 3, 3, 4])
        3

    This also works with nominal (non-numeric) data:

        >>> mode(["red", "blue", "blue", "red", "green", "red", "red"])
        'red'

    If there are multiple modes with same frequency, return the first one
    encountered:

        >>> mode(['red', 'red', 'green', 'blue', 'blue'])
        'red'

    If *data* is empty, ``mode``, raises StatisticsError.

    """
    
    title = 'mode'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.mode(self.input(0)))
        

class Multimode_Node(NodeBase):
    """
    Return a list of the most frequently occurring values.

    Will return more than one result if there are multiple modes
    or an empty list if *data* is empty.

    >>> multimode('aabbbbbbbbcc')
    ['b']
    >>> multimode('aabbbbccddddeeffffgg')
    ['b', 'd', 'f']
    >>> multimode('')
    []
    """
    
    title = 'multimode'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.multimode(self.input(0)))
        

class Pstdev_Node(NodeBase):
    """
    Return the square root of the population variance.

    See ``pvariance`` for arguments and other details.

    >>> pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
    0.986893273527251

    """
    
    title = 'pstdev'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='mu', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.pstdev(self.input(0), self.input(1)))
        

class Pvariance_Node(NodeBase):
    """
    Return the population variance of ``data``.

    data should be a sequence or iterable of Real-valued numbers, with at least one
    value. The optional argument mu, if given, should be the mean of
    the data. If it is missing or None, the mean is automatically calculated.

    Use this function to calculate the variance from the entire population.
    To estimate the variance from a sample, the ``variance`` function is
    usually a better choice.

    Examples:

    >>> data = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
    >>> pvariance(data)
    1.25

    If you have already calculated the mean of the data, you can pass it as
    the optional second argument to avoid recalculating it:

    >>> mu = mean(data)
    >>> pvariance(data, mu)
    1.25

    Decimals and Fractions are supported:

    >>> from decimal import Decimal as D
    >>> pvariance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])
    Decimal('24.815')

    >>> from fractions import Fraction as F
    >>> pvariance([F(1, 4), F(5, 4), F(1, 2)])
    Fraction(13, 72)

    """
    
    title = 'pvariance'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='mu', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.pvariance(self.input(0), self.input(1)))
        

class Quantiles_Node(NodeBase):
    """
    Divide *data* into *n* continuous intervals with equal probability.

    Returns a list of (n - 1) cut points separating the intervals.

    Set *n* to 4 for quartiles (the default).  Set *n* to 10 for deciles.
    Set *n* to 100 for percentiles which gives the 99 cuts points that
    separate *data* in to 100 equal sized groups.

    The *data* can be any iterable containing sample.
    The cut points are linearly interpolated between data points.

    If *method* is set to *inclusive*, *data* is treated as population
    data.  The minimum value is treated as the 0th percentile and the
    maximum value is treated as the 100th percentile.
    """
    
    title = 'quantiles'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.quantiles(self.input(0)))
        

class Sqrt_Node(NodeBase):
    """
    Return the square root of x."""
    
    title = 'sqrt'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.sqrt(self.input(0)))
        

class Stdev_Node(NodeBase):
    """
    Return the square root of the sample variance.

    See ``variance`` for arguments and other details.

    >>> stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
    1.0810874155219827

    """
    
    title = 'stdev'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='xbar', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.stdev(self.input(0), self.input(1)))
        

class Variance_Node(NodeBase):
    """
    Return the sample variance of data.

    data should be an iterable of Real-valued numbers, with at least two
    values. The optional argument xbar, if given, should be the mean of
    the data. If it is missing or None, the mean is automatically calculated.

    Use this function when your data is a sample from a population. To
    calculate the variance from the entire population, see ``pvariance``.

    Examples:

    >>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    >>> variance(data)
    1.3720238095238095

    If you have already calculated the mean of your data, you can pass it as
    the optional second argument ``xbar`` to avoid recalculating it:

    >>> m = mean(data)
    >>> variance(data, m)
    1.3720238095238095

    This function does not check that ``xbar`` is actually the mean of
    ``data``. Giving arbitrary values for ``xbar`` may lead to invalid or
    impossible results.

    Decimals and Fractions are supported:

    >>> from decimal import Decimal as D
    >>> variance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])
    Decimal('31.01875')

    >>> from fractions import Fraction as F
    >>> variance([F(1, 6), F(1, 2), F(5, 3)])
    Fraction(67, 108)

    """
    
    title = 'variance'
    type_ = 'statistics'
    init_inputs = [
        NodeInputBP(label='data'),
        NodeInputBP(label='xbar', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, statistics.variance(self.input(0), self.input(1)))
        


export_nodes(
    _Coerce_Node,
    _Convert_Node,
    _Exact_Ratio_Node,
    _Fail_Neg_Node,
    _Find_Lteq_Node,
    _Find_Rteq_Node,
    _Isfinite_Node,
    _Normal_Dist_Inv_Cdf_Node,
    _Ss_Node,
    _Sum_Node,
    Bisect_Left_Node,
    Bisect_Right_Node,
    Erf_Node,
    Exp_Node,
    Fabs_Node,
    Fmean_Node,
    Fsum_Node,
    Geometric_Mean_Node,
    Harmonic_Mean_Node,
    Mean_Node,
    Median_Node,
    Median_Grouped_Node,
    Median_High_Node,
    Median_Low_Node,
    Mode_Node,
    Multimode_Node,
    Pstdev_Node,
    Pvariance_Node,
    Quantiles_Node,
    Sqrt_Node,
    Stdev_Node,
    Variance_Node,
)
