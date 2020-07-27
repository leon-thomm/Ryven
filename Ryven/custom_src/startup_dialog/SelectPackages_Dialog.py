from PySide2.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QWidget, QLabel, \
    QListWidget, QListWidgetItem
import os

from custom_src.global_tools.Debugger import Debugger


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
        auto_import_button.setFocus()
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
        folders_list = [x[0] for x in os.walk(packages_dir) if
                        os.path.basename(os.path.normpath(x[0])) in self.required_packages]

        required_files = self.required_packages.copy()

        for folder in folders_list:
            for r_f in required_files:
                if r_f + '.rpc' in os.listdir(packages_dir + '/' + folder):
                    self.file_paths.append(os.path.normpath(packages_dir + '/' + folder + '/' + r_f + '.rpc'))
                    break
            self.rebuild_selected_packages_list_widget()

        self.clean_packages_list()

        if self.all_required_packages_selected():
            self.finished()

    def add_package_button_clicked(self):
        file_names = \
            QFileDialog.getOpenFileNames(self, 'select package files', '../packages', 'Ryven Package(*.rpc)')[0]

        for file_name in file_names:
            try:
                f = open(file_name)
                f.close()
                self.file_paths.append(file_name)
            except FileNotFoundError:
                Debugger.debug('couldn\'t open file')

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
        self.clean_packages_list()
        if self.all_required_packages_selected():
            self.finished()

    def clean_packages_list(self):
        """remove duplicates from self.file_paths"""

        files_dict = {}

        for p in self.file_paths:
            filename = os.path.splitext(os.path.basename(p))[0]
            files_dict[filename] = p

        self.file_paths = list(files_dict.values())

        self.rebuild_selected_packages_list_widget()

    def all_required_packages_selected(self):
        files = [os.path.splitext(os.path.basename(path))[0] for path in self.file_paths]

        # search for missing packages
        for p in self.required_packages:
            if p not in files:
                return False
        return True

    def finished(self):
        self.accept()