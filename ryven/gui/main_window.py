import sys
import os
import os.path

from qtpy.QtGui import QIcon, QKeySequence
from qtpy.QtWidgets import QMainWindow, QFileDialog, QShortcut, QAction, QActionGroup, QMenu, QMessageBox

from ryven import __version__
from ryven.gui.main_console import MainConsole
from ryven.gui.flow_ui import FlowUI
from ryven.gui.styling.window_theme import WindowTheme
from ryven.main.nodes_package import NodesPackage
from ryven.gui.uic.ui_main_window import Ui_MainWindow
from ryven.main.utils import import_nodes_package, abs_path_from_package_dir, abs_path_from_ryven_dir
from ryven.main.nodes.NodeBase import NodeBase
from ryven.gui.dialogs import GetTextDialog, ChooseFlowDialog

# ryvencore_qt
import ryvencore_qt as rc
import ryvencore_qt.src.widgets as rc_GUI


class MainWindow(QMainWindow):

    def __init__(
            self,

            window_title,
            window_theme: WindowTheme,
            flow_theme,

            # Notice, the below default values are overwritten by the default values of the cmd
            # line argument parser, when launching the application with cmd line arguments.

            action: str = "create new project",  # or "open project'
            requested_packages: set = set(),
            required_packages: set = None,  # only valid when project_content is provided
            project_content: dict = None,
            info_msgs_enabled: bool = False,
            performance_mode: str = 'pretty',
            animations_enabled: bool = True,

            parent=None,
    ):
        super().__init__(parent)

        self.session_gui, self.core_session = None, None
        self.theme = window_theme
        self.node_packages = {}  # {Node: str}
        self.flow_UIs = {}

        #
        # Init Session GUI
        #

        self.session_gui = rc.SessionGUI(self)
        self.core_session = self.session_gui.core_session
        if info_msgs_enabled:
            self.core_session._info_messenger().enable(traceback=True)
        else:
            self.core_session._info_messenger().disable()

        self.session_gui.flow_view_created.connect(self.flow_created)
        self.session_gui.flow_renamed.connect(self.flow_renamed)
        self.session_gui.flow_deleted.connect(self.flow_deleted)

        self.session_gui.design.load_from_config(abs_path_from_package_dir('gui/styling/design_config.json'))

        self.session_gui.design.set_flow_theme(name=flow_theme)
        self.session_gui.design.set_performance_mode(performance_mode)
        self.session_gui.design.set_animations_enabled(animations_enabled)

        #
        # Assemble Window UI
        #

        self.setup_ui()

        self.flow_view_theme_actions = []
        self.setup_menu_actions()

        self.setWindowTitle(window_title)
        self.setWindowIcon(QIcon(abs_path_from_package_dir('resources/pics/Ryven_icon.png')))
        self.ui.flows_tab_widget.removeTab(0)  # remove placeholder tab

        #
        # Configure window-wide Shortcuts
        #

        save_shortcut = QShortcut(QKeySequence.Save, self)
        save_shortcut.activated.connect(self.on_save_project_triggered)
        import_nodes_shortcut = QShortcut(QKeySequence('Ctrl+i'), self)
        import_nodes_shortcut.activated.connect(self.on_import_nodes_triggered)

        #
        # Setup Main Console
        #

        MainConsole.instance.session = self.session_gui
        MainConsole.instance.reset_interpreter()
        NodeBase.main_console = MainConsole.instance

        #
        # Setup ryvencore Session
        #

        self.import_nodes(path=abs_path_from_package_dir('main/nodes/built_in/'))

        # Requested packages take precedence over other packages
        print('importing requested packages...')
        self.import_packages(requested_packages)
        if action == 'create project':
            self.core_session.create_flow(title='hello world')
        elif action == 'open project':
            print('importing required packages...')
            self.import_packages(required_packages)
            print('loading project...')
            self.core_session.load(project_content)
            print('done')

        self.resize(1500, 800)  # FIXME: this renders the --geometry argument useless, no?
        # self.showMaximized()

    def print_info(self):
        print('''
CONTROLS
    nodes dialog: right mouse in scene
    place nodes: drag and drop from left
        or hit enter in scene dialog
    select: left mouse
    pan / navigating scene: right mouse
    save: ctrl+s
    import: ctrl+i
        ''')

    # UI

    def setup_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusBar.hide()

        # main console
        if MainConsole.instance is not None:
            self.ui.main_vertical_splitter.addWidget(MainConsole.instance)
            self.ui.console_placeholder_widget.setParent(None)
        # self.ui.right_vertical_splitter.setSizes([600, 0])

        # splitter sizes
        # self.ui.left_vertical_splitter.setSizes([350, 350])
        self.ui.main_vertical_splitter.setSizes([700, 0])

        self.flows_list_widget = rc_GUI.FlowsList(self.session_gui)
        self.ui.flows_groupBox.layout().addWidget(self.flows_list_widget)

        self.nodes_list_widget = rc_GUI.NodeListWidget(self.session_gui)
        self.ui.nodes_groupBox.layout().addWidget(self.nodes_list_widget)

        self.ui.main_horizontal_splitter.setSizes([120, 800-120])

    def setup_menu_actions(self):

        # flow designs
        light_themes_menu = QMenu('light')
        for d in self.session_gui.design.flow_themes:
            design_action = QAction(d.name, self)
            if d.type_ == 'dark':
                self.ui.menuFlow_Design_Style.addAction(design_action)
            else:
                light_themes_menu.addAction(design_action)

            design_action.triggered.connect(self.on_design_action_triggered)
            self.flow_view_theme_actions.append(design_action)

        self.ui.menuFlow_Design_Style.addMenu(light_themes_menu)

        self.ui.actionImport_Nodes.triggered.connect(self.on_import_nodes_triggered)
        self.ui.actionImport_Example_Nodes.triggered.connect(self.on_import_example_nodes_triggered)
        self.ui.actionSave_Project.triggered.connect(self.on_save_project_triggered)
        # TODO: rename occurences of "Script" to "Flow" in the UI
        self.ui.actionNew_Script.triggered.connect(self.on_new_flow_triggered)
        self.ui.actionRename_Script.triggered.connect(self.on_rename_flow_triggered)
        self.ui.actionDelete_Script.triggered.connect(self.on_delete_flow_triggered)
        self.ui.actionEnableInfoMessages.triggered.connect(self.on_enable_info_msgs_triggered)
        self.ui.actionDisableInfoMessages.triggered.connect(self.on_disable_info_msgs_triggered)
        self.ui.actionSave_Pic_Viewport.triggered.connect(self.on_save_scene_pic_viewport_triggered)
        self.ui.actionSave_Pic_Whole_Scene_scaled.triggered.connect(self.on_save_scene_pic_whole_triggered)

        # performance mode
        self.ac_perf_mode_fast = QAction('Fast', self)
        self.ac_perf_mode_fast.setCheckable(True)

        self.ac_perf_mode_pretty = QAction('Pretty', self)
        self.ac_perf_mode_pretty.setCheckable(True)

        perf_mode_ag = QActionGroup(self)
        perf_mode_ag.addAction(self.ac_perf_mode_fast)
        perf_mode_ag.addAction(self.ac_perf_mode_pretty)

        self.ac_perf_mode_fast.setChecked(self.session_gui.design.performance_mode == 'fast')
        self.ac_perf_mode_pretty.setChecked(self.session_gui.design.performance_mode == 'pretty')

        perf_mode_ag.triggered.connect(self.on_performance_mode_changed)

        perf_menu = QMenu('Performance Mode', self)
        perf_menu.addAction(self.ac_perf_mode_fast)
        perf_menu.addAction(self.ac_perf_mode_pretty)

        self.ui.menuView.addMenu(perf_menu)

        # animations
        self.ac_anims_active = QAction('Enabled', self)
        self.ac_anims_active.setCheckable(True)

        self.ac_anims_inactive = QAction('Disabled', self)
        self.ac_anims_inactive.setCheckable(True)

        anims_ag = QActionGroup(self)
        anims_ag.addAction(self.ac_anims_active)
        anims_ag.addAction(self.ac_anims_inactive)

        self.ac_anims_active.setChecked(self.session_gui.design.animations_enabled)
        self.ac_anims_inactive.setChecked(not self.session_gui.design.animations_enabled)

        anims_ag.triggered.connect(self.on_animation_enabling_changed)

        animations_menu = QMenu('Animations', self)
        animations_menu.addAction(self.ac_anims_active)
        animations_menu.addAction(self.ac_anims_inactive)

        self.ui.menuView.addMenu(animations_menu)

    def load_stylesheet(self, ss):
        ss_content = ''
        try:
            f = open(abs_path_from_package_dir('resources/stylesheets/' + ss + '.txt'))
            ss_content = f.read()
            f.close()
        finally:
            self.session_gui.set_stylesheet(ss_content)
            self.setStyleSheet(ss_content)

    # SLOTS

    def on_import_nodes_triggered(self):
        file_path = QFileDialog.getOpenFileName(self, 'select nodes file', abs_path_from_ryven_dir('nodes'), 'Python File (*.py)')[0]
        if file_path != '':
            self.import_nodes(path=os.path.dirname(file_path))

    def on_import_example_nodes_triggered(self):
        file_path = QFileDialog.getOpenFileName(self, 'select nodes file', abs_path_from_package_dir('example_nodes'), 'Python File (*.py)')[0]
        if file_path != '':
            self.import_nodes(path=os.path.dirname(file_path))

    def on_performance_mode_changed(self, action):
        if action == self.ac_perf_mode_fast:
            self.session_gui.design.set_performance_mode('fast')
        else:
            self.session_gui.design.set_performance_mode('pretty')

    def on_animation_enabling_changed(self, action):
        if action == self.ac_anims_active:
            self.session_gui.design.animations_enabled = True
        else:
            self.session_gui.design.animations_enabled = False

    def on_design_action_triggered(self):
        index = self.flow_view_theme_actions.index(self.sender())
        self.session_gui.design.set_flow_theme(self.session_gui.design.flow_themes[index])

    def on_enable_info_msgs_triggered(self):
        rc.InfoMsgs.enable()

    def on_disable_info_msgs_triggered(self):
        rc.InfoMsgs.disable()

    def on_save_scene_pic_viewport_triggered(self):
        """Saves a picture of the currently visible viewport."""
        if len(self.core_session.flows) == 0:
            return

        file_path = QFileDialog.getSaveFileName(self, 'select file', '', 'PNG(*.png)')[0]
        flow = self.ui.flows_tab_widget.currentWidget().flow
        view = self.session_gui.flow_views[flow]
        img = view.get_viewport_img()
        img.save(file_path)

    def on_save_scene_pic_whole_triggered(self):
        """Saves a picture of the whole currently visible scene."""
        if len(self.session_gui.flows) == 0:
            return

        file_path = QFileDialog.getSaveFileName(self, 'select file', '', 'PNG(*.png)')[0]
        flow = self.ui.flows_tab_widget.currentWidget().flow
        view = self.session_gui.flow_views[flow]
        img = view.get_whole_scene_img()
        img.save(file_path)

    def on_save_project_triggered(self):
        file_name = QFileDialog.getSaveFileName(self, 'select location and give file name',
                                                abs_path_from_ryven_dir('saves'), 'JSON(*.json)')[0]
        if not file_name.endswith('.json'):
            file_name += '.json'

        if file_name != '':
            self.save_project(file_name)

    def on_new_flow_triggered(self):
        new_flow_title = GetTextDialog('choose unique title', '', 'new flow title', self).get_text()

        if self.core_session.flow_title_valid(new_flow_title):
            self.core_session.create_flow(new_flow_title)
        else:
            flow = [f for f in self.core_session.flows if f.title == new_flow_title][0]
            self.focus_on_flow(flow)

    def on_rename_flow_triggered(self):
        flow = ChooseFlowDialog('choose flow', self.core_session.flows, self).get_flow()
        new_title = GetTextDialog('new title', flow.title, 'new flow title', self).get_text()

        if self.core_session.flow_title_valid(new_title):
            self.core_session.rename_flow(flow, new_title)

    def on_delete_flow_triggered(self):
        flow = ChooseFlowDialog('choose flow', self.core_session.flows, self).get_flow()

        msg_box = QMessageBox(QMessageBox.Warning, 'sure about deleting flow?',
                              'You are about to delete a flow. This cannot be undone, all content will be gone. '
                              'Do you want to continue?', QMessageBox.Cancel | QMessageBox.Yes, self)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        ret = msg_box.exec_()
        if ret != QMessageBox.Yes:
            return

        self.core_session.delete_flow(flow)

    # SESSION

    def flow_created(self, flow, flow_view):
        flow_widget = FlowUI(self, flow, flow_view)
        self.flow_UIs[flow] = flow_widget
        self.ui.flows_tab_widget.addTab(flow_widget, flow.title)
        self.focus_on_flow(flow)

    def flow_renamed(self, flow):
        self.ui.flows_tab_widget.setTabText(
            self.session_gui.core_session.flows.index(flow),
            flow.title
        )

    def flow_deleted(self, flow):
        self.ui.flows_tab_widget.removeTab(self.ui.flows_tab_widget.indexOf(self.flow_UIs[flow]))
        del self.flow_UIs[flow]

    def get_current_flow(self):
        return self.core_session.flows[self.ui.flows_tab_widget.currentIndex()]

    def focus_on_flow(self, flow):
        self.ui.flows_tab_widget.setCurrentWidget(self.flow_UIs[flow])

    def import_packages(self, packages_list: [NodesPackage]):
        for p in packages_list:
            self.import_nodes(p)

    def import_nodes(self, package: NodesPackage = None, path: str = None):

        if package is not None:
            p = package
        else:
            p = NodesPackage(path)

        if p in self.node_packages.values():
            # never import package twice!
            # different packages with same name are forbidden
            print('package with this name already exists')
            return

        try:
            nodes = import_nodes_package(p)
        except ModuleNotFoundError as e:
            msg_box = QMessageBox(QMessageBox.Warning, 'Missing Python module', str(e), QMessageBox.Ok, self)
            msg_box.exec_()
            sys.exit(e)

        self.core_session.register_nodes(nodes)

        for n in nodes:
            self.node_packages[n] = p

        self.nodes_list_widget.update_list(self.core_session.nodes)

    def save_project(self, file_name):
        import json

        file = None
        try:
            if os.path.exists(file_name):
                os.remove(file_name)
            file = open(file_name, 'w')
        except FileNotFoundError:
            rc.InfoMsgs.write('couldn\'t open file')
            return

        general_project_info_dict = {'type': 'Ryven project file', 'ryven version': __version__}

        flows_data = self.core_session.serialize()

        required_packages = set()
        for node in self.core_session.all_node_objects():
            if node.__class__ not in self.node_packages.keys() or \
                    self.node_packages[node.__class__] is None or \
                    self.node_packages[node.__class__].name == 'built_in':
                continue
            required_packages.add(
                self.node_packages[node.__class__]
            )

        whole_project_dict = {'general info': general_project_info_dict,
                              'required packages': [p.config_data() for p in required_packages],
                              **flows_data}

        data = json.dumps(whole_project_dict, indent=4)
        rc.InfoMsgs.write(data)

        file.write(data)
        file.close()
