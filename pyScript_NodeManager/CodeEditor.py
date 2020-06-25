from PySide2.QtWidgets import QTextEdit
from PySide2.QtGui import QFont, QFontMetrics, QTextCharFormat, QTextCursor, QColor
from PySide2.QtCore import Qt

import re


class CodeEditor(QTextEdit):
    def __init__(self):
        super(CodeEditor, self).__init__()

        self.static_elements = []
        self.components = []

        font = QFont('Consolas', 13)
        self.setFont(font)
        self.setTabStopWidth(QFontMetrics(font).width('    '))
        self.just_changed_text = False

        self.setStyleSheet('''
            background-color: #2b2b2b;
        ''')

        self.textChanged.connect(self.text_changed)

    def set_code(self, code):
        self.setPlainText(code)

    def text_changed(self):
        return

        if self.just_changed_text:
            self.just_changed_text = False
            return

        code: str = self.toPlainText()

        self.replace_patterns(code)


    def replace_patterns(self, code):

        # clear format
        fmt = QTextCharFormat()
        fmt.setBackground(QColor('#2b2b2b'))

        cursor = QTextCursor(self.document())
        cursor.setPosition(0, QTextCursor.MoveAnchor)
        cursor.setPosition(len(code)-1, QTextCursor.KeepAnchor)
        self.just_changed_text = True
        cursor.setCharFormat(fmt)

        # static elements
        color = QColor(255, 255, 0, 50)

        for pattern in self.static_elements:
            positions = [i for i in range(len(code)) if code.startswith(pattern, i)]
            for occ in reversed(positions):
                fmt.setBackground(color)
                cursor.setPosition(occ, QTextCursor.MoveAnchor)
                cursor.setPosition(occ+len(pattern), QTextCursor.KeepAnchor)
                self.just_changed_text = True
                cursor.setCharFormat(fmt)

        # usable components
        color = QColor(100, 100, 255, 200)

        for pattern in self.components:
            positions = [i for i in range(len(code)) if code.startswith(pattern, i)]
            for occ in reversed(positions):
                fmt.setBackground(color)
                cursor.setPosition(occ, QTextCursor.MoveAnchor)
                cursor.setPosition(occ+len(pattern), QTextCursor.KeepAnchor)
                self.just_changed_text = True
                cursor.setCharFormat(fmt)





class CodeEditor_Small(QTextEdit):
    def __init__(self):
        super(CodeEditor_Small, self).__init__()

        font = QFont('Consolas', 8)
        self.setFont(font)
        self.setTabStopWidth(QFontMetrics(font).width('    '))

        self.setStyleSheet('''
            background-color: #2b2b2b;
        ''')

    def get_code(self):
        return self.toPlainText()