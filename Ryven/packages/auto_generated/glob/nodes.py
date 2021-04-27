
from NENV import *

import glob


class NodeBase(Node):
    pass


class _Glob0_Node(NodeBase):
    title = '_glob0'
    type_ = 'glob'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='dirname'),
        NodeInputBP(label='basename'),
        NodeInputBP(label='dironly'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._glob0(self.input(0), self.input(1), self.input(2)))
        

class _Glob1_Node(NodeBase):
    title = '_glob1'
    type_ = 'glob'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='dirname'),
        NodeInputBP(label='pattern'),
        NodeInputBP(label='dironly'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._glob1(self.input(0), self.input(1), self.input(2)))
        

class _Glob2_Node(NodeBase):
    title = '_glob2'
    type_ = 'glob'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='dirname'),
        NodeInputBP(label='pattern'),
        NodeInputBP(label='dironly'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._glob2(self.input(0), self.input(1), self.input(2)))
        

class _Iglob_Node(NodeBase):
    title = '_iglob'
    type_ = 'glob'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='pathname'),
        NodeInputBP(label='recursive'),
        NodeInputBP(label='dironly'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._iglob(self.input(0), self.input(1), self.input(2)))
        

class _Ishidden_Node(NodeBase):
    title = '_ishidden'
    type_ = 'glob'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='path'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._ishidden(self.input(0)))
        

class _Isrecursive_Node(NodeBase):
    title = '_isrecursive'
    type_ = 'glob'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='pattern'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._isrecursive(self.input(0)))
        

class _Iterdir_Node(NodeBase):
    title = '_iterdir'
    type_ = 'glob'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='dirname'),
        NodeInputBP(label='dironly'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._iterdir(self.input(0), self.input(1)))
        

class _Rlistdir_Node(NodeBase):
    title = '_rlistdir'
    type_ = 'glob'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='dirname'),
        NodeInputBP(label='dironly'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._rlistdir(self.input(0), self.input(1)))
        

class Escape_Node(NodeBase):
    title = 'escape'
    type_ = 'glob'
    doc = """Escape all special characters.
    """
    init_inputs = [
        NodeInputBP(label='pathname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob.escape(self.input(0)))
        

class Glob_Node(NodeBase):
    title = 'glob'
    type_ = 'glob'
    doc = """Return a list of paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    """
    init_inputs = [
        NodeInputBP(label='pathname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob.glob(self.input(0)))
        

class Glob0_Node(NodeBase):
    title = 'glob0'
    type_ = 'glob'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='dirname'),
        NodeInputBP(label='pattern'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob.glob0(self.input(0), self.input(1)))
        

class Glob1_Node(NodeBase):
    title = 'glob1'
    type_ = 'glob'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='dirname'),
        NodeInputBP(label='pattern'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob.glob1(self.input(0), self.input(1)))
        

class Has_Magic_Node(NodeBase):
    title = 'has_magic'
    type_ = 'glob'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob.has_magic(self.input(0)))
        

class Iglob_Node(NodeBase):
    title = 'iglob'
    type_ = 'glob'
    doc = """Return an iterator which yields the paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    """
    init_inputs = [
        NodeInputBP(label='pathname'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob.iglob(self.input(0)))
        


export_nodes(
    _Glob0_Node,
    _Glob1_Node,
    _Glob2_Node,
    _Iglob_Node,
    _Ishidden_Node,
    _Isrecursive_Node,
    _Iterdir_Node,
    _Rlistdir_Node,
    Escape_Node,
    Glob_Node,
    Glob0_Node,
    Glob1_Node,
    Has_Magic_Node,
    Iglob_Node,
)
