import ryvencore_qt as rc
import doctest


class AutoNode_doctest_DocFileSuite(rc.Node):
    title = 'DocFileSuite'
    description = '''A unittest suite for one or more doctest files.

    The path to each doctest file is given as a string; the
    interpretation of that string depends on the keyword argument
    "module_relative".

    A number of options may be provided as keyword arguments:

    module_relative
      If "module_relative" is True, then the given file paths are
      interpreted as os-independent module-relative paths.  By
      default, these paths are relative to the calling module's
      directory; but if the "package" argument is specified, then
      they are relative to that package.  To ensure os-independence,
      "filename" should use "/" characters to separate path
      segments, and may not be an absolute path (i.e., it may not
      begin with "/").

      If "module_relative" is False, then the given file paths are
      interpreted as os-specific paths.  These paths may be absolute
      or relative (to the current working directory).

    package
      A Python package or the name of a Python package whose directory
      should be used as the base directory for module relative paths.
      If "package" is not specified, then the calling module's
      directory is used as the base directory for module relative
      filenames.  It is an error to specify "package" if
      "module_relative" is False.

    setUp
      A set-up function.  This is called before running the
      tests in each file. The setUp function will be passed a DocTest
      object.  The setUp function can access the test globals as the
      globs attribute of the test passed.

    tearDown
      A tear-down function.  This is called after running the
      tests in each file.  The tearDown function will be passed a DocTest
      object.  The tearDown function can access the test globals as the
      globs attribute of the test passed.

    globs
      A dictionary containing initial global variables for the tests.

    optionflags
      A set of doctest option flags expressed as an integer.

    parser
      A DocTestParser (or subclass) that should be used to extract
      tests from the files.

    encoding
      An encoding that will be used to convert the files to unicode.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest.DocFileSuite())
        


class AutoNode_doctest_DocFileTest(rc.Node):
    title = 'DocFileTest'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='module_relative'),
rc.NodeInputBP(label='package'),
rc.NodeInputBP(label='globs'),
rc.NodeInputBP(label='parser'),
rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest.DocFileTest(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode_doctest_DocTestSuite(rc.Node):
    title = 'DocTestSuite'
    description = '''
    Convert doctest tests for a module to a unittest test suite.

    This converts each documentation string in a module that
    contains doctest tests to a unittest test case.  If any of the
    tests in a doc string fail, then the test case fails.  An exception
    is raised showing the name of the file containing the test and a
    (sometimes approximate) line number.

    The `module` argument provides the module to be tested.  The argument
    can be either a module or a module name.

    If no argument is given, the calling module is used.

    A number of options may be provided as keyword arguments:

    setUp
      A set-up function.  This is called before running the
      tests in each file. The setUp function will be passed a DocTest
      object.  The setUp function can access the test globals as the
      globs attribute of the test passed.

    tearDown
      A tear-down function.  This is called after running the
      tests in each file.  The tearDown function will be passed a DocTest
      object.  The tearDown function can access the test globals as the
      globs attribute of the test passed.

    globs
      A dictionary containing initial global variables for the tests.

    optionflags
       A set of doctest option flags expressed as an integer.
    '''
    init_inputs = [
        rc.NodeInputBP(label='module'),
rc.NodeInputBP(label='globs'),
rc.NodeInputBP(label='extraglobs'),
rc.NodeInputBP(label='test_finder'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest.DocTestSuite(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_doctest__comment_line(rc.Node):
    title = '_comment_line'
    description = '''Return a commented form of the given line'''
    init_inputs = [
        rc.NodeInputBP(label='line'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest._comment_line(self.input(0)))
        


class AutoNode_doctest__ellipsis_match(rc.Node):
    title = '_ellipsis_match'
    description = '''
    Essentially the only subtle case:
    >>> _ellipsis_match('aa...aa', 'aaa')
    False
    '''
    init_inputs = [
        rc.NodeInputBP(label='want'),
rc.NodeInputBP(label='got'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest._ellipsis_match(self.input(0), self.input(1)))
        


class AutoNode_doctest__exception_traceback(rc.Node):
    title = '_exception_traceback'
    description = '''
    Return a string containing a traceback message for the given
    exc_info tuple (as returned by sys.exc_info()).
    '''
    init_inputs = [
        rc.NodeInputBP(label='exc_info'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest._exception_traceback(self.input(0)))
        


class AutoNode_doctest__extract_future_flags(rc.Node):
    title = '_extract_future_flags'
    description = '''
    Return the compiler-flags associated with the future features that
    have been imported into the given namespace (globs).
    '''
    init_inputs = [
        rc.NodeInputBP(label='globs'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest._extract_future_flags(self.input(0)))
        


class AutoNode_doctest__indent(rc.Node):
    title = '_indent'
    description = '''
    Add the given number of space characters to the beginning of
    every non-blank line in `s`, and return the result.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='indent'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest._indent(self.input(0), self.input(1)))
        


