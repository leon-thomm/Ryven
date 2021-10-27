
from NENV import *

import traceback


class NodeBase(Node):
    pass


class _Format_Final_Exc_Line_Node(NodeBase):
    """
    """
    
    title = '_format_final_exc_line'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='etype'),
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback._format_final_exc_line(self.input(0), self.input(1)))
        

class _Some_Str_Node(NodeBase):
    """
    """
    
    title = '_some_str'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback._some_str(self.input(0)))
        

class Clear_Frames_Node(NodeBase):
    """
    Clear all references to local variables in the frames of a traceback."""
    
    title = 'clear_frames'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='tb'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.clear_frames(self.input(0)))
        

class Extract_Stack_Node(NodeBase):
    """
    Extract the raw traceback from the current stack frame.

    The return value has the same format as for extract_tb().  The
    optional 'f' and 'limit' arguments have the same meaning as for
    print_stack().  Each item in the list is a quadruple (filename,
    line number, function name, text), and the entries are in order
    from oldest to newest stack frame.
    """
    
    title = 'extract_stack'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='f', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='limit', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.extract_stack(self.input(0), self.input(1)))
        

class Extract_Tb_Node(NodeBase):
    """
    
    Return a StackSummary object representing a list of
    pre-processed entries from traceback.

    This is useful for alternate formatting of stack traces.  If
    'limit' is omitted or None, all entries are extracted.  A
    pre-processed stack trace entry is a FrameSummary object
    containing attributes filename, lineno, name, and line
    representing the information that is usually printed for a stack
    trace.  The line is a string with leading and trailing
    whitespace stripped; if the source is not available it is None.
    """
    
    title = 'extract_tb'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='tb'),
        NodeInputBP(label='limit', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.extract_tb(self.input(0), self.input(1)))
        

class Format_Exc_Node(NodeBase):
    """
    Like print_exc() but return a string."""
    
    title = 'format_exc'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='limit', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='chain', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.format_exc(self.input(0), self.input(1)))
        

class Format_Exception_Node(NodeBase):
    """
    Format a stack trace and the exception information.

    The arguments have the same meaning as the corresponding arguments
    to print_exception().  The return value is a list of strings, each
    ending in a newline and some containing internal newlines.  When
    these lines are concatenated and printed, exactly the same text is
    printed as does print_exception().
    """
    
    title = 'format_exception'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='etype'),
        NodeInputBP(label='value'),
        NodeInputBP(label='tb'),
        NodeInputBP(label='limit', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='chain', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.format_exception(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

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
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='etype'),
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.format_exception_only(self.input(0), self.input(1)))
        

class Format_List_Node(NodeBase):
    """
    Format a list of tuples or FrameSummary objects for printing.

    Given a list of tuples or FrameSummary objects as returned by
    extract_tb() or extract_stack(), return a list of strings ready
    for printing.

    Each string in the resulting list corresponds to the item with the
    same index in the argument list.  Each string ends in a newline;
    the strings may contain internal newlines as well, for those items
    whose source text line is not None.
    """
    
    title = 'format_list'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='extracted_list'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.format_list(self.input(0)))
        

class Format_Stack_Node(NodeBase):
    """
    Shorthand for 'format_list(extract_stack(f, limit))'."""
    
    title = 'format_stack'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='f', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='limit', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.format_stack(self.input(0), self.input(1)))
        

class Format_Tb_Node(NodeBase):
    """
    A shorthand for 'format_list(extract_tb(tb, limit))'."""
    
    title = 'format_tb'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='tb'),
        NodeInputBP(label='limit', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.format_tb(self.input(0), self.input(1)))
        

class Print_Exc_Node(NodeBase):
    """
    Shorthand for 'print_exception(*sys.exc_info(), limit, file)'."""
    
    title = 'print_exc'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='limit', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='file', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='chain', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.print_exc(self.input(0), self.input(1), self.input(2)))
        

class Print_Exception_Node(NodeBase):
    """
    Print exception up to 'limit' stack trace entries from 'tb' to 'file'.

    This differs from print_tb() in the following ways: (1) if
    traceback is not None, it prints a header "Traceback (most recent
    call last):"; (2) it prints the exception type and value after the
    stack trace; (3) if type is SyntaxError and value has the
    appropriate format, it prints the line where the syntax error
    occurred with a caret on the next line indicating the approximate
    position of the error.
    """
    
    title = 'print_exception'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='etype'),
        NodeInputBP(label='value'),
        NodeInputBP(label='tb'),
        NodeInputBP(label='limit', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='file', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='chain', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.print_exception(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class Print_Last_Node(NodeBase):
    """
    This is a shorthand for 'print_exception(sys.last_type,
    sys.last_value, sys.last_traceback, limit, file)'."""
    
    title = 'print_last'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='limit', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='file', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='chain', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.print_last(self.input(0), self.input(1), self.input(2)))
        

class Print_List_Node(NodeBase):
    """
    Print the list of tuples as returned by extract_tb() or
    extract_stack() as a formatted stack trace to the given file."""
    
    title = 'print_list'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='extracted_list'),
        NodeInputBP(label='file', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.print_list(self.input(0), self.input(1)))
        

class Print_Stack_Node(NodeBase):
    """
    Print a stack trace from its invocation point.

    The optional 'f' argument can be used to specify an alternate
    stack frame at which to start. The optional 'limit' and 'file'
    arguments have the same meaning as for print_exception().
    """
    
    title = 'print_stack'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='f', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='limit', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='file', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.print_stack(self.input(0), self.input(1), self.input(2)))
        

class Print_Tb_Node(NodeBase):
    """
    Print up to 'limit' stack trace entries from the traceback 'tb'.

    If 'limit' is omitted or None, all entries are printed.  If 'file'
    is omitted or None, the output goes to sys.stderr; otherwise
    'file' should be an open file or file-like object with a write()
    method.
    """
    
    title = 'print_tb'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='tb'),
        NodeInputBP(label='limit', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='file', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.print_tb(self.input(0), self.input(1), self.input(2)))
        

class Walk_Stack_Node(NodeBase):
    """
    Walk a stack yielding the frame and line number for each frame.

    This will follow f.f_back from the given frame. If no frame is given, the
    current stack is used. Usually used with StackSummary.extract.
    """
    
    title = 'walk_stack'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='f'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.walk_stack(self.input(0)))
        

class Walk_Tb_Node(NodeBase):
    """
    Walk a traceback yielding the frame and line number for each frame.

    This will follow tb.tb_next (and thus is in the opposite order to
    walk_stack). Usually used with StackSummary.extract.
    """
    
    title = 'walk_tb'
    type_ = 'traceback'
    init_inputs = [
        NodeInputBP(label='tb'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, traceback.walk_tb(self.input(0)))
        


export_nodes(
    _Format_Final_Exc_Line_Node,
    _Some_Str_Node,
    Clear_Frames_Node,
    Extract_Stack_Node,
    Extract_Tb_Node,
    Format_Exc_Node,
    Format_Exception_Node,
    Format_Exception_Only_Node,
    Format_List_Node,
    Format_Stack_Node,
    Format_Tb_Node,
    Print_Exc_Node,
    Print_Exception_Node,
    Print_Last_Node,
    Print_List_Node,
    Print_Stack_Node,
    Print_Tb_Node,
    Walk_Stack_Node,
    Walk_Tb_Node,
)
