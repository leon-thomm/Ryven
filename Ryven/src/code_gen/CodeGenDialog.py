from PySide2.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QPlainTextEdit, QShortcut, QMessageBox, QGroupBox, \
    QScrollArea, QCheckBox, QLabel


class CodeGenDialog(QDialog):
    def __init__(self, modules: dict, parent=None):
        super(CodeGenDialog, self).__init__(parent)

        self.modules = modules

        main_layout = QVBoxLayout()

        imports_group_box = QGroupBox('Imports')
        imports_group_box.setLayout(QVBoxLayout())

        info_text_edit = QPlainTextEdit('''I found the following imports in the inspected components. Please unselect all imports whose source code you want me to include in the output. All checked modules remain imported using the import statements. Notice that import alias names (import ... as ...) of course won\'t work when including the module\'s source. Same goes for imports using 'from' (indicated in the list below). And for those, the whole (direct) source will be included if you unselect a module.''')
        info_text_edit.setReadOnly(True)
        imports_group_box.layout().addWidget(info_text_edit)

        imports_scroll_area = QScrollArea()
        imports_scroll_area.setLayout(QVBoxLayout())

        self.import_widget_assignment = {'imports': {}, 'fromimports': {}}

        # imports
        imports_scroll_area.layout().addWidget(QLabel('imports:'))
        for i in modules['imports'].keys():
            import_check_box = QCheckBox(i)
            import_check_box.setChecked(True)
            imports_scroll_area.layout().addWidget(import_check_box)
            self.import_widget_assignment['imports'][import_check_box] = i

        # from-imports
        imports_scroll_area.layout().addWidget(QLabel('\'from\'-imports:'))
        for i in modules['fromimports'].keys():
            names = modules['fromimports'][i][2]
            from_names_list = ', '.join(names)
            import_check_box = QCheckBox(i + ': ' + from_names_list)
            import_check_box.setChecked(True)
            imports_scroll_area.layout().addWidget(import_check_box)
            self.import_widget_assignment['fromimports'][import_check_box] = i

        imports_group_box.layout().addWidget(imports_scroll_area)

        main_layout.addWidget(imports_group_box)

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout.addWidget(button_box)

        self.setLayout(main_layout)
        self.resize(500, 500)

        self.setWindowTitle('Source Code Gen Manager')

    def get_import_selection(self) -> dict:
        imports = self.modules['imports']
        ia = self.import_widget_assignment['imports']
        for k in ia.keys():
            imports[ia[k]][1] = k.isChecked()

        fromimports = self.modules['fromimports']
        fia = self.import_widget_assignment['fromimports']
        for k in fia.keys():
            fromimports[fia[k]][1] = k.isChecked()

        return {'imports': imports, 'fromimports': fromimports}