from qtpy.QtWidgets import QWidget, QHBoxLayout, QComboBox

from ryvencore_qt import GUI

from code_editor.CodePreviewWidget import CodePreviewWidget
from uic.ui_script import Ui_script_widget


class ScriptUI(QWidget):
    def __init__(self, main_window, script, flow_view):
        super().__init__(main_window)

        self.script = script
        self.flow_view = flow_view
        
        # UI
        self.ui = Ui_script_widget()
        self.ui.setupUi(self)

        self.script.flow.algorithm_mode_changed.connect(self.flow_alg_mode_changed)
        # self.script.flow_view.viewport_update_mode_changed.connect(self.flow_vp_update_mode_changed)

        self.flow_alg_mode_dropdown = QComboBox()
        self.flow_alg_mode_dropdown.addItem('data-flow')
        self.flow_alg_mode_dropdown.addItem('exec-flow')
        self.ui.settings_groupBox.layout().addWidget(self.flow_alg_mode_dropdown)
        self.flow_alg_mode_dropdown.currentTextChanged.connect(self.flow_algorithm_mode_toggled)

        # catch up on flow modes
        self.flow_alg_mode_changed(self.script.flow.algorithm_mode())
        # self.flow_vp_update_mode_changed(self.script.flow_view.viewport_update_mode())

        # variables list widget
        self.vars_list_widget = GUI.VarsList(self.script.vars_manager)
        self.ui.variables_group_box.layout().addWidget(self.vars_list_widget)
        self.ui.settings_vars_splitter.setSizes([40, 700])

        # flow
        self.ui.splitter.insertWidget(0, self.flow_view)

        # code preview
        self.code_preview_widget = CodePreviewWidget(main_window, self.flow_view)
        self.ui.source_code_groupBox.layout().addWidget(self.code_preview_widget)

        # logs
        self.ui.logs_scrollArea.setWidget(self.create_loggers_widget())
        self.ui.splitter.setSizes([700, 0])
        self.script.logs_manager.new_logger_created.connect(self.add_logger_widget)

        # catch up on logs which might have been loaded from a project already
        for logger in self.script.logs_manager.loggers:
            self.add_logger_widget(logger)


    def create_loggers_widget(self):
        w = QWidget()
        w.setLayout(QHBoxLayout())
        # w.setStyleSheet('')
        return w


    def add_logger_widget(self, logger):
        self.ui.logs_scrollArea.widget().layout().addWidget(GUI.LogWidget(logger))


    def flow_alg_mode_changed(self, mode: str):
        if mode == 'data':
            self.flow_alg_mode_dropdown.setCurrentIndex(0)
        elif mode == 'exec':
            self.flow_alg_mode_dropdown.setCurrentIndex(1)

    
    def flow_algorithm_mode_toggled(self):
        mode = ''
        if self.flow_alg_mode_dropdown.currentIndex() == 0:
            mode = 'data'
        else:
            mode = 'exec'
        self.script.flow.set_algorithm_mode(mode)
