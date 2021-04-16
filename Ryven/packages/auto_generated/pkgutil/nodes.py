import ryvencore_qt as rc
import pkgutil


class AutoNode_pkgutil__get_spec(rc.Node):
    title = '_get_spec'
    description = '''Return the finder-specific module spec.'''
    init_inputs = [
        rc.NodeInputBP(label='finder'),
rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil._get_spec(self.input(0), self.input(1)))
        


class AutoNode_pkgutil__import_imp(rc.Node):
    title = '_import_imp'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil._import_imp())
        


class AutoNode_pkgutil__iter_file_finder_modules(rc.Node):
    title = '_iter_file_finder_modules'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='importer'),
rc.NodeInputBP(label='prefix'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil._iter_file_finder_modules(self.input(0), self.input(1)))
        


class AutoNode_pkgutil_extend_path(rc.Node):
    title = 'extend_path'
    description = '''Extend a package's path.

    Intended use is to place the following code in a package's __init__.py:

        from pkgutil import extend_path
        __path__ = extend_path(__path__, __name__)

    This will add to the package's __path__ all subdirectories of
    directories on sys.path named after the package.  This is useful
    if one wants to distribute different parts of a single logical
    package as multiple directories.

    It also looks for *.pkg files beginning where * matches the name
    argument.  This feature is similar to *.pth files (see site.py),
    except that it doesn't special-case lines starting with 'import'.
    A *.pkg file is trusted at face value: apart from checking for
    duplicates, all entries found in a *.pkg file are added to the
    path, regardless of whether they are exist the filesystem.  (This
    is a feature.)

    If the input path is not a list (as is the case for frozen
    packages) it is returned unchanged.  The input path is not
    modified; an extended copy is returned.  Items are only appended
    to the copy at the end.

    It is assumed that sys.path is a sequence.  Items of sys.path that
    are not (unicode or 8-bit) strings referring to existing
    directories are ignored.  Unicode items of sys.path that cause
    errors when used as filenames may cause this function to raise an
    exception (in line with os.path.isdir() behavior).
    '''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil.extend_path(self.input(0), self.input(1)))
        


