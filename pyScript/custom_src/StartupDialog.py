from PySide2.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QFileDialog, QWidget, QLabel, QListWidget, QListWidgetItem
from PySide2.QtGui import QIcon

import os

from custom_src.GlobalAccess import GlobalStorage


class StartupDialog(QDialog):
    def __init__(self):
        super(StartupDialog, self).__init__()

        self.setLayout(QVBoxLayout())

        # info text edit
        info_text_edit = QTextEdit()
        info_text_edit.setHtml('''
            <h2 style="font-family: Courier New; font-size: xx-large; color: #a9d5ef;">Welcome to pyScript</h2>
            <div style="font-family: Corbel; font-size: large;">
            
            <p><img style="float:right;" height=150 src="stuff/pics/program_icon_light.png">Hi,
            I am Leon Thomm - the creator of pyScript. Please always keep in mind, that this
            is not a professional piece of software. Don\'t forget to save! :)
            I am sure there are bugs and problems but as long as you keep behaving
            as intended, you shouldn\'t get into too much trouble. This software is made with Qt and some further 
            Python libraries were used. All rights remain to the lawful owners. All direct pyScript source code is
            written by me.
            <br>
            Enjoy! Cheers.</p>
            <br>
            <br>
            Please select a mode to start the editor with. You can either create a plain new
            project, or you can load a saved one.
            </div>
        ''')
        info_text_edit.setReadOnly(True)
        self.layout().addWidget(info_text_edit)

        # buttons
        buttons_widget = QWidget()
        plain_project_push_button = QPushButton('create new plain project')
        plain_project_push_button.clicked.connect(self.plain_project_button_clicked)
        load_project_push_button = QPushButton('load project')
        load_project_push_button.clicked.connect(self.load_project_button_clicked)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(plain_project_push_button)
        buttons_layout.addWidget(load_project_push_button)

        buttons_widget.setLayout(buttons_layout)

        self.layout().addWidget(buttons_widget)

        self.setWindowTitle('pyScript')
        self.setWindowIcon(QIcon('stuff/pics/program_icon.png'))
        self.setFixedSize(500, 300)

        self.load_stylesheet('dark')

        self.editor_startup_configuration = {}


    def load_stylesheet(self, ss):
        ss_content = ''
        try:
            f = open('stuff/stylesheets/'+ss+'.txt')
            ss_content = f.read()
            f.close()
        finally:
            self.setStyleSheet(ss_content)


    def plain_project_button_clicked(self):
        self.editor_startup_configuration['config'] = 'create plain new project'
        self.accept()


    def load_project_button_clicked(self):
        self.editor_startup_configuration['config'] = 'open project'
        import json

        file_name = QFileDialog.getOpenFileName(self, 'select project file', '../saves', 'PyScript Project(*.pypro)')[0]
        j_str = ''
        try:
            f = open(file_name)
            j_str = f.read()
            f.close()
        except FileNotFoundError:
            GlobalStorage.debug('couldn\'t open file')
            return


        # strict=False has to be to allow 'control characters' like '\n' for newline when loading the json
        j_obj = json.loads(j_str, strict=False)

        if j_obj['general info']['type'] != 'pyScriptFP project file':
            return

        # scan for all required packages
        packages = []
        package_file_paths = []

        scripts = j_obj['scripts']
        for script in scripts:
            flow = script['flow']
            for n in flow['nodes']:
                package = n['parent node package']
                if package != 'built in' and not packages.__contains__(package):
                    packages.append(package)

        # GlobalStorage.debug('packages:', packages)

        if len(packages) > 0:
            select_packages_dialog = SelectPackages_Dialog(self, packages)
            select_packages_dialog.exec_()
            package_file_paths = select_packages_dialog.file_paths


        self.editor_startup_configuration['required packages'] = package_file_paths
        self.editor_startup_configuration['content'] = j_obj

        self.accept()





class SelectPackages_Dialog(QDialog):
    def __init__(self, parent, packages):
        super(SelectPackages_Dialog, self).__init__(parent)

        self.file_paths = []
        self.required_packages = packages

        self.setLayout(QVBoxLayout())

        self.layout().addWidget(QLabel('You need to select the locations of the following required node packages'))

        # package lists
        required_packages_list_widget = QListWidget()
        for p in packages:
            package_item = QListWidgetItem()
            package_item.setText(p)
            required_packages_list_widget.addItem(package_item)
        
        
        selected_items_widget = QWidget()
        selected_items_widget.setLayout(QVBoxLayout())
        self.selected_packages_list_widget = QListWidget()
        selected_items_widget.layout().addWidget(self.selected_packages_list_widget)

        auto_import_button = QPushButton('auto import')
        auto_import_button.clicked.connect(self.auto_import_button_clicked)
        selected_items_widget.layout().addWidget(auto_import_button)

        add_package_button = QPushButton('add')
        add_package_button.clicked.connect(self.add_package_button_clicked)
        selected_items_widget.layout().addWidget(add_package_button)

        clear_package_list_button = QPushButton('clear')
        clear_package_list_button.clicked.connect(self.clear_selected_packages_list)
        selected_items_widget.layout().addWidget(clear_package_list_button)

        finished_button = QPushButton('OK')
        finished_button.clicked.connect(self.finished_button_clicked)
        selected_items_widget.layout().addWidget(finished_button)

        packages_lists_widget = QWidget()
        packages_lists_widget.setLayout(QHBoxLayout())
        packages_lists_widget.layout().addWidget(required_packages_list_widget)
        packages_lists_widget.layout().addWidget(selected_items_widget)

        self.layout().addWidget(packages_lists_widget)

        self.setWindowTitle('select required packages')
        


    def auto_import_button_clicked(self):
        packages_dir = '../packages'
        folders_list = [x[0] for x in os.walk(packages_dir)]
        required_files = self.required_packages.copy()

        for folder in folders_list:
            for r_f in required_files:
                if r_f+'.pypac' in os.listdir(packages_dir+'/'+folder):
                    self.file_paths.append(packages_dir+'/'+folder+'/'+r_f+'.pypac')
                    break
            self.rebuild_selected_packages_list_widget()

        if len(self.file_paths) == len(self.required_packages):
            self.finished()


    def add_package_button_clicked(self):
        file_names = QFileDialog.getOpenFileNames(self, 'select package files', '../packages', 'PyScript Package(*.pypac)')[0]
        
        for file_name in file_names:
            try:
                f = open(file_name)
                f.close()
                self.file_paths.append(file_name)
            except FileNotFoundError:
                GlobalStorage.debug('couldn\'t open file')
        
        self.rebuild_selected_packages_list_widget()
    
    
    def rebuild_selected_packages_list_widget(self):
        # remove all items
        self.selected_packages_list_widget.clear()

        for f in self.file_paths:
            file_item = QListWidgetItem()
            file_item.setText(f)
            self.selected_packages_list_widget.addItem(file_item)


    def clear_selected_packages_list(self):
        self.file_paths.clear()
        self.rebuild_selected_packages_list_widget()


    def finished_button_clicked(self):
        # TODO analyse for potentially wrong packages

        self.finished()


    def finished(self):
        self.accept()