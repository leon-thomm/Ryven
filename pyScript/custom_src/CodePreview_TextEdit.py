from PySide2.QtWidgets import QTextEdit
from PySide2.QtGui import QFont

from custom_src.CodePreview_Highlighter import CodePreview_Highlighter


class CodePreview_TextEdit(QTextEdit):
    def __init__(self):
        super(CodePreview_TextEdit, self).__init__()

        self.setFont(QFont('source code pro', 10))
        self.setReadOnly(True)

        self.highlighter = CodePreview_Highlighter()

    def enable_highlighting(self):
        self.highlighter.setDocument(self.document())
        self.setStyleSheet('''
        QTextEdit {
            background-color: #333333;
            color: #eeeeff;
            border-radius: 3px;
        }
        ''')

    def disable_highlighting(self):
        self.highlighter.setDocument(None)
        self.setStyleSheet('''
        QTextEdit {
            background-color: #1a1a1a;
            color: #eeeeff;
            border-radius: 3px;
        }
        ''')