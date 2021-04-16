import ryvencore_qt as rc
import _struct


class AutoNode__struct__clearcache(rc.Node):
    title = '_clearcache'
    type_ = '_struct'
    doc = '''Clear the internal cache.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _struct._clearcache())
        


class AutoNode__struct_calcsize(rc.Node):
    title = 'calcsize'
    type_ = '_struct'
    doc = '''Return size in bytes of the struct described by the format string.'''
    init_inputs = [
        rc.NodeInputBP(label='format'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _struct.calcsize(self.input(0)))
        


class AutoNode__struct_iter_unpack(rc.Node):
    title = 'iter_unpack'
    type_ = '_struct'
    doc = '''Return an iterator yielding tuples unpacked from the given bytes.

The bytes are unpacked according to the format string, like
a repeated invocation of unpack_from().

Requires that the bytes length be a multiple of the format struct size.'''
    init_inputs = [
        rc.NodeInputBP(label='format'),
rc.NodeInputBP(label='buffer'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _struct.iter_unpack(self.input(0), self.input(1)))
        


class AutoNode__struct_unpack(rc.Node):
    title = 'unpack'
    type_ = '_struct'
    doc = '''Return a tuple containing values unpacked according to the format string.

The buffer's size in bytes must be calcsize(format).

See help(struct) for more on format strings.'''
    init_inputs = [
        rc.NodeInputBP(label='format'),
rc.NodeInputBP(label='buffer'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _struct.unpack(self.input(0), self.input(1)))
        


class AutoNode__struct_unpack_from(rc.Node):
    title = 'unpack_from'
    type_ = '_struct'
    doc = '''Return a tuple containing values unpacked according to the format string.

The buffer's size, minus offset, must be at least calcsize(format).

See help(struct) for more on format strings.'''
    init_inputs = [
        rc.NodeInputBP(label='format'),
rc.NodeInputBP(label='buffer'),
rc.NodeInputBP(label='offset'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _struct.unpack_from(self.input(0), self.input(1), self.input(2)))
        