import os,  sys

from PySide2.QtGui import QColor, QFontDatabase, QIcon, QKeySequence
from PySide2.QtWidgets import QMainWindow, QFileDialog, QShortcut

# parent UI
from ui.ui_main_window import Ui_MainWindow

from custom_src.Node import Node, NodePort, SetVariable_Node, GetVariable_Node
from custom_src.Script import Script
from custom_src.custom_list_widgets.ScriptsListWidget import ScriptsListWidget
from custom_src.custom_nodes.GetVar_NodeInstance import GetVar_NodeInstance
from custom_src.custom_nodes.SetVar_NodeInstance import SetVar_NodeInstance
from custom_src.global_tools.Debugger import Debugger
from custom_src.Designs import Design


class MainWindow(QMainWindow):
    """MainWindow still lacks cleanup and documentation, sorry."""

    def __init__(self, config):
        super(MainWindow, self).__init__()

        QFontDatabase.addApplicationFont('fonts/poppins/Poppins-Medium.ttf')
        QFontDatabase.addApplicationFont('fonts/source code pro/SourceCodePro-Regular.ttf')

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.splitter.setSizes([120, 800])
        self.setWindowTitle('pyScript')
        self.setWindowIcon(QIcon('stuff/pics/program_icon.png'))
        self.load_stylesheet('dark')
        self.ui.scripts_tab_widget.removeTab(0)
        self.ui.actionImport_Nodes.triggered.connect(self.on_import_nodes_triggered)
        self.ui.actionSave_Project.triggered.connect(self.on_save_project_triggered)
        self.ui.actionDesignDark_Std.triggered.connect(self.on_dark_std_design_triggered)
        self.ui.actionDesignDark_Tron.triggered.connect(self.on_dark_tron_design_triggered)
        self.ui.actionEnableDebugging.triggered.connect(self.on_enable_debugging_triggered)
        self.ui.actionDisableDebugging.triggered.connect(self.on_disable_debugging_triggered)
        self.ui.actionSave_Pic_Viewport.triggered.connect(self.on_save_scene_pic_viewport_triggered)
        self.ui.actionSave_Pic_Whole_Scene_scaled.triggered.connect(self.on_save_scene_pic_whole_triggered)

        # Shortcuts
        save_shortcut = QShortcut(QKeySequence.Save, self)
        save_shortcut.activated.connect(self.on_save_project_triggered)

        self.custom_nodes = []
        self.all_nodes = [SetVariable_Node(), GetVariable_Node()]


        # holds NI subCLASSES for imported nodes:
        self.all_node_instance_classes = {
            self.all_nodes[0]: SetVar_NodeInstance,
            self.all_nodes[1]: GetVar_NodeInstance
        }  # (key: node obj, val: NI subclass) (used in Flow)

        # {node : {str: PortInstanceWidget-subclass}} (used in PortInstance)
        self.custom_node_input_widget_classes = {}

        # clear temp folder
        for f in os.listdir('temp'):
            os.remove('temp/'+f)

        self.scripts = []
        self.scripts_list_widget = ScriptsListWidget(self, self.scripts)
        self.ui.scripts_scrollArea.setWidget(self.scripts_list_widget)
        self.ui.add_new_script_pushButton.clicked.connect(self.create_new_script_button_pressed)
        self.ui.new_script_name_lineEdit.returnPressed.connect(self.create_new_script_le_return_pressed)

        self.design_style = 'dark std'


        if config['config'] == 'create plain new project':
            self.try_to_create_new_script()
        elif config['config'] == 'open project':
            self.import_required_packages(config['required packages'])
            self.parse_project(config['content'])

        self.resize(1500, 800)



    def load_stylesheet(self, ss):
        ss_content = ''
        try:
            f = open('stuff/stylesheets/'+ss+'.txt')
            ss_content = f.read()
            f.close()
        finally:
            self.setStyleSheet(ss_content)

    def on_dark_std_design_triggered(self):
        self.set_design('dark std')

    def on_dark_tron_design_triggered(self):
        self.set_design('dark tron')

    def set_design(self, new_design):
        Design.flow_style = new_design
        self.design_style = new_design
        for script in self.scripts:
            script.flow.design_style_changed()

    def on_enable_debugging_triggered(self):
        Debugger.enable()

    def on_disable_debugging_triggered(self):
        Debugger.disable()


    def on_save_scene_pic_viewport_triggered(self):
        if len(self.scripts) == 0:
            return

        file_path = QFileDialog.getSaveFileName(self, 'select file', '', 'PNG(*.png)')[0]
        img = self.scripts[self.ui.scripts_tab_widget.currentIndex()].flow.get_viewport_img()
        img.save(file_path)

    def on_save_scene_pic_whole_triggered(self):
        if len(self.scripts) == 0:
            return

        file_path = QFileDialog.getSaveFileName(self, 'select file', '', 'PNG(*.png)')[0]
        img = self.scripts[self.ui.scripts_tab_widget.currentIndex()].flow.get_whole_scene_img()
        img.save(file_path)


    def create_new_script_button_pressed(self):
        self.try_to_create_new_script(name=self.ui.new_script_name_lineEdit.text())

    def create_new_script_le_return_pressed(self):
        self.try_to_create_new_script(name=self.ui.new_script_name_lineEdit.text())


    def try_to_create_new_script(self, name='fancy script', config=None):
        if len(name) == 0:
            return
        for s in self.scripts:
            if s.name == name:
                return


        new_script = Script(self, name, config)
        new_script.name_changed.connect(self.rename_script)
        self.ui.scripts_tab_widget.addTab(new_script.widget, new_script.name)
        self.scripts.append(new_script)
        self.scripts_list_widget.recreate_ui()

    def rename_script(self, script, new_name):
        self.ui.scripts_tab_widget.setTabText(self.scripts.index(script), new_name)
        script.name = new_name

    def delete_script(self, script):
        index = self.scripts.index(script)
        self.ui.scripts_tab_widget.removeTab(index)
        del self.scripts[index]


    def on_import_nodes_triggered(self):
        file_path = QFileDialog.getOpenFileName(self, 'select nodes file', '../packages', 'PyScript Packages(*.pypac)',)[0]
        if file_path != '':
            self.import_nodes_package_from_file(file_path)

    def import_required_packages(self, packages_list):
        for p in packages_list:
            self.import_nodes_package_from_file(p)

    def import_nodes_package_from_file(self, file_path):
        j_str = ''
        try:
            f = open(file_path)
            j_str = f.read()
            f.close()
        except FileExistsError or FileNotFoundError:
            Debugger.debug('couldn\'t open file')
            return


        # Important: translate the package first (metacore files -> src code files)
        PackageTranslator = self.get_class_from_file(file_path='../pyScript_PackageTranslator',
                                                     file_name='pyScript_PackageTranslator',
                                                     class_name='PackageTranslator')
        package_translator = PackageTranslator(os.path.dirname(os.path.abspath(file_path)))


        self.parse_nodes(j_str, os.path.dirname(file_path), os.path.splitext(os.path.basename(file_path))[0])


    def parse_nodes(self, j_str, package_path, package_name):
        import json

        # strict=False is necessary to allow 'control characters' like '\n' for newline when loading the json
        j_obj = json.loads(j_str, strict=False)

        Debugger.debug(j_obj['type'])
        if j_obj['type'] != 'vyScriptFP nodes package':
            return

        # package_title = j_obj['title']
        # package_description = j_obj['description']
        j_nodes_list = j_obj['nodes']

        num_nodes = len(j_nodes_list)
        for ni in range(num_nodes):  # new node
            j_node = j_nodes_list[ni]

            new_node = Node()


            node_title = j_node['title']
            node_class_name = j_node['class name']
            node_description = j_node['description']
            node_type = j_node['type']
            node_has_main_widget = j_node['has main widget']
            node_main_widget_pos = j_node['widget position'] if node_has_main_widget else None
            node_design_style = j_node['design style']
            node_color = j_node['color']

            # every node has a custom module name which differs from it's name to prevent import issues when using
            # multiple (different) Nodes with same titles
            # FOR FURTHER EXPLANATION: see node manager
            node_module_name = j_node['module name']
            module_name_separator = '___'



            #   CUSTOM CLASS IMPORTS ----------------------------------------------------------------------------
            # creating all the necessary path variables here for all potentially imported classes


            #       IMPORT NODE INSTANCE SUBCLASS
            node_instance_class_file_path = package_path+'/nodes/'+node_module_name+'/'
            node_instance_widgets_file_path = node_instance_class_file_path+'/widgets'
            node_instance_filename = node_module_name  # the NI file's name is just the 'module name'
            new_node_instance_class = self.get_class_from_file(file_path=node_instance_class_file_path,
                                                               file_name=node_instance_filename,
                                                               class_name=node_class_name+'_NodeInstance')
            self.all_node_instance_classes[new_node] = new_node_instance_class

            #       IMPORT MAIN WIDGET
            if node_has_main_widget:
                main_widget_filename = node_module_name+module_name_separator+'main_widget'
                new_node.main_widget_class = self.get_class_from_file(file_path=node_instance_widgets_file_path,
                                                                      file_name=main_widget_filename,
                                                                      class_name=node_class_name+'_NodeInstance_MainWidget')

            #       I need to create the dict for the node's potential custom input widgets already here
            self.custom_node_input_widget_classes[new_node] = {}
            for w_name in j_node['custom input widgets']:
                input_widget_filename = node_module_name+module_name_separator+w_name
                custom_widget_class = self.get_class_from_file(file_path=node_instance_widgets_file_path,
                                                               file_name=input_widget_filename,
                                                               class_name=w_name+'_PortInstanceWidget')
                self.custom_node_input_widget_classes[new_node][w_name] = custom_widget_class


            #   note: the input widget classes get imported below in the loop
            # ---------------------------------------------------------------------------------------------------


            j_n_inputs = j_node['inputs']
            inputs = []
            num_inputs = len(j_n_inputs)
            for ii in range(num_inputs):
                j_input = j_n_inputs[ii]
                i_type = j_input['type']
                i_label = j_input['label']
                i_has_widget = None
                i_widget_type = ''
                i_widget_name = ''
                i_widget_pos = None
                if i_type == 'data':
                    i_has_widget = j_input['has widget']
                    if i_has_widget:
                        i_widget_type = j_input['widget type']
                        i_widget_pos = j_input['widget position']
                        if i_widget_type == 'custom widget':
                            i_widget_name = j_input['widget name']
                new_input = NodePort()
                new_input.type_ = i_type
                new_input.label = i_label
                if i_has_widget:
                    new_input.widget_type = i_widget_type
                    new_input.widget_name = i_widget_name
                    if i_widget_pos:
                        new_input.widget_pos = i_widget_pos
                else:
                    new_input.widget_type = 'None'
                inputs.append(new_input)

            j_n_outputs = j_node['outputs']
            outputs = []
            num_outputs = len(j_n_outputs)
            for oi in range(num_outputs):
                j_output = j_n_outputs[oi]
                o_type = j_output['type']
                o_label = j_output['label']
                new_output = NodePort()
                new_output.type_ = o_type
                new_output.label = o_label
                outputs.append(new_output)

            new_node.title = node_title
            new_node.description = node_description
            new_node.type_ = node_type
            new_node.package = package_name
            new_node.has_main_widget = node_has_main_widget
            if node_has_main_widget:
                new_node.main_widget_pos = node_main_widget_pos
            new_node.design_style = node_design_style
            new_node.color = QColor(node_color)
            new_node.inputs = inputs
            new_node.outputs = outputs

            
            self.custom_nodes.append(new_node)
            self.all_nodes.append(new_node)


        Debugger.debug(len(self.custom_nodes), 'nodes imported')


    def get_class_from_file(self, file_path, file_name, class_name):
        Debugger.debug(file_path)
        Debugger.debug(file_name)
        Debugger.debug(class_name)
        sys.path.append(file_path)
        new_module = __import__(file_name, fromlist=[class_name])
        new_class = getattr(new_module, class_name)
        return new_class



    def parse_project(self, j_obj):

        if j_obj['general info']['type'] != 'pyScriptFP project file':
            return

        for s in j_obj['scripts']:  # fill flows
            self.try_to_create_new_script(config=s)


    def on_save_project_triggered(self):
        file_name = ''
        file_name = QFileDialog.getSaveFileName(self, 'select location and give file name',
                                                '../saves', 'PyScript Project(*.pypro)')[0]
        if file_name != '':
            self.save_project(file_name)


    def save_project(self, file_name):
        import json

        file = None
        try:
            file = open(file_name, 'w')
        except FileNotFoundError:
            Debugger.debug('couldn\'t open file')
            return


        general_project_info_dict = {'type': 'pyScriptFP project file'}

        scripts_data = []
        for script in self.scripts:
            scripts_data.append(script.get_json_data())

        whole_project_dict = {'general info': general_project_info_dict,
                              'scripts': scripts_data}

        json_str = json.dumps(whole_project_dict)
        Debugger.debug(json_str)


        file.write(json_str)
        file.close()