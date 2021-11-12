
from ryven.NENV import *

import gettext


class NodeBase(Node):
    pass


class Catalog_Node(NodeBase):
    """
    """
    
    title = 'Catalog'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='domain'),
        NodeInputBP(label='localedir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='languages', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='class_', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='fallback', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='codeset', dtype=dtypes.Data(default=['unspecified'], size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.Catalog(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class _As_Int_Node(NodeBase):
    """
    """
    
    title = '_as_int'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext._as_int(self.input(0)))
        

class _Error_Node(NodeBase):
    """
    """
    
    title = '_error'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext._error(self.input(0)))
        

class _Expand_Lang_Node(NodeBase):
    """
    """
    
    title = '_expand_lang'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='loc'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext._expand_lang(self.input(0)))
        

class _Parse_Node(NodeBase):
    """
    """
    
    title = '_parse'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='tokens'),
        NodeInputBP(label='priority', dtype=dtypes.Data(default=-1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext._parse(self.input(0), self.input(1)))
        

class _Tokenize_Node(NodeBase):
    """
    """
    
    title = '_tokenize'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='plural'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext._tokenize(self.input(0)))
        

class Bind_Textdomain_Codeset_Node(NodeBase):
    """
    """
    
    title = 'bind_textdomain_codeset'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='domain'),
        NodeInputBP(label='codeset', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.bind_textdomain_codeset(self.input(0), self.input(1)))
        

class Bindtextdomain_Node(NodeBase):
    """
    """
    
    title = 'bindtextdomain'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='domain'),
        NodeInputBP(label='localedir', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.bindtextdomain(self.input(0), self.input(1)))
        

class C2Py_Node(NodeBase):
    """
    Gets a C expression as used in PO files for plural forms and returns a
    Python function that implements an equivalent expression.
    """
    
    title = 'c2py'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='plural'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.c2py(self.input(0)))
        

class Dgettext_Node(NodeBase):
    """
    """
    
    title = 'dgettext'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='domain'),
        NodeInputBP(label='message'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.dgettext(self.input(0), self.input(1)))
        

class Dngettext_Node(NodeBase):
    """
    """
    
    title = 'dngettext'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='domain'),
        NodeInputBP(label='msgid1'),
        NodeInputBP(label='msgid2'),
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.dngettext(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Dnpgettext_Node(NodeBase):
    """
    """
    
    title = 'dnpgettext'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='domain'),
        NodeInputBP(label='context'),
        NodeInputBP(label='msgid1'),
        NodeInputBP(label='msgid2'),
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.dnpgettext(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Dpgettext_Node(NodeBase):
    """
    """
    
    title = 'dpgettext'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='domain'),
        NodeInputBP(label='context'),
        NodeInputBP(label='message'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.dpgettext(self.input(0), self.input(1), self.input(2)))
        

class Find_Node(NodeBase):
    """
    """
    
    title = 'find'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='domain'),
        NodeInputBP(label='localedir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='languages', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='all', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.find(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Gettext_Node(NodeBase):
    """
    """
    
    title = 'gettext'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='message'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.gettext(self.input(0)))
        

class Install_Node(NodeBase):
    """
    """
    
    title = 'install'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='domain'),
        NodeInputBP(label='localedir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='codeset', dtype=dtypes.Data(default=['unspecified'], size='s')),
        NodeInputBP(label='names', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.install(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Ldgettext_Node(NodeBase):
    """
    """
    
    title = 'ldgettext'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='domain'),
        NodeInputBP(label='message'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.ldgettext(self.input(0), self.input(1)))
        

class Ldngettext_Node(NodeBase):
    """
    """
    
    title = 'ldngettext'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='domain'),
        NodeInputBP(label='msgid1'),
        NodeInputBP(label='msgid2'),
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.ldngettext(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Lgettext_Node(NodeBase):
    """
    """
    
    title = 'lgettext'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='message'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.lgettext(self.input(0)))
        

class Lngettext_Node(NodeBase):
    """
    """
    
    title = 'lngettext'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='msgid1'),
        NodeInputBP(label='msgid2'),
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.lngettext(self.input(0), self.input(1), self.input(2)))
        

class Ngettext_Node(NodeBase):
    """
    """
    
    title = 'ngettext'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='msgid1'),
        NodeInputBP(label='msgid2'),
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.ngettext(self.input(0), self.input(1), self.input(2)))
        

class Npgettext_Node(NodeBase):
    """
    """
    
    title = 'npgettext'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='context'),
        NodeInputBP(label='msgid1'),
        NodeInputBP(label='msgid2'),
        NodeInputBP(label='n'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.npgettext(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Pgettext_Node(NodeBase):
    """
    """
    
    title = 'pgettext'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='context'),
        NodeInputBP(label='message'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.pgettext(self.input(0), self.input(1)))
        

class Textdomain_Node(NodeBase):
    """
    """
    
    title = 'textdomain'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='domain', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.textdomain(self.input(0)))
        

class Translation_Node(NodeBase):
    """
    """
    
    title = 'translation'
    type_ = 'gettext'
    init_inputs = [
        NodeInputBP(label='domain'),
        NodeInputBP(label='localedir', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='languages', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='class_', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='fallback', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='codeset', dtype=dtypes.Data(default=['unspecified'], size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, gettext.translation(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


export_nodes(
    Catalog_Node,
    _As_Int_Node,
    _Error_Node,
    _Expand_Lang_Node,
    _Parse_Node,
    _Tokenize_Node,
    Bind_Textdomain_Codeset_Node,
    Bindtextdomain_Node,
    C2Py_Node,
    Dgettext_Node,
    Dngettext_Node,
    Dnpgettext_Node,
    Dpgettext_Node,
    Find_Node,
    Gettext_Node,
    Install_Node,
    Ldgettext_Node,
    Ldngettext_Node,
    Lgettext_Node,
    Lngettext_Node,
    Ngettext_Node,
    Npgettext_Node,
    Pgettext_Node,
    Textdomain_Node,
    Translation_Node,
)
