import sys

from qtpy.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QWidget, QLabel, \
    QListWidget, QListWidgetItem
import os
from os.path import basename, abspath, dirname, normpath, join, splitext

from nodes_package import NodesPackage


class SelectPackages_Dialog(QDialog):
    """
    Now only used to state new paths to required packages that are not valid anymore.
    The 'auto import' feature is therefore probably useless by now.
    """

    def __init__(self, parent, required_packages: [str]):
        super(SelectPackages_Dialog, self).__init__(parent)

        self.file_paths = []
        self.required_packages: [str] = required_packages
        self.packages = []

        self.setLayout(QVBoxLayout())

        self.layout().addWidget(QLabel('You need to select the locations of the following required node packages'))

        # package lists
        required_packages_list_widget = QListWidget()
        for p_name in required_packages:
            required_packages_list_widget.addItem(QListWidgetItem(p_name))

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
        folders_list = [basename(x[0]) for x in os.walk(packages_dir) if
                        basename(x[0]) in self.required_packages]

        required_packages = self.required_packages.copy()

        for pkg_name in required_packages:

            p_dir = join(packages_dir, pkg_name)
            p_file = normpath(join(p_dir, 'nodes.py'))

            if pkg_name in folders_list and \
                    'nodes.py' in os.listdir(p_dir) and \
                    p_file not in self.file_paths:

                self.file_paths.append(p_file)
                self.packages.append(NodesPackage(dirname(p_file)))

        self.rebuild_selected_packages_list_widget()

        self.clean_packages_list()

        if self.all_required_packages_selected():
            self.finished()

    def add_package_button_clicked(self):

        file_names = QFileDialog.getOpenFileNames(self, 'select package file (nodes.py)', '../packages', '(*.py)')[0]

        for file_name in file_names:
            try:
                # simply try to open the file to make sure it's valid
                f = open(file_name)
                f.close()

                self.file_paths.append(file_name)
                self.packages.append(NodesPackage(dirname(file_name)))

            except FileNotFoundError:
                pass

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
        self.packages.clear()

        self.rebuild_selected_packages_list_widget()

    def finished_button_clicked(self):
        self.clean_packages_list()
        if self.all_required_packages_selected():
            self.finished()

    def clean_packages_list(self):
        """remove duplicates from self.file_paths"""

        files_dict = {}

        for p in self.file_paths:
            package_name = basename(dirname(p))
            files_dict[package_name] = p

        self.file_paths = list(files_dict.values())

        self.rebuild_selected_packages_list_widget()

    def all_required_packages_selected(self):

        selected_packages = [basename(normpath(np.directory)) for np in self.packages]

        # search for missing packages
        for p in self.required_packages:
            if p not in selected_packages:
                return False

        return True

    def finished(self):
        self.accept()

    def closeEvent(self, arg__1) -> None:
        sys.exit()
