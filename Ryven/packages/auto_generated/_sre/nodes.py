
from NENV import *

import _sre


class NodeBase(Node):
    pass


class AutoNode__sre_ascii_iscased(NodeBase):
    title = 'ascii_iscased'
    type_ = '_sre'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='character'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sre.ascii_iscased(self.input(0)))
        

class AutoNode__sre_ascii_tolower(NodeBase):
    title = 'ascii_tolower'
    type_ = '_sre'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='character'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sre.ascii_tolower(self.input(0)))
        

class AutoNode__sre_compile(NodeBase):
    title = 'compile'
    type_ = '_sre'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='pattern'),
        NodeInputBP(label='flags'),
        NodeInputBP(label='code'),
        NodeInputBP(label='groups'),
        NodeInputBP(label='groupindex'),
        NodeInputBP(label='indexgroup'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sre.compile(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class AutoNode__sre_getcodesize(NodeBase):
    title = 'getcodesize'
    type_ = '_sre'
    doc = """"""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sre.getcodesize())
        

class AutoNode__sre_unicode_iscased(NodeBase):
    title = 'unicode_iscased'
    type_ = '_sre'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='character'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sre.unicode_iscased(self.input(0)))
        

class AutoNode__sre_unicode_tolower(NodeBase):
    title = 'unicode_tolower'
    type_ = '_sre'
    doc = """"""
    init_inputs = [
        NodeInputBP(label='character'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _sre.unicode_tolower(self.input(0)))
        


export_nodes(
    AutoNode__sre_ascii_iscased,
    AutoNode__sre_ascii_tolower,
    AutoNode__sre_compile,
    AutoNode__sre_getcodesize,
    AutoNode__sre_unicode_iscased,
    AutoNode__sre_unicode_tolower,
)
