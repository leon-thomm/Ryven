import ryvencore_qt as rc
import enum


class AutoNode_enum__decompose(rc.Node):
    title = '_decompose'
    doc = '''
    Extract all members from the value.
    '''
    init_inputs = [
        rc.NodeInputBP(label='flag'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, enum._decompose(self.input(0), self.input(1)))
        


class AutoNode_enum__high_bit(rc.Node):
    title = '_high_bit'
    doc = '''
    returns index of highest bit, or -1 if value is zero or negative
    '''
    init_inputs = [
        rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, enum._high_bit(self.input(0)))
        


class AutoNode_enum__is_descriptor(rc.Node):
    title = '_is_descriptor'
    doc = '''
    Returns True if obj is a descriptor, False otherwise.
    '''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, enum._is_descriptor(self.input(0)))
        


class AutoNode_enum__is_dunder(rc.Node):
    title = '_is_dunder'
    doc = '''
    Returns True if a __dunder__ name, False otherwise.
    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, enum._is_dunder(self.input(0)))
        


class AutoNode_enum__is_sunder(rc.Node):
    title = '_is_sunder'
    doc = '''
    Returns True if a _sunder_ name, False otherwise.
    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, enum._is_sunder(self.input(0)))
        


class AutoNode_enum__make_class_unpicklable(rc.Node):
    title = '_make_class_unpicklable'
    doc = '''
    Make the given class un-picklable.
    '''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, enum._make_class_unpicklable(self.input(0)))
        


class AutoNode_enum__power_of_two(rc.Node):
    title = '_power_of_two'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, enum._power_of_two(self.input(0)))
        


class AutoNode_enum__reduce_ex_by_name(rc.Node):
    title = '_reduce_ex_by_name'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='proto'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, enum._reduce_ex_by_name(self.input(0), self.input(1)))
        


class AutoNode_enum_unique(rc.Node):
    title = 'unique'
    doc = '''
    Class decorator for enumerations ensuring unique member values.
    '''
    init_inputs = [
        rc.NodeInputBP(label='enumeration'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, enum.unique(self.input(0)))
        