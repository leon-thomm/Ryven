import ryvencore_qt as rc
import glob


class AutoNode_glob__glob0(rc.Node):
    title = '_glob0'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='dirname'),
rc.NodeInputBP(label='basename'),
rc.NodeInputBP(label='dironly'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._glob0(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_glob__glob1(rc.Node):
    title = '_glob1'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='dirname'),
rc.NodeInputBP(label='pattern'),
rc.NodeInputBP(label='dironly'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._glob1(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_glob__glob2(rc.Node):
    title = '_glob2'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='dirname'),
rc.NodeInputBP(label='pattern'),
rc.NodeInputBP(label='dironly'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._glob2(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_glob__iglob(rc.Node):
    title = '_iglob'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='pathname'),
rc.NodeInputBP(label='recursive'),
rc.NodeInputBP(label='dironly'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._iglob(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_glob__ishidden(rc.Node):
    title = '_ishidden'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._ishidden(self.input(0)))
        


class AutoNode_glob__isrecursive(rc.Node):
    title = '_isrecursive'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='pattern'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._isrecursive(self.input(0)))
        


class AutoNode_glob__iterdir(rc.Node):
    title = '_iterdir'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='dirname'),
rc.NodeInputBP(label='dironly'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._iterdir(self.input(0), self.input(1)))
        


class AutoNode_glob__rlistdir(rc.Node):
    title = '_rlistdir'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='dirname'),
rc.NodeInputBP(label='dironly'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob._rlistdir(self.input(0), self.input(1)))
        


class AutoNode_glob_escape(rc.Node):
    title = 'escape'
    description = '''Escape all special characters.
    '''
    init_inputs = [
        rc.NodeInputBP(label='pathname'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob.escape(self.input(0)))
        


class AutoNode_glob_glob(rc.Node):
    title = 'glob'
    description = '''Return a list of paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    '''
    init_inputs = [
        rc.NodeInputBP(label='pathname'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob.glob(self.input(0)))
        


class AutoNode_glob_glob0(rc.Node):
    title = 'glob0'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='dirname'),
rc.NodeInputBP(label='pattern'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob.glob0(self.input(0), self.input(1)))
        


class AutoNode_glob_glob1(rc.Node):
    title = 'glob1'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='dirname'),
rc.NodeInputBP(label='pattern'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob.glob1(self.input(0), self.input(1)))
        


class AutoNode_glob_has_magic(rc.Node):
    title = 'has_magic'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob.has_magic(self.input(0)))
        


class AutoNode_glob_iglob(rc.Node):
    title = 'iglob'
    description = '''Return an iterator which yields the paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    '''
    init_inputs = [
        rc.NodeInputBP(label='pathname'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, glob.iglob(self.input(0)))
        