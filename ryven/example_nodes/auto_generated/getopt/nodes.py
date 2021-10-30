
from ryven.NENV import *

import getopt


class NodeBase(Node):
    pass


class __Node(NodeBase):
    """
    """
    
    title = '_'
    type_ = 'getopt'
    init_inputs = [
        NodeInputBP(label='message'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, getopt._(self.input(0)))
        

class Do_Longs_Node(NodeBase):
    """
    """
    
    title = 'do_longs'
    type_ = 'getopt'
    init_inputs = [
        NodeInputBP(label='opts'),
        NodeInputBP(label='opt'),
        NodeInputBP(label='longopts'),
        NodeInputBP(label='args'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, getopt.do_longs(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Do_Shorts_Node(NodeBase):
    """
    """
    
    title = 'do_shorts'
    type_ = 'getopt'
    init_inputs = [
        NodeInputBP(label='opts'),
        NodeInputBP(label='optstring'),
        NodeInputBP(label='shortopts'),
        NodeInputBP(label='args'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, getopt.do_shorts(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Getopt_Node(NodeBase):
    """
    getopt(args, options[, long_options]) -> opts, args

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

    """
    
    title = 'getopt'
    type_ = 'getopt'
    init_inputs = [
        NodeInputBP(label='args'),
        NodeInputBP(label='shortopts'),
        NodeInputBP(label='longopts', dtype=dtypes.Data(default=[], size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, getopt.getopt(self.input(0), self.input(1), self.input(2)))
        

class Gnu_Getopt_Node(NodeBase):
    """
    getopt(args, options[, long_options]) -> opts, args

    This function works like getopt(), except that GNU style scanning
    mode is used by default. This means that option and non-option
    arguments may be intermixed. The getopt() function stops
    processing options as soon as a non-option argument is
    encountered.

    If the first character of the option string is `+', or if the
    environment variable POSIXLY_CORRECT is set, then option
    processing stops as soon as a non-option argument is encountered.

    """
    
    title = 'gnu_getopt'
    type_ = 'getopt'
    init_inputs = [
        NodeInputBP(label='args'),
        NodeInputBP(label='shortopts'),
        NodeInputBP(label='longopts', dtype=dtypes.Data(default=[], size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, getopt.gnu_getopt(self.input(0), self.input(1), self.input(2)))
        

class Long_Has_Args_Node(NodeBase):
    """
    """
    
    title = 'long_has_args'
    type_ = 'getopt'
    init_inputs = [
        NodeInputBP(label='opt'),
        NodeInputBP(label='longopts'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, getopt.long_has_args(self.input(0), self.input(1)))
        

class Short_Has_Arg_Node(NodeBase):
    """
    """
    
    title = 'short_has_arg'
    type_ = 'getopt'
    init_inputs = [
        NodeInputBP(label='opt'),
        NodeInputBP(label='shortopts'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, getopt.short_has_arg(self.input(0), self.input(1)))
        


export_nodes(
    __Node,
    Do_Longs_Node,
    Do_Shorts_Node,
    Getopt_Node,
    Gnu_Getopt_Node,
    Long_Has_Args_Node,
    Short_Has_Arg_Node,
)
