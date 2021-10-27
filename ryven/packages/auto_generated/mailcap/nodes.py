
from NENV import *

import mailcap


class NodeBase(Node):
    pass


class _Readmailcapfile_Node(NodeBase):
    """
    Read a mailcap file and return a dictionary keyed by MIME type.

    Each MIME type is mapped to an entry consisting of a list of
    dictionaries; the list will contain more than one such dictionary
    if a given MIME type appears more than once in the mailcap file.
    Each dictionary contains key-value pairs for that MIME type, where
    the viewing command is stored with the key "view".
    """
    
    title = '_readmailcapfile'
    type_ = 'mailcap'
    init_inputs = [
        NodeInputBP(label='fp'),
        NodeInputBP(label='lineno'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailcap._readmailcapfile(self.input(0), self.input(1)))
        

class Findmatch_Node(NodeBase):
    """
    Find a match for a mailcap entry.

    Return a tuple containing the command line, and the mailcap entry
    used; (None, None) if no match is found.  This may invoke the
    'test' command of several matching entries before deciding which
    entry to use.

    """
    
    title = 'findmatch'
    type_ = 'mailcap'
    init_inputs = [
        NodeInputBP(label='caps'),
        NodeInputBP(label='MIMEtype'),
        NodeInputBP(label='key', dtype=dtypes.Data(default='view', size='s')),
        NodeInputBP(label='filename', dtype=dtypes.Data(default='/dev/null', size='s')),
        NodeInputBP(label='plist', dtype=dtypes.Data(default=[], size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailcap.findmatch(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Findparam_Node(NodeBase):
    """
    """
    
    title = 'findparam'
    type_ = 'mailcap'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='plist'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailcap.findparam(self.input(0), self.input(1)))
        

class Getcaps_Node(NodeBase):
    """
    Return a dictionary containing the mailcap database.

    The dictionary maps a MIME type (in all lowercase, e.g. 'text/plain')
    to a list of dictionaries corresponding to mailcap entries.  The list
    collects all the entries for that MIME type from all available mailcap
    files.  Each dictionary contains key-value pairs for that MIME type,
    where the viewing command is stored with the key "view".

    """
    
    title = 'getcaps'
    type_ = 'mailcap'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailcap.getcaps())
        

class Lineno_Sort_Key_Node(NodeBase):
    """
    """
    
    title = 'lineno_sort_key'
    type_ = 'mailcap'
    init_inputs = [
        NodeInputBP(label='entry'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailcap.lineno_sort_key(self.input(0)))
        

class Listmailcapfiles_Node(NodeBase):
    """
    Return a list of all mailcap files found on the system."""
    
    title = 'listmailcapfiles'
    type_ = 'mailcap'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailcap.listmailcapfiles())
        

class Lookup_Node(NodeBase):
    """
    """
    
    title = 'lookup'
    type_ = 'mailcap'
    init_inputs = [
        NodeInputBP(label='caps'),
        NodeInputBP(label='MIMEtype'),
        NodeInputBP(label='key', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailcap.lookup(self.input(0), self.input(1), self.input(2)))
        

class Parsefield_Node(NodeBase):
    """
    Separate one key-value pair in a mailcap entry."""
    
    title = 'parsefield'
    type_ = 'mailcap'
    init_inputs = [
        NodeInputBP(label='line'),
        NodeInputBP(label='i'),
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailcap.parsefield(self.input(0), self.input(1), self.input(2)))
        

class Parseline_Node(NodeBase):
    """
    Parse one entry in a mailcap file and return a dictionary.

    The viewing command is stored as the value with the key "view",
    and the rest of the fields produce key-value pairs in the dict.
    """
    
    title = 'parseline'
    type_ = 'mailcap'
    init_inputs = [
        NodeInputBP(label='line'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailcap.parseline(self.input(0)))
        

class Readmailcapfile_Node(NodeBase):
    """
    Read a mailcap file and return a dictionary keyed by MIME type."""
    
    title = 'readmailcapfile'
    type_ = 'mailcap'
    init_inputs = [
        NodeInputBP(label='fp'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailcap.readmailcapfile(self.input(0)))
        

class Show_Node(NodeBase):
    """
    """
    
    title = 'show'
    type_ = 'mailcap'
    init_inputs = [
        NodeInputBP(label='caps'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailcap.show(self.input(0)))
        

class Subst_Node(NodeBase):
    """
    """
    
    title = 'subst'
    type_ = 'mailcap'
    init_inputs = [
        NodeInputBP(label='field'),
        NodeInputBP(label='MIMEtype'),
        NodeInputBP(label='filename'),
        NodeInputBP(label='plist', dtype=dtypes.Data(default=[], size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailcap.subst(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Test_Node(NodeBase):
    """
    """
    
    title = 'test'
    type_ = 'mailcap'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mailcap.test())
        


export_nodes(
    _Readmailcapfile_Node,
    Findmatch_Node,
    Findparam_Node,
    Getcaps_Node,
    Lineno_Sort_Key_Node,
    Listmailcapfiles_Node,
    Lookup_Node,
    Parsefield_Node,
    Parseline_Node,
    Readmailcapfile_Node,
    Show_Node,
    Subst_Node,
    Test_Node,
)
