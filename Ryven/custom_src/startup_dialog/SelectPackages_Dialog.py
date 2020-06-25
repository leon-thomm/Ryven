from PySide2.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QWidget, QLabel, \
    QListWidget, QListWidgetItem
import os

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
                if r_f + '.pypac' in os.listdir(packages_dir + '/' + folder):
                    self.file_paths.append(packages_dir + '/' + folder + '/' + r_f + '.pypac')
                    break
            self.rebuild_selected_packages_list_widget()

        if len(self.file_paths) == len(self.required_packages):
            self.finished()

    def add_package_button_clicked(self):
        file_names = \
        QFileDialog.getOpenFileNames(self, 'select package files', '../packages', 'PyScript Package(*.pypac)')[0]

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