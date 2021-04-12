import ryvencore_qt as rc
import fnmatch


class AutoNode_fnmatch_filter(rc.Node):
    title = 'filter'
    description = '''Return the subset of the list NAMES that match PAT.'''
    init_inputs = [
        rc.NodeInputBP(label='names'),
rc.NodeInputBP(label='pat'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fnmatch.filter(self.input(0), self.input(1)))
        


class AutoNode_fnmatch_fnmatch(rc.Node):
    title = 'fnmatch'
    description = '''Test whether FILENAME matches PATTERN.

    Patterns are Unix shell style:

    *       matches everything
    ?       matches any single character
    [seq]   matches any character in seq
    [!seq]  matches any char not in seq

    An initial period in FILENAME is not special.
    Both FILENAME and PATTERN are first case-normalized
    if the operating system requires it.
    If you don't want this, use fnmatchcase(FILENAME, PATTERN).
    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='pat'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fnmatch.fnmatch(self.input(0), self.input(1)))
        


class AutoNode_fnmatch_fnmatchcase(rc.Node):
    title = 'fnmatchcase'
    description = '''Test whether FILENAME matches PATTERN, including case.

    This is a version of fnmatch() which doesn't case-normalize
    its arguments.
    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='pat'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fnmatch.fnmatchcase(self.input(0), self.input(1)))
        


class AutoNode_fnmatch_translate(rc.Node):
    title = 'translate'
    description = '''Translate a shell PATTERN to a regular expression.

    There is no way to quote meta-characters.
    '''
    init_inputs = [
        rc.NodeInputBP(label='pat'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fnmatch.translate(self.input(0)))
        