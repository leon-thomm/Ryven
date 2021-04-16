import ryvencore_qt as rc
import marshal


class AutoNode_marshal_dump(rc.Node):
    title = 'dump'
    type_ = 'marshal'
    doc = '''Write the value on the open file.

  value
    Must be a supported type.
  file
    Must be a writeable binary file.
  version
    Indicates the data format that dump should use.

If the value has (or contains an object that has) an unsupported type, a
ValueError exception is raised - but garbage data will also be written
to the file. The object will not be properly read back by load().'''
    init_inputs = [
        rc.NodeInputBP(label='value'),
rc.NodeInputBP(label='file'),
rc.NodeInputBP(label='version'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, marshal.dump(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_marshal_dumps(rc.Node):
    title = 'dumps'
    type_ = 'marshal'
    doc = '''Return the bytes object that would be written to a file by dump(value, file).

  value
    Must be a supported type.
  version
    Indicates the data format that dumps should use.

Raise a ValueError exception if value has (or contains an object that has) an
unsupported type.'''
    init_inputs = [
        rc.NodeInputBP(label='value'),
rc.NodeInputBP(label='version'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, marshal.dumps(self.input(0), self.input(1)))
        


class AutoNode_marshal_load(rc.Node):
    title = 'load'
    type_ = 'marshal'
    doc = '''Read one value from the open file and return it.

  file
    Must be readable binary file.

If no valid value is read (e.g. because the data has a different Python
version's incompatible marshal format), raise EOFError, ValueError or
TypeError.

Note: If an object containing an unsupported type was marshalled with
dump(), load() will substitute None for the unmarshallable type.'''
    init_inputs = [
        rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, marshal.load(self.input(0)))
        


class AutoNode_marshal_loads(rc.Node):
    title = 'loads'
    type_ = 'marshal'
    doc = '''Convert the bytes-like object to a value.

If no valid value is found, raise EOFError, ValueError or TypeError.  Extra
bytes in the input are ignored.'''
    init_inputs = [
        rc.NodeInputBP(label='bytes'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, marshal.loads(self.input(0)))
        