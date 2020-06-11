from PySide2.QtWidgets import QTextEdit
from PySide2.QtGui import QFont


class CodePreview_TextEdit(QTextEdit):
    def __init__(self):
        super(CodePreview_TextEdit, self).__init__()

        self.setFont(QFont('source code pro', 10))
        self.setReadOnly(True)

        self.setStyleSheet('''
        QTextEdit {
            background-color: #1a1a1a;
        }
        ''')