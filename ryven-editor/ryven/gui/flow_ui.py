"""A UI for flows. Will be displayed in the tab widget in MainWindow."""

from qtpy.QtWidgets import QWidget, QHBoxLayout, QComboBox, QMainWindow,QHBoxLayout, QTabWidget,QDockWidget
from qtpy.QtCore import Qt, QByteArray

import ryvencore_qt.src.widgets as GUI
from ryvencore.RC import FlowAlg
from ryvencore import Flow

from ryven.gui.code_editor.CodePreviewWidget import CodePreviewWidget
from ryven.gui.uic.ui_flow_window import Ui_FlowWindow
from ryvencore_qt.src.flows.FlowView import FlowView

class FlowUI(QMainWindow):

    flow_alg_mode_display_titles = {
        FlowAlg.DATA: 'data-flow',
        FlowAlg.DATA_OPT: 'data-flow opt',
        FlowAlg.EXEC: 'exec-flow',
    }

    def __init__(self, main_window, flow:Flow, flow_view:FlowView):
        super().__init__(main_window)

        self.setWindowFlag(Qt.Widget)
        self.flow:Flow = flow
        self.flow_view:FlowView = flow_view
        # UI
        self.ui = Ui_FlowWindow()
        self.ui.setupUi(self)
        #this is needed because it seems that qt compiler doesn't work well
        self.ui.logger_dock.setWidget(self.ui.logs_scrollArea)
        central_layout = QHBoxLayout()
        self.ui.centralwidget.setLayout(central_layout)
        self.setLayout(central_layout)
        
        #add widget actions to menu
        all_dock_widgets:list[QDockWidget] = [d for d in self.findChildren(QDockWidget)]
        windows_menu = flow_view.menu().addMenu("Windows")
        for w in all_dock_widgets:
            windows_menu.addAction(w.toggleViewAction())
            
        #set tabs to be on top
        self.setTabPosition(Qt.AllDockWidgetAreas, QTabWidget.North)
        #tabify all right docks
        right_area_widgets = [d for d in self.findChildren(QDockWidget) if self.dockWidgetArea(d) == Qt.RightDockWidgetArea]
        for i in range(1, len(right_area_widgets)):
            self.tabifyDockWidget(right_area_widgets[i-1], right_area_widgets[i])
        
        self.flow.algorithm_mode_changed.sub(self.flow_alg_mode_changed)

        self.flow_alg_mode_dropdown = QComboBox()
        for mode, title in self.flow_alg_mode_display_titles.items():
            self.flow_alg_mode_dropdown.addItem(title)
        self.ui.settings_dock.setWidget(self.flow_alg_mode_dropdown)
        self.flow_alg_mode_dropdown.currentTextChanged.connect(self.flow_algorithm_mode_toggled)

        # catch up on flow modes
        self.flow_alg_mode_changed(self.flow.algorithm_mode())

        # variables list widget
        self.vars_list_widget = GUI.VarsList(self.flow.session.addons.get('Variables'), self.flow) # TODO: how are vars now managed?
        self.ui.variables_dock.setWidget(self.vars_list_widget)

        # flow
        self.ui.centralwidget.layout().addWidget(self.flow_view)

        # code preview
        self.code_preview_widget = CodePreviewWidget(main_window, self.flow_view)
        self.ui.source_dock.setWidget(self.code_preview_widget)
        # logs
        self.ui.logs_scrollArea.setWidget(self.create_loggers_widget())

        # TODO: need to connect to logging event but seems it isn't implemented yet
        #self.flow.session.addons.get('Logging').logs_manager.new_logger_created.connect(self.add_logger_widget)

        # catch up on logs which might have been loaded from a project already
        logging = self.flow.session.addons.get('Logging')
        for logger in logging.loggers:
            self.add_logger_widget(logger)
        logging.log_created.sub(self.add_logger_widget)


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
    def save(self) -> dict[str, str]:
        return {
            'geometry': self.saveGeometry().toHex().data().decode(),
            'state' : self.saveState().toHex().data().decode()
        }
        
    #Loads from a dictionary that contains all the flow uis
    def load(self, flow_uis_dir:dict[str, dict[str, str]]):
        flow_dir = flow_uis_dir[str(self.flow.prev_global_id)]
        self.load_directly(flow_dir)
    #Loads directly from a dictionary that contains a geometry and a state dict
    def load_directly(self, flow_dict: dict[str, str] | dict[str, QByteArray]):
        load = lambda key: flow_dict[key] if type(flow_dict[key]) is QByteArray or type(flow_dict[key]) is bytes else bytes.fromhex(flow_dict[key])
        self.restoreGeometry(load("geometry"))
        self.restoreState(load("state"))
        
        