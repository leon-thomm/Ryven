
from NENV import *

import pydoc


class NodeBase(Node):
    pass


class _Adjust_Cli_Sys_Path_Node(NodeBase):
    """
    Ensures current directory is on sys.path, and __main__ directory is not.

    Exception: __main__ dir is left alone if it's also pydoc's directory.
    """
    
    title = '_adjust_cli_sys_path'
    type_ = 'pydoc'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc._adjust_cli_sys_path())
        

class _Escape_Stdout_Node(NodeBase):
    """
    """
    
    title = '_escape_stdout'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='text'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc._escape_stdout(self.input(0)))
        

class _Findclass_Node(NodeBase):
    """
    """
    
    title = '_findclass'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc._findclass(self.input(0)))
        

class _Finddoc_Node(NodeBase):
    """
    """
    
    title = '_finddoc'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc._finddoc(self.input(0)))
        

class _Get_Revised_Path_Node(NodeBase):
    """
    Ensures current directory is on returned path, and argv0 directory is not

    Exception: argv0 dir is left alone if it's also pydoc's directory.

    Returns a new path entry list, or None if no adjustment is needed.
    """
    
    title = '_get_revised_path'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='given_path'),
        NodeInputBP(label='argv0'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc._get_revised_path(self.input(0), self.input(1)))
        

class _Getdoc_Node(NodeBase):
    """
    Get the documentation string for an object.

    All tabs are expanded to spaces.  To clean up docstrings that are
    indented to line up with blocks of code, any whitespace than can be
    uniformly removed from the second line onwards is removed."""
    
    title = '_getdoc'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc._getdoc(self.input(0)))
        

class _Getowndoc_Node(NodeBase):
    """
    Get the documentation string for an object if it is not
    inherited from its class."""
    
    title = '_getowndoc'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc._getowndoc(self.input(0)))
        

class _Is_Bound_Method_Node(NodeBase):
    """
    
    Returns True if fn is a bound method, regardless of whether
    fn was implemented in Python or in C.
    """
    
    title = '_is_bound_method'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='fn'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc._is_bound_method(self.input(0)))
        

class _Split_List_Node(NodeBase):
    """
    Split sequence s via predicate, and return pair ([true], [false]).

    The return value is a 2-tuple of lists,
        ([x for x in s if predicate(x)],
         [x for x in s if not predicate(x)])
    """
    
    title = '_split_list'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='predicate'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc._split_list(self.input(0), self.input(1)))
        

class _Start_Server_Node(NodeBase):
    """
    Start an HTTP server thread on a specific port.

    Start an HTML/text server thread, so HTML or text documents can be
    browsed dynamically and interactively with a Web browser.  Example use:

        >>> import time
        >>> import pydoc

        Define a URL handler.  To determine what the client is asking
        for, check the URL and content_type.

        Then get or generate some text or HTML code and return it.

        >>> def my_url_handler(url, content_type):
        ...     text = 'the URL sent was: (%s, %s)' % (url, content_type)
        ...     return text

        Start server thread on port 0.
        If you use port 0, the server will pick a random port number.
        You can then use serverthread.port to get the port number.

        >>> port = 0
        >>> serverthread = pydoc._start_server(my_url_handler, port)

        Check that the server is really started.  If it is, open browser
        and get first page.  Use serverthread.url as the starting page.

        >>> if serverthread.serving:
        ...    import webbrowser

        The next two lines are commented out so a browser doesn't open if
        doctest is run on this module.

        #...    webbrowser.open(serverthread.url)
        #True

        Let the server do its thing. We just need to monitor its status.
        Use time.sleep so the loop doesn't hog the CPU.

        >>> starttime = time.monotonic()
        >>> timeout = 1                    #seconds

        This is a short timeout for testing purposes.

        >>> while serverthread.serving:
        ...     time.sleep(.01)
        ...     if serverthread.serving and time.monotonic() - starttime > timeout:
        ...          serverthread.stop()
        ...          break

        Print any errors that may have occurred.

        >>> print(serverthread.error)
        None
   """
    
    title = '_start_server'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='urlhandler'),
        NodeInputBP(label='hostname'),
        NodeInputBP(label='port'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc._start_server(self.input(0), self.input(1), self.input(2)))
        

class _Url_Handler_Node(NodeBase):
    """
    The pydoc url handler for use with the pydoc server.

    If the content_type is 'text/css', the _pydoc.css style
    sheet is read and returned if it exits.

    If the content_type is 'text/html', then the result of
    get_html_page(url) is returned.
    """
    
    title = '_url_handler'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='url'),
        NodeInputBP(label='content_type', dtype=dtypes.Data(default='text/html', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc._url_handler(self.input(0), self.input(1)))
        

class Allmethods_Node(NodeBase):
    """
    """
    
    title = 'allmethods'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='cl'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.allmethods(self.input(0)))
        

