import os
import pathlib

from qtpy.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QFileDialog,
    QRadioButton, QLabel, QFormLayout, QComboBox, QDialogButtonBox,
    QCheckBox, QListWidget, QListWidgetItem,
    QStyleOptionFrame, QStyle)
from qtpy.QtCore import Qt, QSize
from qtpy.QtGui import QIcon, QPainter

from ryven.main.nodes_package import NodesPackage
from ryven.main.utils import (
    abs_path_from_package_dir, abs_path_from_ryven_dir, ryven_dir_path,
    process_nodes_packages)
from ryven.gui.styling.window_theme import apply_stylesheet


CREATE_PROJECT = '<create new project>'
DEFAULT_FLOW_THEME = '<default>'
FLOW_THEMES = [
    DEFAULT_FLOW_THEME,
    # FIXME: Automatically get flow themes?
    'toy', 'tron', 'ghost', 'blender', 'simple', 'ueli',
    'pure dark', 'colorful dark',
    'pure light', 'colorful light', 'industrial', 'fusion']


class ElideLabel(QLabel):
    """A QLabel with ellipsis, if the text is too long to be fully displayed.

    See:
        https://stackoverflow.com/questions/68092087/one-line-elideable-qlabel#answer-68092991

    Copyright (C) 2021  https://github.com/MaurizioB/
    """
    _elideMode = Qt.ElideMiddle

    def setText(self, label, *args, **kwargs):
        """Sets text and tooltip."""
        s = str(label)
        super().setText(s, *args, **kwargs)
        self.setToolTip(s)

    def elideMode(self):
        return self._elideMode

    def setElideMode(self, mode):
        if self._elideMode != mode and mode != Qt.ElideNone:
            self._elideMode = mode
            self.updateGeometry()

    def minimumSizeHint(self):
        return self.sizeHint()

    def sizeHint(self):
        hint = self.fontMetrics().boundingRect(self.text()).size()
        l, t, r, b = self.getContentsMargins()
        margin = self.margin() * 2
        return QSize(
            min(100, hint.width()) + l + r + margin,
            min(self.fontMetrics().height(), hint.height()) + t + b + margin
        )

    def paintEvent(self, event):
        qp = QPainter(self)
        opt = QStyleOptionFrame()
        self.initStyleOption(opt)
        self.style().drawControl(
            QStyle.CE_ShapedFrame, opt, qp, self)
        l, t, r, b = self.getContentsMargins()
        margin = self.margin()
        try:
            # since Qt >= 5.11
            m = self.fontMetrics().horizontalAdvance('x') / 2 - margin
        except:
            m = self.fontMetrics().width('x') / 2 - margin
        r = self.contentsRect().adjusted(
            margin + m,  margin, -(margin + m), -margin)
        qp.drawText(r, self.alignment(),
            self.fontMetrics().elidedText(
                self.text(), self.elideMode(), r.width()))


