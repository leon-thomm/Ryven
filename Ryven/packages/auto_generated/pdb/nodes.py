import ryvencore_qt as rc
import pdb


class AutoNode_pdb_find_function(rc.Node):
    title = 'find_function'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='funcname'),
rc.NodeInputBP(label='filename'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pdb.find_function(self.input(0), self.input(1)))
        


class AutoNode_pdb_getsourcelines(rc.Node):
    title = 'getsourcelines'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pdb.getsourcelines(self.input(0)))
        


class AutoNode_pdb_help(rc.Node):
    title = 'help'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pdb.help())
        


class AutoNode_pdb_lasti2lineno(rc.Node):
    title = 'lasti2lineno'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='code'),
rc.NodeInputBP(label='lasti'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pdb.lasti2lineno(self.input(0), self.input(1)))
        


class AutoNode_pdb_main(rc.Node):
    title = 'main'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pdb.main())
        


class AutoNode_pdb_pm(rc.Node):
    title = 'pm'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pdb.pm())
        


class AutoNode_pdb_post_mortem(rc.Node):
    title = 'post_mortem'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='t'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pdb.post_mortem(self.input(0)))
        


class AutoNode_pdb_run(rc.Node):
    title = 'run'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='statement'),
rc.NodeInputBP(label='globals'),
rc.NodeInputBP(label='locals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pdb.run(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_pdb_runcall(rc.Node):
    title = 'runcall'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pdb.runcall())
        


class AutoNode_pdb_runctx(rc.Node):
    title = 'runctx'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='statement'),
rc.NodeInputBP(label='globals'),
rc.NodeInputBP(label='locals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pdb.runctx(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_pdb_runeval(rc.Node):
    title = 'runeval'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='expression'),
rc.NodeInputBP(label='globals'),
rc.NodeInputBP(label='locals'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pdb.runeval(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_pdb_set_trace(rc.Node):
    title = 'set_trace'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pdb.set_trace())
        


class AutoNode_pdb_test(rc.Node):
    title = 'test'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pdb.test())
        