class Apropos_Node(NodeBase):
    """
    Print all the one-line module summaries that contain a substring."""
    
    title = 'apropos'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='key'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.apropos(self.input(0)))
        

class Browse_Node(NodeBase):
    """
    Start the enhanced pydoc Web server and open a Web browser.

    Use port '0' to start the server on an arbitrary port.
    Set open_browser to False to suppress opening a browser.
    """
    
    title = 'browse'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='port', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.browse(self.input(0)))
        

class Classify_Class_Attrs_Node(NodeBase):
    """
    Wrap inspect.classify_class_attrs, with fixup for data descriptors."""
    
    title = 'classify_class_attrs'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.classify_class_attrs(self.input(0)))
        

class Classname_Node(NodeBase):
    """
    Get a class name and qualify it with a module name if necessary."""
    
    title = 'classname'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='object'),
        NodeInputBP(label='modname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.classname(self.input(0), self.input(1)))
        

class Cli_Node(NodeBase):
    """
    Command-line interface (looks at sys.argv to decide what to do)."""
    
    title = 'cli'
    type_ = 'pydoc'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.cli())
        

class Cram_Node(NodeBase):
    """
    Omit part of a string if needed to make it fit in a maximum length."""
    
    title = 'cram'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='text'),
        NodeInputBP(label='maxlen'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.cram(self.input(0), self.input(1)))
        

class Describe_Node(NodeBase):
    """
    Produce a short description of the given thing."""
    
    title = 'describe'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='thing'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.describe(self.input(0)))
        

class Doc_Node(NodeBase):
    """
    Display text documentation, given an object or a path to an object."""
    
    title = 'doc'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='thing'),
        NodeInputBP(label='title', dtype=dtypes.Data(default='Python Library Documentation: %s', size='s')),
        NodeInputBP(label='forceload', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='output', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.doc(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Format_Exception_Only_Node(NodeBase):
    """
    Format the exception part of a traceback.

    The arguments are the exception type and value such as given by
    sys.last_type and sys.last_value. The return value is a list of
    strings, each ending in a newline.

    Normally, the list contains a single string; however, for
    SyntaxError exceptions, it contains several lines that (when
    printed) display detailed information about where the syntax
    error occurred.

    The message indicating which exception occurred is always the last
    string in the list.

    """
    
    title = 'format_exception_only'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='etype'),
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.format_exception_only(self.input(0), self.input(1)))
        

class Getdoc_Node(NodeBase):
    """
    Get the doc string or comments for an object."""
    
    title = 'getdoc'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.getdoc(self.input(0)))
        

class Getpager_Node(NodeBase):
    """
    Decide what method to use for paging through text."""
    
    title = 'getpager'
    type_ = 'pydoc'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.getpager())
        

class Importfile_Node(NodeBase):
    """
    Import a Python source file or compiled file given its path."""
    
    title = 'importfile'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.importfile(self.input(0)))
        

class Isdata_Node(NodeBase):
    """
    Check if an object is of a type that probably means it's data."""
    
    title = 'isdata'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.isdata(self.input(0)))
        

class Ispackage_Node(NodeBase):
    """
    Guess whether a path refers to a package directory."""
    
    title = 'ispackage'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.ispackage(self.input(0)))
        

class Ispath_Node(NodeBase):
    """
    """
    
    title = 'ispath'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.ispath(self.input(0)))
        

class Locate_Node(NodeBase):
    """
    Locate an object by name or dotted path, importing as necessary."""
    
    title = 'locate'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='forceload', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.locate(self.input(0), self.input(1)))
        

class Pager_Node(NodeBase):
    """
    The first time this is called, determine what kind of pager to use."""
    
    title = 'pager'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='text'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.pager(self.input(0)))
        

class Pathdirs_Node(NodeBase):
    """
    Convert sys.path into a list of absolute, existing, unique paths."""
    
    title = 'pathdirs'
    type_ = 'pydoc'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.pathdirs())
        

class Pipepager_Node(NodeBase):
    """
    Page through text by feeding it to another program."""
    
    title = 'pipepager'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='text'),
        NodeInputBP(label='cmd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.pipepager(self.input(0), self.input(1)))
        

class Plain_Node(NodeBase):
    """
    Remove boldface formatting from text."""
    
    title = 'plain'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='text'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.plain(self.input(0)))
        

class Plainpager_Node(NodeBase):
    """
    Simply print unformatted text.  This is the ultimate fallback."""
    
    title = 'plainpager'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='text'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.plainpager(self.input(0)))
        