class StartupDialog(QDialog):
    """The welcome dialog.

    The user can choose between creating a new project and loading a saved or
    example project. When a project is loaded, it scans for validity of all
    the required packages for the project, and in case some paths are invalid,
    they are shown in the dialog. The user than can autoimport those missing
    packages or cherry pick packages.

    The user can also set some common configuration options.
    """

    def __init__(self, configs, parent=None):
        """Inizialize the `StartupDialog` class.

        Parameters
        ----------
        configs : dict
            The configuration dictionary, which most likely comes from the
            parsing the command line arguments.
        parent : QWidget, optional
            The parent `QWidget`.
            The default is `None`.

        Returns
        -------
        None.

        """
        super().__init__(parent)

        # Make a copy of the configs dictionary, so that we do not mess with it
        self.configs = configs.copy()

        #
        # Layout the contents of the dialog
        #

        layout = QVBoxLayout()

        # Top info text edit
        info_text_edit = QTextEdit()
        info_text_edit.setHtml(f'''
            <center>
                <h2 style="font-family: Segoe UI; font-size: xx-large; font-weight: 400; color: #a9d5ef;">
                    Welcome to Ryven
                </h2>
            </center>
            <div style="font-family: Corbel; font-size: x-large;">
                <img style="float:right;" height=120 src="{abs_path_from_package_dir('resources/pics/Ryven_icon_blurred.png')}"
                >Hey, it's Leon, the creator of Ryven. Keep in mind that this
                is not a professional piece of software. Don't forget to save!
                There are always some bugs and issues, but as long as you keep
                behaving as intended, you shouldn't get into too much trouble.
                Have fun!
            </div>
        ''')
        info_text_edit.setReadOnly(True)
        layout.addWidget(info_text_edit)

        # The form with the configuration options
        fbox = QFormLayout()

        # Project
        project_label = QLabel('Project:')

        project_layout = QVBoxLayout()
        self.project_name = ElideLabel()
        if configs['project']:
            self.project_name.setText(configs['project'])
        else:
            self.project_name.setText(CREATE_PROJECT)
        project_layout.addWidget(self.project_name)

        project_buttons_widget = QDialogButtonBox()
        self.create_project_button = QPushButton('New')
        self.create_project_button.setToolTip('Create a new project')
        self.create_project_button.setDefault(True)
        self.create_project_button.clicked.connect(self.create_project_button_clicked)
        project_buttons_widget.addButton(self.create_project_button, QDialogButtonBox.ActionRole)
        load_project_button = QPushButton('Load')
        load_project_button.setToolTip('Load an existing project')
        load_project_button.clicked.connect(self.load_project_button_clicked)
        project_buttons_widget.addButton(load_project_button, QDialogButtonBox.ActionRole)
        load_example_project_button = QPushButton('Example')
        load_example_project_button.setToolTip('Load a Ryven example')
        load_example_project_button.clicked.connect(self.load_example_project_button_clicked)
        project_buttons_widget.addButton(load_example_project_button, QDialogButtonBox.ActionRole)
        project_layout.addWidget(project_buttons_widget)

        fbox.addRow(project_label, project_layout)

        # Nodes packages
        packages_label = QLabel('Nodes packages:')

        packages_layout = QVBoxLayout()
        packages_sublayout = QHBoxLayout()

        # FIXME: The three following columns should have half their default size!
        # ???: How is that achieved?
        packages_imported_layout = QVBoxLayout()
        label_imported = QLabel('Imported:')
        label_imported.setToolTip('Nodes packages which are required by the project and are found')
        label_imported.setAlignment(Qt.AlignCenter)
        packages_imported_layout.addWidget(label_imported)
        self.imported_list_widget = QListWidget()
        packages_imported_layout.addWidget(self.imported_list_widget)
        packages_sublayout.addLayout(packages_imported_layout)

        packages_missing_layout = QVBoxLayout()
        label_missing = QLabel('Missing:')
        label_missing.setToolTip('Nodes packages which are required by the project but could not be found')
        label_missing.setAlignment(Qt.AlignCenter)
        packages_missing_layout.addWidget(label_missing)
        self.missing_list_widget = QListWidget()
        packages_missing_layout.addWidget(self.missing_list_widget)
        packages_sublayout.addLayout(packages_missing_layout)

        packages_manually_layout = QVBoxLayout()
        label_manually = QLabel('Manually imported:')
        label_manually.setToolTip('Nodes packages which are manually imported\nThey will override the packages required by the project\nAdditional packages can be imported later …')
        label_manually.setAlignment(Qt.AlignCenter)
        packages_manually_layout.addWidget(label_manually)
        self.manually_list_widget = QListWidget()
        self.manually_list_widget.setSelectionMode(QListWidget.MultiSelection)
        self.manually_list_widget.itemSelectionChanged.connect(self.packages_manually_selection)
        packages_manually_layout.addWidget(self.manually_list_widget)
        packages_sublayout.addLayout(packages_manually_layout)

        packages_layout.addLayout(packages_sublayout)

        packages_buttons_widget = QDialogButtonBox()
        self.autoimport_packages_button = QPushButton('Auto import')
        self.autoimport_packages_button.setToolTip('Automatically find and import missing packages')
        self.autoimport_packages_button.clicked.connect(self.autoimport_package_clicked)
        packages_buttons_widget.addButton(self.autoimport_packages_button, QDialogButtonBox.ActionRole)
        self.autoimport_packages_button.setEnabled(False)
        import_package_button = QPushButton('Import')
        import_package_button.setToolTip('Manually load a nodes package')
        import_package_button.clicked.connect(self.import_package_clicked)
        packages_buttons_widget.addButton(import_package_button, QDialogButtonBox.ActionRole)
        self.remove_packages_button = QPushButton('Remove')
        self.remove_packages_button.setToolTip('Remove manually imported nodes packages')
        self.remove_packages_button.clicked.connect(self.remove_packages_clicked)
        self.remove_packages_button.setEnabled(False)
        packages_buttons_widget.addButton(self.remove_packages_button, QDialogButtonBox.ActionRole)
        self.clear_packages_button = QPushButton('Clear')
        self.clear_packages_button.setToolTip('Clear the list of manually imported nodes packages ')
        self.clear_packages_button.clicked.connect(self.clear_packages_clicked)
        self.clear_packages_button.setEnabled(False)
        packages_buttons_widget.addButton(self.clear_packages_button, QDialogButtonBox.ActionRole)
        packages_layout.addWidget(packages_buttons_widget)

        fbox.addRow(packages_label, packages_layout)

        # Window theme
        windowtheme_label = QLabel('Window theme:')
        windowtheme_layout = QHBoxLayout()
        self.dark_theme_rb = QRadioButton('dark')
        self.dark_theme_rb.toggled.connect(self.windowtheme_toggled)
        self.light_theme_rb = QRadioButton('light')
        self.light_theme_rb.toggled.connect(self.windowtheme_toggled)
        plain_theme_rb = QRadioButton('plain')
        plain_theme_rb.toggled.connect(self.windowtheme_toggled)
        windowtheme_layout.addWidget(self.dark_theme_rb)
        windowtheme_layout.addWidget(self.light_theme_rb)
        windowtheme_layout.addWidget(plain_theme_rb)
        fbox.addRow(windowtheme_label, windowtheme_layout)

        # Flow theme
        flowtheme_label = QLabel('Flow theme:')
        flowtheme_widget = QComboBox()
        flowtheme_widget.setToolTip('Select the theme of the flow display\nCan also be changed later …')
        flowtheme_widget.addItems(FLOW_THEMES)
        flowtheme_widget.insertSeparator(1)
        flowtheme_widget.currentTextChanged.connect(self.flowtheme_selected)
        fbox.addRow(flowtheme_label, flowtheme_widget)

        # FIXME: Should the performance/animations and info-message be added?

        # Debug
        debug_label = QLabel('Debug:')
        debug_cb = QCheckBox('Enable debug output')
        debug_cb.setToolTip('Select if debug output should be displayed\nCan also be changed later …')
        debug_cb.toggled.connect(self.debug_toggled)
        fbox.addRow(debug_label, debug_cb)

        layout.addLayout(fbox)

        # Buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.ok_button = buttons.button(QDialogButtonBox.Ok)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

        #
        # Populate/set the widgets
        #

        # Set project
        self.load_project(configs['project'])

        # Set requested nodes
        self.update_packages_lists()

        # Set window theme
        self.dark_theme_rb.setChecked(configs['window_theme'] == 'dark')
        self.light_theme_rb.setChecked(configs['window_theme']== 'light')
        plain_theme_rb.setChecked(configs['window_theme'] not in ('dark', 'light'))

        # Set flow theme
        if configs['flow_theme']:
            idx = flowtheme_widget.findText(configs['flow_theme'])
        else:
            idx = -1
        if idx < 0:
            idx = flowtheme_widget.findText(DEFAULT_FLOW_THEME)
        flowtheme_widget.setCurrentIndex(idx)

        # Set debug
        debug_cb.setChecked(configs['debug'])

        # Set window title and icon
        self.setWindowTitle('Ryven')
        self.setWindowIcon(QIcon(abs_path_from_package_dir('resources/pics/Ryven_icon.png')))

    #
    # Call-back methods
    #

    # Project

    def create_project_button_clicked(self):
        """Call-back method, whenever the 'New' button was clicked."""
        # Create a new project
        self.load_project(None)

    def load_project_button_clicked(self):
        """Call-back method, whenever the 'Load' button was clicked."""
        # Load a saved project, starting in the user's ryven directory
        project_path = self.get_project(abs_path_from_ryven_dir('saves'))

        if project_path is not None:
            self.load_project(project_path)

    def load_example_project_button_clicked(self):
        """Call-back method, whenever the 'Example' button was clicked."""
        # Load an example project, starting in the ryven's example directory
        project_path = self.get_project(
            abs_path_from_package_dir('examples_projects'),
            title='Select Ryven example')

        if project_path is not None:
            self.load_project(project_path)

    # Nodes packages

    def packages_manually_selection(self):
        """Call-back method, whenever a package in the manual list was selected."""
        # En/Disable the 'Remove' button
        if self.manually_list_widget.selectedItems():
            self.remove_packages_button.setEnabled(True)
        else:
            self.remove_packages_button.setEnabled(False)

    def autoimport_package_clicked(self):
        """Call-back method, whenever the 'Auto import' button was clicked."""
        # Search in user packages
        self.auto_import(pathlib.Path(ryven_dir_path(), 'nodes'))
        self.update_packages_lists()

        # Search in example packages
        self.auto_import(pathlib.Path(abs_path_from_package_dir('example_nodes')))
        self.update_packages_lists()

    def import_package_clicked(self):
        """Call-back method, whenever the 'Import' button was clicked."""
        # Import a nodes package, starting in the user's ryven directory
        file_name = QFileDialog.getOpenFileName(
            self, 'Select',
            abs_path_from_ryven_dir('packages'),
            '(nodes.py)')[0]

        if file_name:
            file_path = pathlib.Path(file_name)
            if file_path.exists():
                self.configs['nodes'].add(NodesPackage(file_path.parent))
                self.update_packages_lists()

    def remove_packages_clicked(self):
        """Call-back method, whenever the 'Remove' button was clicked."""
        # Remove packages selected in the manual imported list
        for item in self.manually_list_widget.selectedItems():
            node_name = item.text()
            for node in self.configs['nodes']:
                if node.name == node_name:
                    self.configs['nodes'].remove(node)
                    break

        self.update_packages_lists()

    def clear_packages_clicked(self):
        """Call-back method, whenver the 'Clear' button was clicked."""
        # Clear the manual imported list
        self.configs['nodes'].clear()

        self.update_packages_lists()

    # Window theme

    def windowtheme_toggled(self):
        """Call-back method, whenever a window theme radio button was toggled."""
        # Apply the selected window theme
        if self.dark_theme_rb.isChecked():
            self.configs['window_theme'] = apply_stylesheet('dark')
        elif self.light_theme_rb.isChecked():
            self.configs['window_theme'] = apply_stylesheet('light')
        else:
            self.configs['window_theme'] = apply_stylesheet(None)

    # Flow theme

    def flowtheme_selected(self, theme):
        """Call-back method, whenever a new flow theme was selected."""
        # "Apply" the selected flow theme
        if theme == DEFAULT_FLOW_THEME:
            self.configs['flow_theme'] = None
        else:
            self.configs['flow_theme'] = theme

    # Debug

    def debug_toggled(self, check):
        """Call-back method, whenever the debug checkbox was toggled."""
        # "Apply" the debug option
        self.configs['debug'] = check

    #
    # Helper/Working methods
    #

    def get_project(self, base_dir: str, title='Select project file'):
        """Get a project file from the user.

        Parameters
        ----------
        base_dir : str|pathlib.Path
            The initial directory shown in the file dialog.
        title : str, optional
            The title of the file dialog.
            The default is 'Select project file'.

        Returns
        -------
        file_path : pathlib.Path|None
            The path of the selected file.

        """
        # Get the file from the user
        file_name = QFileDialog.getOpenFileName(
            self, title,
            str(base_dir), 'JSON (*.json)'
            )[0]

        if file_name:
            file_path = pathlib.Path(file_name)
            if file_path.exists():
                return file_path

        return None

    def load_project(self, project_path: pathlib.Path):
        """Load a project file.

        It opens the project file and scans for all required node packages.
        These are displayed in the imported packages list. All packages which
        could not be found are displayed in the missing packages list.

        Parameters
        ----------
        project_path : pathlib.Path
            The project's file name to be loaded.

        Returns
        -------
        None.

        """

        self.imported_list_widget.clear()
        self.missing_list_widget.clear()

        if project_path is None:
            self.configs['project'] = None
            self.project_name.setText(CREATE_PROJECT)
            self.create_project_button.setEnabled(False)

        else:
            self.configs['project'] = project_path
            self.project_name.setText(project_path)
            self.create_project_button.setEnabled(True)

            required_nodes, missing_nodes, _ = process_nodes_packages(project_path)
            item_flags = ~Qt.ItemIsSelectable & ~Qt.ItemIsEditable
            for node in sorted(required_nodes, key=lambda n: n.name):
                node_item = QListWidgetItem(node.name)
                node_item.setToolTip(node.directory)
                node_item.setFlags(item_flags)
                self.imported_list_widget.addItem(node_item)
            for node_path in sorted(missing_nodes, key=lambda p: p.name):
                node_item = QListWidgetItem(node_path.name)
                node_item.setToolTip(str(node_path))
                node_item.setFlags(item_flags)
                self.missing_list_widget.addItem(node_item)

        self.update_packages_lists()

    def auto_import(self, packages_dir: str):
        """Automatically find and import missing packages.

        Parameters
        ----------
        packages_dir : str|pathlib.Path
            The directory under which packages should be searched.

        Returns
        -------
        None.

        """
        # List of packages which are missing
        missing_packages = [
            self.missing_list_widget.item(i).text()
            for i in range(self.missing_list_widget.count())]

        # Search for missing packages under `package_dir`
        for top, dirs, files in os.walk(packages_dir):
            path = pathlib.Path(top)
            if path.name in missing_packages:
                node_path = path.joinpath('nodes.py')
                if node_path.exists():
                    self.configs['nodes'].add(NodesPackage(path))

    def update_packages_lists(self):
        """Update the packages lists and buttons.

        1. Mark all imported packages, if they were manually imported.
        2. Mark all missing packages, if they were manually imported.
        3. Repopulate the list with manually imported packages.
        4. En/Disable 'Ok', 'Auto import' and 'Clear' buttons.
        """
        # Mark all imported packages, if they were manually imported
        for i in range(self.imported_list_widget.count()):
            node_item = self.imported_list_widget.item(i)
            font = node_item.font()
            for node in self.configs['nodes']:
                if node_item.text() == node.name:
                    # Required package is overwritten by manually imported package
                    font.setStrikeOut(True)
                    break
            else:
                font.setStrikeOut(False)
            node_item.setFont(font)

        # Mark all missing packages, if they were manually imported
        missing_packages = False         # Track, if we have to enable the 'Auto import' button
        for i in range(self.missing_list_widget.count()):
            node_item = self.missing_list_widget.item(i)
            font = node_item.font()
            for node in self.configs['nodes']:
                if node_item.text() == node.name:
                    # Missing package is provided by manually imported package
                    font.setStrikeOut(True)
                    break
            else:
                font.setStrikeOut(False)
                missing_packages = True
            node_item.setFont(font)

        # Repopulate the list with manually imported packages
        self.manually_list_widget.clear()
        for node in sorted(self.configs['nodes'], key=lambda n: n.name):
            node_item = QListWidgetItem(node.name)
            node_item.setToolTip(str(node.directory))
            node_item.setFlags(~Qt.ItemIsEditable)
            self.manually_list_widget.addItem(node_item)

        # Update the buttons
        if missing_packages:
            # There are still packages missing
            self.ok_button.setEnabled(False)
            self.ok_button.setToolTip('Import all missing packages first')
            self.autoimport_packages_button.setEnabled(True)
        else:
            # No missing packages
            self.ok_button.setEnabled(True)
            self.ok_button.setToolTip(None)
            self.autoimport_packages_button.setEnabled(False)
        self.clear_packages_button.setEnabled(bool(self.configs['nodes']))
