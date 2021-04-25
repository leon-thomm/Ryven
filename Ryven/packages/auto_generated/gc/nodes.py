
from NENV import *

import gc


class NodeBase(Node):
    pass


class AutoNode_gc_collect(NodeBase):
    title = 'collect'
    type_ = 'gc'
    doc = """Run the garbage collector.

With no arguments, run a full collection.  The optional argument
may be an integer specifying which generation to collect.  A ValueError
is raised if the generation number is invalid.

The number of unreachable objects is returned."""
    init_inputs = [
        NodeInputBP(label='generation'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.collect(self.input(0)))
        

class AutoNode_gc_disable(NodeBase):
    title = 'disable'
    type_ = 'gc'
    doc = """Disable automatic garbage collection."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.disable())
        

class AutoNode_gc_enable(NodeBase):
    title = 'enable'
    type_ = 'gc'
    doc = """Enable automatic garbage collection."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.enable())
        

class AutoNode_gc_freeze(NodeBase):
    title = 'freeze'
    type_ = 'gc'
    doc = """Freeze all current tracked objects and ignore them for future collections.

This can be used before a POSIX fork() call to make the gc copy-on-write friendly.
Note: collection before a POSIX fork() call may free pages for future allocation
which can cause copy-on-write."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.freeze())
        

class AutoNode_gc_get_count(NodeBase):
    title = 'get_count'
    type_ = 'gc'
    doc = """Return a three-tuple of the current collection counts."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.get_count())
        

class AutoNode_gc_get_debug(NodeBase):
    title = 'get_debug'
    type_ = 'gc'
    doc = """Get the garbage collection debugging flags."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.get_debug())
        

class AutoNode_gc_get_freeze_count(NodeBase):
    title = 'get_freeze_count'
    type_ = 'gc'
    doc = """Return the number of objects in the permanent generation."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.get_freeze_count())
        

class AutoNode_gc_get_objects(NodeBase):
    title = 'get_objects'
    type_ = 'gc'
    doc = """Return a list of objects tracked by the collector (excluding the list returned).

  generation
    Generation to extract the objects from.

If generation is not None, return only the objects tracked by the collector
that are in that generation."""
    init_inputs = [
        NodeInputBP(label='generation'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.get_objects(self.input(0)))
        

class AutoNode_gc_get_stats(NodeBase):
    title = 'get_stats'
    type_ = 'gc'
    doc = """Return a list of dictionaries containing per-generation statistics."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.get_stats())
        

class AutoNode_gc_get_threshold(NodeBase):
    title = 'get_threshold'
    type_ = 'gc'
    doc = """Return the current collection thresholds."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.get_threshold())
        

class AutoNode_gc_is_tracked(NodeBase):
    title = 'is_tracked'
    type_ = 'gc'
    doc = """Returns true if the object is tracked by the garbage collector.

Simple atomic objects will return false."""
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.is_tracked(self.input(0)))
        

class AutoNode_gc_isenabled(NodeBase):
    title = 'isenabled'
    type_ = 'gc'
    doc = """Returns true if automatic garbage collection is enabled."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.isenabled())
        

class AutoNode_gc_set_debug(NodeBase):
    title = 'set_debug'
    type_ = 'gc'
    doc = """Set the garbage collection debugging flags.

  flags
    An integer that can have the following bits turned on:
      DEBUG_STATS - Print statistics during collection.
      DEBUG_COLLECTABLE - Print collectable objects found.
      DEBUG_UNCOLLECTABLE - Print unreachable but uncollectable objects
        found.
      DEBUG_SAVEALL - Save objects to gc.garbage rather than freeing them.
      DEBUG_LEAK - Debug leaking programs (everything but STATS).

Debugging information is written to sys.stderr."""
    init_inputs = [
        NodeInputBP(label='flags'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.set_debug(self.input(0)))
        

class AutoNode_gc_unfreeze(NodeBase):
    title = 'unfreeze'
    type_ = 'gc'
    doc = """Unfreeze all objects in the permanent generation.

Put all objects in the permanent generation back into oldest generation."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gc.unfreeze())
        


export_nodes(
    AutoNode_gc_collect,
    AutoNode_gc_disable,
    AutoNode_gc_enable,
    AutoNode_gc_freeze,
    AutoNode_gc_get_count,
    AutoNode_gc_get_debug,
    AutoNode_gc_get_freeze_count,
    AutoNode_gc_get_objects,
    AutoNode_gc_get_stats,
    AutoNode_gc_get_threshold,
    AutoNode_gc_is_tracked,
    AutoNode_gc_isenabled,
    AutoNode_gc_set_debug,
    AutoNode_gc_unfreeze,
)
