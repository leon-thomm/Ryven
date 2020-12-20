from PySide2.QtWidgets import QWidget, QHBoxLayout

import ryvencore.ryvencore as rc

from custom_src.source_code_preview.CodePreview_Widget import CodePreview_Widget
from ui.ui_script import Ui_script_widget


class ScriptUI(QWidget):
    def __init__(self, script):
        super().__init__()

        self.script = script
        
        # UI
        self.ui = Ui_script_widget()
        self.ui.setupUi(self)

        self.script.flow_algorithm_mode_changed.connect(self.flow_alg_mode_changed)
        self.script.flow_viewport_update_mode_changed.connect(self.flow_vp_update_mode_changed)
        
        # catch up on flow modes
        self.flow_alg_mode_changed(self.script.flow_algorithm_mode())
        self.flow_vp_update_mode_changed(self.script.flow_viewport_update_mode())

        # variables list widget
        self.vars_list_widget = rc.ConvUI.VarsList(self.script.vars_manager)
        self.ui.variables_group_box.layout().addWidget(self.vars_list_widget)
        self.ui.settings_vars_splitter.setSizes([40, 700])

        self.ui.algorithm_data_flow_radioButton.toggled.connect(
            self.flow_algorithm_mode_toggled
        )
        self.ui.viewport_update_mode_sync_radioButton.toggled.connect(
            self.flow_viewport_update_mode_toggled
        )

        # flow
        self.ui.splitter.insertWidget(0, self.script.flow)

        # code preview
        self.code_preview_widget = CodePreview_Widget()
        self.ui.source_code_groupBox.layout().addWidget(self.code_preview_widget)

        # logs
        self.ui.logs_scrollArea.setWidget(self.create_logs_widget())
        self.ui.splitter.setSizes([700, 0])
        self.script.logger.new_log_created.connect(self.add_log_widget)
        # self.script.logger.create_default_logs()

        # catch up on logs which might have been loaded from a project already
        for log in self.script.logger.logs:
            self.add_log_widget(log)


    def create_logs_widget(self):
        w = QWidget()
        w.setLayout(QHBoxLayout())
        w.setStyleSheet('')
        return w


    def add_log_widget(self, log):
        self.ui.logs_scrollArea.widget().layout().addWidget(rc.ConvUI.LogWidget(log))


    def show_NI_code(self, ni):
        """Called from flow when the selection changed."""
        self.code_preview_widget.set_new_NI(ni)


    def flow_alg_mode_changed(self, mode: str):
        if mode == 'data flow':
            self.ui.algorithm_data_flow_radioButton.setChecked(True)
        elif mode == 'exec flow':
            self.ui.algorithm_exec_flow_radioButton.setChecked(True)
    
    
    def flow_vp_update_mode_changed(self, mode: str):
        if mode == 'sync':
            self.ui.viewport_update_mode_sync_radioButton.setChecked(True)
        elif mode == 'async':
            self.ui.viewport_update_mode_async_radioButton.setChecked(True)
    
    
    def flow_algorithm_mode_toggled(self):
        mode = ''
        if self.ui.algorithm_data_flow_radioButton.isChecked():
            mode = 'data flow'
        elif self.ui.algorithm_exec_flow_radioButton.isChecked():
            mode = 'exec flow'
        self.script.set_flow_algorithm_mode(mode)


    def flow_viewport_update_mode_toggled(self):
        mode = ''
        if self.ui.viewport_update_mode_sync_radioButton.isChecked():
            mode = 'sync'
        elif self.ui.viewport_update_mode_async_radioButton.isChecked():
            mode = 'async'
        self.script.set_flow_viewport_update_mode(mode)
