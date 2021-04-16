import ryvencore_qt as rc
import ensurepip


class AutoNode_ensurepip__bootstrap(rc.Node):
    title = '_bootstrap'
    doc = '''
    Bootstrap pip into the current Python installation (or the given root
    directory). Returns pip command status code.

    Note that calling this function will alter both sys.path and os.environ.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ensurepip._bootstrap())
        


class AutoNode_ensurepip__disable_pip_configuration_settings(rc.Node):
    title = '_disable_pip_configuration_settings'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ensurepip._disable_pip_configuration_settings())
        


class AutoNode_ensurepip__main(rc.Node):
    title = '_main'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='argv'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ensurepip._main(self.input(0)))
        


class AutoNode_ensurepip__run_pip(rc.Node):
    title = '_run_pip'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='args'),
rc.NodeInputBP(label='additional_paths'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ensurepip._run_pip(self.input(0), self.input(1)))
        


class AutoNode_ensurepip__uninstall_helper(rc.Node):
    title = '_uninstall_helper'
    doc = '''Helper to support a clean default uninstall process on Windows

    Note that calling this function may alter os.environ.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ensurepip._uninstall_helper())
        


class AutoNode_ensurepip_bootstrap(rc.Node):
    title = 'bootstrap'
    doc = '''
    Bootstrap pip into the current Python installation (or the given root
    directory).

    Note that calling this function will alter both sys.path and os.environ.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ensurepip.bootstrap())
        


class AutoNode_ensurepip_version(rc.Node):
    title = 'version'
    doc = '''
    Returns a string specifying the bundled version of pip.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ensurepip.version())
        