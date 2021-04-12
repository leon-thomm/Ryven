import ryvencore_qt as rc
import _weakref


class AutoNode__weakref__remove_dead_weakref(rc.Node):
    title = '_remove_dead_weakref'
    type_ = '_weakref'
    description = '''Atomically remove key from dict if it points to a dead weakref.'''
    init_inputs = [
        rc.NodeInputBP(label='dct'),
rc.NodeInputBP(label='key'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _weakref._remove_dead_weakref(self.input(0), self.input(1)))
        


class AutoNode__weakref_getweakrefcount(rc.Node):
    title = 'getweakrefcount'
    type_ = '_weakref'
    description = '''Return the number of weak references to 'object'.'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _weakref.getweakrefcount(self.input(0)))
        