import ryvencore_qt as rc
import pydoc


class AutoNode_pydoc__adjust_cli_sys_path(rc.Node):
    title = '_adjust_cli_sys_path'
    doc = '''Ensures current directory is on sys.path, and __main__ directory is not.

    Exception: __main__ dir is left alone if it's also pydoc's directory.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc._adjust_cli_sys_path())
        


class AutoNode_pydoc__escape_stdout(rc.Node):
    title = '_escape_stdout'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc._escape_stdout(self.input(0)))
        


class AutoNode_pydoc__get_revised_path(rc.Node):
    title = '_get_revised_path'
    doc = '''Ensures current directory is on returned path, and argv0 directory is not

    Exception: argv0 dir is left alone if it's also pydoc's directory.

    Returns a new path entry list, or None if no adjustment is needed.
    '''
    init_inputs = [
        rc.NodeInputBP(label='given_path'),
rc.NodeInputBP(label='argv0'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc._get_revised_path(self.input(0), self.input(1)))
        


class AutoNode_pydoc__is_bound_method(rc.Node):
    title = '_is_bound_method'
    doc = '''
    Returns True if fn is a bound method, regardless of whether
    fn was implemented in Python or in C.
    '''
    init_inputs = [
        rc.NodeInputBP(label='fn'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc._is_bound_method(self.input(0)))
        


class AutoNode_pydoc__split_list(rc.Node):
    title = '_split_list'
    doc = '''Split sequence s via predicate, and return pair ([true], [false]).

    The return value is a 2-tuple of lists,
        ([x for x in s if predicate(x)],
         [x for x in s if not predicate(x)])
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='predicate'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc._split_list(self.input(0), self.input(1)))
        


