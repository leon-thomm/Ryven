import ryvencore_qt as rc
import modulefinder


class AutoNode_modulefinder_AddPackagePath(rc.Node):
    title = 'AddPackagePath'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='packagename'),
rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, modulefinder.AddPackagePath(self.input(0), self.input(1)))
        


class AutoNode_modulefinder_ReplacePackage(rc.Node):
    title = 'ReplacePackage'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='oldname'),
rc.NodeInputBP(label='newname'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, modulefinder.ReplacePackage(self.input(0), self.input(1)))
        


class AutoNode_modulefinder__find_module(rc.Node):
    title = '_find_module'
    description = '''An importlib reimplementation of imp.find_module (for our purposes).'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, modulefinder._find_module(self.input(0), self.input(1)))
        


class AutoNode_modulefinder_test(rc.Node):
    title = 'test'
    description = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, modulefinder.test())
        