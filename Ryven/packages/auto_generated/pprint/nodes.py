import ryvencore_qt as rc
import pprint


class AutoNode_pprint__perfcheck(rc.Node):
    title = '_perfcheck'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pprint._perfcheck(self.input(0)))
        


class AutoNode_pprint__recursion(rc.Node):
    title = '_recursion'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pprint._recursion(self.input(0)))
        


class AutoNode_pprint__safe_repr(rc.Node):
    title = '_safe_repr'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
rc.NodeInputBP(label='context'),
rc.NodeInputBP(label='maxlevels'),
rc.NodeInputBP(label='level'),
rc.NodeInputBP(label='sort_dicts'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pprint._safe_repr(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_pprint__safe_tuple(rc.Node):
    title = '_safe_tuple'
    description = '''Helper function for comparing 2-tuples'''
    init_inputs = [
        rc.NodeInputBP(label='t'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pprint._safe_tuple(self.input(0)))
        


class AutoNode_pprint__wrap_bytes_repr(rc.Node):
    title = '_wrap_bytes_repr'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
rc.NodeInputBP(label='width'),
rc.NodeInputBP(label='allowance'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pprint._wrap_bytes_repr(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_pprint_isreadable(rc.Node):
    title = 'isreadable'
    description = '''Determine if saferepr(object) is readable by eval().'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pprint.isreadable(self.input(0)))
        


class AutoNode_pprint_isrecursive(rc.Node):
    title = 'isrecursive'
    description = '''Determine if object requires a recursive representation.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pprint.isrecursive(self.input(0)))
        


class AutoNode_pprint_pformat(rc.Node):
    title = 'pformat'
    description = '''Format a Python object into a pretty-printed representation.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
rc.NodeInputBP(label='indent'),
rc.NodeInputBP(label='width'),
rc.NodeInputBP(label='depth'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pprint.pformat(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_pprint_pp(rc.Node):
    title = 'pp'
    description = '''Pretty-print a Python object'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pprint.pp(self.input(0)))
        


class AutoNode_pprint_pprint(rc.Node):
    title = 'pprint'
    description = '''Pretty-print a Python object to a stream [default is sys.stdout].'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
rc.NodeInputBP(label='stream'),
rc.NodeInputBP(label='indent'),
rc.NodeInputBP(label='width'),
rc.NodeInputBP(label='depth'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pprint.pprint(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_pprint_saferepr(rc.Node):
    title = 'saferepr'
    description = '''Version of repr() which can handle recursive data structures.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pprint.saferepr(self.input(0)))
        