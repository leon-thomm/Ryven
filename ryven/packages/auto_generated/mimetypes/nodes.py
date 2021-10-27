
from NENV import *

import mimetypes


class NodeBase(Node):
    pass


class _Default_Mime_Types_Node(NodeBase):
    """
    """
    
    title = '_default_mime_types'
    type_ = 'mimetypes'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mimetypes._default_mime_types())
        

class _Main_Node(NodeBase):
    """
    """
    
    title = '_main'
    type_ = 'mimetypes'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mimetypes._main())
        

class Add_Type_Node(NodeBase):
    """
    Add a mapping between a type and an extension.

    When the extension is already known, the new
    type will replace the old one. When the type
    is already known the extension will be added
    to the list of known extensions.

    If strict is true, information will be added to
    list of standard types, else to the list of non-standard
    types.
    """
    
    title = 'add_type'
    type_ = 'mimetypes'
    init_inputs = [
        NodeInputBP(label='type'),
        NodeInputBP(label='ext'),
        NodeInputBP(label='strict', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mimetypes.add_type(self.input(0), self.input(1), self.input(2)))
        

class Guess_All_Extensions_Node(NodeBase):
    """
    Guess the extensions for a file based on its MIME type.

    Return value is a list of strings giving the possible filename
    extensions, including the leading dot ('.').  The extension is not
    guaranteed to have been associated with any particular data
    stream, but would be mapped to the MIME type `type' by
    guess_type().  If no extension can be guessed for `type', None
    is returned.

    Optional `strict' argument when false adds a bunch of commonly found,
    but non-standard types.
    """
    
    title = 'guess_all_extensions'
    type_ = 'mimetypes'
    init_inputs = [
        NodeInputBP(label='type'),
        NodeInputBP(label='strict', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mimetypes.guess_all_extensions(self.input(0), self.input(1)))
        

class Guess_Extension_Node(NodeBase):
    """
    Guess the extension for a file based on its MIME type.

    Return value is a string giving a filename extension, including the
    leading dot ('.').  The extension is not guaranteed to have been
    associated with any particular data stream, but would be mapped to the
    MIME type `type' by guess_type().  If no extension can be guessed for
    `type', None is returned.

    Optional `strict' argument when false adds a bunch of commonly found,
    but non-standard types.
    """
    
    title = 'guess_extension'
    type_ = 'mimetypes'
    init_inputs = [
        NodeInputBP(label='type'),
        NodeInputBP(label='strict', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mimetypes.guess_extension(self.input(0), self.input(1)))
        

class Guess_Type_Node(NodeBase):
    """
    Guess the type of a file based on its URL.

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
    """
    
    title = 'guess_type'
    type_ = 'mimetypes'
    init_inputs = [
        NodeInputBP(label='url'),
        NodeInputBP(label='strict', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mimetypes.guess_type(self.input(0), self.input(1)))
        

class Init_Node(NodeBase):
    """
    """
    
    title = 'init'
    type_ = 'mimetypes'
    init_inputs = [
        NodeInputBP(label='files', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mimetypes.init(self.input(0)))
        

class Read_Mime_Types_Node(NodeBase):
    """
    """
    
    title = 'read_mime_types'
    type_ = 'mimetypes'
    init_inputs = [
        NodeInputBP(label='file'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, mimetypes.read_mime_types(self.input(0)))
        


export_nodes(
    _Default_Mime_Types_Node,
    _Main_Node,
    Add_Type_Node,
    Guess_All_Extensions_Node,
    Guess_Extension_Node,
    Guess_Type_Node,
    Init_Node,
    Read_Mime_Types_Node,
)
