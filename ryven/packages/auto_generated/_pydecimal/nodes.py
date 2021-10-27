
from NENV import *

import _pydecimal


class NodeBase(Node):
    pass


class _All_Zeros_Node(NodeBase):
    """
    Matches zero or more characters at the beginning of the string."""
    
    title = '_all_zeros'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='string'),
        NodeInputBP(label='pos', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='endpos', dtype=dtypes.Data(default=9223372036854775807, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._all_zeros(self.input(0), self.input(1), self.input(2)))
        

class _Convert_For_Comparison_Node(NodeBase):
    """
    Given a Decimal instance self and a Python object other, return
    a pair (s, o) of Decimal instances such that "s op o" is
    equivalent to "self op other" for any of the 6 comparison
    operators "op".

    """
    
    title = '_convert_for_comparison'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='equality_op', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._convert_for_comparison(self.input(0), self.input(1)))
        

class _Convert_Other_Node(NodeBase):
    """
    Convert other to Decimal.

    Verifies that it's ok to use in an implicit construction.
    If allow_float is true, allow conversion from float;  this
    is used in the comparison methods (__eq__ and friends).

    """
    
    title = '_convert_other'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='other'),
        NodeInputBP(label='raiseit', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='allow_float', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._convert_other(self.input(0), self.input(1), self.input(2)))
        

class _Dec_From_Triple_Node(NodeBase):
    """
    Create a decimal instance directly, without any validation,
    normalization (e.g. removal of leading zeros) or argument
    conversion.

    This function is for *internal use only*.
    """
    
    title = '_dec_from_triple'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='sign'),
        NodeInputBP(label='coefficient'),
        NodeInputBP(label='exponent'),
        NodeInputBP(label='special', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._dec_from_triple(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Decimal_Lshift_Exact_Node(NodeBase):
    """
     Given integers n and e, return n * 10**e if it's an integer, else None.

    The computation is designed to avoid computing large powers of 10
    unnecessarily.

    >>> _decimal_lshift_exact(3, 4)
    30000
    >>> _decimal_lshift_exact(300, -999999999)  # returns None

    """
    
    title = '_decimal_lshift_exact'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='n'),
        NodeInputBP(label='e'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._decimal_lshift_exact(self.input(0), self.input(1)))
        

class _Dexp_Node(NodeBase):
    """
    Compute an approximation to exp(c*10**e), with p decimal places of
    precision.

    Returns integers d, f such that:

      10**(p-1) <= d <= 10**p, and
      (d-1)*10**f < exp(c*10**e) < (d+1)*10**f

    In other words, d*10**f is an approximation to exp(c*10**e) with p
    digits of precision, and with an error in d of at most 1.  This is
    almost, but not quite, the same as the error being < 1ulp: when d
    = 10**(p-1) the error could be up to 10 ulp."""
    
    title = '_dexp'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='c'),
        NodeInputBP(label='e'),
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._dexp(self.input(0), self.input(1), self.input(2)))
        

class _Div_Nearest_Node(NodeBase):
    """
    Closest integer to a/b, a and b positive integers; rounds to even
    in the case of a tie.

    """
    
    title = '_div_nearest'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._div_nearest(self.input(0), self.input(1)))
        

class _Dlog_Node(NodeBase):
    """
    Given integers c, e and p with c > 0, compute an integer
    approximation to 10**p * log(c*10**e), with an absolute error of
    at most 1.  Assumes that c*10**e is not exactly 1."""
    
    title = '_dlog'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='c'),
        NodeInputBP(label='e'),
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._dlog(self.input(0), self.input(1), self.input(2)))
        

class _Dlog10_Node(NodeBase):
    """
    Given integers c, e and p with c > 0, p >= 0, compute an integer
    approximation to 10**p * log10(c*10**e), with an absolute error of
    at most 1.  Assumes that c*10**e is not exactly 1."""
    
    title = '_dlog10'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='c'),
        NodeInputBP(label='e'),
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._dlog10(self.input(0), self.input(1), self.input(2)))
        

class _Dpower_Node(NodeBase):
    """
    Given integers xc, xe, yc and ye representing Decimals x = xc*10**xe and
    y = yc*10**ye, compute x**y.  Returns a pair of integers (c, e) such that:

      10**(p-1) <= c <= 10**p, and
      (c-1)*10**e < x**y < (c+1)*10**e

    in other words, c*10**e is an approximation to x**y with p digits
    of precision, and with an error in c of at most 1.  (This is
    almost, but not quite, the same as the error being < 1ulp: when c
    == 10**(p-1) we can only guarantee error < 10ulp.)

    We assume that: x is positive and not equal to 1, and y is nonzero.
    """
    
    title = '_dpower'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='xc'),
        NodeInputBP(label='xe'),
        NodeInputBP(label='yc'),
        NodeInputBP(label='ye'),
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._dpower(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class _Exact_Half_Node(NodeBase):
    """
    Matches zero or more characters at the beginning of the string."""
    
    title = '_exact_half'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='string'),
        NodeInputBP(label='pos', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='endpos', dtype=dtypes.Data(default=9223372036854775807, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._exact_half(self.input(0), self.input(1), self.input(2)))
        

class _Format_Align_Node(NodeBase):
    """
    Given an unpadded, non-aligned numeric string 'body' and sign
    string 'sign', add padding and alignment conforming to the given
    format specifier dictionary 'spec' (as produced by
    parse_format_specifier).

    """
    
    title = '_format_align'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='sign'),
        NodeInputBP(label='body'),
        NodeInputBP(label='spec'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._format_align(self.input(0), self.input(1), self.input(2)))
        

