import ryvencore_qt as rc
import decimal


class AutoNode_decimal_getcontext(rc.Node):
    title = 'getcontext'
    doc = '''Get the current default context.

'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, decimal.getcontext())
        


class AutoNode_decimal_localcontext(rc.Node):
    title = 'localcontext'
    doc = '''Return a context manager that will set the default context to a copy of ctx
on entry to the with-statement and restore the previous default context when
exiting the with-statement. If no context is specified, a copy of the current
default context is used.

'''
    init_inputs = [
        rc.NodeInputBP(label='ctx'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, decimal.localcontext(self.input(0)))
        


class AutoNode_decimal_setcontext(rc.Node):
    title = 'setcontext'
    doc = '''Set a new default context.

'''
    init_inputs = [
        rc.NodeInputBP(label='context'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, decimal.setcontext(self.input(0)))
        