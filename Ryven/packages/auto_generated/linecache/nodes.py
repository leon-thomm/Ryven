
from NENV import *

import linecache


class NodeBase(Node):
    pass


class Checkcache_Node(NodeBase):
    """
    Discard cache entries that are out of date.
    (This is not checked upon each call!)"""
    
    title = 'checkcache'
    type_ = 'linecache'
    init_inputs = [
        NodeInputBP(label='filename', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, linecache.checkcache(self.input(0)))
        

class Clearcache_Node(NodeBase):
    """
    Clear the cache entirely."""
    
    title = 'clearcache'
    type_ = 'linecache'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, linecache.clearcache())
        

class Getline_Node(NodeBase):
    """
    Get a line for a Python source file from the cache.
    Update the cache if it doesn't contain an entry for this file already."""
    
    title = 'getline'
    type_ = 'linecache'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='lineno'),
        NodeInputBP(label='module_globals', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, linecache.getline(self.input(0), self.input(1), self.input(2)))
        

class Getlines_Node(NodeBase):
    """
    Get the lines for a Python source file from the cache.
    Update the cache if it doesn't contain an entry for this file already."""
    
    title = 'getlines'
    type_ = 'linecache'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='module_globals', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, linecache.getlines(self.input(0), self.input(1)))
        

class Lazycache_Node(NodeBase):
    """
    Seed the cache for filename with module_globals.

    The module loader will be asked for the source only when getlines is
    called, not immediately.

    If there is an entry in the cache already, it is not altered.

    :return: True if a lazy load is registered in the cache,
        otherwise False. To register such a load a module loader with a
        get_source method must be found, the filename must be a cachable
        filename, and the filename must not be already cached.
    """
    
    title = 'lazycache'
    type_ = 'linecache'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='module_globals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, linecache.lazycache(self.input(0), self.input(1)))
        

class Updatecache_Node(NodeBase):
    """
    Update a cache entry and return its list of lines.
    If something's wrong, print a message, discard the cache entry,
    and return an empty list."""
    
    title = 'updatecache'
    type_ = 'linecache'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='module_globals', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, linecache.updatecache(self.input(0), self.input(1)))
        


export_nodes(
    Checkcache_Node,
    Clearcache_Node,
    Getline_Node,
    Getlines_Node,
    Lazycache_Node,
    Updatecache_Node,
)
