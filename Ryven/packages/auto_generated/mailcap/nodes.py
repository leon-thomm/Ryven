import ryvencore_qt as rc
import mailcap


class AutoNode_mailcap__readmailcapfile(rc.Node):
    title = '_readmailcapfile'
    doc = '''Read a mailcap file and return a dictionary keyed by MIME type.

    Each MIME type is mapped to an entry consisting of a list of
    dictionaries; the list will contain more than one such dictionary
    if a given MIME type appears more than once in the mailcap file.
    Each dictionary contains key-value pairs for that MIME type, where
    the viewing command is stored with the key "view".
    '''
    init_inputs = [
        rc.NodeInputBP(label='fp'),
rc.NodeInputBP(label='lineno'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailcap._readmailcapfile(self.input(0), self.input(1)))
        


class AutoNode_mailcap_findmatch(rc.Node):
    title = 'findmatch'
    doc = '''Find a match for a mailcap entry.

    Return a tuple containing the command line, and the mailcap entry
    used; (None, None) if no match is found.  This may invoke the
    'test' command of several matching entries before deciding which
    entry to use.

    '''
    init_inputs = [
        rc.NodeInputBP(label='caps'),
rc.NodeInputBP(label='MIMEtype'),
rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='plist'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailcap.findmatch(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_mailcap_findparam(rc.Node):
    title = 'findparam'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='plist'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailcap.findparam(self.input(0), self.input(1)))
        


class AutoNode_mailcap_getcaps(rc.Node):
    title = 'getcaps'
    doc = '''Return a dictionary containing the mailcap database.

    The dictionary maps a MIME type (in all lowercase, e.g. 'text/plain')
    to a list of dictionaries corresponding to mailcap entries.  The list
    collects all the entries for that MIME type from all available mailcap
    files.  Each dictionary contains key-value pairs for that MIME type,
    where the viewing command is stored with the key "view".

    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailcap.getcaps())
        


class AutoNode_mailcap_lineno_sort_key(rc.Node):
    title = 'lineno_sort_key'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='entry'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailcap.lineno_sort_key(self.input(0)))
        


class AutoNode_mailcap_listmailcapfiles(rc.Node):
    title = 'listmailcapfiles'
    doc = '''Return a list of all mailcap files found on the system.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailcap.listmailcapfiles())
        


class AutoNode_mailcap_lookup(rc.Node):
    title = 'lookup'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='caps'),
rc.NodeInputBP(label='MIMEtype'),
rc.NodeInputBP(label='key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailcap.lookup(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_mailcap_parsefield(rc.Node):
    title = 'parsefield'
    doc = '''Separate one key-value pair in a mailcap entry.'''
    init_inputs = [
        rc.NodeInputBP(label='line'),
rc.NodeInputBP(label='i'),
rc.NodeInputBP(label='n'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailcap.parsefield(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_mailcap_parseline(rc.Node):
    title = 'parseline'
    doc = '''Parse one entry in a mailcap file and return a dictionary.

    The viewing command is stored as the value with the key "view",
    and the rest of the fields produce key-value pairs in the dict.
    '''
    init_inputs = [
        rc.NodeInputBP(label='line'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailcap.parseline(self.input(0)))
        


class AutoNode_mailcap_readmailcapfile(rc.Node):
    title = 'readmailcapfile'
    doc = '''Read a mailcap file and return a dictionary keyed by MIME type.'''
    init_inputs = [
        rc.NodeInputBP(label='fp'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailcap.readmailcapfile(self.input(0)))
        


class AutoNode_mailcap_show(rc.Node):
    title = 'show'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='caps'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailcap.show(self.input(0)))
        


class AutoNode_mailcap_subst(rc.Node):
    title = 'subst'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='field'),
rc.NodeInputBP(label='MIMEtype'),
rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='plist'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailcap.subst(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_mailcap_test(rc.Node):
    title = 'test'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailcap.test())
        