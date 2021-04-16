import ryvencore_qt as rc
import filecmp


class AutoNode_filecmp__cmp(rc.Node):
    title = '_cmp'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
rc.NodeInputBP(label='sh'),
rc.NodeInputBP(label='abs'),
rc.NodeInputBP(label='cmp'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, filecmp._cmp(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_filecmp__do_cmp(rc.Node):
    title = '_do_cmp'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='f1'),
rc.NodeInputBP(label='f2'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, filecmp._do_cmp(self.input(0), self.input(1)))
        


class AutoNode_filecmp__filter(rc.Node):
    title = '_filter'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='flist'),
rc.NodeInputBP(label='skip'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, filecmp._filter(self.input(0), self.input(1)))
        


class AutoNode_filecmp__sig(rc.Node):
    title = '_sig'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='st'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, filecmp._sig(self.input(0)))
        


class AutoNode_filecmp_clear_cache(rc.Node):
    title = 'clear_cache'
    doc = '''Clear the filecmp cache.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, filecmp.clear_cache())
        


class AutoNode_filecmp_cmp(rc.Node):
    title = 'cmp'
    doc = '''Compare two files.

    Arguments:

    f1 -- First file name

    f2 -- Second file name

    shallow -- Just check stat signature (do not read the files).
               defaults to True.

    Return value:

    True if the files are the same, False otherwise.

    This function uses a cache for past comparisons and the results,
    with cache entries invalidated if their stat information
    changes.  The cache may be cleared by calling clear_cache().

    '''
    init_inputs = [
        rc.NodeInputBP(label='f1'),
rc.NodeInputBP(label='f2'),
rc.NodeInputBP(label='shallow'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, filecmp.cmp(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_filecmp_cmpfiles(rc.Node):
    title = 'cmpfiles'
    doc = '''Compare common files in two directories.

    a, b -- directory names
    common -- list of file names found in both directories
    shallow -- if true, do comparison based solely on stat() information

    Returns a tuple of three lists:
      files that compare equal
      files that are different
      filenames that aren't regular files.

    '''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
rc.NodeInputBP(label='common'),
rc.NodeInputBP(label='shallow'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, filecmp.cmpfiles(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_filecmp_demo(rc.Node):
    title = 'demo'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, filecmp.demo())
        