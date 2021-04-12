import ryvencore_qt as rc
import linecache


class AutoNode_linecache_checkcache(rc.Node):
    title = 'checkcache'
    description = '''Discard cache entries that are out of date.
    (This is not checked upon each call!)'''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, linecache.checkcache(self.input(0)))
        


class AutoNode_linecache_clearcache(rc.Node):
    title = 'clearcache'
    description = '''Clear the cache entirely.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, linecache.clearcache())
        


class AutoNode_linecache_getline(rc.Node):
    title = 'getline'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='lineno'),
rc.NodeInputBP(label='module_globals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, linecache.getline(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_linecache_getlines(rc.Node):
    title = 'getlines'
    description = '''Get the lines for a Python source file from the cache.
    Update the cache if it doesn't contain an entry for this file already.'''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='module_globals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, linecache.getlines(self.input(0), self.input(1)))
        


class AutoNode_linecache_lazycache(rc.Node):
    title = 'lazycache'
    description = '''Seed the cache for filename with module_globals.

    The module loader will be asked for the source only when getlines is
    called, not immediately.

    If there is an entry in the cache already, it is not altered.

    :return: True if a lazy load is registered in the cache,
        otherwise False. To register such a load a module loader with a
        get_source method must be found, the filename must be a cachable
        filename, and the filename must not be already cached.
    '''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='module_globals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, linecache.lazycache(self.input(0), self.input(1)))
        


class AutoNode_linecache_updatecache(rc.Node):
    title = 'updatecache'
    description = '''Update a cache entry and return its list of lines.
    If something's wrong, print a message, discard the cache entry,
    and return an empty list.'''
    init_inputs = [
        rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='module_globals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, linecache.updatecache(self.input(0), self.input(1)))
        