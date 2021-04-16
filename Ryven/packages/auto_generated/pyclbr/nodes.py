import ryvencore_qt as rc
import pyclbr


class AutoNode_pyclbr__create_tree(rc.Node):
    title = '_create_tree'
    doc = '''Return the tree for a particular module.

    fullmodule (full module name), inpackage+module, becomes o.module.
    path is passed to recursive calls of _readmodule.
    fname becomes o.file.
    source is tokenized.  Imports cause recursive calls to _readmodule.
    tree is {} or {'__path__': <submodule search locations>}.
    inpackage, None or string, is passed to recursive calls of _readmodule.

    The effect of recursive calls is mutation of global _modules.
    '''
    init_inputs = [
        rc.NodeInputBP(label='fullmodule'),
rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='fname'),
rc.NodeInputBP(label='source'),
rc.NodeInputBP(label='tree'),
rc.NodeInputBP(label='inpackage'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pyclbr._create_tree(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode_pyclbr__getname(rc.Node):
    title = '_getname'
    doc = '''Return (dotted-name or None, next-token) tuple for token source g.'''
    init_inputs = [
        rc.NodeInputBP(label='g'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pyclbr._getname(self.input(0)))
        


class AutoNode_pyclbr__getnamelist(rc.Node):
    title = '_getnamelist'
    doc = '''Return list of (dotted-name, as-name or None) tuples for token source g.

    An as-name is the name that follows 'as' in an as clause.
    '''
    init_inputs = [
        rc.NodeInputBP(label='g'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pyclbr._getnamelist(self.input(0)))
        


class AutoNode_pyclbr__main(rc.Node):
    title = '_main'
    doc = '''Print module output (default this file) for quick visual check.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pyclbr._main())
        


class AutoNode_pyclbr__nest_class(rc.Node):
    title = '_nest_class'
    doc = '''Return a Class after nesting within ob.'''
    init_inputs = [
        rc.NodeInputBP(label='ob'),
rc.NodeInputBP(label='class_name'),
rc.NodeInputBP(label='lineno'),
rc.NodeInputBP(label='super'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pyclbr._nest_class(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_pyclbr__nest_function(rc.Node):
    title = '_nest_function'
    doc = '''Return a Function after nesting within ob.'''
    init_inputs = [
        rc.NodeInputBP(label='ob'),
rc.NodeInputBP(label='func_name'),
rc.NodeInputBP(label='lineno'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pyclbr._nest_function(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_pyclbr__readmodule(rc.Node):
    title = '_readmodule'
    doc = '''Do the hard work for readmodule[_ex].

    If inpackage is given, it must be the dotted name of the package in
    which we are searching for a submodule, and then PATH must be the
    package search path; otherwise, we are searching for a top-level
    module, and path is combined with sys.path.
    '''
    init_inputs = [
        rc.NodeInputBP(label='module'),
rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='inpackage'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pyclbr._readmodule(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_pyclbr_readmodule(rc.Node):
    title = 'readmodule'
    doc = '''Return Class objects for the top-level classes in module.

    This is the original interface, before Functions were added.
    '''
    init_inputs = [
        rc.NodeInputBP(label='module'),
rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pyclbr.readmodule(self.input(0), self.input(1)))
        


class AutoNode_pyclbr_readmodule_ex(rc.Node):
    title = 'readmodule_ex'
    doc = '''Return a dictionary with all functions and classes in module.

    Search for module in PATH + sys.path.
    If possible, include imported superclasses.
    Do this by reading source, without importing (and executing) it.
    '''
    init_inputs = [
        rc.NodeInputBP(label='module'),
rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pyclbr.readmodule_ex(self.input(0), self.input(1)))
        