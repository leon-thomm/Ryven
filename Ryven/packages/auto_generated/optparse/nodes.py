import ryvencore_qt as rc
import optparse


class AutoNode_optparse__(rc.Node):
    title = '_'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='message'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, optparse._(self.input(0)))
        


class AutoNode_optparse__match_abbrev(rc.Node):
    title = '_match_abbrev'
    doc = '''_match_abbrev(s : string, wordmap : {string : Option}) -> string

    Return the string key in 'wordmap' for which 's' is an unambiguous
    abbreviation.  If 's' is found to be ambiguous or doesn't match any of
    'words', raise BadOptionError.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='wordmap'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, optparse._match_abbrev(self.input(0), self.input(1)))
        


class AutoNode_optparse__parse_int(rc.Node):
    title = '_parse_int'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='val'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, optparse._parse_int(self.input(0)))
        


class AutoNode_optparse__parse_num(rc.Node):
    title = '_parse_num'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='val'),
rc.NodeInputBP(label='type'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, optparse._parse_num(self.input(0), self.input(1)))
        


class AutoNode_optparse__repr(rc.Node):
    title = '_repr'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, optparse._repr(self.input(0)))
        


class AutoNode_optparse_check_builtin(rc.Node):
    title = 'check_builtin'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='option'),
rc.NodeInputBP(label='opt'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, optparse.check_builtin(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_optparse_check_choice(rc.Node):
    title = 'check_choice'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='option'),
rc.NodeInputBP(label='opt'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, optparse.check_choice(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_optparse_gettext(rc.Node):
    title = 'gettext'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='message'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, optparse.gettext(self.input(0)))
        


class AutoNode_optparse_ngettext(rc.Node):
    title = 'ngettext'
    doc = '''None'''
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
        self.set_output_val(0, optparse.ngettext(self.input(0), self.input(1), self.input(2)))
        