class AutoNode_doctest__load_testfile(rc.Node):
    title = '_load_testfile'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='package'),
rc.NodeInputBP(label='module_relative'),
rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest._load_testfile(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_doctest__module_relative_path(rc.Node):
    title = '_module_relative_path'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='module'),
rc.NodeInputBP(label='test_path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest._module_relative_path(self.input(0), self.input(1)))
        


class AutoNode_doctest__newline_convert(rc.Node):
    title = '_newline_convert'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest._newline_convert(self.input(0)))
        


class AutoNode_doctest__normalize_module(rc.Node):
    title = '_normalize_module'
    description = '''
    Return the module specified by `module`.  In particular:
      - If `module` is a module, then return module.
      - If `module` is a string, then import and return the
        module with that name.
      - If `module` is None, then return the calling module.
        The calling module is assumed to be the module of
        the stack frame at the given depth in the call stack.
    '''
    init_inputs = [
        rc.NodeInputBP(label='module'),
rc.NodeInputBP(label='depth'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest._normalize_module(self.input(0), self.input(1)))
        


class AutoNode_doctest__strip_exception_details(rc.Node):
    title = '_strip_exception_details'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='msg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest._strip_exception_details(self.input(0)))
        


class AutoNode_doctest__test(rc.Node):
    title = '_test'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest._test())
        


