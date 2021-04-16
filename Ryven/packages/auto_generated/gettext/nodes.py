import ryvencore_qt as rc
import gettext


class AutoNode_gettext_Catalog(rc.Node):
    title = 'Catalog'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='domain'),
rc.NodeInputBP(label='localedir'),
rc.NodeInputBP(label='languages'),
rc.NodeInputBP(label='class_'),
rc.NodeInputBP(label='fallback'),
rc.NodeInputBP(label='codeset'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.Catalog(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode_gettext__as_int(rc.Node):
    title = '_as_int'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='n'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext._as_int(self.input(0)))
        


class AutoNode_gettext__error(rc.Node):
    title = '_error'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext._error(self.input(0)))
        


class AutoNode_gettext__expand_lang(rc.Node):
    title = '_expand_lang'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='loc'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext._expand_lang(self.input(0)))
        


class AutoNode_gettext__parse(rc.Node):
    title = '_parse'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='tokens'),
rc.NodeInputBP(label='priority'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext._parse(self.input(0), self.input(1)))
        


class AutoNode_gettext__tokenize(rc.Node):
    title = '_tokenize'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='plural'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext._tokenize(self.input(0)))
        


class AutoNode_gettext_bind_textdomain_codeset(rc.Node):
    title = 'bind_textdomain_codeset'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='domain'),
rc.NodeInputBP(label='codeset'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.bind_textdomain_codeset(self.input(0), self.input(1)))
        


class AutoNode_gettext_bindtextdomain(rc.Node):
    title = 'bindtextdomain'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='domain'),
rc.NodeInputBP(label='localedir'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.bindtextdomain(self.input(0), self.input(1)))
        


class AutoNode_gettext_c2py(rc.Node):
    title = 'c2py'
    doc = '''Gets a C expression as used in PO files for plural forms and returns a
    Python function that implements an equivalent expression.
    '''
    init_inputs = [
        rc.NodeInputBP(label='plural'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.c2py(self.input(0)))
        


class AutoNode_gettext_dgettext(rc.Node):
    title = 'dgettext'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='domain'),
rc.NodeInputBP(label='message'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.dgettext(self.input(0), self.input(1)))
        


class AutoNode_gettext_dngettext(rc.Node):
    title = 'dngettext'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='domain'),
rc.NodeInputBP(label='msgid1'),
rc.NodeInputBP(label='msgid2'),
rc.NodeInputBP(label='n'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.dngettext(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_gettext_dnpgettext(rc.Node):
    title = 'dnpgettext'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='domain'),
rc.NodeInputBP(label='context'),
rc.NodeInputBP(label='msgid1'),
rc.NodeInputBP(label='msgid2'),
rc.NodeInputBP(label='n'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.dnpgettext(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        


class AutoNode_gettext_dpgettext(rc.Node):
    title = 'dpgettext'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='domain'),
rc.NodeInputBP(label='context'),
rc.NodeInputBP(label='message'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.dpgettext(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_gettext_find(rc.Node):
    title = 'find'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='domain'),
rc.NodeInputBP(label='localedir'),
rc.NodeInputBP(label='languages'),
rc.NodeInputBP(label='all'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.find(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_gettext_gettext(rc.Node):
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
        self.set_output_val(0, gettext.gettext(self.input(0)))
        


class AutoNode_gettext_install(rc.Node):
    title = 'install'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='domain'),
rc.NodeInputBP(label='localedir'),
rc.NodeInputBP(label='codeset'),
rc.NodeInputBP(label='names'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.install(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_gettext_ldgettext(rc.Node):
    title = 'ldgettext'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='domain'),
rc.NodeInputBP(label='message'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.ldgettext(self.input(0), self.input(1)))
        


class AutoNode_gettext_ldngettext(rc.Node):
    title = 'ldngettext'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='domain'),
rc.NodeInputBP(label='msgid1'),
rc.NodeInputBP(label='msgid2'),
rc.NodeInputBP(label='n'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.ldngettext(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_gettext_lgettext(rc.Node):
    title = 'lgettext'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='message'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.lgettext(self.input(0)))
        


class AutoNode_gettext_lngettext(rc.Node):
    title = 'lngettext'
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
        self.set_output_val(0, gettext.lngettext(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_gettext_ngettext(rc.Node):
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
        self.set_output_val(0, gettext.ngettext(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_gettext_npgettext(rc.Node):
    title = 'npgettext'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='context'),
rc.NodeInputBP(label='msgid1'),
rc.NodeInputBP(label='msgid2'),
rc.NodeInputBP(label='n'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.npgettext(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_gettext_pgettext(rc.Node):
    title = 'pgettext'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='context'),
rc.NodeInputBP(label='message'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.pgettext(self.input(0), self.input(1)))
        


class AutoNode_gettext_textdomain(rc.Node):
    title = 'textdomain'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='domain'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.textdomain(self.input(0)))
        


class AutoNode_gettext_translation(rc.Node):
    title = 'translation'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='domain'),
rc.NodeInputBP(label='localedir'),
rc.NodeInputBP(label='languages'),
rc.NodeInputBP(label='class_'),
rc.NodeInputBP(label='fallback'),
rc.NodeInputBP(label='codeset'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, gettext.translation(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        