class AutoNode_pydoc__start_server(rc.Node):
    title = '_start_server'
    doc = '''Start an HTTP server thread on a specific port.

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
   '''
    init_inputs = [
        rc.NodeInputBP(label='urlhandler'),
rc.NodeInputBP(label='hostname'),
rc.NodeInputBP(label='port'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc._start_server(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_pydoc__url_handler(rc.Node):
    title = '_url_handler'
    doc = '''The pydoc url handler for use with the pydoc server.

    If the content_type is 'text/css', the _pydoc.css style
    sheet is read and returned if it exits.

    If the content_type is 'text/html', then the result of
    get_html_page(url) is returned.
    '''
    init_inputs = [
        rc.NodeInputBP(label='url'),
rc.NodeInputBP(label='content_type'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc._url_handler(self.input(0), self.input(1)))
        


class AutoNode_pydoc_allmethods(rc.Node):
    title = 'allmethods'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='cl'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.allmethods(self.input(0)))
        


class AutoNode_pydoc_apropos(rc.Node):
    title = 'apropos'
    doc = '''Print all the one-line module summaries that contain a substring.'''
    init_inputs = [
        rc.NodeInputBP(label='key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.apropos(self.input(0)))
        


class AutoNode_pydoc_browse(rc.Node):
    title = 'browse'
    doc = '''Start the enhanced pydoc Web server and open a Web browser.

    Use port '0' to start the server on an arbitrary port.
    Set open_browser to False to suppress opening a browser.
    '''
    init_inputs = [
        rc.NodeInputBP(label='port'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.browse(self.input(0)))
        


class AutoNode_pydoc_classify_class_attrs(rc.Node):
    title = 'classify_class_attrs'
    doc = '''Wrap inspect.classify_class_attrs, with fixup for data descriptors.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.classify_class_attrs(self.input(0)))
        


class AutoNode_pydoc_classname(rc.Node):
    title = 'classname'
    doc = '''Get a class name and qualify it with a module name if necessary.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
rc.NodeInputBP(label='modname'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.classname(self.input(0), self.input(1)))
        


class AutoNode_pydoc_cli(rc.Node):
    title = 'cli'
    doc = '''Command-line interface (looks at sys.argv to decide what to do).'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.cli())
        


class AutoNode_pydoc_cram(rc.Node):
    title = 'cram'
    doc = '''Omit part of a string if needed to make it fit in a maximum length.'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
rc.NodeInputBP(label='maxlen'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.cram(self.input(0), self.input(1)))
        


class AutoNode_pydoc_describe(rc.Node):
    title = 'describe'
    doc = '''Produce a short description of the given thing.'''
    init_inputs = [
        rc.NodeInputBP(label='thing'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.describe(self.input(0)))
        


class AutoNode_pydoc_doc(rc.Node):
    title = 'doc'
    doc = '''Display text documentation, given an object or a path to an object.'''
    init_inputs = [
        rc.NodeInputBP(label='thing'),
rc.NodeInputBP(label='title'),
rc.NodeInputBP(label='forceload'),
rc.NodeInputBP(label='output'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.doc(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_pydoc_format_exception_only(rc.Node):
    title = 'format_exception_only'
    doc = '''Format the exception part of a traceback.

    The arguments are the exception type and value such as given by
    sys.last_type and sys.last_value. The return value is a list of
    strings, each ending in a newline.

    Normally, the list contains a single string; however, for
    SyntaxError exceptions, it contains several lines that (when
    printed) display detailed information about where the syntax
    error occurred.

    The message indicating which exception occurred is always the last
    string in the list.

    '''
    init_inputs = [
        rc.NodeInputBP(label='etype'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.format_exception_only(self.input(0), self.input(1)))
        


class AutoNode_pydoc_getdoc(rc.Node):
    title = 'getdoc'
    doc = '''Get the doc string or comments for an object.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.getdoc(self.input(0)))
        


class AutoNode_pydoc_getpager(rc.Node):
    title = 'getpager'
    doc = '''Decide what method to use for paging through text.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.getpager())
        


class AutoNode_pydoc_importfile(rc.Node):
    title = 'importfile'
    doc = '''Import a Python source file or compiled file given its path.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.importfile(self.input(0)))
        


class AutoNode_pydoc_isdata(rc.Node):
    title = 'isdata'
    doc = '''Check if an object is of a type that probably means it's data.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.isdata(self.input(0)))
        


class AutoNode_pydoc_ispackage(rc.Node):
    title = 'ispackage'
    doc = '''Guess whether a path refers to a package directory.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.ispackage(self.input(0)))
        


class AutoNode_pydoc_ispath(rc.Node):
    title = 'ispath'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.ispath(self.input(0)))
        


class AutoNode_pydoc_locate(rc.Node):
    title = 'locate'
    doc = '''Locate an object by name or dotted path, importing as necessary.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='forceload'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.locate(self.input(0), self.input(1)))
        


class AutoNode_pydoc_pager(rc.Node):
    title = 'pager'
    doc = '''The first time this is called, determine what kind of pager to use.'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.pager(self.input(0)))
        


class AutoNode_pydoc_pathdirs(rc.Node):
    title = 'pathdirs'
    doc = '''Convert sys.path into a list of absolute, existing, unique paths.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.pathdirs())
        


class AutoNode_pydoc_pipepager(rc.Node):
    title = 'pipepager'
    doc = '''Page through text by feeding it to another program.'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
rc.NodeInputBP(label='cmd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.pipepager(self.input(0), self.input(1)))
        


class AutoNode_pydoc_plain(rc.Node):
    title = 'plain'
    doc = '''Remove boldface formatting from text.'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.plain(self.input(0)))
        


class AutoNode_pydoc_plainpager(rc.Node):
    title = 'plainpager'
    doc = '''Simply print unformatted text.  This is the ultimate fallback.'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.plainpager(self.input(0)))
        


class AutoNode_pydoc_render_doc(rc.Node):
    title = 'render_doc'
    doc = '''Render text documentation, given an object or a path to an object.'''
    init_inputs = [
        rc.NodeInputBP(label='thing'),
rc.NodeInputBP(label='title'),
rc.NodeInputBP(label='forceload'),
rc.NodeInputBP(label='renderer'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.render_doc(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_pydoc_replace(rc.Node):
    title = 'replace'
    doc = '''Do a series of global replacements on a string.'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.replace(self.input(0)))
        


class AutoNode_pydoc_resolve(rc.Node):
    title = 'resolve'
    doc = '''Given an object or a path to an object, get the object and its name.'''
    init_inputs = [
        rc.NodeInputBP(label='thing'),
rc.NodeInputBP(label='forceload'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.resolve(self.input(0), self.input(1)))
        


class AutoNode_pydoc_safeimport(rc.Node):
    title = 'safeimport'
    doc = '''Import a module; handle errors; return None if the module isn't found.

    If the module *is* found but an exception occurs, it's wrapped in an
    ErrorDuringImport exception and reraised.  Unlike __import__, if a
    package path is specified, the module at the end of the path is returned,
    not the package at the beginning.  If the optional 'forceload' argument
    is 1, we reload the module from disk (unless it's a dynamic extension).'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='forceload'),
rc.NodeInputBP(label='cache'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.safeimport(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_pydoc_sort_attributes(rc.Node):
    title = 'sort_attributes'
    doc = '''Sort the attrs list in-place by _fields and then alphabetically by name'''
    init_inputs = [
        rc.NodeInputBP(label='attrs'),
rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.sort_attributes(self.input(0), self.input(1)))
        


class AutoNode_pydoc_source_synopsis(rc.Node):
    title = 'source_synopsis'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.source_synopsis(self.input(0)))
        


class AutoNode_pydoc_splitdoc(rc.Node):
    title = 'splitdoc'
    doc = '''Split a doc string into a synopsis line (if any) and the rest.'''
    init_inputs = [
        rc.NodeInputBP(label='doc'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.splitdoc(self.input(0)))
        


class AutoNode_pydoc_stripid(rc.Node):
    title = 'stripid'
    doc = '''Remove the hexadecimal id from a Python object representation.'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.stripid(self.input(0)))
        


class AutoNode_pydoc_synopsis(rc.Node):
    title = 'synopsis'
    doc = '''Get the one-line summary out of a module file.'''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='cache'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.synopsis(self.input(0), self.input(1)))
        


class AutoNode_pydoc_tempfilepager(rc.Node):
    title = 'tempfilepager'
    doc = '''Page through text by invoking a program on a temporary file.'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
rc.NodeInputBP(label='cmd'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.tempfilepager(self.input(0), self.input(1)))
        


class AutoNode_pydoc_ttypager(rc.Node):
    title = 'ttypager'
    doc = '''Page through text on a text terminal.'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.ttypager(self.input(0)))
        


class AutoNode_pydoc_visiblename(rc.Node):
    title = 'visiblename'
    doc = '''Decide whether to show documentation on a variable.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='all'),
rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.visiblename(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_pydoc_writedoc(rc.Node):
    title = 'writedoc'
    doc = '''Write HTML documentation to a file in the current directory.'''
    init_inputs = [
        rc.NodeInputBP(label='thing'),
rc.NodeInputBP(label='forceload'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.writedoc(self.input(0), self.input(1)))
        


class AutoNode_pydoc_writedocs(rc.Node):
    title = 'writedocs'
    doc = '''Write out HTML documentation for all modules in a directory tree.'''
    init_inputs = [
        rc.NodeInputBP(label='dir'),
rc.NodeInputBP(label='pkgpath'),
rc.NodeInputBP(label='done'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pydoc.writedocs(self.input(0), self.input(1), self.input(2)))
        