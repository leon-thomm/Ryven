import ryvencore_qt as rc
import copyreg


class AutoNode_copyreg___newobj__(rc.Node):
    title = '__newobj__'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copyreg.__newobj__(self.input(0)))
        


class AutoNode_copyreg___newobj_ex__(rc.Node):
    title = '__newobj_ex__'
    doc = '''Used by pickle protocol 4, instead of __newobj__ to allow classes with
    keyword-only arguments to be pickled correctly.
    '''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='args'),
rc.NodeInputBP(label='kwargs'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copyreg.__newobj_ex__(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_copyreg__reconstructor(rc.Node):
    title = '_reconstructor'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
rc.NodeInputBP(label='base'),
rc.NodeInputBP(label='state'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copyreg._reconstructor(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_copyreg__reduce_ex(rc.Node):
    title = '_reduce_ex'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='proto'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copyreg._reduce_ex(self.input(0), self.input(1)))
        


class AutoNode_copyreg__slotnames(rc.Node):
    title = '_slotnames'
    doc = '''Return a list of slot names for a given class.

    This needs to find slots defined by the class and its bases, so we
    can't simply return the __slots__ attribute.  We must walk down
    the Method Resolution Order and concatenate the __slots__ of each
    class found there.  (This assumes classes don't modify their
    __slots__ attribute to misrepresent their slots after the class is
    defined.)
    '''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copyreg._slotnames(self.input(0)))
        


class AutoNode_copyreg_add_extension(rc.Node):
    title = 'add_extension'
    doc = '''Register an extension code.'''
    init_inputs = [
        rc.NodeInputBP(label='module'),
rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='code'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copyreg.add_extension(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_copyreg_clear_extension_cache(rc.Node):
    title = 'clear_extension_cache'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copyreg.clear_extension_cache())
        


class AutoNode_copyreg_constructor(rc.Node):
    title = 'constructor'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copyreg.constructor(self.input(0)))
        


class AutoNode_copyreg_pickle(rc.Node):
    title = 'pickle'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='ob_type'),
rc.NodeInputBP(label='pickle_function'),
rc.NodeInputBP(label='constructor_ob'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copyreg.pickle(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_copyreg_pickle_complex(rc.Node):
    title = 'pickle_complex'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='c'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copyreg.pickle_complex(self.input(0)))
        


class AutoNode_copyreg_remove_extension(rc.Node):
    title = 'remove_extension'
    doc = '''Unregister an extension code.  For testing only.'''
    init_inputs = [
        rc.NodeInputBP(label='module'),
rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='code'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, copyreg.remove_extension(self.input(0), self.input(1), self.input(2)))
        