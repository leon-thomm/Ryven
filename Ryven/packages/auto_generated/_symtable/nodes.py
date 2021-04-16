import ryvencore_qt as rc
import _symtable


class AutoNode__symtable_symtable(rc.Node):
    title = 'symtable'
    type_ = '_symtable'
    doc = '''Return symbol and scope dictionaries used internally by compiler.'''
    init_inputs = [
        rc.NodeInputBP(label='source'),
rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='startstr'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _symtable.symtable(self.input(0), self.input(1), self.input(2)))
        