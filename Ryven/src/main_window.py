import sys
from os.path import join, dirname

from qtpy.QtGui import QIcon, QKeySequence
from qtpy.QtWidgets import QMainWindow, QFileDialog, QDialog, QShortcut, QAction, QActionGroup, QMenu, QMessageBox

from main_console import *
from script_UI import ScriptUI
from styling.window_theme import WindowTheme
from nodes_package import NodesPackage
from uic.ui_main_window import Ui_MainWindow
from tools import import_nodes_package
from nodes.NodeBase import NodeBase
from dialogs import GetTextDialog, ChooseScriptDialog

# ryvencore_qt
import ryvencore_qt as rc
import ryvencore_qt.src.conv_gui as rc_GUI



class MainWindow(QMainWindow):

    def __init__(self, config, window_theme: WindowTheme):
        super(MainWindow, self).__init__()

        self.session = None
        self.theme = window_theme
        self.node_packages = {}  # {Node: str}
        self.script_UIs = {}

        # SESSION
        self.session = rc.Session(node_class=NodeBase)
        # self.session.info_messenger().enable(True)

        self.session.flow_view_created.connect(self.script_created)
        self.session.script_renamed.connect(self.script_renamed)
        self.session.script_deleted.connect(self.script_deleted)

        # LOAD DESIGN AND FLOW THEME
        self.session.design.load_from_config('styling/design_config.json')

        if self.theme.name == 'dark':
            self.session.design.set_flow_theme(name='pure dark')
        else:  # 'light'
            self.session.design.set_flow_theme(name='pure light')

        # UI
        self.setup_ui()

        self.flow_view_theme_actions = []
        self.setup_menu_actions()

        self.setWindowTitle('Ryven')
        self.setWindowIcon(QIcon('../resources/pics/Ryven_icon.png'))
        self.ui.scripts_tab_widget.removeTab(0)  # remove placeholder tab

        # SHORTCUTS
        save_shortcut = QShortcut(QKeySequence.Save, self)
        save_shortcut.activated.connect(self.on_save_project_triggered)
        import_nodes_shortcut = QShortcut(QKeySequence('Ctrl+i'), self)
        import_nodes_shortcut.activated.connect(self.on_import_nodes_triggered)

        # TEMP FOLDER
        if not os.path.exists('../temp'):
            os.mkdir('../temp')
        for f in os.listdir('../temp'):
            os.remove('temp/'+f)

        # PROJECT SETUP
        if 'info_msgs' in sys.argv:
            rc.InfoMsgs.enable()

        #   SETUP MAIN CONSOLE
        MainConsole.instance.session = self.session
        MainConsole.instance.reset_interpreter()
        NodeBase.main_console = MainConsole.instance

        #   REGISTER BUILT-IN NODES
        self.import_nodes(path=join(dirname(__file__), 'nodes/built_in/'))

        #   LOAD PROJECT
        if config['config'] == 'create plain new project':
            self.session.create_script(title='hello world')
        elif config['config'] == 'open project':
            print('importing packages...')
            self.import_packages(config['required packages'])
            print('loading project...')
            self.session.load(config['content'])
            print('finished')

        self.resize(1500, 800)
        # self.showMaximized()

    def print_info(self):
        print('''
CONTROLS
place: right mouse
select: left mouse
pan: right mouse
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
            self.ui.bottom_splitter.addWidget(MainConsole.instance)
        # self.ui.right_vertical_splitter.setSizes([600, 0])

        # splitter sizes
        # self.ui.left_vertical_splitter.setSizes([350, 350])
        self.ui.main_vertical_splitter.setSizes([700, 0])

        self.nodes_list_widget = rc_GUI.NodeListWidget(self.session)
        self.ui.nodes_groupBox.layout().addWidget(self.nodes_list_widget)

    def setup_menu_actions(self):

        # flow designs
        light_themes_menu = QMenu('light')
        for d in self.session.design.flow_themes:
            design_action = QAction(d.name, self)
            if d.type_ == 'dark':
                self.ui.menuFlow_Design_Style.addAction(design_action)
            else:
                light_themes_menu.addAction(design_action)

            design_action.triggered.connect(self.on_design_action_triggered)
            self.flow_view_theme_actions.append(design_action)

        self.ui.menuFlow_Design_Style.addMenu(light_themes_menu)

        self.ui.actionImport_Nodes.triggered.connect(self.on_import_nodes_triggered)
        self.ui.actionSave_Project.triggered.connect(self.on_save_project_triggered)
        self.ui.actionNew_Script.triggered.connect(self.on_new_script_triggered)
        self.ui.actionRename_Script.triggered.connect(self.on_rename_script_triggered)
        self.ui.actionDelete_Script.triggered.connect(self.on_delete_script_triggered)
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

        self.ac_perf_mode_fast.setChecked(self.session.design.performance_mode == 'fast')
        self.ac_perf_mode_pretty.setChecked(self.session.design.performance_mode == 'pretty')

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

        self.ac_anims_active.setChecked(self.session.design.animations_enabled)
        self.ac_anims_inactive.setChecked(not self.session.design.animations_enabled)

        anims_ag.triggered.connect(self.on_animation_enabling_changed)

        animations_menu = QMenu('Animations', self)
        animations_menu.addAction(self.ac_anims_active)
        animations_menu.addAction(self.ac_anims_inactive)

        self.ui.menuView.addMenu(animations_menu)

    def load_stylesheet(self, ss):
        ss_content = ''
        try:
            f = open('../resources/stylesheets/'+ss+'.txt')
            ss_content = f.read()
            f.close()
        finally:
            self.session.set_stylesheet(ss_content)
            self.setStyleSheet(ss_content)

    # SLOTS

    def on_import_nodes_triggered(self):
        file_path = QFileDialog.getOpenFileName(self, 'select nodes file', '../packages', '(*.py)',)[0]
        if file_path != '':
            self.import_nodes(path=dirname(file_path))

    def on_performance_mode_changed(self, action):
        if action == self.ac_perf_mode_fast:
            self.session.design.set_performance_mode('fast')
        else:
            self.session.design.set_performance_mode('pretty')

    def on_animation_enabling_changed(self, action):
        if action == self.ac_anims_active:
            self.session.design.animations_enabled = True
        else:
            self.session.design.animations_enabled = False

    def on_design_action_triggered(self):
        index = self.flow_view_theme_actions.index(self.sender())
        self.session.design.set_flow_theme(self.session.design.flow_themes[index])

    def on_enable_info_msgs_triggered(self):
        rc.InfoMsgs.enable()

    def on_disable_info_msgs_triggered(self):
        rc.InfoMsgs.disable()

    def on_save_scene_pic_viewport_triggered(self):
        """Saves a picture of the currently visible viewport."""
        if len(self.session.scripts) == 0:
            return

        file_path = QFileDialog.getSaveFileName(self, 'select file', '', 'PNG(*.png)')[0]
        script = self.ui.scripts_tab_widget.currentWidget().script
        view = self.session.flow_views[script]
        img = view.get_viewport_img()
        img.save(file_path)

    def on_save_scene_pic_whole_triggered(self):
        """Saves a picture of the whole currently visible scene."""
        if len(self.session.scripts) == 0:
            return

        file_path = QFileDialog.getSaveFileName(self, 'select file', '', 'PNG(*.png)')[0]
        script = self.ui.scripts_tab_widget.currentWidget().script
        view = self.session.flow_views[script]
        img = view.get_whole_scene_img()
        img.save(file_path)

    def on_save_project_triggered(self):
        file_name = QFileDialog.getSaveFileName(self, 'select location and give file name',
                                                '../saves', '(*.json)')[0]
        if file_name != '':
            self.save_project(file_name)

    def on_new_script_triggered(self):
        new_script_title = GetTextDialog('choose unique title', '', 'new script title', self).get_text()

        if new_script_title not in (s.title for s in self.session.scripts):
            self.session.create_script(new_script_title)
        else:
            script = [s for s in self.session.scripts if s.title == new_script_title][0]
            self.focus_on_script(script)

    def on_rename_script_triggered(self):
        script = ChooseScriptDialog('choose script', self.session.scripts, self).get_script()
        new_title = GetTextDialog('new title', script.title, 'new script title', self).get_text()

        all_other_script_titles = [
            s.title for s in self.session.scripts if s != script
        ]

        if new_title not in all_other_script_titles:
            self.session.rename_script(script, new_title)

    def on_delete_script_triggered(self):
        script = ChooseScriptDialog('choose script', self.session.scripts, self).get_script()

        msg_box = QMessageBox(QMessageBox.Warning, 'sure about deleting script?',
                              'You are about to delete a script. This cannot be undone, all content will be gone. '
                              'Do you want to continue?', QMessageBox.Cancel | QMessageBox.Yes, self)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        ret = msg_box.exec_()
        if ret != QMessageBox.Yes:
            return

        self.session.delete_script(script)

    # SESSION

    def script_created(self, script, flow_view):
        script_widget = ScriptUI(self, script, flow_view)
        self.script_UIs[script] = script_widget
        self.ui.scripts_tab_widget.addTab(script_widget, script.title)
        self.focus_on_script(script)

    def script_renamed(self, script):
        self.ui.scripts_tab_widget.setTabText(
            self.session.scripts.index(script),
            script.title
        )

    def script_deleted(self, script):
        self.ui.scripts_tab_widget.removeTab(self.ui.scripts_tab_widget.indexOf(self.script_UIs[script]))
        del self.script_UIs[script]

    def get_current_script(self):
        return self.session.scripts[self.ui.scripts_tab_widget.currentIndex()]

    def focus_on_script(self, script):
        self.ui.scripts_tab_widget.setCurrentWidget(self.script_UIs[script])

    def import_packages(self, packages_list: [NodesPackage]):
        for p in packages_list:
            self.import_nodes(p)

    def import_nodes(self, package: NodesPackage = None, path: str = None):

        if package is not None:
            p = package
        else:
            p = NodesPackage(path)

        try:
            nodes = import_nodes_package(p)
        except ModuleNotFoundError as e:
            msg_box = QMessageBox(QMessageBox.Warning, 'Missing Python module', str(e), QMessageBox.Ok, self)
            msg_box.exec_()
            sys.exit()

        self.session.register_nodes(nodes)

        for n in nodes:
            self.node_packages[n] = p

        self.nodes_list_widget.update_list(self.session.nodes)

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

        general_project_info_dict = {'type': 'Ryven project file'}

        scripts_data = self.session.serialize()

        required_packages = set()
        for node in self.session.all_node_objects():
            if node.__class__ not in self.node_packages.keys() or \
                    self.node_packages[node.__class__] is None or \
                    self.node_packages[node.__class__].name == 'built_in':
                continue
            required_packages.add(
                self.node_packages[node.__class__]
            )

        whole_project_dict = {'general info': general_project_info_dict,
                              'required packages': [p.config_data() for p in required_packages],
                              **scripts_data}

        data = json.dumps(whole_project_dict, indent=4)
        rc.InfoMsgs.write(data)

        file.write(data)
        file.close()
