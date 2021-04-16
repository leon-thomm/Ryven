import ryvencore_qt as rc
import plistlib


class AutoNode_plistlib__count_to_size(rc.Node):
    title = '_count_to_size'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='count'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._count_to_size(self.input(0)))
        


class AutoNode_plistlib__date_from_string(rc.Node):
    title = '_date_from_string'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._date_from_string(self.input(0)))
        


class AutoNode_plistlib__date_to_string(rc.Node):
    title = '_date_to_string'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='d'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._date_to_string(self.input(0)))
        


class AutoNode_plistlib__decode_base64(rc.Node):
    title = '_decode_base64'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._decode_base64(self.input(0)))
        


class AutoNode_plistlib__encode_base64(rc.Node):
    title = '_encode_base64'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='maxlinelength'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._encode_base64(self.input(0), self.input(1)))
        


class AutoNode_plistlib__escape(rc.Node):
    title = '_escape'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='text'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._escape(self.input(0)))
        


class AutoNode_plistlib__is_fmt_binary(rc.Node):
    title = '_is_fmt_binary'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='header'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._is_fmt_binary(self.input(0)))
        


class AutoNode_plistlib__is_fmt_xml(rc.Node):
    title = '_is_fmt_xml'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='header'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._is_fmt_xml(self.input(0)))
        


class AutoNode_plistlib__maybe_open(rc.Node):
    title = '_maybe_open'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib._maybe_open())
        


class AutoNode_plistlib_dump(rc.Node):
    title = 'dump'
    doc = '''Write 'value' to a .plist file. 'fp' should be a writable,
    binary file object.
    '''
    init_inputs = [
        rc.NodeInputBP(label='value'),
rc.NodeInputBP(label='fp'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.dump(self.input(0), self.input(1)))
        


class AutoNode_plistlib_dumps(rc.Node):
    title = 'dumps'
    doc = '''Return a bytes object with the contents for a .plist file.
    '''
    init_inputs = [
        rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.dumps(self.input(0)))
        


class AutoNode_plistlib_load(rc.Node):
    title = 'load'
    doc = '''Read a .plist file. 'fp' should be a readable and binary file object.
    Return the unpacked root object (which usually is a dictionary).
    '''
    init_inputs = [
        rc.NodeInputBP(label='fp'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.load(self.input(0)))
        


class AutoNode_plistlib_loads(rc.Node):
    title = 'loads'
    doc = '''Read a .plist file from a bytes object.
    Return the unpacked root object (which usually is a dictionary).
    '''
    init_inputs = [
        rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.loads(self.input(0)))
        


class AutoNode_plistlib_readPlist(rc.Node):
    title = 'readPlist'
    doc = '''
    Read a .plist from a path or file. pathOrFile should either
    be a file name, or a readable binary file object.

    This function is deprecated, use load instead.
    '''
    init_inputs = [
        rc.NodeInputBP(label='pathOrFile'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.readPlist(self.input(0)))
        


class AutoNode_plistlib_readPlistFromBytes(rc.Node):
    title = 'readPlistFromBytes'
    doc = '''
    Read a plist data from a bytes object. Return the root object.

    This function is deprecated, use loads instead.
    '''
    init_inputs = [
        rc.NodeInputBP(label='data'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.readPlistFromBytes(self.input(0)))
        


class AutoNode_plistlib_warn(rc.Node):
    title = 'warn'
    doc = '''Issue a warning, or maybe ignore it or raise an exception.'''
    init_inputs = [
        rc.NodeInputBP(label='message'),
rc.NodeInputBP(label='category'),
rc.NodeInputBP(label='stacklevel'),
rc.NodeInputBP(label='source'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.warn(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_plistlib_writePlist(rc.Node):
    title = 'writePlist'
    doc = '''
    Write 'value' to a .plist file. 'pathOrFile' may either be a
    file name or a (writable) file object.

    This function is deprecated, use dump instead.
    '''
    init_inputs = [
        rc.NodeInputBP(label='value'),
rc.NodeInputBP(label='pathOrFile'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.writePlist(self.input(0), self.input(1)))
        


class AutoNode_plistlib_writePlistToBytes(rc.Node):
    title = 'writePlistToBytes'
    doc = '''
    Return 'value' as a plist-formatted bytes object.

    This function is deprecated, use dumps instead.
    '''
    init_inputs = [
        rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, plistlib.writePlistToBytes(self.input(0)))
        