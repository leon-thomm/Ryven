
from ryven.NENV import *

import locale


class NodeBase(Node):
    pass


class _Append_Modifier_Node(NodeBase):
    """
    """
    
    title = '_append_modifier'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='modifier'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale._append_modifier(self.input(0), self.input(1)))
        

class _Build_Localename_Node(NodeBase):
    """
     Builds a locale code from the given tuple (language code,
        encoding).

        No aliasing or normalizing takes place.

    """
    
    title = '_build_localename'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='localetuple'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale._build_localename(self.input(0)))
        

class _Format_Node(NodeBase):
    """
    """
    
    title = '_format'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='percent'),
        NodeInputBP(label='value'),
        NodeInputBP(label='grouping', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='monetary', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale._format(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class _Group_Node(NodeBase):
    """
    """
    
    title = '_group'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='monetary', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale._group(self.input(0), self.input(1)))
        

class _Grouping_Intervals_Node(NodeBase):
    """
    """
    
    title = '_grouping_intervals'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='grouping'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale._grouping_intervals(self.input(0)))
        

class _Parse_Localename_Node(NodeBase):
    """
     Parses the locale code for localename and returns the
        result as tuple (language code, encoding).

        The localename is normalized and passed through the locale
        alias engine. A ValueError is raised in case the locale name
        cannot be parsed.

        The language code corresponds to RFC 1766.  code and encoding
        can be None in case the values cannot be determined or are
        unknown to this implementation.

    """
    
    title = '_parse_localename'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='localename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale._parse_localename(self.input(0)))
        

class _Print_Locale_Node(NodeBase):
    """
     Test function.
    """
    
    title = '_print_locale'
    type_ = 'locale'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale._print_locale())
        

class _Replace_Encoding_Node(NodeBase):
    """
    """
    
    title = '_replace_encoding'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale._replace_encoding(self.input(0), self.input(1)))
        

class _Strcoll_Node(NodeBase):
    """
     strcoll(string,string) -> int.
        Compares two strings according to the locale.
    """
    
    title = '_strcoll'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale._strcoll(self.input(0), self.input(1)))
        

class _Strip_Padding_Node(NodeBase):
    """
    """
    
    title = '_strip_padding'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='amount'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale._strip_padding(self.input(0), self.input(1)))
        

class _Strxfrm_Node(NodeBase):
    """
     strxfrm(string) -> string.
        Returns a string that behaves for cmp locale-aware.
    """
    
    title = '_strxfrm'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale._strxfrm(self.input(0)))
        

class _Test_Node(NodeBase):
    """
    """
    
    title = '_test'
    type_ = 'locale'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale._test())
        

class Atof_Node(NodeBase):
    """
    Parses a string as a float according to the locale settings."""
    
    title = 'atof'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='string'),
        NodeInputBP(label='func', dtype=dtypes.Data(default=float, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.atof(self.input(0), self.input(1)))
        

class Atoi_Node(NodeBase):
    """
    Converts a string to an integer according to the locale settings."""
    
    title = 'atoi'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='string'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.atoi(self.input(0)))
        

