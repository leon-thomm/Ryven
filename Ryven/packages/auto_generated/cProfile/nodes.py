import ryvencore_qt as rc
import cProfile


class AutoNode_cProfile_label(rc.Node):
    title = 'label'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='code'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cProfile.label(self.input(0)))
        


class AutoNode_cProfile_main(rc.Node):
    title = 'main'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cProfile.main())
        


class AutoNode_cProfile_run(rc.Node):
    title = 'run'
    doc = '''Run statement under profiler optionally saving results in filename

    This function takes a single argument that can be passed to the
    "exec" statement, and an optional file name.  In all cases this
    routine attempts to "exec" its first argument and gather profiling
    statistics from the execution. If no file name is present, then this
    function automatically prints a simple profiling report, sorted by the
    standard name string (file/line/function-name) that is presented in
    each line.
    '''
    init_inputs = [
        rc.NodeInputBP(label='statement'),
rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='sort'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cProfile.run(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_cProfile_runctx(rc.Node):
    title = 'runctx'
    doc = '''Run statement under profiler, supplying your own globals and locals,
    optionally saving results in filename.

    statement and filename have the same semantics as profile.run
    '''
    init_inputs = [
        rc.NodeInputBP(label='statement'),
rc.NodeInputBP(label='globals'),
rc.NodeInputBP(label='locals'),
rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='sort'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, cProfile.runctx(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        