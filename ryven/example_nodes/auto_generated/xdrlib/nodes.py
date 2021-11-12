
from ryven.NENV import *

import xdrlib


class NodeBase(Node):
    pass


class Raise_Conversion_Error_Node(NodeBase):
    """
     Wrap any raised struct.errors in a ConversionError. """
    
    title = 'raise_conversion_error'
    type_ = 'xdrlib'
    init_inputs = [
        NodeInputBP(label='function'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, xdrlib.raise_conversion_error(self.input(0)))
        

class Wraps_Node(NodeBase):
    """
    Decorator factory to apply update_wrapper() to a wrapper function

       Returns a decorator that invokes update_wrapper() with the decorated
       function as the wrapper argument and the arguments to wraps() as the
       remaining arguments. Default arguments are as for update_wrapper().
       This is a convenience function to simplify applying partial() to
       update_wrapper().
    """
    
    title = 'wraps'
    type_ = 'xdrlib'
    init_inputs = [
        NodeInputBP(label='wrapped'),
        NodeInputBP(label='assigned', dtype=dtypes.Data(default=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), size='s')),
        NodeInputBP(label='updated', dtype=dtypes.Data(default=('__dict__',), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, xdrlib.wraps(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    Raise_Conversion_Error_Node,
    Wraps_Node,
)
