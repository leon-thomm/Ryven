import ryvencore_qt as rc
import copy


class AutoNode_copy__copy_immutable(rc.Node):
    title = '_copy_immutable'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copy._copy_immutable(self.input(0)))
        


class AutoNode_copy__deepcopy_atomic(rc.Node):
    title = '_deepcopy_atomic'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='memo'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copy._deepcopy_atomic(self.input(0), self.input(1)))
        


class AutoNode_copy__deepcopy_dict(rc.Node):
    title = '_deepcopy_dict'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='memo'),
rc.NodeInputBP(label='deepcopy'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copy._deepcopy_dict(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_copy__deepcopy_list(rc.Node):
    title = '_deepcopy_list'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='memo'),
rc.NodeInputBP(label='deepcopy'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copy._deepcopy_list(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_copy__deepcopy_method(rc.Node):
    title = '_deepcopy_method'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='memo'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copy._deepcopy_method(self.input(0), self.input(1)))
        


class AutoNode_copy__deepcopy_tuple(rc.Node):
    title = '_deepcopy_tuple'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='memo'),
rc.NodeInputBP(label='deepcopy'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copy._deepcopy_tuple(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_copy__keep_alive(rc.Node):
    title = '_keep_alive'
    description = '''Keeps a reference to the object x in the memo.

    Because we remember objects by their id, we have
    to assure that possibly temporary objects are kept
    alive by referencing them.
    We store a reference at the id of the memo, which should
    normally not be used unless someone tries to deepcopy
    the memo itself...
    '''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='memo'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copy._keep_alive(self.input(0), self.input(1)))
        


class AutoNode_copy__reconstruct(rc.Node):
    title = '_reconstruct'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='memo'),
rc.NodeInputBP(label='func'),
rc.NodeInputBP(label='args'),
rc.NodeInputBP(label='state'),
rc.NodeInputBP(label='listiter'),
rc.NodeInputBP(label='dictiter'),
rc.NodeInputBP(label='deepcopy'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copy._reconstruct(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        


class AutoNode_copy_copy(rc.Node):
    title = 'copy'
    description = '''Shallow copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.
    '''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copy.copy(self.input(0)))
        


class AutoNode_copy_deepcopy(rc.Node):
    title = 'deepcopy'
    description = '''Deep copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.
    '''
    init_inputs = [
        rc.NodeInputBP(label='x'),
rc.NodeInputBP(label='memo'),
rc.NodeInputBP(label='_nil'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copy.deepcopy(self.input(0), self.input(1), self.input(2)))
        