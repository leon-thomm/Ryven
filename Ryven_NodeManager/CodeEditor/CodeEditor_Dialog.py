from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QShortcut

from CodeEditor.CodeEditor_TextEdit import CodeEditor_TextEdit


class CodeEditor_Dialog(QDialog):
    def __init__(self, parent):
        super(CodeEditor_Dialog, self).__init__(parent)

        self.code_src_file_path = None
        self.code_initial = None

        self.text_edit = CodeEditor_TextEdit()
        self.text_edit.set_code(self.code_initial)


        # shortcuts
        save_shortcut = QShortcut(QKeySequence.Save, self)
        save_shortcut.activated.connect(self.close)


        # UI
        layout = QVBoxLayout()

        buttons_layout = QHBoxLayout()
        reset_push_button = QPushButton('reset')
        reset_push_button.clicked.connect(self.reset_clicked)
        ok_push_button = QPushButton('OK')
        ok_push_button.clicked.connect(self.close)
        buttons_layout.addStretch()
        buttons_layout.addWidget(reset_push_button)
        buttons_layout.addWidget(ok_push_button)

        layout.addWidget(self.text_edit)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

        self.resize(900, 500)
        self.setWindowTitle('edit metacode')

    def set_code(self, code, code_src_file_path=None):
        self.code_src_file_path = code_src_file_path
        self.code_initial = code
        self.text_edit.set_code(code)

    def get_code(self):
        return self.text_edit.get_code()

    def read_code_from_source(self):
        if self.code_src_file_path is None:
            return None

        try:
            f = open(self.code_src_file_path)
            code = f.read()
            f.close()
            return code
        except FileNotFoundError:
            # if the file has been removed, the initial code should be taken as source
            return self.code_initial

    def code_edited(self):
        return self.text_edit.get_code() != self.code_initial

    def code_source_changed(self):
        if self.code_src_file_path is None:
            return False
        else:
            return self.read_code_from_source() != self.code_initial

    def reset_clicked(self):
        msg_box = QMessageBox(QMessageBox.Warning, 'Resetting code',
                              'sure?', QMessageBox.Cancel | QMessageBox.Yes, self)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        ret = msg_box.exec_()
        if ret != QMessageBox.Yes:
            return

        self.text_edit.set_code(self.code_initial)