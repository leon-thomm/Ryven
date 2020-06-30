from PySide2.QtWidgets import QTextEdit
from PySide2.QtGui import QFont, QFontMetrics

from custom_src.source_code_preview.CodePreview_Highlighter import CodePreview_Highlighter


class CodePreview_TextEdit(QTextEdit):
    def __init__(self):
        super(CodePreview_TextEdit, self).__init__()

        self.highlighting = True
        self.editing = False

        self.setFont(QFont('source code pro', 10))
        self.setReadOnly(True)
        self.setTabStopWidth(QFontMetrics(self.font()).width(' ')*4)

        self.highlighter = CodePreview_Highlighter()

    def set_code(self, new_code):
        self.setText(new_code.replace('    ', '\t'))
        self.update_appearance()

    def get_code(self):
        return self.toPlainText().replace('\t', '    ')

    def enable_highlighting(self):
        self.highlighting = True
        self.update_appearance()

    def disable_highlighting(self):
        self.highlighting = False
        self.update_appearance()

    def update_appearance(self):
        if self.highlighting:
            if self.editing:
                self.highlighter.setDocument(self.document())
                self.setStyleSheet('''
                QTextEdit {
                    background-color: #353535;
                    color: #eeeeff;
                    border-radius: 3px;
                    border: 1px solid #4f5d66;
                }
                ''')
            else:
                self.highlighter.setDocument(self.document())
                self.setStyleSheet('''
                QTextEdit {
                    background-color: #323232;
                    color: #eeeeff;
                    border-radius: 3px;
                }
                ''')
        else:
            self.highlighter.setDocument(None)
            self.setStyleSheet('''
            QTextEdit {
                background-color: #202020;
                color: #eeeeff;
                border-radius: 3px;
            }
            ''')

    def enable_editing(self):
        self.editing = True
        self.setReadOnly(False)
        self.update_appearance()

    def disable_editing(self):
        self.editing = False
        self.setReadOnly(True)
        self.update_appearance()