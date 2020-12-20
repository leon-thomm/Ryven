from PySide2.QtCore import QObject, Signal

from ryvencore.Flow import Flow
from ryvencore.logging.Logger import Logger
from ryvencore.script_variables.VarsManager import VarsManager


class Script(QObject):

    # name_changed = Signal(str)
    flow_algorithm_mode_changed = Signal(str)
    flow_viewport_update_mode_changed = Signal(str)

    def __init__(self, session, title: str = None, config: dict = None, flow_size: list = None):
        super(Script, self).__init__()

        self.session = session

        # GENERAL ATTRIBUTES
        self.logger = Logger(self)

        # self.variables = []
        self.vars_manager = None
        self.title = title
        self.flow = None
        self.thumbnail_source = ''  # URL to the Script's thumbnail picture

        if config:
            self.title = config['name']
            self.vars_manager = VarsManager(self, config['variables'])
            self.flow = Flow(session, self, flow_size, config['flow'])
        else:
            self.flow = Flow(session, self, flow_size)
            self.vars_manager = VarsManager(self)


    # def show_NI_code(self, ni):
    #     """Called from flow when the selection changed."""
    #     self.code_preview_widget.set_new_NI(ni)


    def flow_algorithm_mode(self):
        """Returns the current algorithm mode of the flow"""
        return self.flow.algorithm_mode

    def set_flow_algorithm_mode(self, mode):
        """Sets the algorithm mode of the flow"""
        self.flow.algorithm_mode = mode

    def flow_viewport_update_mode(self):
        """Returns the current viewport update mode (sync or async) of the flow"""
        return self.flow.viewport_update_mode

    def set_flow_viewport_update_mode(self, mode):
        """Sets the viewport update mode of the flow"""
        self.flow.viewport_update_mode = mode

    def generate_code(self):
        """In production, no working prototype"""
        return  # migrate to main window later
        cg = CodeGenerator(self.session,
                           self.flow.all_node_instances,
                           self.vars_manager.config_data(),
                           self.flow.algorithm_mode)
        code = cg.generate()
        if code is None:
            print('couldn\'t generate code')
        else:
            print(code)


    def config_data(self):
        script_dict = {'name': self.title,
                       'variables': self.vars_manager.config_data(),
                       'flow': self.flow.config_data()}

        return script_dict