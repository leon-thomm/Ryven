import ryvencore_qt as rc
import encodings


class AutoNode_encodings__alias_mbcs(rc.Node):
    title = '_alias_mbcs'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, encodings._alias_mbcs(self.input(0)))
        


class AutoNode_encodings_normalize_encoding(rc.Node):
    title = 'normalize_encoding'
    doc = ''' Normalize an encoding name.

        Normalization works as follows: all non-alphanumeric
        characters except the dot used for Python package names are
        collapsed and replaced with a single underscore, e.g. '  -;#'
        becomes '_'. Leading and trailing underscores are removed.

        Note that encoding names should be ASCII only.

    '''
    init_inputs = [
        rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, encodings.normalize_encoding(self.input(0)))
        


class AutoNode_encodings_search_function(rc.Node):
    title = 'search_function'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, encodings.search_function(self.input(0)))
        