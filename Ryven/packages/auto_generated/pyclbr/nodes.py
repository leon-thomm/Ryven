
from NENV import *

import pyclbr


class NodeBase(Node):
    pass


class _Create_Tree_Node(NodeBase):
    """
    Return the tree for a particular module.

    fullmodule (full module name), inpackage+module, becomes o.module.
    path is passed to recursive calls of _readmodule.
    fname becomes o.file.
    source is tokenized.  Imports cause recursive calls to _readmodule.
    tree is {} or {'__path__': <submodule search locations>}.
    inpackage, None or string, is passed to recursive calls of _readmodule.

    The effect of recursive calls is mutation of global _modules.
    """
    
    title = '_create_tree'
    type_ = 'pyclbr'
    init_inputs = [
        NodeInputBP(label='fullmodule'),
        NodeInputBP(label='path'),
        NodeInputBP(label='fname'),
        NodeInputBP(label='source'),
        NodeInputBP(label='tree'),
        NodeInputBP(label='inpackage'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pyclbr._create_tree(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class _Getname_Node(NodeBase):
    """
    Return (dotted-name or None, next-token) tuple for token source g."""
    
    title = '_getname'
    type_ = 'pyclbr'
    init_inputs = [
        NodeInputBP(label='g'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pyclbr._getname(self.input(0)))
        

class _Getnamelist_Node(NodeBase):
    """
    Return list of (dotted-name, as-name or None) tuples for token source g.

    An as-name is the name that follows 'as' in an as clause.
    """
    
    title = '_getnamelist'
    type_ = 'pyclbr'
    init_inputs = [
        NodeInputBP(label='g'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pyclbr._getnamelist(self.input(0)))
        

class _Main_Node(NodeBase):
    """
    Print module output (default this file) for quick visual check."""
    
    title = '_main'
    type_ = 'pyclbr'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pyclbr._main())
        

class _Nest_Class_Node(NodeBase):
    """
    Return a Class after nesting within ob."""
    
    title = '_nest_class'
    type_ = 'pyclbr'
    init_inputs = [
        NodeInputBP(label='ob'),
        NodeInputBP(label='class_name'),
        NodeInputBP(label='lineno'),
        NodeInputBP(label='super', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pyclbr._nest_class(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Nest_Function_Node(NodeBase):
    """
    Return a Function after nesting within ob."""
    
    title = '_nest_function'
    type_ = 'pyclbr'
    init_inputs = [
        NodeInputBP(label='ob'),
        NodeInputBP(label='func_name'),
        NodeInputBP(label='lineno'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pyclbr._nest_function(self.input(0), self.input(1), self.input(2)))
        

class _Readmodule_Node(NodeBase):
    """
    Do the hard work for readmodule[_ex].

    If inpackage is given, it must be the dotted name of the package in
    which we are searching for a submodule, and then PATH must be the
    package search path; otherwise, we are searching for a top-level
    module, and path is combined with sys.path.
    """
    
    title = '_readmodule'
    type_ = 'pyclbr'
    init_inputs = [
        NodeInputBP(label='module'),
        NodeInputBP(label='path'),
        NodeInputBP(label='inpackage', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pyclbr._readmodule(self.input(0), self.input(1), self.input(2)))
        

class Readmodule_Node(NodeBase):
    """
    Return Class objects for the top-level classes in module.

    This is the original interface, before Functions were added.
    """
    
    title = 'readmodule'
    type_ = 'pyclbr'
    init_inputs = [
        NodeInputBP(label='module'),
        NodeInputBP(label='path', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pyclbr.readmodule(self.input(0), self.input(1)))
        

class Readmodule_Ex_Node(NodeBase):
    """
    Return a dictionary with all functions and classes in module.

    Search for module in PATH + sys.path.
    If possible, include imported superclasses.
    Do this by reading source, without importing (and executing) it.
    """
    
    title = 'readmodule_ex'
    type_ = 'pyclbr'
    init_inputs = [
        NodeInputBP(label='module'),
        NodeInputBP(label='path', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, pyclbr.readmodule_ex(self.input(0), self.input(1)))
        


export_nodes(
    _Create_Tree_Node,
    _Getname_Node,
    _Getnamelist_Node,
    _Main_Node,
    _Nest_Class_Node,
    _Nest_Function_Node,
    _Readmodule_Node,
    Readmodule_Node,
    Readmodule_Ex_Node,
)
