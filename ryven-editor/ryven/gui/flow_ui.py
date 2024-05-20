"""A UI for flows. Will be displayed in the tab widget in MainWindow."""

from qtpy.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QComboBox,
    QMainWindow,
    QHBoxLayout,
    QTabWidget,
    QDockWidget,
    QUndoView,
    QAction
)
from qtpy.QtCore import Qt, QByteArray

import ryvencore_qt.src.widgets as GUI
from ryvencore.RC import FlowAlg
from ryvencore import Flow

from ryven.gui.code_editor.CodePreviewWidget import CodePreviewWidget
from ryven.gui.uic.ui_flow_window import Ui_FlowWindow
from ryvencore_qt.src.flows.FlowView import FlowView
from ryvencore_qt.src.flows.nodes.NodeInspector import InspectorView
from typing import List


class FlowUI(QMainWindow):
    flow_alg_mode_display_titles = {
        FlowAlg.DATA: 'data-flow',
        FlowAlg.DATA_OPT: 'data-flow opt',
        FlowAlg.EXEC: 'exec-flow',
    }

    def __init__(self, main_window, flow: Flow, flow_view: FlowView):
        super().__init__(main_window)

        self.setWindowFlag(Qt.Widget)
        self.flow: Flow = flow
        self.flow_view: FlowView = flow_view
        # UI
        self.ui = Ui_FlowWindow()
        self.ui.setupUi(self)
        # this is needed because there's no option in qt designer (propably)
        self.ui.logger_dock.setWidget(self.ui.logs_scrollArea)
        central_layout = QHBoxLayout()
        self.ui.centralwidget.setLayout(central_layout)
        self.setLayout(central_layout)

        # add widget actions to menu
        # should be list[QDockWidget] in 3.9+
        all_dock_widgets: List[QDockWidget] = [d for d in self.findChildren(QDockWidget)]
        windows_menu = flow_view.menu().addMenu("Windows")
        open_all_action = QAction('Open All', self)
        open_all_action.triggered.connect(self.open_docks)
        close_all_action = QAction('Close All Tabs', self)
        close_all_action.triggered.connect(self.close_docks)
        windows_menu.addActions([open_all_action, close_all_action])
        for w in all_dock_widgets:
            windows_menu.addAction(w.toggleViewAction())

        # set tabs to be on top
        self.setTabPosition(Qt.AllDockWidgetAreas, QTabWidget.North)
        # tabify all right docks
        right_area_widgets = [
            d
            for d in self.findChildren(QDockWidget)
            if self.dockWidgetArea(d) == Qt.RightDockWidgetArea
        ]
        for i in range(1, len(right_area_widgets)):
            self.tabifyDockWidget(right_area_widgets[i - 1], right_area_widgets[i])
        
        # inspector dock first
        self.ui.inspector_dock.raise_()

        self.flow.algorithm_mode_changed.sub(self.flow_alg_mode_changed)

        self.flow_alg_mode_dropdown = QComboBox()
        for mode, title in self.flow_alg_mode_display_titles.items():
            self.flow_alg_mode_dropdown.addItem(title)
        self.ui.settings_dock.setWidget(self.flow_alg_mode_dropdown)
        self.flow_alg_mode_dropdown.currentTextChanged.connect(self.flow_algorithm_mode_toggled)

        # catch up on flow modes
        self.flow_alg_mode_changed(self.flow.algorithm_mode())

        # variables list widget
        self.vars_list_widget = GUI.VarsList(
            self.flow.session.addons.get('Variables'), self.flow
        )  # TODO: how are vars now managed?
        self.ui.variables_dock.setWidget(self.vars_list_widget)

        # flow
        self.ui.centralwidget.layout().addWidget(self.flow_view)
        self.flow_view.design.performance_mode_changed.connect(self.set_performance_mode)
        self.set_performance_mode(self.flow_view.design.performance_mode)

        # code preview
        self.code_preview_widget = CodePreviewWidget(main_window, self.flow_view)
        self.ui.source_dock.setWidget(self.code_preview_widget)
        
        # inspector widget
        self.inspector_widget = InspectorView(self.flow_view)
        self.ui.inspector_dock.setWidget(self.inspector_widget)
        
        #undo history widget
        self.undo_widget = QUndoView(stack=self.flow_view._undo_stack)  # type: ignore
        self.ui.undo_history_dock.setWidget(self.undo_widget)
        # logs
        self.ui.logs_scrollArea.setWidget(self.create_loggers_widget())

        # TODO: need to connect to logging event but seems it isn't implemented yet
        # self.flow.session.addons.get('Logging').logs_manager.new_logger_created.connect(self.add_logger_widget)

        # catch up on logs which might have been loaded from a project already
        logging = self.flow.session.addons.get('Logging')
        for logger in logging.loggers:
            self.add_logger_widget(logger)
        logging.log_created.sub(self.add_logger_widget)

    def open_docks(self, docks):
        for dock in self.findChildren(QDockWidget):
            dock.show()
    
    def close_docks(self, dock):
        for dock in self.findChildren(QDockWidget):
            if not dock.isFloating():
                dock.close()
            
    # created to avoid __del__
    def unload(self):
        """Disconnects the flow ui from the design or main application signals"""
        self.flow_view.design.performance_mode_changed.disconnect(self.set_performance_mode)
        self.flow_view._undo_stack.clear()

    def set_performance_mode(self, mode: str):
        if mode == 'fast':
            self.setDockOptions(self.dockOptions() & ~QMainWindow.AnimatedDocks)
        else:
            self.setDockOptions(self.dockOptions() | QMainWindow.AnimatedDocks)

    def create_loggers_widget(self):
        w = QWidget()
        w.setLayout(QHBoxLayout())
        # w.setStyleSheet('')
        return w

    def add_logger_widget(self, logger):
        self.ui.logs_scrollArea.widget().layout().addWidget(GUI.LogWidget(logger))

    def flow_alg_mode_changed(self, mode: str):
        self.flow_alg_mode_dropdown.setCurrentText(
            self.flow_alg_mode_display_titles[FlowAlg.from_str(mode)]
        )

    def flow_algorithm_mode_toggled(self):
        self.flow.set_algorithm_mode(
            FlowAlg.str(
                list(self.flow_alg_mode_display_titles.keys())
                [self.flow_alg_mode_dropdown.currentIndex()]
            )
        )

    # should be dict[str, str] in 3.9+
    def save_state(self) -> dict:
        return {
            'geometry': self.saveGeometry().toHex().data().decode(),
            'state': self.saveState().toHex().data().decode(),
            'view': self.flow_view.save_state(),
        }

    # should be dict[str, dict[str, str]] in 3.9+
    def load(self, flow_uis_dir: dict):
        """
        Loads from a dictionary that contains all the flow UIs using the prev_global_id of the flow
        """
        flow_dir = flow_uis_dir[str(self.flow.prev_global_id)]
        self.load_directly(flow_dir)

    # Loads directly from a dictionary that contains a geometry and a state dict
    # should be dict[str, str] in 3.9+
    def load_directly(self, flow_dict: dict):
        """
        Directly loads from a dictionary that contains a geometry and state values. Does not fail
        if the values are not found. Values can be either str, QByteArray or bytes.
        """
        load = (
            lambda key: flow_dict[key]
            if type(flow_dict[key]) is QByteArray or type(flow_dict[key]) is bytes
            else bytes.fromhex(flow_dict[key])
        )
        if 'geometry' in flow_dict:
            self.restoreGeometry(load('geometry'))
        if 'state' in flow_dict:
            self.restoreState(load('state'))
        if 'view' in flow_dict:
            self.flow_view.load(flow_dict['view'])
