from qtpy.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QFileDialog, QRadioButton
from qtpy.QtGui import QIcon

from ryven.main.nodes_package import NodesPackage
from ryven.main.utils import abs_path_from_package_dir, abs_path_from_ryven_dir
from ryven.gui.styling.window_theme import apply_stylesheet
from ryven.gui.startup_dialog.SelectPackages_Dialog import SelectPackages_Dialog


class StartupDialog(QDialog):
    """
    The welcome dialog. The user can choose between creating a new project and loading a saved project.
    When a project is loaded, it scans for validity of all the required packages for the project, and in case
    some paths are invalid, the SelectPackages_Dialog is opened to get the paths to those missing package files.
    """

    def __init__(self):
        super(StartupDialog, self).__init__()

        layout = QVBoxLayout()

        # info text edit
        info_text_edit = QTextEdit()
        info_text_edit.setHtml('''
            <center>
                <h2 style="font-family: Segoe UI; font-size: xx-large; font-weight: 400; color: #a9d5ef;">
                    Welcome to Ryven
                </h2>
            </center>
            <div style="font-family: Corbel; font-size: x-large;">
            
                <p>
                    <img style="float:right;" height=120 src="../resources/pics/Ryven_icon_blurred.png">Hey,
                    it's Leon, the creator of Ryven. Keep in mind that this
                    is not a professional piece of software. Don\'t forget to save!
                    There are always some bugs and issues but as long as you keep behaving
                    as intended, you shouldn\'t get into too much trouble. Have fun!
                </p>
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
        load_example_project_push_button = QPushButton('load example')
        load_example_project_push_button.clicked.connect(self.load_example_project_button_clicked)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(plain_project_push_button)
        buttons_layout.addWidget(load_project_push_button)
        buttons_layout.addWidget(load_example_project_push_button)

        layout.addLayout(buttons_layout)

        self.window_theme = apply_stylesheet('dark')

        choose_theme_layout = QHBoxLayout()
        self.dark_theme_rb = QRadioButton('dark')
        self.dark_theme_rb.setChecked(True)
        self.dark_theme_rb.toggled.connect(self.theme_toggled)
        self.light_theme_rb = QRadioButton('light')
        self.light_theme_rb.toggled.connect(self.theme_toggled)
        choose_theme_layout.addWidget(self.dark_theme_rb)
        choose_theme_layout.addWidget(self.light_theme_rb)
        layout.addLayout(choose_theme_layout)

        self.setLayout(layout)

        self.setWindowTitle('Ryven')
        self.setWindowIcon(QIcon(abs_path_from_package_dir('resources/pics/Ryven_icon.png')))
        self.setFixedSize(500, 280)

        self.editor_startup_configuration = {}


    def theme_toggled(self):
        if self.dark_theme_rb.isChecked():
            self.window_theme = apply_stylesheet('dark')
        else:
            self.window_theme = apply_stylesheet('light')


    def plain_project_button_clicked(self):
        self.editor_startup_configuration['config'] = 'create plain new project'
        self.accept()


    def load_project_button_clicked(self):
        self.open_project(base_dir=abs_path_from_ryven_dir('saves'))


    def load_example_project_button_clicked(self):
        self.open_project(base_dir=abs_path_from_package_dir('examples_projects'))


    def open_project(self, base_dir: str):
        """1. Opens a file dialog for selecting a project tile; returns on FileNotFoundError,
        2. Opens the project and scans all required node packages,
        3. If node packages are missing (i.e. they cannot be found under the path specified
        in the project file anymore) it opens the SelectPackages_Dialog

        :param base_dir: path to directory where file dialog opens
        """

        self.editor_startup_configuration['config'] = 'open project'
        import json

        file_name = \
            QFileDialog.getOpenFileName(
                self, 'select project file',
                base_dir, 'JSON (*.json)'
            )[0]

        try:
            f = open(file_name)
            project_str = f.read()
            f.close()
        except FileNotFoundError:
            # TODO: do something useful here
            return

        # strict=False has to be to allow 'control characters' like '\n' for newline when loading the json
        project_dict = json.loads(project_str, strict=False)

        # scan for all required packages
        valid_node_packages = []
        missing_node_package_names = []
        for p in project_dict['required packages']:
            try:
                f = open(p['dir']+'/nodes.py')
                f.close()
                valid_node_packages.append(NodesPackage(p['dir']))
            except FileNotFoundError:
                missing_node_package_names.append(p['name'])

        node_packages = valid_node_packages.copy()

        if len(missing_node_package_names) > 0:
            select_packages_dialog = SelectPackages_Dialog(self, required_packages=missing_node_package_names)
            select_packages_dialog.exec_()
            node_packages += select_packages_dialog.packages

        self.editor_startup_configuration['required packages'] = node_packages
        self.editor_startup_configuration['content'] = project_dict

        self.accept()
