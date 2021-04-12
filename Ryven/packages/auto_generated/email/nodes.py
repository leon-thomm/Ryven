import ryvencore_qt as rc
import email


class AutoNode_email_message_from_binary_file(rc.Node):
    title = 'message_from_binary_file'
    description = '''Read a binary file and parse its contents into a Message object model.

    Optional _class and strict are passed to the Parser constructor.
    '''
    init_inputs = [
        rc.NodeInputBP(label='fp'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, email.message_from_binary_file(self.input(0)))
        


class AutoNode_email_message_from_bytes(rc.Node):
    title = 'message_from_bytes'
    description = '''Parse a bytes string into a Message object model.

    Optional _class and strict are passed to the Parser constructor.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, email.message_from_bytes(self.input(0)))
        


class AutoNode_email_message_from_file(rc.Node):
    title = 'message_from_file'
    description = '''Read a file and parse its contents into a Message object model.

    Optional _class and strict are passed to the Parser constructor.
    '''
    init_inputs = [
        rc.NodeInputBP(label='fp'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, email.message_from_file(self.input(0)))
        


class AutoNode_email_message_from_string(rc.Node):
    title = 'message_from_string'
    description = '''Parse a string into a Message object model.

    Optional _class and strict are passed to the Parser constructor.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, email.message_from_string(self.input(0)))
        