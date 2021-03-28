from PySide2.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QFileDialog
from PySide2.QtGui import QIcon


from ..startup_dialog.SelectPackages_Dialog import SelectPackages_Dialog


class StartupDialog(QDialog):
    def __init__(self):
        super(StartupDialog, self).__init__()

        layout = QVBoxLayout()

        # info text edit
        info_text_edit = QTextEdit()
        info_text_edit.setHtml('''
            <h2 style="font-family: Courier New; font-size: xx-large; color: #a9d5ef;">Welcome to Ryven</h2>
            <div style="font-family: Corbel; font-size: x-large;">
            
            <p><img style="float:right;" height=120 src="../resources/pics/Ryven_icon_blurred.png">Hey,
            it's Leon, the creator of Ryven. Keep in mind that this
            is not a professional piece of software. Don\'t forget to save!
            There are fore sure some bugs, but as long as you keep behaving
            as intended, you shouldn\'t get into too much trouble. Have fun!</p>
            <br>
            <br>
            Please select a mode to start the editor with. You can either create a plain new
            project, or you can load a saved one.
            </div>
        ''')
        info_text_edit.setReadOnly(True)
        layout.addWidget(info_text_edit)

        # buttons
        plain_project_push_button = QPushButton('create new project')
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
        self.setWindowIcon(QIcon('../resources/pics/Ryven_icon.png'))
        self.setFixedSize(550, 300)

        self.editor_startup_configuration = {}


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
            # InfoMsgs.write('couldn\'t open file')
            return


        # strict=False has to be to allow 'control characters' like '\n' for newline when loading the json
        j_obj = json.loads(j_str, strict=False)

        if j_obj['general info']['type'] != 'Ryven project file':
            return

        # scan for all required packages
        packages = self.extract_required_packages(j_obj)

        package_file_paths = []
        if len(packages) > 0:
            select_packages_dialog = SelectPackages_Dialog(self, packages)
            select_packages_dialog.exec_()
            package_file_paths = select_packages_dialog.file_paths


        self.editor_startup_configuration['required packages'] = package_file_paths
        self.editor_startup_configuration['content'] = j_obj

        self.accept()

    def extract_required_packages(self, j_obj):

        if 'required packages' in j_obj:
            return j_obj['required packages']

        # backwards compatibility
        packages = []
        scripts = j_obj['scripts']
        for script in scripts:
            flow = script['flow']
            for n in flow['nodes']:
                package = n['parent node package']
                if package != 'built in' and not packages.__contains__(package):
                    packages.append(package)

        return packages