
from NENV import *

import re


class NodeBase(Node):
    pass


class _Compile_Node(NodeBase):
    """
    """
    
    title = '_compile'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='flags'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re._compile(self.input(0), self.input(1)))
        

class _Expand_Node(NodeBase):
    """
    """
    
    title = '_expand'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='match'),
        NodeInputBP(label='template'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re._expand(self.input(0), self.input(1), self.input(2)))
        

class _Pickle_Node(NodeBase):
    """
    """
    
    title = '_pickle'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='p'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re._pickle(self.input(0)))
        

class _Subx_Node(NodeBase):
    """
    """
    
    title = '_subx'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='template'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re._subx(self.input(0), self.input(1)))
        

class Compile_Node(NodeBase):
    """
    Compile a regular expression pattern, returning a Pattern object."""
    
    title = 'compile'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re.compile(self.input(0), self.input(1)))
        

class Escape_Node(NodeBase):
    """
    
    Escape special characters in a string.
    """
    
    title = 'escape'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re.escape(self.input(0)))
        

class Findall_Node(NodeBase):
    """
    Return a list of all non-overlapping matches in the string.

    If one or more capturing groups are present in the pattern, return
    a list of groups; this will be a list of tuples if the pattern
    has more than one group.

    Empty matches are included in the result."""
    
    title = 'findall'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='string'),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re.findall(self.input(0), self.input(1), self.input(2)))
        

class Finditer_Node(NodeBase):
    """
    Return an iterator over all non-overlapping matches in the
    string.  For each match, the iterator returns a Match object.

    Empty matches are included in the result."""
    
    title = 'finditer'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='string'),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re.finditer(self.input(0), self.input(1), self.input(2)))
        

class Fullmatch_Node(NodeBase):
    """
    Try to apply the pattern to all of the string, returning
    a Match object, or None if no match was found."""
    
    title = 'fullmatch'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='string'),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re.fullmatch(self.input(0), self.input(1), self.input(2)))
        

class Match_Node(NodeBase):
    """
    Try to apply the pattern at the start of the string, returning
    a Match object, or None if no match was found."""
    
    title = 'match'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='string'),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re.match(self.input(0), self.input(1), self.input(2)))
        

class Purge_Node(NodeBase):
    """
    Clear the regular expression caches"""
    
    title = 'purge'
    type_ = 're'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re.purge())
        

class Search_Node(NodeBase):
    """
    Scan through string looking for a match to the pattern, returning
    a Match object, or None if no match was found."""
    
    title = 'search'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='string'),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re.search(self.input(0), self.input(1), self.input(2)))
        

class Split_Node(NodeBase):
    """
    Split the source string by the occurrences of the pattern,
    returning a list containing the resulting substrings.  If
    capturing parentheses are used in pattern, then the text of all
    groups in the pattern are also returned as part of the resulting
    list.  If maxsplit is nonzero, at most maxsplit splits occur,
    and the remainder of the string is returned as the final element
    of the list."""
    
    title = 'split'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='string'),
        NodeInputBP(label='maxsplit', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re.split(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Sub_Node(NodeBase):
    """
    Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the Match object and must return
    a replacement string to be used."""
    
    title = 'sub'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='repl'),
        NodeInputBP(label='string'),
        NodeInputBP(label='count', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re.sub(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Subn_Node(NodeBase):
    """
    Return a 2-tuple containing (new_string, number).
    new_string is the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in the source
    string by the replacement repl.  number is the number of
    substitutions that were made. repl can be either a string or a
    callable; if a string, backslash escapes in it are processed.
    If it is a callable, it's passed the Match object and must
    return a replacement string to be used."""
    
    title = 'subn'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='repl'),
        NodeInputBP(label='string'),
        NodeInputBP(label='count', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re.subn(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Template_Node(NodeBase):
    """
    Compile a template pattern, returning a Pattern object"""
    
    title = 'template'
    type_ = 're'
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='flags', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, re.template(self.input(0), self.input(1)))
        


export_nodes(
    _Compile_Node,
    _Expand_Node,
    _Pickle_Node,
    _Subx_Node,
    Compile_Node,
    Escape_Node,
    Findall_Node,
    Finditer_Node,
    Fullmatch_Node,
    Match_Node,
    Purge_Node,
    Search_Node,
    Split_Node,
    Sub_Node,
    Subn_Node,
    Template_Node,
)
