from PySide2.QtWidgets import QTextEdit
from PySide2.QtGui import QFont, QFontMetrics

from CodeEditor.CodeEditor_Hightlighter import CodeEditor_Highlighter


class CodeEditor_TextEdit(QTextEdit):
    def __init__(self):
        super(CodeEditor_TextEdit, self).__init__()

        self.highlighting = True

        self.setFont(QFont('source code pro', 11))
        self.setTabStopWidth(QFontMetrics(self.font()).width(' ')*4)

        self.highlighter = CodeEditor_Highlighter()
        self.highlighter.setDocument(self.document())

        self.setStyleSheet('''
        QTextEdit {
            background-color: #353535;
            color: #eeeeff;
            border-radius: 3px;
            border: 1px solid #4f5d66;
        }
        ''')

    def set_code(self, new_code):
        self.setText(new_code)

    def get_code(self):
        return self.toPlainText().replace('\t', '    ')