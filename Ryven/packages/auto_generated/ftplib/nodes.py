import ryvencore_qt as rc
import ftplib


class AutoNode_ftplib_ftpcp(rc.Node):
    title = 'ftpcp'
    description = '''Copy file from one FTP-instance to another.'''
    init_inputs = [
        rc.NodeInputBP(label='source'),
rc.NodeInputBP(label='sourcename'),
rc.NodeInputBP(label='target'),
rc.NodeInputBP(label='targetname'),
rc.NodeInputBP(label='type'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ftplib.ftpcp(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_ftplib_parse150(rc.Node):
    title = 'parse150'
    description = '''Parse the '150' response for a RETR request.
    Returns the expected transfer size or None; size is not guaranteed to
    be present in the 150 message.
    '''
    init_inputs = [
        rc.NodeInputBP(label='resp'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ftplib.parse150(self.input(0)))
        


class AutoNode_ftplib_parse227(rc.Node):
    title = 'parse227'
    description = '''Parse the '227' response for a PASV request.
    Raises error_proto if it does not contain '(h1,h2,h3,h4,p1,p2)'
    Return ('host.addr.as.numbers', port#) tuple.'''
    init_inputs = [
        rc.NodeInputBP(label='resp'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ftplib.parse227(self.input(0)))
        


class AutoNode_ftplib_parse229(rc.Node):
    title = 'parse229'
    description = '''Parse the '229' response for an EPSV request.
    Raises error_proto if it does not contain '(|||port|)'
    Return ('host.addr.as.numbers', port#) tuple.'''
    init_inputs = [
        rc.NodeInputBP(label='resp'),
rc.NodeInputBP(label='peer'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ftplib.parse229(self.input(0), self.input(1)))
        


class AutoNode_ftplib_parse257(rc.Node):
    title = 'parse257'
    description = '''Parse the '257' response for a MKD or PWD request.
    This is a response to a MKD or PWD request: a directory name.
    Returns the directoryname in the 257 reply.'''
    init_inputs = [
        rc.NodeInputBP(label='resp'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ftplib.parse257(self.input(0)))
        


class AutoNode_ftplib_print_line(rc.Node):
    title = 'print_line'
    description = '''Default retrlines callback to print a line.'''
    init_inputs = [
        rc.NodeInputBP(label='line'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ftplib.print_line(self.input(0)))
        


class AutoNode_ftplib_test(rc.Node):
    title = 'test'
    description = '''Test program.
    Usage: ftp [-d] [-r[file]] host [-l[dir]] [-d[dir]] [-p] [file] ...

    -d dir
    -l list
    -p password
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ftplib.test())
        