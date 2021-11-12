
from ryven.NENV import *

import fnmatch


class NodeBase(Node):
    pass


class Filter_Node(NodeBase):
    """
    Construct a list from those elements of the iterable NAMES that match PAT."""
    
    title = 'filter'
    type_ = 'fnmatch'
    init_inputs = [
        NodeInputBP(label='names'),
        NodeInputBP(label='pat'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fnmatch.filter(self.input(0), self.input(1)))
        

class Fnmatch_Node(NodeBase):
    """
    Test whether FILENAME matches PATTERN.

    Patterns are Unix shell style:

    *       matches everything
    ?       matches any single character
    [seq]   matches any character in seq
    [!seq]  matches any char not in seq

    An initial period in FILENAME is not special.
    Both FILENAME and PATTERN are first case-normalized
    if the operating system requires it.
    If you don't want this, use fnmatchcase(FILENAME, PATTERN).
    """
    
    title = 'fnmatch'
    type_ = 'fnmatch'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='pat'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fnmatch.fnmatch(self.input(0), self.input(1)))
        

class Fnmatchcase_Node(NodeBase):
    """
    Test whether FILENAME matches PATTERN, including case.

    This is a version of fnmatch() which doesn't case-normalize
    its arguments.
    """
    
    title = 'fnmatchcase'
    type_ = 'fnmatch'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='pat'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fnmatch.fnmatchcase(self.input(0), self.input(1)))
        

class Translate_Node(NodeBase):
    """
    Translate a shell PATTERN to a regular expression.

    There is no way to quote meta-characters.
    """
    
    title = 'translate'
    type_ = 'fnmatch'
    init_inputs = [
        NodeInputBP(label='pat'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, fnmatch.translate(self.input(0)))
        


export_nodes(
    Filter_Node,
    Fnmatch_Node,
    Fnmatchcase_Node,
    Translate_Node,
)