class Currency_Node(NodeBase):
    """
    Formats val according to the currency settings
    in the current locale."""
    
    title = 'currency'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='val'),
        NodeInputBP(label='symbol', dtype=dtypes.Data(default=True, size='s')),
        NodeInputBP(label='grouping', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='international', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.currency(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Delocalize_Node(NodeBase):
    """
    Parses a string as a normalized number according to the locale settings."""
    
    title = 'delocalize'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='string'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.delocalize(self.input(0)))
        

class Format_Node(NodeBase):
    """
    Deprecated, use format_string instead."""
    
    title = 'format'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='percent'),
        NodeInputBP(label='value'),
        NodeInputBP(label='grouping', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='monetary', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.format(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Format_String_Node(NodeBase):
    """
    Formats a string in the same way that the % formatting would use,
    but takes the current locale into account.

    Grouping is applied if the third parameter is true.
    Conversion uses monetary thousands separator and grouping strings if
    forth parameter monetary is true."""
    
    title = 'format_string'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='f'),
        NodeInputBP(label='val'),
        NodeInputBP(label='grouping', dtype=dtypes.Data(default=False, size='s')),
        NodeInputBP(label='monetary', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.format_string(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Getdefaultlocale_Node(NodeBase):
    """
     Tries to determine the default locale settings and returns
        them as tuple (language code, encoding).

        According to POSIX, a program which has not called
        setlocale(LC_ALL, "") runs using the portable 'C' locale.
        Calling setlocale(LC_ALL, "") lets it use the default locale as
        defined by the LANG variable. Since we don't want to interfere
        with the current locale setting we thus emulate the behavior
        in the way described above.

        To maintain compatibility with other platforms, not only the
        LANG variable is tested, but a list of variables given as
        envvars parameter. The first found to be defined will be
        used. envvars defaults to the search path used in GNU gettext;
        it must always contain the variable name 'LANG'.

        Except for the code 'C', the language code corresponds to RFC
        1766.  code and encoding can be None in case the values cannot
        be determined.

    """
    
    title = 'getdefaultlocale'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='envvars', dtype=dtypes.Data(default=('LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE'), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.getdefaultlocale(self.input(0)))
        

class Getlocale_Node(NodeBase):
    """
     Returns the current setting for the given locale category as
        tuple (language code, encoding).

        category may be one of the LC_* value except LC_ALL. It
        defaults to LC_CTYPE.

        Except for the code 'C', the language code corresponds to RFC
        1766.  code and encoding can be None in case the values cannot
        be determined.

    """
    
    title = 'getlocale'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='category', dtype=dtypes.Data(default=2, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.getlocale(self.input(0)))
        

class Getpreferredencoding_Node(NodeBase):
    """
    Return the charset that the user is likely using."""
    
    title = 'getpreferredencoding'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='do_setlocale', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.getpreferredencoding(self.input(0)))
        

class Localeconv_Node(NodeBase):
    """
    () -> dict. Returns numeric and monetary locale-specific parameters."""
    
    title = 'localeconv'
    type_ = 'locale'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.localeconv())
        

class Normalize_Node(NodeBase):
    """
     Returns a normalized locale code for the given locale
        name.

        The returned locale code is formatted for use with
        setlocale().

        If normalization fails, the original name is returned
        unchanged.

        If the given encoding is not known, the function defaults to
        the default encoding for the locale code just like setlocale()
        does.

    """
    
    title = 'normalize'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='localename'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.normalize(self.input(0)))
        

class Resetlocale_Node(NodeBase):
    """
     Sets the locale for category to the default setting.

        The default setting is determined by calling
        getdefaultlocale(). category defaults to LC_ALL.

    """
    
    title = 'resetlocale'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='category', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.resetlocale(self.input(0)))
        

class Setlocale_Node(NodeBase):
    """
     Set the locale for the given category.  The locale can be
        a string, an iterable of two strings (language code and encoding),
        or None.

        Iterables are converted to strings using the locale aliasing
        engine.  Locale strings are passed directly to the C lib.

        category may be given as one of the LC_* values.

    """
    
    title = 'setlocale'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='category'),
        NodeInputBP(label='locale', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.setlocale(self.input(0), self.input(1)))
        

class Str_Node(NodeBase):
    """
    Convert float to string, taking the locale into account."""
    
    title = 'str'
    type_ = 'locale'
    init_inputs = [
        NodeInputBP(label='val'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, locale.str(self.input(0)))
        


export_nodes(
    _Append_Modifier_Node,
    _Build_Localename_Node,
    _Format_Node,
    _Group_Node,
    _Grouping_Intervals_Node,
    _Parse_Localename_Node,
    _Print_Locale_Node,
    _Replace_Encoding_Node,
    _Strcoll_Node,
    _Strip_Padding_Node,
    _Strxfrm_Node,
    _Test_Node,
    Atof_Node,
    Atoi_Node,
    Currency_Node,
    Delocalize_Node,
    Format_Node,
    Format_String_Node,
    Getdefaultlocale_Node,
    Getlocale_Node,
    Getpreferredencoding_Node,
    Localeconv_Node,
    Normalize_Node,
    Resetlocale_Node,
    Setlocale_Node,
    Str_Node,
)
