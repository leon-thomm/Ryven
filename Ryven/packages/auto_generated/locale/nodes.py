import ryvencore_qt as rc
import locale


class AutoNode_locale__append_modifier(rc.Node):
    title = '_append_modifier'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='code'),
rc.NodeInputBP(label='modifier'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale._append_modifier(self.input(0), self.input(1)))
        


class AutoNode_locale__build_localename(rc.Node):
    title = '_build_localename'
    description = ''' Builds a locale code from the given tuple (language code,
        encoding).

        No aliasing or normalizing takes place.

    '''
    init_inputs = [
        rc.NodeInputBP(label='localetuple'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale._build_localename(self.input(0)))
        


class AutoNode_locale__format(rc.Node):
    title = '_format'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='percent'),
rc.NodeInputBP(label='value'),
rc.NodeInputBP(label='grouping'),
rc.NodeInputBP(label='monetary'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale._format(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_locale__group(rc.Node):
    title = '_group'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='monetary'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale._group(self.input(0), self.input(1)))
        


class AutoNode_locale__grouping_intervals(rc.Node):
    title = '_grouping_intervals'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='grouping'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale._grouping_intervals(self.input(0)))
        


class AutoNode_locale__parse_localename(rc.Node):
    title = '_parse_localename'
    description = ''' Parses the locale code for localename and returns the
        result as tuple (language code, encoding).

        The localename is normalized and passed through the locale
        alias engine. A ValueError is raised in case the locale name
        cannot be parsed.

        The language code corresponds to RFC 1766.  code and encoding
        can be None in case the values cannot be determined or are
        unknown to this implementation.

    '''
    init_inputs = [
        rc.NodeInputBP(label='localename'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale._parse_localename(self.input(0)))
        


class AutoNode_locale__print_locale(rc.Node):
    title = '_print_locale'
    description = ''' Test function.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale._print_locale())
        


class AutoNode_locale__replace_encoding(rc.Node):
    title = '_replace_encoding'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='code'),
rc.NodeInputBP(label='encoding'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale._replace_encoding(self.input(0), self.input(1)))
        


class AutoNode_locale__strcoll(rc.Node):
    title = '_strcoll'
    description = ''' strcoll(string,string) -> int.
        Compares two strings according to the locale.
    '''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale._strcoll(self.input(0), self.input(1)))
        


class AutoNode_locale__strip_padding(rc.Node):
    title = '_strip_padding'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='s'),
rc.NodeInputBP(label='amount'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale._strip_padding(self.input(0), self.input(1)))
        


class AutoNode_locale__strxfrm(rc.Node):
    title = '_strxfrm'
    description = ''' strxfrm(string) -> string.
        Returns a string that behaves for cmp locale-aware.
    '''
    init_inputs = [
        rc.NodeInputBP(label='s'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale._strxfrm(self.input(0)))
        


class AutoNode_locale__test(rc.Node):
    title = '_test'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale._test())
        


class AutoNode_locale_atof(rc.Node):
    title = 'atof'
    description = '''Parses a string as a float according to the locale settings.'''
    init_inputs = [
        rc.NodeInputBP(label='string'),
rc.NodeInputBP(label='func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.atof(self.input(0), self.input(1)))
        


class AutoNode_locale_atoi(rc.Node):
    title = 'atoi'
    description = '''Converts a string to an integer according to the locale settings.'''
    init_inputs = [
        rc.NodeInputBP(label='string'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.atoi(self.input(0)))
        


class AutoNode_locale_currency(rc.Node):
    title = 'currency'
    description = '''Formats val according to the currency settings
    in the current locale.'''
    init_inputs = [
        rc.NodeInputBP(label='val'),
rc.NodeInputBP(label='symbol'),
rc.NodeInputBP(label='grouping'),
rc.NodeInputBP(label='international'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.currency(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_locale_delocalize(rc.Node):
    title = 'delocalize'
    description = '''Parses a string as a normalized number according to the locale settings.'''
    init_inputs = [
        rc.NodeInputBP(label='string'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.delocalize(self.input(0)))
        


class AutoNode_locale_format(rc.Node):
    title = 'format'
    description = '''Deprecated, use format_string instead.'''
    init_inputs = [
        rc.NodeInputBP(label='percent'),
rc.NodeInputBP(label='value'),
rc.NodeInputBP(label='grouping'),
rc.NodeInputBP(label='monetary'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.format(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_locale_format_string(rc.Node):
    title = 'format_string'
    description = '''Formats a string in the same way that the % formatting would use,
    but takes the current locale into account.

    Grouping is applied if the third parameter is true.
    Conversion uses monetary thousands separator and grouping strings if
    forth parameter monetary is true.'''
    init_inputs = [
        rc.NodeInputBP(label='f'),
rc.NodeInputBP(label='val'),
rc.NodeInputBP(label='grouping'),
rc.NodeInputBP(label='monetary'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.format_string(self.input(0), self.input(1), self.input(2), self.input(3)))
        


class AutoNode_locale_getdefaultlocale(rc.Node):
    title = 'getdefaultlocale'
    description = ''' Tries to determine the default locale settings and returns
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

    '''
    init_inputs = [
        rc.NodeInputBP(label='envvars'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.getdefaultlocale(self.input(0)))
        


class AutoNode_locale_getlocale(rc.Node):
    title = 'getlocale'
    description = ''' Returns the current setting for the given locale category as
        tuple (language code, encoding).

        category may be one of the LC_* value except LC_ALL. It
        defaults to LC_CTYPE.

        Except for the code 'C', the language code corresponds to RFC
        1766.  code and encoding can be None in case the values cannot
        be determined.

    '''
    init_inputs = [
        rc.NodeInputBP(label='category'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.getlocale(self.input(0)))
        


class AutoNode_locale_getpreferredencoding(rc.Node):
    title = 'getpreferredencoding'
    description = '''Return the charset that the user is likely using.'''
    init_inputs = [
        rc.NodeInputBP(label='do_setlocale'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.getpreferredencoding(self.input(0)))
        


class AutoNode_locale_localeconv(rc.Node):
    title = 'localeconv'
    description = '''() -> dict. Returns numeric and monetary locale-specific parameters.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.localeconv())
        


