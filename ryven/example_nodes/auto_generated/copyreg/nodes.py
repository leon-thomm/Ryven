
from ryven.NENV import *

import copyreg


class NodeBase(Node):
    pass


class __Newobj___Node(NodeBase):
    """
    """
    
    title = '__newobj__'
    type_ = 'copyreg'
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copyreg.__newobj__(self.input(0)))
        

class __Newobj_Ex___Node(NodeBase):
    """
    Used by pickle protocol 4, instead of __newobj__ to allow classes with
    keyword-only arguments to be pickled correctly.
    """
    
    title = '__newobj_ex__'
    type_ = 'copyreg'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='args'),
        NodeInputBP(label='kwargs'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copyreg.__newobj_ex__(self.input(0), self.input(1), self.input(2)))
        

class _Reconstructor_Node(NodeBase):
    """
    """
    
    title = '_reconstructor'
    type_ = 'copyreg'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='base'),
        NodeInputBP(label='state'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copyreg._reconstructor(self.input(0), self.input(1), self.input(2)))
        

class _Reduce_Ex_Node(NodeBase):
    """
    """
    
    title = '_reduce_ex'
    type_ = 'copyreg'
    init_inputs = [
        NodeInputBP(label='proto'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copyreg._reduce_ex(self.input(0)))
        

class _Slotnames_Node(NodeBase):
    """
    Return a list of slot names for a given class.

    This needs to find slots defined by the class and its bases, so we
    can't simply return the __slots__ attribute.  We must walk down
    the Method Resolution Order and concatenate the __slots__ of each
    class found there.  (This assumes classes don't modify their
    __slots__ attribute to misrepresent their slots after the class is
    defined.)
    """
    
    title = '_slotnames'
    type_ = 'copyreg'
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copyreg._slotnames(self.input(0)))
        

class Add_Extension_Node(NodeBase):
    """
    Register an extension code."""
    
    title = 'add_extension'
    type_ = 'copyreg'
    init_inputs = [
        NodeInputBP(label='module'),
        NodeInputBP(label='name'),
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copyreg.add_extension(self.input(0), self.input(1), self.input(2)))
        

class Clear_Extension_Cache_Node(NodeBase):
    """
    """
    
    title = 'clear_extension_cache'
    type_ = 'copyreg'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copyreg.clear_extension_cache())
        

class Constructor_Node(NodeBase):
    """
    """
    
    title = 'constructor'
    type_ = 'copyreg'
    init_inputs = [
        NodeInputBP(label='object'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copyreg.constructor(self.input(0)))
        

class Pickle_Node(NodeBase):
    """
    """
    
    title = 'pickle'
    type_ = 'copyreg'
    init_inputs = [
        NodeInputBP(label='ob_type'),
        NodeInputBP(label='pickle_function'),
        NodeInputBP(label='constructor_ob', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copyreg.pickle(self.input(0), self.input(1), self.input(2)))
        

class Pickle_Complex_Node(NodeBase):
    """
    """
    
    title = 'pickle_complex'
    type_ = 'copyreg'
    init_inputs = [
        NodeInputBP(label='c'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copyreg.pickle_complex(self.input(0)))
        

class Remove_Extension_Node(NodeBase):
    """
    Unregister an extension code.  For testing only."""
    
    title = 'remove_extension'
    type_ = 'copyreg'
    init_inputs = [
        NodeInputBP(label='module'),
        NodeInputBP(label='name'),
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, copyreg.remove_extension(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    __Newobj___Node,
    __Newobj_Ex___Node,
    _Reconstructor_Node,
    _Reduce_Ex_Node,
    _Slotnames_Node,
    Add_Extension_Node,
    Clear_Extension_Cache_Node,
    Constructor_Node,
    Pickle_Node,
    Pickle_Complex_Node,
    Remove_Extension_Node,
)
