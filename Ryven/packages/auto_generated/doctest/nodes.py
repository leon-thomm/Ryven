
from NENV import *

import doctest


class NodeBase(Node):
    pass


class Docfilesuite_Node(NodeBase):
    """
    A unittest suite for one or more doctest files.

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
    """
    
    title = 'DocFileSuite'
    type_ = 'doctest'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.DocFileSuite())
        

class Docfiletest_Node(NodeBase):
    """
    """
    
    title = 'DocFileTest'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='module_relative', dtype=dtypes.Data(default=True, size='s')),
        NodeInputBP(label='package', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='globs', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='parser', dtype=dtypes.Data(default=<doctest.DocTestParser object at 0x000001B84293D820>, size='s')),
        NodeInputBP(label='encoding', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.DocFileTest(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class Doctestsuite_Node(NodeBase):
    """
    
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
    """
    
    title = 'DocTestSuite'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='module', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='globs', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='extraglobs', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='test_finder', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.DocTestSuite(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Comment_Line_Node(NodeBase):
    """
    Return a commented form of the given line"""
    
    title = '_comment_line'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='line'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest._comment_line(self.input(0)))
        

class _Ellipsis_Match_Node(NodeBase):
    """
    
    Essentially the only subtle case:
    >>> _ellipsis_match('aa...aa', 'aaa')
    False
    """
    
    title = '_ellipsis_match'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='want'),
        NodeInputBP(label='got'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest._ellipsis_match(self.input(0), self.input(1)))
        

class _Exception_Traceback_Node(NodeBase):
    """
    
    Return a string containing a traceback message for the given
    exc_info tuple (as returned by sys.exc_info()).
    """
    
    title = '_exception_traceback'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='exc_info'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest._exception_traceback(self.input(0)))
        

class _Extract_Future_Flags_Node(NodeBase):
    """
    
    Return the compiler-flags associated with the future features that
    have been imported into the given namespace (globs).
    """
    
    title = '_extract_future_flags'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='globs'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest._extract_future_flags(self.input(0)))
        

class _Indent_Node(NodeBase):
    """
    
    Add the given number of space characters to the beginning of
    every non-blank line in `s`, and return the result.
    """
    
    title = '_indent'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='indent', dtype=dtypes.Data(default=4, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest._indent(self.input(0), self.input(1)))
        

class _Load_Testfile_Node(NodeBase):
    """
    """
    
    title = '_load_testfile'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='package'),
        NodeInputBP(label='module_relative'),
        NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest._load_testfile(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Module_Relative_Path_Node(NodeBase):
    """
    """
    
    title = '_module_relative_path'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='module'),
        NodeInputBP(label='test_path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest._module_relative_path(self.input(0), self.input(1)))
        

class _Newline_Convert_Node(NodeBase):
    """
    """
    
    title = '_newline_convert'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest._newline_convert(self.input(0)))
        

class _Normalize_Module_Node(NodeBase):
    """
    
    Return the module specified by `module`.  In particular:
      - If `module` is a module, then return module.
      - If `module` is a string, then import and return the
        module with that name.
      - If `module` is None, then return the calling module.
        The calling module is assumed to be the module of
        the stack frame at the given depth in the call stack.
    """
    
    title = '_normalize_module'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='module'),
        NodeInputBP(label='depth', dtype=dtypes.Data(default=2, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest._normalize_module(self.input(0), self.input(1)))
        

class _Strip_Exception_Details_Node(NodeBase):
    """
    """
    
    title = '_strip_exception_details'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='msg'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest._strip_exception_details(self.input(0)))
        

class _Test_Node(NodeBase):
    """
    """
    
    title = '_test'
    type_ = 'doctest'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest._test())
        

class Debug_Node(NodeBase):
    """
    Debug a single doctest docstring.

    Provide the module (or dotted name of the module) containing the
    test to be debugged and the name (within the module) of the object
    with the docstring with tests to be debugged.
    """
    
    title = 'debug'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='module'),
        NodeInputBP(label='name'),
        NodeInputBP(label='pm', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.debug(self.input(0), self.input(1), self.input(2)))
        

