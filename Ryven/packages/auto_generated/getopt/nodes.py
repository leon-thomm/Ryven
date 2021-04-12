import ryvencore_qt as rc
import getopt


class AutoNode_getopt__(rc.Node):
    title = '_'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='message'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, getopt._(self.input(0)))
        


class AutoNode_getopt_do_longs(rc.Node):
    title = 'do_longs'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='opts'),
rc.NodeInputBP(label='opt'),
rc.NodeInputBP(label='longopts'),
rc.NodeInputBP(label='args'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, getopt.do_longs(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_getopt_do_shorts(rc.Node):
    title = 'do_shorts'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='opts'),
rc.NodeInputBP(label='optstring'),
rc.NodeInputBP(label='shortopts'),
rc.NodeInputBP(label='args'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, getopt.do_shorts(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_getopt_getopt(rc.Node):
    title = 'getopt'
    description = '''getopt(args, options[, long_options]) -> opts, args

    Parses command line options and parameter list.  args is the
    argument list to be parsed, without the leading reference to the
    running program.  Typically, this means "sys.argv[1:]".  shortopts
    is the string of option letters that the script wants to
    recognize, with options that require an argument followed by a
    colon (i.e., the same format that Unix getopt() uses).  If
    specified, longopts is a list of strings with the names of the
    long options which should be supported.  The leading '--'
    characters should not be included in the option name.  Options
    which require an argument should be followed by an equal sign
    ('=').

    The return value consists of two elements: the first is a list of
    (option, value) pairs; the second is the list of program arguments
    left after the option list was stripped (this is a trailing slice
    of the first argument).  Each option-and-value pair returned has
    the option as its first element, prefixed with a hyphen (e.g.,
    '-x'), and the option argument as its second element, or an empty
    string if the option has no argument.  The options occur in the
    list in the same order in which they were found, thus allowing
    multiple occurrences.  Long and short options may be mixed.

    '''
    init_inputs = [
        rc.NodeInputBP(label='args'),
rc.NodeInputBP(label='shortopts'),
rc.NodeInputBP(label='longopts'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, getopt.getopt(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_getopt_gnu_getopt(rc.Node):
    title = 'gnu_getopt'
    description = '''getopt(args, options[, long_options]) -> opts, args

    This function works like getopt(), except that GNU style scanning
    mode is used by default. This means that option and non-option
    arguments may be intermixed. The getopt() function stops
    processing options as soon as a non-option argument is
    encountered.

    If the first character of the option string is `+', or if the
    environment variable POSIXLY_CORRECT is set, then option
    processing stops as soon as a non-option argument is encountered.

    '''
    init_inputs = [
        rc.NodeInputBP(label='args'),
rc.NodeInputBP(label='shortopts'),
rc.NodeInputBP(label='longopts'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, getopt.gnu_getopt(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_getopt_long_has_args(rc.Node):
    title = 'long_has_args'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='opt'),
rc.NodeInputBP(label='longopts'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, getopt.long_has_args(self.input(0), self.input(1)))
        


class AutoNode_getopt_short_has_arg(rc.Node):
    title = 'short_has_arg'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='opt'),
rc.NodeInputBP(label='shortopts'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, getopt.short_has_arg(self.input(0), self.input(1)))
        