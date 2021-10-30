
from ryven.NENV import *

import warnings


class NodeBase(Node):
    pass


class _Add_Filter_Node(NodeBase):
    """
    """
    
    title = '_add_filter'
    type_ = 'warnings'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._add_filter())
        

class _Formatwarning_Orig_Node(NodeBase):
    """
    Function to format a warning the standard way."""
    
    title = '_formatwarning_orig'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='message'),
        NodeInputBP(label='category'),
        NodeInputBP(label='filename'),
        NodeInputBP(label='lineno'),
        NodeInputBP(label='line', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._formatwarning_orig(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class _Formatwarnmsg_Node(NodeBase):
    """
    Function to format a warning the standard way."""
    
    title = '_formatwarnmsg'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='msg'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._formatwarnmsg(self.input(0)))
        

class _Formatwarnmsg_Impl_Node(NodeBase):
    """
    """
    
    title = '_formatwarnmsg_impl'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='msg'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._formatwarnmsg_impl(self.input(0)))
        

class _Getaction_Node(NodeBase):
    """
    """
    
    title = '_getaction'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='action'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._getaction(self.input(0)))
        

class _Getcategory_Node(NodeBase):
    """
    """
    
    title = '_getcategory'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='category'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._getcategory(self.input(0)))
        

class _Is_Internal_Frame_Node(NodeBase):
    """
    Signal whether the frame is an internal CPython implementation detail."""
    
    title = '_is_internal_frame'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='frame'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._is_internal_frame(self.input(0)))
        

class _Next_External_Frame_Node(NodeBase):
    """
    Find the next frame that doesn't involve CPython internals."""
    
    title = '_next_external_frame'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='frame'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._next_external_frame(self.input(0)))
        

class _Processoptions_Node(NodeBase):
    """
    """
    
    title = '_processoptions'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='args'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._processoptions(self.input(0)))
        

class _Setoption_Node(NodeBase):
    """
    """
    
    title = '_setoption'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='arg'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._setoption(self.input(0)))
        

class _Showwarning_Orig_Node(NodeBase):
    """
    Hook to write a warning to a file; replace if you like."""
    
    title = '_showwarning_orig'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='message'),
        NodeInputBP(label='category'),
        NodeInputBP(label='filename'),
        NodeInputBP(label='lineno'),
        NodeInputBP(label='file', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='line', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._showwarning_orig(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class _Showwarnmsg_Node(NodeBase):
    """
    Hook to write a warning to a file; replace if you like."""
    
    title = '_showwarnmsg'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='msg'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._showwarnmsg(self.input(0)))
        

class _Showwarnmsg_Impl_Node(NodeBase):
    """
    """
    
    title = '_showwarnmsg_impl'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='msg'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._showwarnmsg_impl(self.input(0)))
        

class _Warn_Unawaited_Coroutine_Node(NodeBase):
    """
    """
    
    title = '_warn_unawaited_coroutine'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='coro'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings._warn_unawaited_coroutine(self.input(0)))
        

class Filterwarnings_Node(NodeBase):
    """
    Insert an entry into the list of warnings filters (at the front).

    'action' -- one of "error", "ignore", "always", "default", "module",
                or "once"
    'message' -- a regex that the warning message must match
    'category' -- a class that the warning must be a subclass of
    'module' -- a regex that the module name must match
    'lineno' -- an integer line number, 0 matches all warnings
    'append' -- if true, append to the list of filters
    """
    
    title = 'filterwarnings'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='action'),
        NodeInputBP(label='message', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='category', dtype=dtypes.Data(default=Warning, size='s')),
        NodeInputBP(label='module', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='lineno', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='append', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings.filterwarnings(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class Formatwarning_Node(NodeBase):
    """
    Function to format a warning the standard way."""
    
    title = 'formatwarning'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='message'),
        NodeInputBP(label='category'),
        NodeInputBP(label='filename'),
        NodeInputBP(label='lineno'),
        NodeInputBP(label='line', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings.formatwarning(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Resetwarnings_Node(NodeBase):
    """
    Clear the list of warning filters, so that no filters are active."""
    
    title = 'resetwarnings'
    type_ = 'warnings'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings.resetwarnings())
        

class Showwarning_Node(NodeBase):
    """
    Hook to write a warning to a file; replace if you like."""
    
    title = 'showwarning'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='message'),
        NodeInputBP(label='category'),
        NodeInputBP(label='filename'),
        NodeInputBP(label='lineno'),
        NodeInputBP(label='file', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='line', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings.showwarning(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class Simplefilter_Node(NodeBase):
    """
    Insert a simple entry into the list of warnings filters (at the front).

    A simple filter matches all modules and messages.
    'action' -- one of "error", "ignore", "always", "default", "module",
                or "once"
    'category' -- a class that the warning must be a subclass of
    'lineno' -- an integer line number, 0 matches all warnings
    'append' -- if true, append to the list of filters
    """
    
    title = 'simplefilter'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='action'),
        NodeInputBP(label='category', dtype=dtypes.Data(default=Warning, size='s')),
        NodeInputBP(label='lineno', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='append', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings.simplefilter(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Warn_Node(NodeBase):
    """
    Issue a warning, or maybe ignore it or raise an exception."""
    
    title = 'warn'
    type_ = 'warnings'
    init_inputs = [
        NodeInputBP(label='message'),
        NodeInputBP(label='category', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='stacklevel', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='source', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, warnings.warn(self.input(0), self.input(1), self.input(2), self.input(3)))
        


export_nodes(
    _Add_Filter_Node,
    _Formatwarning_Orig_Node,
    _Formatwarnmsg_Node,
    _Formatwarnmsg_Impl_Node,
    _Getaction_Node,
    _Getcategory_Node,
    _Is_Internal_Frame_Node,
    _Next_External_Frame_Node,
    _Processoptions_Node,
    _Setoption_Node,
    _Showwarning_Orig_Node,
    _Showwarnmsg_Node,
    _Showwarnmsg_Impl_Node,
    _Warn_Unawaited_Coroutine_Node,
    Filterwarnings_Node,
    Formatwarning_Node,
    Resetwarnings_Node,
    Showwarning_Node,
    Simplefilter_Node,
    Warn_Node,
)
