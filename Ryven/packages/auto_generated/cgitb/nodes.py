
from NENV import *

import cgitb


class NodeBase(Node):
    pass


class Enable_Node(NodeBase):
    title = 'enable'
    type_ = 'cgitb'
    doc = """Install an exception handler that formats tracebacks as HTML.

    The optional argument 'display' can be set to 0 to suppress sending the
    traceback to the browser, and 'logdir' can be set to a directory to cause
    tracebacks to be written to files there."""
    init_inputs = [
        NodeInputBP(label='display', dtype=dtypes.Data(default=1, size='s')),
        NodeInputBP(label='logdir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='context', dtype=dtypes.Data(default=5, size='s')),
        NodeInputBP(label='format', dtype=dtypes.Data(default='html', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.enable(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Grey_Node(NodeBase):
    title = 'grey'
    type_ = 'cgitb'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='text'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.grey(self.input(0)))
        

class Handler_Node(NodeBase):
    title = 'handler'
    type_ = 'cgitb'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='info', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.handler(self.input(0)))
        

class Html_Node(NodeBase):
    title = 'html'
    type_ = 'cgitb'
    doc = """Return a nice HTML document describing a given traceback."""
    init_inputs = [
        NodeInputBP(label='einfo'),
        NodeInputBP(label='context', dtype=dtypes.Data(default=5, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.html(self.input(0), self.input(1)))
        

class Lookup_Node(NodeBase):
    title = 'lookup'
    type_ = 'cgitb'
    doc = """Find the value for a given name in the given environment."""
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='frame'),
        NodeInputBP(label='locals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.lookup(self.input(0), self.input(1), self.input(2)))
        

class Reset_Node(NodeBase):
    title = 'reset'
    type_ = 'cgitb'
    doc = """Return a string that resets the CGI and browser to a known state."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.reset())
        

class Scanvars_Node(NodeBase):
    title = 'scanvars'
    type_ = 'cgitb'
    doc = """Scan one logical line of Python and look up values of variables used."""
    init_inputs = [
        NodeInputBP(label='reader'),
        NodeInputBP(label='frame'),
        NodeInputBP(label='locals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.scanvars(self.input(0), self.input(1), self.input(2)))
        

class Small_Node(NodeBase):
    title = 'small'
    type_ = 'cgitb'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='text'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.small(self.input(0)))
        

class Strong_Node(NodeBase):
    title = 'strong'
    type_ = 'cgitb'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='text'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.strong(self.input(0)))
        

class Text_Node(NodeBase):
    title = 'text'
    type_ = 'cgitb'
    doc = """Return a plain text document describing a given traceback."""
    init_inputs = [
        NodeInputBP(label='einfo'),
        NodeInputBP(label='context', dtype=dtypes.Data(default=5, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.text(self.input(0), self.input(1)))
        


export_nodes(
    Enable_Node,
    Grey_Node,
    Handler_Node,
    Html_Node,
    Lookup_Node,
    Reset_Node,
    Scanvars_Node,
    Small_Node,
    Strong_Node,
    Text_Node,
)