class Render_Doc_Node(NodeBase):
    """
    Render text documentation, given an object or a path to an object."""
    
    title = 'render_doc'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='thing'),
        NodeInputBP(label='title', dtype=dtypes.Data(default='Python Library Documentation: %s', size='s')),
        NodeInputBP(label='forceload', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='renderer', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.render_doc(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Replace_Node(NodeBase):
    """
    Do a series of global replacements on a string."""
    
    title = 'replace'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='text'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.replace(self.input(0)))
        

class Resolve_Node(NodeBase):
    """
    Given an object or a path to an object, get the object and its name."""
    
    title = 'resolve'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='thing'),
        NodeInputBP(label='forceload', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.resolve(self.input(0), self.input(1)))
        

class Safeimport_Node(NodeBase):
    """
    Import a module; handle errors; return None if the module isn't found.

    If the module *is* found but an exception occurs, it's wrapped in an
    ErrorDuringImport exception and reraised.  Unlike __import__, if a
    package path is specified, the module at the end of the path is returned,
    not the package at the beginning.  If the optional 'forceload' argument
    is 1, we reload the module from disk (unless it's a dynamic extension)."""
    
    title = 'safeimport'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='path'),
        NodeInputBP(label='forceload', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='cache', dtype=dtypes.Data(default={}, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.safeimport(self.input(0), self.input(1), self.input(2)))
        

class Sort_Attributes_Node(NodeBase):
    """
    Sort the attrs list in-place by _fields and then alphabetically by name"""
    
    title = 'sort_attributes'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='attrs'),
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.sort_attributes(self.input(0), self.input(1)))
        

class Source_Synopsis_Node(NodeBase):
    """
    """
    
    title = 'source_synopsis'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.source_synopsis(self.input(0)))
        

class Splitdoc_Node(NodeBase):
    """
    Split a doc string into a synopsis line (if any) and the rest."""
    
    title = 'splitdoc'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='doc'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.splitdoc(self.input(0)))
        

class Stripid_Node(NodeBase):
    """
    Remove the hexadecimal id from a Python object representation."""
    
    title = 'stripid'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='text'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.stripid(self.input(0)))
        

class Synopsis_Node(NodeBase):
    """
    Get the one-line summary out of a module file."""
    
    title = 'synopsis'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='cache', dtype=dtypes.Data(default={}, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.synopsis(self.input(0), self.input(1)))
        

class Tempfilepager_Node(NodeBase):
    """
    Page through text by invoking a program on a temporary file."""
    
    title = 'tempfilepager'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='text'),
        NodeInputBP(label='cmd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.tempfilepager(self.input(0), self.input(1)))
        

class Ttypager_Node(NodeBase):
    """
    Page through text on a text terminal."""
    
    title = 'ttypager'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='text'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.ttypager(self.input(0)))
        

class Visiblename_Node(NodeBase):
    """
    Decide whether to show documentation on a variable."""
    
    title = 'visiblename'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='all', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='obj', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.visiblename(self.input(0), self.input(1), self.input(2)))
        

class Writedoc_Node(NodeBase):
    """
    Write HTML documentation to a file in the current directory."""
    
    title = 'writedoc'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='thing'),
        NodeInputBP(label='forceload', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.writedoc(self.input(0), self.input(1)))
        

class Writedocs_Node(NodeBase):
    """
    Write out HTML documentation for all modules in a directory tree."""
    
    title = 'writedocs'
    type_ = 'pydoc'
    init_inputs = [
        NodeInputBP(label='dir'),
        NodeInputBP(label='pkgpath', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='done', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pydoc.writedocs(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    _Adjust_Cli_Sys_Path_Node,
    _Escape_Stdout_Node,
    _Findclass_Node,
    _Finddoc_Node,
    _Get_Revised_Path_Node,
    _Getdoc_Node,
    _Getowndoc_Node,
    _Is_Bound_Method_Node,
    _Split_List_Node,
    _Start_Server_Node,
    _Url_Handler_Node,
    Allmethods_Node,
    Apropos_Node,
    Browse_Node,
    Classify_Class_Attrs_Node,
    Classname_Node,
    Cli_Node,
    Cram_Node,
    Describe_Node,
    Doc_Node,
    Format_Exception_Only_Node,
    Getdoc_Node,
    Getpager_Node,
    Importfile_Node,
    Isdata_Node,
    Ispackage_Node,
    Ispath_Node,
    Locate_Node,
    Pager_Node,
    Pathdirs_Node,
    Pipepager_Node,
    Plain_Node,
    Plainpager_Node,
    Render_Doc_Node,
    Replace_Node,
    Resolve_Node,
    Safeimport_Node,
    Sort_Attributes_Node,
    Source_Synopsis_Node,
    Splitdoc_Node,
    Stripid_Node,
    Synopsis_Node,
    Tempfilepager_Node,
    Ttypager_Node,
    Visiblename_Node,
    Writedoc_Node,
    Writedocs_Node,
)
