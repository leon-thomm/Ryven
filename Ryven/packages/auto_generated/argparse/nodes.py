import ryvencore_qt as rc
import argparse


class AutoNode_argparse__(rc.Node):
    title = '_'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='message'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, argparse._(self.input(0)))
        


class AutoNode_argparse__copy_items(rc.Node):
    title = '_copy_items'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='items'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, argparse._copy_items(self.input(0)))
        


class AutoNode_argparse__get_action_name(rc.Node):
    title = '_get_action_name'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='argument'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, argparse._get_action_name(self.input(0)))
        


class AutoNode_argparse_ngettext(rc.Node):
    title = 'ngettext'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='msgid1'),
rc.NodeInputBP(label='msgid2'),
rc.NodeInputBP(label='n'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, argparse.ngettext(self.input(0), self.input(1), self.input(2)))
        