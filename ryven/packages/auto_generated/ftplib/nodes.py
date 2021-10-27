
from NENV import *

import ftplib


class NodeBase(Node):
    pass


class Ftpcp_Node(NodeBase):
    """
    Copy file from one FTP-instance to another."""
    
    title = 'ftpcp'
    type_ = 'ftplib'
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='sourcename'),
        NodeInputBP(label='target'),
        NodeInputBP(label='targetname', dtype=dtypes.Data(default='', size='s')),
        NodeInputBP(label='type', dtype=dtypes.Data(default='I', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ftplib.ftpcp(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Parse150_Node(NodeBase):
    """
    Parse the '150' response for a RETR request.
    Returns the expected transfer size or None; size is not guaranteed to
    be present in the 150 message.
    """
    
    title = 'parse150'
    type_ = 'ftplib'
    init_inputs = [
        NodeInputBP(label='resp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ftplib.parse150(self.input(0)))
        

class Parse227_Node(NodeBase):
    """
    Parse the '227' response for a PASV request.
    Raises error_proto if it does not contain '(h1,h2,h3,h4,p1,p2)'
    Return ('host.addr.as.numbers', port#) tuple."""
    
    title = 'parse227'
    type_ = 'ftplib'
    init_inputs = [
        NodeInputBP(label='resp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ftplib.parse227(self.input(0)))
        

class Parse229_Node(NodeBase):
    """
    Parse the '229' response for an EPSV request.
    Raises error_proto if it does not contain '(|||port|)'
    Return ('host.addr.as.numbers', port#) tuple."""
    
    title = 'parse229'
    type_ = 'ftplib'
    init_inputs = [
        NodeInputBP(label='resp'),
        NodeInputBP(label='peer'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ftplib.parse229(self.input(0), self.input(1)))
        

class Parse257_Node(NodeBase):
    """
    Parse the '257' response for a MKD or PWD request.
    This is a response to a MKD or PWD request: a directory name.
    Returns the directoryname in the 257 reply."""
    
    title = 'parse257'
    type_ = 'ftplib'
    init_inputs = [
        NodeInputBP(label='resp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ftplib.parse257(self.input(0)))
        

class Print_Line_Node(NodeBase):
    """
    Default retrlines callback to print a line."""
    
    title = 'print_line'
    type_ = 'ftplib'
    init_inputs = [
        NodeInputBP(label='line'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ftplib.print_line(self.input(0)))
        

class Test_Node(NodeBase):
    """
    Test program.
    Usage: ftp [-d] [-r[file]] host [-l[dir]] [-d[dir]] [-p] [file] ...

    -d dir
    -l list
    -p password
    """
    
    title = 'test'
    type_ = 'ftplib'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ftplib.test())
        


export_nodes(
    Ftpcp_Node,
    Parse150_Node,
    Parse227_Node,
    Parse229_Node,
    Parse257_Node,
    Print_Line_Node,
    Test_Node,
)
