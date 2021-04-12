import ryvencore_qt as rc
import pathlib


class AutoNode_pathlib__getfinalpathname(rc.Node):
    title = '_getfinalpathname'
    description = '''A helper function for samepath on windows.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pathlib._getfinalpathname(self.input(0)))
        


class AutoNode_pathlib__ignore_error(rc.Node):
    title = '_ignore_error'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='exception'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pathlib._ignore_error(self.input(0)))
        


class AutoNode_pathlib__is_wildcard_pattern(rc.Node):
    title = '_is_wildcard_pattern'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='pat'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pathlib._is_wildcard_pattern(self.input(0)))
        


class AutoNode_pathlib_urlquote_from_bytes(rc.Node):
    title = 'urlquote_from_bytes'
    description = '''Like quote(), but accepts a bytes object rather than a str, and does
    not perform string-to-bytes encoding.  It always returns an ASCII string.
    quote_from_bytes(b'abc def?') -> 'abc%20def%3f'
    '''
    init_inputs = [
        rc.NodeInputBP(label='bs'),
rc.NodeInputBP(label='safe'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pathlib.urlquote_from_bytes(self.input(0), self.input(1)))
        