class _Format_Number_Node(NodeBase):
    """
    Format a number, given the following data:

    is_negative: true if the number is negative, else false
    intpart: string of digits that must appear before the decimal point
    fracpart: string of digits that must come after the point
    exp: exponent, as an integer
    spec: dictionary resulting from parsing the format specifier

    This function uses the information in spec to:
      insert separators (decimal separator and thousands separators)
      format the sign
      format the exponent
      add trailing '%' for the '%' type
      zero-pad if necessary
      fill and align if necessary
    """
    
    title = '_format_number'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='is_negative'),
        NodeInputBP(label='intpart'),
        NodeInputBP(label='fracpart'),
        NodeInputBP(label='exp'),
        NodeInputBP(label='spec'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._format_number(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class _Format_Sign_Node(NodeBase):
    """
    Determine sign character."""
    
    title = '_format_sign'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='is_negative'),
        NodeInputBP(label='spec'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._format_sign(self.input(0), self.input(1)))
        

class _Group_Lengths_Node(NodeBase):
    """
    Convert a localeconv-style grouping into a (possibly infinite)
    iterable of integers representing group lengths.

    """
    
    title = '_group_lengths'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='grouping'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._group_lengths(self.input(0)))
        

class _Iexp_Node(NodeBase):
    """
    Given integers x and M, M > 0, such that x/M is small in absolute
    value, compute an integer approximation to M*exp(x/M).  For 0 <=
    x/M <= 2.4, the absolute error in the result is bounded by 60 (and
    is usually much smaller)."""
    
    title = '_iexp'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='M'),
        NodeInputBP(label='L', dtype=dtypes.Data(default=8, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._iexp(self.input(0), self.input(1), self.input(2)))
        

class _Ilog_Node(NodeBase):
    """
    Integer approximation to M*log(x/M), with absolute error boundable
    in terms only of x/M.

    Given positive integers x and M, return an integer approximation to
    M * log(x/M).  For L = 8 and 0.1 <= x/M <= 10 the difference
    between the approximation and the exact result is at most 22.  For
    L = 8 and 1.0 <= x/M <= 10.0 the difference is at most 15.  In
    both cases these are upper bounds on the error; it will usually be
    much smaller."""
    
    title = '_ilog'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='M'),
        NodeInputBP(label='L', dtype=dtypes.Data(default=8, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._ilog(self.input(0), self.input(1), self.input(2)))
        

class _Insert_Thousands_Sep_Node(NodeBase):
    """
    Insert thousands separators into a digit string.

    spec is a dictionary whose keys should include 'thousands_sep' and
    'grouping'; typically it's the result of parsing the format
    specifier using _parse_format_specifier.

    The min_width keyword argument gives the minimum length of the
    result, which will be padded on the left with zeros if necessary.

    If necessary, the zero padding adds an extra '0' on the left to
    avoid a leading thousands separator.  For example, inserting
    commas every three digits in '123456', with min_width=8, gives
    '0,123,456', even though that has length 9.

    """
    
    title = '_insert_thousands_sep'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='digits'),
        NodeInputBP(label='spec'),
        NodeInputBP(label='min_width', dtype=dtypes.Data(default=1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._insert_thousands_sep(self.input(0), self.input(1), self.input(2)))
        

class _Log10_Digits_Node(NodeBase):
    """
    Given an integer p >= 0, return floor(10**p)*log(10).

        For example, self.getdigits(3) returns 2302.
        """
    
    title = '_log10_digits'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._log10_digits(self.input(0)))
        

class _Log10_Lb_Node(NodeBase):
    """
    Compute a lower bound for 100*log10(c) for a positive integer c."""
    
    title = '_log10_lb'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='c'),
        NodeInputBP(label='correction', dtype=dtypes.Data(default={'1': 100, '2': 70, '3': 53, '4': 40, '5': 31, '6': 23, '7': 16, '8': 10, '9': 5}, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._log10_lb(self.input(0), self.input(1)))
        

class _Namedtuple_Node(NodeBase):
    """
    Returns a new subclass of tuple with named fields.

    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessible by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)

    """
    
    title = '_namedtuple'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='typename'),
        NodeInputBP(label='field_names'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._namedtuple(self.input(0), self.input(1)))
        

