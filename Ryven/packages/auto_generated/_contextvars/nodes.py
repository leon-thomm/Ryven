import ryvencore_qt as rc
import _contextvars


class AutoNode__contextvars_copy_context(rc.Node):
    title = 'copy_context'
    type_ = '_contextvars'
    description = ''''''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _contextvars.copy_context())
        