import ryvencore_qt as rc
import pstats


class AutoNode_pstats_add_callers(rc.Node):
    title = 'add_callers'
    doc = '''Combine two caller lists in a single list.'''
    init_inputs = [
        rc.NodeInputBP(label='target'),
rc.NodeInputBP(label='source'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.add_callers(self.input(0), self.input(1)))
        


class AutoNode_pstats_add_func_stats(rc.Node):
    title = 'add_func_stats'
    doc = '''Add together all the stats for two profile entries.'''
    init_inputs = [
        rc.NodeInputBP(label='target'),
rc.NodeInputBP(label='source'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.add_func_stats(self.input(0), self.input(1)))
        


class AutoNode_pstats_count_calls(rc.Node):
    title = 'count_calls'
    doc = '''Sum the caller statistics to get total number of calls received.'''
    init_inputs = [
        rc.NodeInputBP(label='callers'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.count_calls(self.input(0)))
        


class AutoNode_pstats_f8(rc.Node):
    title = 'f8'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.f8(self.input(0)))
        


class AutoNode_pstats_func_get_function_name(rc.Node):
    title = 'func_get_function_name'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='func'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.func_get_function_name(self.input(0)))
        


class AutoNode_pstats_func_std_string(rc.Node):
    title = 'func_std_string'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='func_name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.func_std_string(self.input(0)))
        


class AutoNode_pstats_func_strip_path(rc.Node):
    title = 'func_strip_path'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='func_name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, pstats.func_strip_path(self.input(0)))
        