class AutoNode_locale_normalize(rc.Node):
    title = 'normalize'
    description = ''' Returns a normalized locale code for the given locale
        name.

        The returned locale code is formatted for use with
        setlocale().

        If normalization fails, the original name is returned
        unchanged.

        If the given encoding is not known, the function defaults to
        the default encoding for the locale code just like setlocale()
        does.

    '''
    init_inputs = [
        rc.NodeInputBP(label='localename'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.normalize(self.input(0)))
        


class AutoNode_locale_resetlocale(rc.Node):
    title = 'resetlocale'
    description = ''' Sets the locale for category to the default setting.

        The default setting is determined by calling
        getdefaultlocale(). category defaults to LC_ALL.

    '''
    init_inputs = [
        rc.NodeInputBP(label='category'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.resetlocale(self.input(0)))
        


class AutoNode_locale_setlocale(rc.Node):
    title = 'setlocale'
    description = ''' Set the locale for the given category.  The locale can be
        a string, an iterable of two strings (language code and encoding),
        or None.

        Iterables are converted to strings using the locale aliasing
        engine.  Locale strings are passed directly to the C lib.

        category may be given as one of the LC_* values.

    '''
    init_inputs = [
        rc.NodeInputBP(label='category'),
rc.NodeInputBP(label='locale'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.setlocale(self.input(0), self.input(1)))
        


class AutoNode_locale_str(rc.Node):
    title = 'str'
    description = '''Convert float to string, taking the locale into account.'''
    init_inputs = [
        rc.NodeInputBP(label='val'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, locale.str(self.input(0)))
        