class AutoNode_doctest_debug(rc.Node):
    title = 'debug'
    description = '''Debug a single doctest docstring.

    Provide the module (or dotted name of the module) containing the
    test to be debugged and the name (within the module) of the object
    with the docstring with tests to be debugged.
    '''
    init_inputs = [
        rc.NodeInputBP(label='module'),
rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='pm'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest.debug(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_doctest_debug_script(rc.Node):
    title = 'debug_script'
    description = '''Debug a test script.  `src` is the script, as a string.'''
    init_inputs = [
        rc.NodeInputBP(label='src'),
rc.NodeInputBP(label='pm'),
rc.NodeInputBP(label='globs'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest.debug_script(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_doctest_debug_src(rc.Node):
    title = 'debug_src'
    description = '''Debug a single doctest docstring, in argument `src`''''
    init_inputs = [
        rc.NodeInputBP(label='src'),
rc.NodeInputBP(label='pm'),
rc.NodeInputBP(label='globs'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest.debug_src(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_doctest_namedtuple(rc.Node):
    title = 'namedtuple'
    description = '''Returns a new subclass of tuple with named fields.

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
        self.set_output_val(0, doctest.namedtuple(self.input(0), self.input(1)))
        


class AutoNode_doctest_register_optionflag(rc.Node):
    title = 'register_optionflag'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest.register_optionflag(self.input(0)))
        


class AutoNode_doctest_run_docstring_examples(rc.Node):
    title = 'run_docstring_examples'
    description = '''
    Test examples in the given object's docstring (`f`), using `globs`
    as globals.  Optional argument `name` is used in failure messages.
    If the optional argument `verbose` is true, then generate output
    even if there are no failures.

    `compileflags` gives the set of flags that should be used by the
    Python compiler when running the examples.  If not specified, then
    it will default to the set of future-import flags that apply to
    `globs`.

    Optional keyword arg `optionflags` specifies options for the
    testing and output.  See the documentation for `testmod` for more
    information.
    '''
    init_inputs = [
        rc.NodeInputBP(label='f'),
rc.NodeInputBP(label='globs'),
rc.NodeInputBP(label='verbose'),
rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='compileflags'),
rc.NodeInputBP(label='optionflags'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest.run_docstring_examples(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode_doctest_script_from_examples(rc.Node):
    title = 'script_from_examples'
    description = '''Extract script from text with examples.

       Converts text with examples to a Python script.  Example input is
       converted to regular code.  Example output and all other words
       are converted to comments:

       >>> text = '''
       ...       Here are examples of simple math.
       ...
       ...           Python has super accurate integer addition
       ...
       ...           >>> 2 + 2
       ...           5
       ...
       ...           And very friendly error messages:
       ...
       ...           >>> 1/0
       ...           To Infinity
       ...           And
       ...           Beyond
       ...
       ...           You can use logic if you want:
       ...
       ...           >>> if 0:
       ...           ...    blah
       ...           ...    blah
       ...           ...
       ...
       ...           Ho hum
       ...           '''

       >>> print(script_from_examples(text))
       # Here are examples of simple math.
       #
       #     Python has super accurate integer addition
       #
       2 + 2
       # Expected:
       ## 5
       #
       #     And very friendly error messages:
       #
       1/0
       # Expected:
       ## To Infinity
       ## And
       ## Beyond
       #
       #     You can use logic if you want:
       #
       if 0:
          blah
          blah
       #
       #     Ho hum
       <BLANKLINE>
       '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest.script_from_examples(self.input(0)))
        


class AutoNode_doctest_set_unittest_reportflags(rc.Node):
    title = 'set_unittest_reportflags'
    description = '''Sets the unittest option flags.

    The old flag is returned so that a runner could restore the old
    value if it wished to:

      >>> import doctest
      >>> old = doctest._unittest_reportflags
      >>> doctest.set_unittest_reportflags(REPORT_NDIFF |
      ...                          REPORT_ONLY_FIRST_FAILURE) == old
      True

      >>> doctest._unittest_reportflags == (REPORT_NDIFF |
      ...                                   REPORT_ONLY_FIRST_FAILURE)
      True

    Only reporting flags can be set:

      >>> doctest.set_unittest_reportflags(ELLIPSIS)
      Traceback (most recent call last):
      ...
      ValueError: ('Only reporting flags allowed', 8)

      >>> doctest.set_unittest_reportflags(old) == (REPORT_NDIFF |
      ...                                   REPORT_ONLY_FIRST_FAILURE)
      True
    '''
    init_inputs = [
        rc.NodeInputBP(label='flags'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest.set_unittest_reportflags(self.input(0)))
        


class AutoNode_doctest_testfile(rc.Node):
    title = 'testfile'
    description = '''
    Test examples in the given file.  Return (#failures, #tests).

    Optional keyword arg "module_relative" specifies how filenames
    should be interpreted:

      - If "module_relative" is True (the default), then "filename"
         specifies a module-relative path.  By default, this path is
         relative to the calling module's directory; but if the
         "package" argument is specified, then it is relative to that
         package.  To ensure os-independence, "filename" should use
         "/" characters to separate path segments, and should not
         be an absolute path (i.e., it may not begin with "/").

      - If "module_relative" is False, then "filename" specifies an
        os-specific path.  The path may be absolute or relative (to
        the current working directory).

    Optional keyword arg "name" gives the name of the test; by default
    use the file's basename.

    Optional keyword argument "package" is a Python package or the
    name of a Python package whose directory should be used as the
    base directory for a module relative filename.  If no package is
    specified, then the calling module's directory is used as the base
    directory for module relative filenames.  It is an error to
    specify "package" if "module_relative" is False.

    Optional keyword arg "globs" gives a dict to be used as the globals
    when executing examples; by default, use {}.  A copy of this dict
    is actually used for each docstring, so that each docstring's
    examples start with a clean slate.

    Optional keyword arg "extraglobs" gives a dictionary that should be
    merged into the globals that are used to execute examples.  By
    default, no extra globals are used.

    Optional keyword arg "verbose" prints lots of stuff if true, prints
    only failures if false; by default, it's true iff "-v" is in sys.argv.

    Optional keyword arg "report" prints a summary at the end when true,
    else prints nothing at the end.  In verbose mode, the summary is
    detailed, else very brief (in fact, empty if all tests passed).

    Optional keyword arg "optionflags" or's together module constants,
    and defaults to 0.  Possible values (see the docs for details):

        DONT_ACCEPT_TRUE_FOR_1
        DONT_ACCEPT_BLANKLINE
        NORMALIZE_WHITESPACE
        ELLIPSIS
        SKIP
        IGNORE_EXCEPTION_DETAIL
        REPORT_UDIFF
        REPORT_CDIFF
        REPORT_NDIFF
        REPORT_ONLY_FIRST_FAILURE

    Optional keyword arg "raise_on_error" raises an exception on the
    first unexpected exception or failure. This allows failures to be
    post-mortem debugged.

    Optional keyword arg "parser" specifies a DocTestParser (or
    subclass) that should be used to extract tests from the files.

    Optional keyword arg "encoding" specifies an encoding that should
    be used to convert the file to unicode.

    Advanced tomfoolery:  testmod runs methods of a local instance of
    class doctest.Tester, then merges the results into (or creates)
    global Tester instance doctest.master.  Methods of doctest.master
    can be called directly too, if you want to do something unusual.
    Passing report=0 to testmod is especially useful then, to delay
    displaying a summary.  Invoke doctest.master.summarize(verbose)
    when you're done fiddling.
    '''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='module_relative'),
rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='package'),
rc.NodeInputBP(label='globs'),
rc.NodeInputBP(label='verbose'),
rc.NodeInputBP(label='report'),
rc.NodeInputBP(label='optionflags'),
rc.NodeInputBP(label='extraglobs'),
rc.NodeInputBP(label='raise_on_error'),
rc.NodeInputBP(label='parser'),
rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest.testfile(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7), self.input(8), self.input(9), self.input(10), self.input(11)))
        


class AutoNode_doctest_testmod(rc.Node):
    title = 'testmod'
    description = '''m=None, name=None, globs=None, verbose=None, report=True,
       optionflags=0, extraglobs=None, raise_on_error=False,
       exclude_empty=False

    Test examples in docstrings in functions and classes reachable
    from module m (or the current module if m is not supplied), starting
    with m.__doc__.

    Also test examples reachable from dict m.__test__ if it exists and is
    not None.  m.__test__ maps names to functions, classes and strings;
    function and class docstrings are tested even if the name is private;
    strings are tested directly, as if they were docstrings.

    Return (#failures, #tests).

    See help(doctest) for an overview.

    Optional keyword arg "name" gives the name of the module; by default
    use m.__name__.

    Optional keyword arg "globs" gives a dict to be used as the globals
    when executing examples; by default, use m.__dict__.  A copy of this
    dict is actually used for each docstring, so that each docstring's
    examples start with a clean slate.

    Optional keyword arg "extraglobs" gives a dictionary that should be
    merged into the globals that are used to execute examples.  By
    default, no extra globals are used.  This is new in 2.4.

    Optional keyword arg "verbose" prints lots of stuff if true, prints
    only failures if false; by default, it's true iff "-v" is in sys.argv.

    Optional keyword arg "report" prints a summary at the end when true,
    else prints nothing at the end.  In verbose mode, the summary is
    detailed, else very brief (in fact, empty if all tests passed).

    Optional keyword arg "optionflags" or's together module constants,
    and defaults to 0.  This is new in 2.3.  Possible values (see the
    docs for details):

        DONT_ACCEPT_TRUE_FOR_1
        DONT_ACCEPT_BLANKLINE
        NORMALIZE_WHITESPACE
        ELLIPSIS
        SKIP
        IGNORE_EXCEPTION_DETAIL
        REPORT_UDIFF
        REPORT_CDIFF
        REPORT_NDIFF
        REPORT_ONLY_FIRST_FAILURE

    Optional keyword arg "raise_on_error" raises an exception on the
    first unexpected exception or failure. This allows failures to be
    post-mortem debugged.

    Advanced tomfoolery:  testmod runs methods of a local instance of
    class doctest.Tester, then merges the results into (or creates)
    global Tester instance doctest.master.  Methods of doctest.master
    can be called directly too, if you want to do something unusual.
    Passing report=0 to testmod is especially useful then, to delay
    displaying a summary.  Invoke doctest.master.summarize(verbose)
    when you're done fiddling.
    '''
    init_inputs = [
        rc.NodeInputBP(label='m'),
rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='globs'),
rc.NodeInputBP(label='verbose'),
rc.NodeInputBP(label='report'),
rc.NodeInputBP(label='optionflags'),
rc.NodeInputBP(label='extraglobs'),
rc.NodeInputBP(label='raise_on_error'),
rc.NodeInputBP(label='exclude_empty'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest.testmod(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7), self.input(8)))
        


class AutoNode_doctest_testsource(rc.Node):
    title = 'testsource'
    description = '''Extract the test sources from a doctest docstring as a script.

    Provide the module (or dotted name of the module) containing the
    test to be debugged and the name (within the module) of the object
    with the doc string with tests to be debugged.
    '''
    init_inputs = [
        rc.NodeInputBP(label='module'),
rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, doctest.testsource(self.input(0), self.input(1)))
        