class AutoNode_pkgutil_find_loader(rc.Node):
    title = 'find_loader'
    description = '''Find a "loader" object for fullname

    This is a backwards compatibility wrapper around
    importlib.util.find_spec that converts most failures to ImportError
    and only returns the loader rather than the full spec
    '''
    init_inputs = [
        rc.NodeInputBP(label='fullname'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil.find_loader(self.input(0)))
        


class AutoNode_pkgutil_get_state(rc.Node):
    title = 'get_data'
    description = '''Get a resource from a package.

    This is a wrapper round the PEP 302 loader get_data API. The package
    argument should be the name of a package, in standard module format
    (foo.bar). The resource argument should be in the form of a relative
    filename, using '/' as the path separator. The parent directory name '..'
    is not allowed, and nor is a rooted name (starting with a '/').

    The function returns a binary string, which is the contents of the
    specified resource.

    For packages located in the filesystem, which have already been imported,
    this is the rough equivalent of

        d = os.path.dirname(sys.modules[package].__file__)
        data = open(os.path.join(d, resource), 'rb').read()

    If the package cannot be located or loaded, or it uses a PEP 302 loader
    which does not support get_state(), then None is returned.
    '''
    init_inputs = [
        rc.NodeInputBP(label='package'),
rc.NodeInputBP(label='resource'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil.get_state(self.input(0), self.input(1)))
        


class AutoNode_pkgutil_get_importer(rc.Node):
    title = 'get_importer'
    description = '''Retrieve a finder for the given path item

    The returned finder is cached in sys.path_importer_cache
    if it was newly created by a path hook.

    The cache (or part of it) can be cleared manually if a
    rescan of sys.path_hooks is necessary.
    '''
    init_inputs = [
        rc.NodeInputBP(label='path_item'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil.get_importer(self.input(0)))
        


class AutoNode_pkgutil_get_loader(rc.Node):
    title = 'get_loader'
    description = '''Get a "loader" object for module_or_name

    Returns None if the module cannot be found or imported.
    If the named module is not already imported, its containing package
    (if any) is imported, in order to establish the package __path__.
    '''
    init_inputs = [
        rc.NodeInputBP(label='module_or_name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil.get_loader(self.input(0)))
        


class AutoNode_pkgutil_iter_importer_modules(rc.Node):
    title = 'iter_importer_modules'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil.iter_importer_modules())
        


class AutoNode_pkgutil_iter_importers(rc.Node):
    title = 'iter_importers'
    description = '''Yield finders for the given module name

    If fullname contains a '.', the finders will be for the package
    containing fullname, otherwise they will be all registered top level
    finders (i.e. those on both sys.meta_path and sys.path_hooks).

    If the named module is in a package, that package is imported as a side
    effect of invoking this function.

    If no module name is specified, all top level finders are produced.
    '''
    init_inputs = [
        rc.NodeInputBP(label='fullname'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil.iter_importers(self.input(0)))
        


class AutoNode_pkgutil_iter_modules(rc.Node):
    title = 'iter_modules'
    description = '''Yields ModuleInfo for all submodules on path,
    or, if path is None, all top-level modules on sys.path.

    'path' should be either None or a list of paths to look for
    modules in.

    'prefix' is a string to output on the front of every module name
    on output.
    '''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='prefix'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil.iter_modules(self.input(0), self.input(1)))
        


class AutoNode_pkgutil_iter_zipimport_modules(rc.Node):
    title = 'iter_zipimport_modules'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='importer'),
rc.NodeInputBP(label='prefix'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil.iter_zipimport_modules(self.input(0), self.input(1)))
        


class AutoNode_pkgutil_namedtuple(rc.Node):
    title = 'namedtuple'
    description = '''Returns a new subclass of tuple with named fields.

    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessible by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)

    '''
    init_inputs = [
        rc.NodeInputBP(label='typename'),
rc.NodeInputBP(label='field_names'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil.namedtuple(self.input(0), self.input(1)))
        


class AutoNode_pkgutil_read_code(rc.Node):
    title = 'read_code'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='stream'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil.read_code(self.input(0)))
        


class AutoNode_pkgutil_simplegeneric(rc.Node):
    title = 'simplegeneric'
    description = '''Single-dispatch generic function decorator.

    Transforms a function into a generic function, which can have different
    behaviours depending upon the type of its first argument. The decorated
    function acts as the default implementation, and additional
    implementations can be registered using the register() attribute of the
    generic function.
    '''
    init_inputs = [
        rc.NodeInputBP(label='func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil.simplegeneric(self.input(0)))
        


class AutoNode_pkgutil_walk_packages(rc.Node):
    title = 'walk_packages'
    description = '''Yields ModuleInfo for all modules recursively
    on path, or, if path is None, all accessible modules.

    'path' should be either None or a list of paths to look for
    modules in.

    'prefix' is a string to output on the front of every module name
    on output.

    Note that this function must import all *packages* (NOT all
    modules!) on the given path, in order to access the __path__
    attribute to find submodules.

    'onerror' is a function which gets called with one argument (the
    name of the package which was being imported) if any exception
    occurs while trying to import a package.  If no onerror function is
    supplied, ImportErrors are caught and ignored, while all other
    exceptions are propagated, terminating the search.

    Examples:

    # list all modules python can access
    walk_packages()

    # list all submodules of ctypes
    walk_packages(ctypes.__path__, ctypes.__name__+'.')
    '''
    init_inputs = [
        rc.NodeInputBP(label='path'),
rc.NodeInputBP(label='prefix'),
rc.NodeInputBP(label='onerror'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pkgutil.walk_packages(self.input(0), self.input(1), self.input(2)))
        