class _Nbits_Node(NodeBase):
    """
    Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6"""
    
    title = '_nbits'
    type_ = '_pydecimal'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._nbits())
        

class _Normalize_Node(NodeBase):
    """
    Normalizes op1, op2 to have the same exp and length of coefficient.

    Done during addition.
    """
    
    title = '_normalize'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='op1'),
        NodeInputBP(label='op2'),
        NodeInputBP(label='prec', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._normalize(self.input(0), self.input(1), self.input(2)))
        

class _Parse_Format_Specifier_Node(NodeBase):
    """
    Parse and validate a format specifier.

    Turns a standard numeric format specifier into a dict, with the
    following entries:

      fill: fill character to pad field to minimum width
      align: alignment type, either '<', '>', '=' or '^'
      sign: either '+', '-' or ' '
      minimumwidth: nonnegative integer giving minimum width
      zeropad: boolean, indicating whether to pad with zeros
      thousands_sep: string to use as thousands separator, or ''
      grouping: grouping for thousands separators, in format
        used by localeconv
      decimal_point: string to use for decimal point
      precision: nonnegative integer giving precision, or None
      type: one of the characters 'eEfFgG%', or None

    """
    
    title = '_parse_format_specifier'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='format_spec'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._parse_format_specifier(self.input(0)))
        

class _Parser_Node(NodeBase):
    """
    Matches zero or more characters at the beginning of the string."""
    
    title = '_parser'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='string'),
        NodeInputBP(label='pos', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='endpos', dtype=dtypes.Data(default=9223372036854775807, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._parser(self.input(0), self.input(1), self.input(2)))
        

class _Rshift_Nearest_Node(NodeBase):
    """
    Given an integer x and a nonnegative integer shift, return closest
    integer to x / 2**shift; use round-to-even in case of a tie.

    """
    
    title = '_rshift_nearest'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='shift'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._rshift_nearest(self.input(0), self.input(1)))
        

class _Sqrt_Nearest_Node(NodeBase):
    """
    Closest integer to the square root of the positive integer n.  a is
    an initial approximation to the square root.  Any positive integer
    will do for a, but the closer a is to the square root of n the
    faster convergence will be.

    """
    
    title = '_sqrt_nearest'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='n'),
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal._sqrt_nearest(self.input(0), self.input(1)))
        

class Getcontext_Node(NodeBase):
    """
    Returns this thread's context.

    If this thread does not yet have a context, returns
    a new context and sets this thread's context.
    New contexts are copies of DefaultContext.
    """
    
    title = 'getcontext'
    type_ = '_pydecimal'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal.getcontext())
        

class Localcontext_Node(NodeBase):
    """
    Return a context manager for a copy of the supplied context

    Uses a copy of the current context if no context is specified
    The returned context manager creates a local decimal context
    in a with statement:
        def sin(x):
             with localcontext() as ctx:
                 ctx.prec += 2
                 # Rest of sin calculation algorithm
                 # uses a precision 2 greater than normal
             return +s  # Convert result to normal precision

         def sin(x):
             with localcontext(ExtendedContext):
                 # Rest of sin calculation algorithm
                 # uses the Extended Context from the
                 # General Decimal Arithmetic Specification
             return +s  # Convert result to normal context

    >>> setcontext(DefaultContext)
    >>> print(getcontext().prec)
    28
    >>> with localcontext():
    ...     ctx = getcontext()
    ...     ctx.prec += 2
    ...     print(ctx.prec)
    ...
    30
    >>> with localcontext(ExtendedContext):
    ...     print(getcontext().prec)
    ...
    9
    >>> print(getcontext().prec)
    28
    """
    
    title = 'localcontext'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='ctx', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal.localcontext(self.input(0)))
        

class Setcontext_Node(NodeBase):
    """
    Set this thread's context to context."""
    
    title = 'setcontext'
    type_ = '_pydecimal'
    init_inputs = [
        NodeInputBP(label='context'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _pydecimal.setcontext(self.input(0)))
        


export_nodes(
    _All_Zeros_Node,
    _Convert_For_Comparison_Node,
    _Convert_Other_Node,
    _Dec_From_Triple_Node,
    _Decimal_Lshift_Exact_Node,
    _Dexp_Node,
    _Div_Nearest_Node,
    _Dlog_Node,
    _Dlog10_Node,
    _Dpower_Node,
    _Exact_Half_Node,
    _Format_Align_Node,
    _Format_Number_Node,
    _Format_Sign_Node,
    _Group_Lengths_Node,
    _Iexp_Node,
    _Ilog_Node,
    _Insert_Thousands_Sep_Node,
    _Log10_Digits_Node,
    _Log10_Lb_Node,
    _Namedtuple_Node,
    _Nbits_Node,
    _Normalize_Node,
    _Parse_Format_Specifier_Node,
    _Parser_Node,
    _Rshift_Nearest_Node,
    _Sqrt_Nearest_Node,
    Getcontext_Node,
    Localcontext_Node,
    Setcontext_Node,
)
