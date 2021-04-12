import ryvencore_qt as rc
import mimetypes


class AutoNode_mimetypes__default_mime_types(rc.Node):
    title = '_default_mime_types'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mimetypes._default_mime_types())
        


class AutoNode_mimetypes__main(rc.Node):
    title = '_main'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mimetypes._main())
        


class AutoNode_mimetypes_add_type(rc.Node):
    title = 'add_type'
    description = '''Add a mapping between a type and an extension.

    When the extension is already known, the new
    type will replace the old one. When the type
    is already known the extension will be added
    to the list of known extensions.

    If strict is true, information will be added to
    list of standard types, else to the list of non-standard
    types.
    '''
    init_inputs = [
        rc.NodeInputBP(label='type'),
rc.NodeInputBP(label='ext'),
rc.NodeInputBP(label='strict'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mimetypes.add_type(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_mimetypes_guess_all_extensions(rc.Node):
    title = 'guess_all_extensions'
    description = '''Guess the extensions for a file based on its MIME type.

    Return value is a list of strings giving the possible filename
    extensions, including the leading dot ('.').  The extension is not
    guaranteed to have been associated with any particular data
    stream, but would be mapped to the MIME type `type' by
    guess_type().  If no extension can be guessed for `type', None
    is returned.

    Optional `strict' argument when false adds a bunch of commonly found,
    but non-standard types.
    '''
    init_inputs = [
        rc.NodeInputBP(label='type'),
rc.NodeInputBP(label='strict'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mimetypes.guess_all_extensions(self.input(0), self.input(1)))
        


class AutoNode_mimetypes_guess_extension(rc.Node):
    title = 'guess_extension'
    description = '''Guess the extension for a file based on its MIME type.

    Return value is a string giving a filename extension, including the
    leading dot ('.').  The extension is not guaranteed to have been
    associated with any particular data stream, but would be mapped to the
    MIME type `type' by guess_type().  If no extension can be guessed for
    `type', None is returned.

    Optional `strict' argument when false adds a bunch of commonly found,
    but non-standard types.
    '''
    init_inputs = [
        rc.NodeInputBP(label='type'),
rc.NodeInputBP(label='strict'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mimetypes.guess_extension(self.input(0), self.input(1)))
        


class AutoNode_mimetypes_guess_type(rc.Node):
    title = 'guess_type'
    description = '''Guess the type of a file based on its URL.

    Return value is a tuple (type, encoding) where type is None if the
    type can't be guessed (no or unknown suffix) or a string of the
    form type/subtype, usable for a MIME Content-type header; and
    encoding is None for no encoding or the name of the program used
    to encode (e.g. compress or gzip).  The mappings are table
    driven.  Encoding suffixes are case sensitive; type suffixes are
    first tried case sensitive, then case insensitive.

    The suffixes .tgz, .taz and .tz (case sensitive!) are all mapped
    to ".tar.gz".  (This is table-driven too, using the dictionary
    suffix_map).

    Optional `strict' argument when false adds a bunch of commonly found, but
    non-standard types.
    '''
    init_inputs = [
        rc.NodeInputBP(label='url'),
rc.NodeInputBP(label='strict'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mimetypes.guess_type(self.input(0), self.input(1)))
        


class AutoNode_mimetypes_init(rc.Node):
    title = 'init'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='files'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mimetypes.init(self.input(0)))
        


class AutoNode_mimetypes_read_mime_types(rc.Node):
    title = 'read_mime_types'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='file'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, mimetypes.read_mime_types(self.input(0)))
        