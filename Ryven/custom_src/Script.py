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

    def __init__(self, main_window, title: str = None, config: dict = None):
        super(Script, self).__init__()

        self.main_window = main_window
        self.widget = WUIScript()

        # GENERAL ATTRIBUTES
        self.logger = Logger(self)
        self.logger.new_log_created.connect(self.add_log_widget)

        # self.variables = []
        self.vars_manager = None
        self.title = title
        self.flow = None
        self.thumbnail_source = ''  # URL to the Script's thumbnail picture
        self.code_preview_widget = CodePreview_Widget()

        if config:
            self.title = config['name']
            self.vars_manager = VarsManager(self, config['variables'])
            self.flow = Flow(main_window, self, config['flow'])
        else:
            self.flow = Flow(main_window, self)
            self.vars_manager = VarsManager(self)

        # variables list widget
        self.vars_list_widget = VariablesListWidget(self.vars_manager)
        self.widget.ui.variables_group_box.layout().addWidget(self.vars_list_widget)
        self.widget.ui.settings_vars_splitter.setSizes([40, 700])

        # self.widget.ui.settings_groupBox.resize(self.widget.ui.settings_groupBox.minimumSize())

        # self.widget.ui.variables_scrollArea.setWidget(self.vars_manager.list_widget)
        # self.widget.ui.add_variable_push_button.clicked.connect(self.add_var_clicked)
        # self.widget.ui.new_var_name_lineEdit.returnPressed.connect(self.new_var_line_edit_return_pressed)
        self.widget.ui.algorithm_data_flow_radioButton.toggled.connect(self.flow.algorithm_mode_data_flow_toggled)
        self.widget.ui.viewport_update_mode_sync_radioButton.toggled.connect(self.flow.viewport_update_mode_sync_toggled)

        # flow
        self.widget.ui.splitter.insertWidget(0, self.flow)

        # code preview
        self.widget.ui.source_code_groupBox.layout().addWidget(self.code_preview_widget)

        # logs
        self.widget.ui.logs_scrollArea.setWidget(self.create_logs_widget())
        self.widget.ui.splitter.setSizes([700, 0])
        self.logger.create_default_logs()


    def create_logs_widget(self):
        w = QWidget()
        w.setLayout(QHBoxLayout())
        w.setStyleSheet('')
        return w

    def add_log_widget(self, log: Log):
        self.widget.ui.logs_scrollArea.widget().layout().addWidget(LogWidget(log))

    def show_NI_code(self, ni):
        """Called from Flow when the selection changed."""
        self.code_preview_widget.set_new_NI(ni)

    # def add_var_clicked(self):
    #     self.vars_manager.create_new_var_and_update(self.widget.ui.new_var_name_lineEdit.text())
    #
    # def new_var_line_edit_return_pressed(self):
    #     self.vars_manager.create_new_var_and_update(self.widget.ui.new_var_name_lineEdit.text())

    def generate_code(self):
        """In production, no working prototype"""
        cg = CodeGenerator(self.main_window,
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