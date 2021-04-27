
from NENV import *

import trace


class NodeBase(Node):
    pass


class _Find_Executable_Linenos_Node(NodeBase):
    title = '_find_executable_linenos'
    type_ = 'trace'
    doc = """Return dict where keys are line numbers in the line number table."""
    init_inputs = [
        NodeInputBP(label='filename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, trace._find_executable_linenos(self.input(0)))
        

class _Find_Lines_Node(NodeBase):
    title = '_find_lines'
    type_ = 'trace'
    doc = """Return lineno dict for all code objects reachable from code."""
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='strs'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, trace._find_lines(self.input(0), self.input(1)))
        

class _Find_Lines_From_Code_Node(NodeBase):
    title = '_find_lines_from_code'
    type_ = 'trace'
    doc = """Return dict where keys are lines in the line number table."""
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='strs'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, trace._find_lines_from_code(self.input(0), self.input(1)))
        

class _Find_Strings_Node(NodeBase):
    title = '_find_strings'
    type_ = 'trace'
    doc = """Return a dict of possible docstring positions.

    The dict maps line numbers to strings.  There is an entry for
    line that contains only a string or a part of a triple-quoted
    string.
    """
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='encoding', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, trace._find_strings(self.input(0), self.input(1)))
        

class _Fullmodname_Node(NodeBase):
    title = '_fullmodname'
    type_ = 'trace'
    doc = """Return a plausible module name for the path."""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, trace._fullmodname(self.input(0)))
        

class _Modname_Node(NodeBase):
    title = '_modname'
    type_ = 'trace'
    doc = """Return a plausible module name for the patch."""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, trace._modname(self.input(0)))
        

class Main_Node(NodeBase):
    title = 'main'
    type_ = 'trace'
    doc = """"""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, trace.main())
        


export_nodes(
    _Find_Executable_Linenos_Node,
    _Find_Lines_Node,
    _Find_Lines_From_Code_Node,
    _Find_Strings_Node,
    _Fullmodname_Node,
    _Modname_Node,
    Main_Node,
)
