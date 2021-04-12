import ryvencore_qt as rc
import cgi


class AutoNode_cgi__parseparam(rc.Node):
    title = '_parseparam'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi._parseparam(self.input(0)))
        


class AutoNode_cgi_closelog(rc.Node):
    title = 'closelog'
    description = '''Close the log file.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.closelog())
        


class AutoNode_cgi_dolog(rc.Node):
    title = 'dolog'
    description = '''Write a log message to the log file.  See initlog() for docs.'''
    init_inputs = [
        rc.NodeInputBP(label='fmt'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.dolog(self.input(0)))
        


class AutoNode_cgi_initlog(rc.Node):
    title = 'initlog'
    description = '''Write a log message, if there is a log file.

    Even though this function is called initlog(), you should always
    use log(); log is a variable that is set either to initlog
    (initially), to dolog (once the log file has been opened), or to
    nolog (when logging is disabled).

    The first argument is a format string; the remaining arguments (if
    any) are arguments to the % operator, so e.g.
        log("%s: %s", "a", "b")
    will write "a: b" to the log file, followed by a newline.

    If the global logfp is not None, it should be a file object to
    which log data is written.

    If the global logfp is None, the global logfile may be a string
    giving a filename to open, in append mode.  This file should be
    world writable!!!  If the file can't be opened, logging is
    silently disabled (since there is no safe place where we could
    send an error message).

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.initlog())
        


class AutoNode_cgi_log(rc.Node):
    title = 'log'
    description = '''Write a log message, if there is a log file.

    Even though this function is called initlog(), you should always
    use log(); log is a variable that is set either to initlog
    (initially), to dolog (once the log file has been opened), or to
    nolog (when logging is disabled).

    The first argument is a format string; the remaining arguments (if
    any) are arguments to the % operator, so e.g.
        log("%s: %s", "a", "b")
    will write "a: b" to the log file, followed by a newline.

    If the global logfp is not None, it should be a file object to
    which log data is written.

    If the global logfp is None, the global logfile may be a string
    giving a filename to open, in append mode.  This file should be
    world writable!!!  If the file can't be opened, logging is
    silently disabled (since there is no safe place where we could
    send an error message).

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.log())
        


class AutoNode_cgi_nolog(rc.Node):
    title = 'nolog'
    description = '''Dummy function, assigned to log when logging is disabled.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.nolog())
        


class AutoNode_cgi_parse(rc.Node):
    title = 'parse'
    description = '''Parse a query in the environment or from a file (default stdin)

        Arguments, all optional:

        fp              : file pointer; default: sys.stdin.buffer

        environ         : environment dictionary; default: os.environ

        keep_blank_values: flag indicating whether blank values in
            percent-encoded forms should be treated as blank strings.
            A true value indicates that blanks should be retained as
            blank strings.  The default false value indicates that
            blank values are to be ignored and treated as if they were
            not included.

        strict_parsing: flag indicating what to do with parsing errors.
            If false (the default), errors are silently ignored.
            If true, errors raise a ValueError exception.
    '''
    init_inputs = [
        rc.NodeInputBP(label='fp'),
rc.NodeInputBP(label='environ'),
rc.NodeInputBP(label='keep_blank_values'),
rc.NodeInputBP(label='strict_parsing'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.parse(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_cgi_parse_header(rc.Node):
    title = 'parse_header'
    description = '''Parse a Content-type like header.

    Return the main content-type and a dictionary of options.

    '''
    init_inputs = [
        rc.NodeInputBP(label='line'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.parse_header(self.input(0)))
        


class AutoNode_cgi_parse_multipart(rc.Node):
    title = 'parse_multipart'
    description = '''Parse multipart input.

    Arguments:
    fp   : input file
    pdict: dictionary containing other parameters of content-type header
    encoding, errors: request encoding and error handler, passed to
        FieldStorage

    Returns a dictionary just like parse_qs(): keys are the field names, each
    value is a list of values for that field. For non-file fields, the value
    is a list of strings.
    '''
    init_inputs = [
        rc.NodeInputBP(label='fp'),
rc.NodeInputBP(label='pdict'),
rc.NodeInputBP(label='encoding'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.parse_multipart(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_cgi_print_arguments(rc.Node):
    title = 'print_arguments'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.print_arguments())
        


class AutoNode_cgi_print_directory(rc.Node):
    title = 'print_directory'
    description = '''Dump the current directory as HTML.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.print_directory())
        


class AutoNode_cgi_print_environ(rc.Node):
    title = 'print_environ'
    description = '''Dump the shell environment as HTML.'''
    init_inputs = [
        rc.NodeInputBP(label='environ'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.print_environ(self.input(0)))
        


class AutoNode_cgi_print_environ_usage(rc.Node):
    title = 'print_environ_usage'
    description = '''Dump a list of environment variables used by CGI as HTML.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.print_environ_usage())
        


class AutoNode_cgi_print_exception(rc.Node):
    title = 'print_exception'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='type'),
rc.NodeInputBP(label='value'),
rc.NodeInputBP(label='tb'),
rc.NodeInputBP(label='limit'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.print_exception(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_cgi_print_form(rc.Node):
    title = 'print_form'
    description = '''Dump the contents of a form as HTML.'''
    init_inputs = [
        rc.NodeInputBP(label='form'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.print_form(self.input(0)))
        


class AutoNode_cgi_test(rc.Node):
    title = 'test'
    description = '''Robust test CGI script, usable as main program.

    Write minimal HTTP headers and dump all information provided to
    the script in HTML form.

    '''
    init_inputs = [
        rc.NodeInputBP(label='environ'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.test(self.input(0)))
        


class AutoNode_cgi_valid_boundary(rc.Node):
    title = 'valid_boundary'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgi.valid_boundary(self.input(0)))
        