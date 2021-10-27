
from NENV import *

import shelve


class NodeBase(Node):
    pass


class Open_Node(NodeBase):
    """
    Open a persistent dictionary for reading and writing.

    The filename parameter is the base filename for the underlying
    database.  As a side-effect, an extension may be added to the
    filename and more than one file may be created.  The optional flag
    parameter has the same interpretation as the flag parameter of
    dbm.open(). The optional protocol parameter specifies the
    version of the pickle protocol.

    See the module's __doc__ string for an overview of the interface.
    """
    
    title = 'open'
    type_ = 'shelve'
    init_inputs = [
        NodeInputBP(label='filename'),
        NodeInputBP(label='flag', dtype=dtypes.Data(default='c', size='s')),
        NodeInputBP(label='protocol', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='writeback', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, shelve.open(self.input(0), self.input(1), self.input(2), self.input(3)))
        


export_nodes(
    Open_Node,
)
