import ryvencore_qt as rc
import difflib


class AutoNode_difflib_IS_CHARACTER_JUNK(rc.Node):
    title = 'IS_CHARACTER_JUNK'
    doc = '''
    Return True for ignorable character: iff `ch` is a space or tab.

    Examples:

    >>> IS_CHARACTER_JUNK(' ')
    True
    >>> IS_CHARACTER_JUNK('\t')
    True
    >>> IS_CHARACTER_JUNK('\n')
    False
    >>> IS_CHARACTER_JUNK('x')
    False
    '''
    init_inputs = [
        rc.NodeInputBP(label='ch'),
rc.NodeInputBP(label='ws'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib.IS_CHARACTER_JUNK(self.input(0), self.input(1)))
        


class AutoNode_difflib_IS_LINE_JUNK(rc.Node):
    title = 'IS_LINE_JUNK'
    doc = '''
    Return True for ignorable line: iff `line` is blank or contains a single '#'.

    Examples:

    >>> IS_LINE_JUNK('\n')
    True
    >>> IS_LINE_JUNK('  #   \n')
    True
    >>> IS_LINE_JUNK('hello\n')
    False
    '''
    init_inputs = [
        rc.NodeInputBP(label='line'),
rc.NodeInputBP(label='pat'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib.IS_LINE_JUNK(self.input(0), self.input(1)))
        


class AutoNode_difflib__calculate_ratio(rc.Node):
    title = '_calculate_ratio'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='matches'),
rc.NodeInputBP(label='length'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib._calculate_ratio(self.input(0), self.input(1)))
        


class AutoNode_difflib__check_types(rc.Node):
    title = '_check_types'
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
        self.set_output_val(0, difflib._check_types(self.input(0), self.input(1)))
        


class AutoNode_difflib__format_range_context(rc.Node):
    title = '_format_range_context'
    doc = '''Convert range to the "ed" format'''
    init_inputs = [
        rc.NodeInputBP(label='start'),
rc.NodeInputBP(label='stop'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib._format_range_context(self.input(0), self.input(1)))
        


class AutoNode_difflib__format_range_unified(rc.Node):
    title = '_format_range_unified'
    doc = '''Convert range to the "ed" format'''
    init_inputs = [
        rc.NodeInputBP(label='start'),
rc.NodeInputBP(label='stop'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib._format_range_unified(self.input(0), self.input(1)))
        


class AutoNode_difflib__keep_original_ws(rc.Node):
    title = '_keep_original_ws'
    doc = '''Replace whitespace with the original whitespace characters in `s`'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='tag_s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib._keep_original_ws(self.input(0), self.input(1)))
        


class AutoNode_difflib__mdiff(rc.Node):
    title = '_mdiff'
    doc = '''Returns generator yielding marked up from/to side by side differences.

    Arguments:
    fromlines -- list of text lines to compared to tolines
    tolines -- list of text lines to be compared to fromlines
    context -- number of context lines to display on each side of difference,
               if None, all from/to text lines will be generated.
    linejunk -- passed on to ndiff (see ndiff documentation)
    charjunk -- passed on to ndiff (see ndiff documentation)

    This function returns an iterator which returns a tuple:
    (from line tuple, to line tuple, boolean flag)

    from/to line tuple -- (line num, line text)
        line num -- integer or None (to indicate a context separation)
        line text -- original line text with following markers inserted:
            '\0+' -- marks start of added text
            '\0-' -- marks start of deleted text
            '\0^' -- marks start of changed text
            '\1' -- marks end of added/deleted/changed text

    boolean flag -- None indicates context separation, True indicates
        either "from" or "to" line contains a change, otherwise False.

    This function/iterator was originally developed to generate side by side
    file difference for making HTML pages (see HtmlDiff class for example
    usage).

    Note, this function utilizes the ndiff function to generate the side by
    side difference markup.  Optional ndiff arguments may be passed to this
    function and they in turn will be passed to ndiff.
    '''
    init_inputs = [
        rc.NodeInputBP(label='fromlines'),
rc.NodeInputBP(label='tolines'),
rc.NodeInputBP(label='context'),
rc.NodeInputBP(label='linejunk'),
rc.NodeInputBP(label='charjunk'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib._mdiff(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_difflib__namedtuple(rc.Node):
    title = '_namedtuple'
    doc = '''Returns a new subclass of tuple with named fields.

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

    '''
    init_inputs = [
        rc.NodeInputBP(label='typename'),
rc.NodeInputBP(label='field_names'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib._namedtuple(self.input(0), self.input(1)))
        


class AutoNode_difflib__nlargest(rc.Node):
    title = '_nlargest'
    doc = '''Find the n largest elements in a dataset.

    Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]
    '''
    init_inputs = [
        rc.NodeInputBP(label='n'),
rc.NodeInputBP(label='iterable'),
rc.NodeInputBP(label='key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib._nlargest(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_difflib__test(rc.Node):
    title = '_test'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib._test())
        


class AutoNode_difflib_context_diff(rc.Node):
    title = 'context_diff'
    doc = '''
    Compare two sequences of lines; generate the delta as a context diff.

    Context diffs are a compact way of showing line changes and a few
    lines of context.  The number of context lines is set by 'n' which
    defaults to three.

    By default, the diff control lines (those with *** or ---) are
    created with a trailing newline.  This is helpful so that inputs
    created from file.readlines() result in diffs that are suitable for
    file.writelines() since both the inputs and outputs have trailing
    newlines.

    For inputs that do not have trailing newlines, set the lineterm
    argument to "" so that the output will be uniformly newline free.

    The context diff format normally has a header for filenames and
    modification times.  Any or all of these may be specified using
    strings for 'fromfile', 'tofile', 'fromfiledate', and 'tofiledate'.
    The modification times are normally expressed in the ISO 8601 format.
    If not specified, the strings default to blanks.

    Example:

    >>> print(''.join(context_diff('one\ntwo\nthree\nfour\n'.splitlines(True),
    ...       'zero\none\ntree\nfour\n'.splitlines(True), 'Original', 'Current')),
    ...       end="")
    *** Original
    --- Current
    ***************
    *** 1,4 ****
      one
    ! two
    ! three
      four
    --- 1,4 ----
    + zero
      one
    ! tree
      four
    '''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
rc.NodeInputBP(label='fromfile'),
rc.NodeInputBP(label='tofile'),
rc.NodeInputBP(label='fromfiledate'),
rc.NodeInputBP(label='tofiledate'),
rc.NodeInputBP(label='n'),
rc.NodeInputBP(label='lineterm'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib.context_diff(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        


class AutoNode_difflib_diff_bytes(rc.Node):
    title = 'diff_bytes'
    doc = '''
    Compare `a` and `b`, two sequences of lines represented as bytes rather
    than str. This is a wrapper for `dfunc`, which is typically either
    unified_diff() or context_diff(). Inputs are losslessly converted to
    strings so that `dfunc` only has to worry about strings, and encoded
    back to bytes on return. This is necessary to compare files with
    unknown or inconsistent encoding. All other inputs (except `n`) must be
    bytes rather than str.
    '''
    init_inputs = [
        rc.NodeInputBP(label='dfunc'),
rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
rc.NodeInputBP(label='fromfile'),
rc.NodeInputBP(label='tofile'),
rc.NodeInputBP(label='fromfiledate'),
rc.NodeInputBP(label='tofiledate'),
rc.NodeInputBP(label='n'),
rc.NodeInputBP(label='lineterm'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib.diff_bytes(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7), self.input(8)))
        


class AutoNode_difflib_get_close_matches(rc.Node):
    title = 'get_close_matches'
    doc = '''Use SequenceMatcher to return list of the best "good enough" matches.

    word is a sequence for which close matches are desired (typically a
    string).

    possibilities is a list of sequences against which to match word
    (typically a list of strings).

    Optional arg n (default 3) is the maximum number of close matches to
    return.  n must be > 0.

    Optional arg cutoff (default 0.6) is a float in [0, 1].  Possibilities
    that don't score at least that similar to word are ignored.

    The best (no more than n) matches among the possibilities are returned
    in a list, sorted by similarity score, most similar first.

    >>> get_close_matches("appel", ["ape", "apple", "peach", "puppy"])
    ['apple', 'ape']
    >>> import keyword as _keyword
    >>> get_close_matches("wheel", _keyword.kwlist)
    ['while']
    >>> get_close_matches("Apple", _keyword.kwlist)
    []
    >>> get_close_matches("accept", _keyword.kwlist)
    ['except']
    '''
    init_inputs = [
        rc.NodeInputBP(label='word'),
rc.NodeInputBP(label='possibilities'),
rc.NodeInputBP(label='n'),
rc.NodeInputBP(label='cutoff'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib.get_close_matches(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_difflib_ndiff(rc.Node):
    title = 'ndiff'
    doc = '''
    Compare `a` and `b` (lists of strings); return a `Differ`-style delta.

    Optional keyword parameters `linejunk` and `charjunk` are for filter
    functions, or can be None:

    - linejunk: A function that should accept a single string argument and
      return true iff the string is junk.  The default is None, and is
      recommended; the underlying SequenceMatcher class has an adaptive
      notion of "noise" lines.

    - charjunk: A function that accepts a character (string of length
      1), and returns true iff the character is junk. The default is
      the module-level function IS_CHARACTER_JUNK, which filters out
      whitespace characters (a blank or tab; note: it's a bad idea to
      include newline in this!).

    Tools/scripts/ndiff.py is a command-line front-end to this function.

    Example:

    >>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
    ...              'ore\ntree\nemu\n'.splitlines(keepends=True))
    >>> print(''.join(diff), end="")
    - one
    ?  ^
    + ore
    ?  ^
    - two
    - three
    ?  -
    + tree
    + emu
    '''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
rc.NodeInputBP(label='linejunk'),
rc.NodeInputBP(label='charjunk'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib.ndiff(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_difflib_restore(rc.Node):
    title = 'restore'
    doc = '''
    Generate one of the two sequences that generated a delta.

    Given a `delta` produced by `Differ.compare()` or `ndiff()`, extract
    lines originating from file 1 or 2 (parameter `which`), stripping off line
    prefixes.

    Examples:

    >>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
    ...              'ore\ntree\nemu\n'.splitlines(keepends=True))
    >>> diff = list(diff)
    >>> print(''.join(restore(diff, 1)), end="")
    one
    two
    three
    >>> print(''.join(restore(diff, 2)), end="")
    ore
    tree
    emu
    '''
    init_inputs = [
        rc.NodeInputBP(label='delta'),
rc.NodeInputBP(label='which'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib.restore(self.input(0), self.input(1)))
        


class AutoNode_difflib_unified_diff(rc.Node):
    title = 'unified_diff'
    doc = '''
    Compare two sequences of lines; generate the delta as a unified diff.

    Unified diffs are a compact way of showing line changes and a few
    lines of context.  The number of context lines is set by 'n' which
    defaults to three.

    By default, the diff control lines (those with ---, +++, or @@) are
    created with a trailing newline.  This is helpful so that inputs
    created from file.readlines() result in diffs that are suitable for
    file.writelines() since both the inputs and outputs have trailing
    newlines.

    For inputs that do not have trailing newlines, set the lineterm
    argument to "" so that the output will be uniformly newline free.

    The unidiff format normally has a header for filenames and modification
    times.  Any or all of these may be specified using strings for
    'fromfile', 'tofile', 'fromfiledate', and 'tofiledate'.
    The modification times are normally expressed in the ISO 8601 format.

    Example:

    >>> for line in unified_diff('one two three four'.split(),
    ...             'zero one tree four'.split(), 'Original', 'Current',
    ...             '2005-01-26 23:30:50', '2010-04-02 10:20:52',
    ...             lineterm=''):
    ...     print(line)                 # doctest: +NORMALIZE_WHITESPACE
    --- Original        2005-01-26 23:30:50
    +++ Current         2010-04-02 10:20:52
    @@ -1,4 +1,4 @@
    +zero
     one
    -two
    -three
    +tree
     four
    '''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
rc.NodeInputBP(label='fromfile'),
rc.NodeInputBP(label='tofile'),
rc.NodeInputBP(label='fromfiledate'),
rc.NodeInputBP(label='tofiledate'),
rc.NodeInputBP(label='n'),
rc.NodeInputBP(label='lineterm'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, difflib.unified_diff(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        