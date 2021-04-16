import ryvencore_qt as rc
import fileinput


class AutoNode_fileinput__test(rc.Node):
    title = '_test'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fileinput._test())
        


class AutoNode_fileinput_close(rc.Node):
    title = 'close'
    doc = '''Close the sequence.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fileinput.close())
        


class AutoNode_fileinput_filelineno(rc.Node):
    title = 'filelineno'
    doc = '''
    Return the line number in the current file. Before the first line
    has been read, returns 0. After the last line of the last file has
    been read, returns the line number of that line within the file.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fileinput.filelineno())
        


class AutoNode_fileinput_filename(rc.Node):
    title = 'filename'
    doc = '''
    Return the name of the file currently being read.
    Before the first line has been read, returns None.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fileinput.filename())
        


class AutoNode_fileinput_fileno(rc.Node):
    title = 'fileno'
    doc = '''
    Return the file number of the current file. When no file is currently
    opened, returns -1.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fileinput.fileno())
        


class AutoNode_fileinput_hook_compressed(rc.Node):
    title = 'hook_compressed'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='mode'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fileinput.hook_compressed(self.input(0), self.input(1)))
        


class AutoNode_fileinput_hook_encoded(rc.Node):
    title = 'hook_encoded'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='encoding'),
rc.NodeInputBP(label='errors'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fileinput.hook_encoded(self.input(0), self.input(1)))
        


class AutoNode_fileinput_input(rc.Node):
    title = 'input'
    doc = '''Return an instance of the FileInput class, which can be iterated.

    The parameters are passed to the constructor of the FileInput class.
    The returned instance, in addition to being an iterator,
    keeps global state for the functions of this module,.
    '''
    init_inputs = [
        rc.NodeInputBP(label='files'),
rc.NodeInputBP(label='inplace'),
rc.NodeInputBP(label='backup'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fileinput.input(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_fileinput_isfirstline(rc.Node):
    title = 'isfirstline'
    doc = '''
    Returns true the line just read is the first line of its file,
    otherwise returns false.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fileinput.isfirstline())
        


class AutoNode_fileinput_isstdin(rc.Node):
    title = 'isstdin'
    doc = '''
    Returns true if the last line was read from sys.stdin,
    otherwise returns false.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fileinput.isstdin())
        


class AutoNode_fileinput_lineno(rc.Node):
    title = 'lineno'
    doc = '''
    Return the cumulative line number of the line that has just been read.
    Before the first line has been read, returns 0. After the last line
    of the last file has been read, returns the line number of that line.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fileinput.lineno())
        


class AutoNode_fileinput_nextfile(rc.Node):
    title = 'nextfile'
    doc = '''
    Close the current file so that the next iteration will read the first
    line from the next file (if any); lines not read from the file will
    not count towards the cumulative line count. The filename is not
    changed until after the first line of the next file has been read.
    Before the first line has been read, this function has no effect;
    it cannot be used to skip the first file. After the last line of the
    last file has been read, this function has no effect.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, fileinput.nextfile())
        