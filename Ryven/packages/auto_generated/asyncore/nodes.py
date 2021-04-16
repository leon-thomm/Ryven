import ryvencore_qt as rc
import asyncore


class AutoNode_asyncore__exception(rc.Node):
    title = '_exception'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncore._exception(self.input(0)))
        


class AutoNode_asyncore__strerror(rc.Node):
    title = '_strerror'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='err'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncore._strerror(self.input(0)))
        


class AutoNode_asyncore_close_all(rc.Node):
    title = 'close_all'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='map'),
rc.NodeInputBP(label='ignore_all'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncore.close_all(self.input(0), self.input(1)))
        


class AutoNode_asyncore_compact_traceback(rc.Node):
    title = 'compact_traceback'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncore.compact_traceback())
        


class AutoNode_asyncore_loop(rc.Node):
    title = 'loop'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='timeout'),
rc.NodeInputBP(label='use_poll'),
rc.NodeInputBP(label='map'),
rc.NodeInputBP(label='count'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncore.loop(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_asyncore_poll(rc.Node):
    title = 'poll'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='timeout'),
rc.NodeInputBP(label='map'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncore.poll(self.input(0), self.input(1)))
        


class AutoNode_asyncore_poll2(rc.Node):
    title = 'poll2'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='timeout'),
rc.NodeInputBP(label='map'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncore.poll2(self.input(0), self.input(1)))
        


class AutoNode_asyncore_poll3(rc.Node):
    title = 'poll3'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='timeout'),
rc.NodeInputBP(label='map'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncore.poll3(self.input(0), self.input(1)))
        


class AutoNode_asyncore_read(rc.Node):
    title = 'read'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncore.read(self.input(0)))
        


class AutoNode_asyncore_readwrite(rc.Node):
    title = 'readwrite'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
rc.NodeInputBP(label='flags'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncore.readwrite(self.input(0), self.input(1)))
        


class AutoNode_asyncore_write(rc.Node):
    title = 'write'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, asyncore.write(self.input(0)))
        