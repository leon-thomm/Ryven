from PySide2.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QFileDialog, QWidget
from PySide2.QtGui import QIcon

from custom_src.global_tools.Debugger import Debugger
from custom_src.startup_dialog.SelectPackages_Dialog import SelectPackages_Dialog


class StartupDialog(QDialog):
    def __init__(self):
        super(StartupDialog, self).__init__()

        layout = QVBoxLayout()

        # info text edit
        info_text_edit = QTextEdit()
        info_text_edit.setHtml('''
            <h2 style="font-family: Courier New; font-size: xx-large; color: #a9d5ef;">Welcome to Ryven</h2>
            <div style="font-family: Corbel; font-size: large;">
            
            <p><img style="float:right;" height=150 src="../resources/pics/program_icon2_light.png">Hi,
            I am Leon, the creator of Ryven. Please always keep in mind, that this
            is not a professional piece of software. Don\'t forget to save! :)
            I am sure there are bugs and problems but as long as you keep behaving
            as intended, you shouldn\'t get into too much trouble.
            <br>
            Note that this software uses Qt
            which is not free for commercial use. All rights remain to their lawful owners.
            All Ryven source code is written by me.
            <br>
            Enjoy!</p>
            <br>
            <br>
            Please select a mode to start the editor with. You can either create a plain new
            project, or you can load a saved one.
            </div>
        ''')
        info_text_edit.setReadOnly(True)
        layout.addWidget(info_text_edit)

        # buttons
        plain_project_push_button = QPushButton('create new plain project')
        plain_project_push_button.setFocus()
        plain_project_push_button.clicked.connect(self.plain_project_button_clicked)
        load_project_push_button = QPushButton('load project')
        load_project_push_button.clicked.connect(self.load_project_button_clicked)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(plain_project_push_button)
        buttons_layout.addWidget(load_project_push_button)

        layout.addLayout(buttons_layout)

        self.setLayout(layout)

        self.setWindowTitle('Ryven')
        self.setWindowIcon(QIcon('../resources/pics/program_icon2.png'))
        self.setFixedSize(500, 280)

        self.load_stylesheet('dark')

        self.editor_startup_configuration = {}


    def load_stylesheet(self, ss):  # TODO: move to global_tools
        """Using the parent's SS doesn't work here, because this dialog does not have any parent -
        MainWindow is yet to be created."""

        ss_content = ''
        try:
            f = open('../resources/stylesheets/'+ss+'.txt')
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

        file_name = QFileDialog.getOpenFileName(self, 'select project file', '../saves', 'Ryven Project(*.rpo *.rypo)')[0]
        j_str = ''
        try:
            f = open(file_name)
            j_str = f.read()
            f.close()
        except FileNotFoundError:
            Debugger.debug('couldn\'t open file')
            return


        # strict=False has to be to allow 'control characters' like '\n' for newline when loading the json
        j_obj = json.loads(j_str, strict=False)

        if j_obj['general info']['type'] != 'Ryven project file':
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


        if len(packages) > 0:
            select_packages_dialog = SelectPackages_Dialog(self, packages)
            select_packages_dialog.exec_()
            package_file_paths = select_packages_dialog.file_paths


        self.editor_startup_configuration['required packages'] = package_file_paths
        self.editor_startup_configuration['content'] = j_obj

        self.accept()