class Debug_Script_Node(NodeBase):
    """
    Debug a test script.  `src` is the script, as a string."""
    
    title = 'debug_script'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='pm', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='globs', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.debug_script(self.input(0), self.input(1), self.input(2)))
        

class Debug_Src_Node(NodeBase):
    """
    Debug a single doctest docstring, in argument `src`'"""
    
    title = 'debug_src'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='pm', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='globs', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.debug_src(self.input(0), self.input(1), self.input(2)))
        

class Namedtuple_Node(NodeBase):
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
    
    title = 'namedtuple'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='typename'),
        NodeInputBP(label='field_names'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.namedtuple(self.input(0), self.input(1)))
        

class Register_Optionflag_Node(NodeBase):
    """
    """
    
    title = 'register_optionflag'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.register_optionflag(self.input(0)))
        

class Run_Docstring_Examples_Node(NodeBase):
    """
    
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
    """
    
    title = 'run_docstring_examples'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='globs'),
        NodeInputBP(label='verbose', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='name', dtype=dtypes.Data(default='NoName', size='s')),
        NodeInputBP(label='compileflags', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='optionflags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.run_docstring_examples(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class Script_From_Examples_Node(NodeBase):
    """
    Extract script from text with examples.

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
       """
    
    title = 'script_from_examples'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.script_from_examples(self.input(0)))
        

class Set_Unittest_Reportflags_Node(NodeBase):
    """
    Sets the unittest option flags.

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
    """
    
    title = 'set_unittest_reportflags'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='flags'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.set_unittest_reportflags(self.input(0)))
        

class Testfile_Node(NodeBase):
    """
    
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
    """
    
    title = 'testfile'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='module_relative', dtype=dtypes.Data(default=True, size='s')),
        NodeInputBP(label='name', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='package', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='globs', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='verbose', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='report', dtype=dtypes.Data(default=True, size='s')),
        NodeInputBP(label='optionflags', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='extraglobs', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='raise_on_error', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='parser', dtype=dtypes.Data(default=<doctest.DocTestParser object at 0x000001B84293D880>, size='s')),
        NodeInputBP(label='encoding', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.testfile(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7), self.input(8), self.input(9), self.input(10), self.input(11)))
        

class Testmod_Node(NodeBase):
    """
    m=None, name=None, globs=None, verbose=None, report=True,
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
    """
    
    title = 'testmod'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='m', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='name', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='globs', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='verbose', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='report', dtype=dtypes.Data(default=True, size='s')),
        NodeInputBP(label='optionflags', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='extraglobs', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='raise_on_error', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='exclude_empty', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.testmod(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7), self.input(8)))
        

class Testsource_Node(NodeBase):
    """
    Extract the test sources from a doctest docstring as a script.

    Provide the module (or dotted name of the module) containing the
    test to be debugged and the name (within the module) of the object
    with the doc string with tests to be debugged.
    """
    
    title = 'testsource'
    type_ = 'doctest'
    init_inputs = [
        NodeInputBP(label='module'),
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, doctest.testsource(self.input(0), self.input(1)))
        


export_nodes(
    Docfilesuite_Node,
    Docfiletest_Node,
    Doctestsuite_Node,
    _Comment_Line_Node,
    _Ellipsis_Match_Node,
    _Exception_Traceback_Node,
    _Extract_Future_Flags_Node,
    _Indent_Node,
    _Load_Testfile_Node,
    _Module_Relative_Path_Node,
    _Newline_Convert_Node,
    _Normalize_Module_Node,
    _Strip_Exception_Details_Node,
    _Test_Node,
    Debug_Node,
    Debug_Script_Node,
    Debug_Src_Node,
    Namedtuple_Node,
    Register_Optionflag_Node,
    Run_Docstring_Examples_Node,
    Script_From_Examples_Node,
    Set_Unittest_Reportflags_Node,
    Testfile_Node,
    Testmod_Node,
    Testsource_Node,
)
