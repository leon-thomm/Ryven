import ryvencore_qt as rc
import mailbox


class AutoNode_mailbox__create_carefully(rc.Node):
    title = '_create_carefully'
    doc = '''Create a file if it doesn't exist and open for reading and writing.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailbox._create_carefully(self.input(0)))
        


class AutoNode_mailbox__create_temporary(rc.Node):
    title = '_create_temporary'
    doc = '''Create a temp file based on path and open for reading and writing.'''
    init_inputs = [
        rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailbox._create_temporary(self.input(0)))
        


class AutoNode_mailbox__lock_file(rc.Node):
    title = '_lock_file'
    doc = '''Lock file f using lockf and dot locking.'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
rc.NodeInputBP(label='dotlock'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailbox._lock_file(self.input(0), self.input(1)))
        


class AutoNode_mailbox__sync_close(rc.Node):
    title = '_sync_close'
    doc = '''Close file f, ensuring all changes are physically on disk.'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailbox._sync_close(self.input(0)))
        


class AutoNode_mailbox__sync_flush(rc.Node):
    title = '_sync_flush'
    doc = '''Ensure changes to file f are physically on disk.'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailbox._sync_flush(self.input(0)))
        


class AutoNode_mailbox__unlock_file(rc.Node):
    title = '_unlock_file'
    doc = '''Unlock file f using lockf and dot locking.'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mailbox._unlock_file(self.input(0)))
        