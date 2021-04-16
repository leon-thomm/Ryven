import ryvencore_qt as rc
import cgitb


class AutoNode_cgitb_enable(rc.Node):
    title = 'enable'
    doc = '''Install an exception handler that formats tracebacks as HTML.

    The optional argument 'display' can be set to 0 to suppress sending the
    traceback to the browser, and 'logdir' can be set to a directory to cause
    tracebacks to be written to files there.'''
    init_inputs = [
        rc.NodeInputBP(label='display'),
rc.NodeInputBP(label='logdir'),
rc.NodeInputBP(label='context'),
rc.NodeInputBP(label='format'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.enable(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_cgitb_grey(rc.Node):
    title = 'grey'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.grey(self.input(0)))
        


class AutoNode_cgitb_handler(rc.Node):
    title = 'handler'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='info'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.handler(self.input(0), self.input(1)))
        


class AutoNode_cgitb_html(rc.Node):
    title = 'html'
    doc = '''Return a nice HTML document describing a given traceback.'''
    init_inputs = [
        rc.NodeInputBP(label='einfo'),
rc.NodeInputBP(label='context'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.html(self.input(0), self.input(1)))
        


class AutoNode_cgitb_lookup(rc.Node):
    title = 'lookup'
    doc = '''Find the value for a given name in the given environment.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='frame'),
rc.NodeInputBP(label='locals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.lookup(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_cgitb_reset(rc.Node):
    title = 'reset'
    doc = '''Return a string that resets the CGI and browser to a known state.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.reset())
        


class AutoNode_cgitb_scanvars(rc.Node):
    title = 'scanvars'
    doc = '''Scan one logical line of Python and look up values of variables used.'''
    init_inputs = [
        rc.NodeInputBP(label='reader'),
rc.NodeInputBP(label='frame'),
rc.NodeInputBP(label='locals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.scanvars(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_cgitb_small(rc.Node):
    title = 'small'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.small(self.input(0)))
        


class AutoNode_cgitb_strong(rc.Node):
    title = 'strong'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.strong(self.input(0)))
        


class AutoNode_cgitb_text(rc.Node):
    title = 'text'
    doc = '''Return a plain text document describing a given traceback.'''
    init_inputs = [
        rc.NodeInputBP(label='einfo'),
rc.NodeInputBP(label='context'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cgitb.text(self.input(0), self.input(1)))
        