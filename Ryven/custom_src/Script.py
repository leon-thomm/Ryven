from PySide2.QtCore import QObject, Signal

# UI
from PySide2.QtWidgets import QHBoxLayout, QWidget

from custom_src.code_gen.CodeGenerator import CodeGenerator
from custom_src.custom_list_widgets.VariablesListWidget import VariablesListWidget
from custom_src.logging.Log import Log
from custom_src.logging.LogWidget import LogWidget
from ui.w_ui_script import WUIScript

from custom_src.Flow import Flow
from custom_src.logging.Logger import Logger
from custom_src.script_variables.VarsManager import VarsManager
from custom_src.source_code_preview.CodePreview_Widget import CodePreview_Widget


class Script(QObject):

    # name_changed = Signal(str)
    flow_algorithm_mode_changed = Signal(str)
    flow_viewport_update_mode_changed = Signal(str)

    def __init__(self, session, title: str = None, config: dict = None):
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
            self.flow = Flow(session, self, config['flow'])
        else:
            self.flow = Flow(session, self)
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