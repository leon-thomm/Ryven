from PySide2.QtCore import QRegExp
from PySide2.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont, QColor


class CodeEditor_Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(CodeEditor_Highlighter, self).__init__(parent)

        keyword_format = QTextCharFormat()
        keyword_format.setFontWeight(QFont.Bold)
        keyword_format.setForeground(QColor(80, 80, 240))

        keyword_patterns = ["class", "def"]

        self.highlighting_rules = [(QRegExp(pattern), keyword_format) for pattern in keyword_patterns]

        # individual patterns
        if_format = QTextCharFormat()
        if_format.setForeground(QColor(255, 153, 51))
        self.highlighting_rules.append((QRegExp('if .+:'),
                                        if_format))

        elif_format = QTextCharFormat()
        elif_format.setForeground(QColor(255, 153, 51))
        self.highlighting_rules.append((QRegExp('elif .+:'),
                                        elif_format))

        else_format = QTextCharFormat()
        else_format.setForeground(QColor(255, 153, 51))
        self.highlighting_rules.append((QRegExp('else:'),
                                        else_format))


        else_format = QTextCharFormat()
        else_format.setFontItalic(True)
        else_format.setForeground(QColor(255, 179, 102))
        self.highlighting_rules.append((QRegExp('pass'),
                                        else_format))

        variable_assignment_format = QTextCharFormat()
        variable_assignment_format.setForeground(QColor(224, 108, 117))
        self.highlighting_rules.append((QRegExp('[a-zA-Z_]+( +)=( +)'),
                                        variable_assignment_format))

        parameter_format = QTextCharFormat()
        parameter_format.setForeground(QColor(229, 192, 123))
        self.highlighting_rules.append((QRegExp("[a-zA-Z_]+\(.*\)"),
                                        parameter_format))  # not working with standard values ('=') yet

        function_call_format = QTextCharFormat()
        function_call_format.setForeground(QColor(204, 204, 255))
        self.highlighting_rules.append((QRegExp('[A-Za-z0-9_]+(?=\\()'),
                                        function_call_format))

        self_format = QTextCharFormat()
        self_format.setForeground(QColor(204, 204, 255))
        self.highlighting_rules.append((QRegExp('self'),
                                        self_format))

        return_format = QTextCharFormat()
        return_format.setFontItalic(True)
        return_format.setForeground(QColor(204, 82, 0))
        self.highlighting_rules.append((QRegExp('return'),
                                        return_format))


        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setFontItalic(True)
        singleLineCommentFormat.setForeground(QColor(92, 99, 112))
        self.highlighting_rules.append((QRegExp('#[^\n]*'),
                                        singleLineCommentFormat))


    def highlightBlock(self, text):
        for pattern, _format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, _format)
                index = expression.indexIn(text, index + length)