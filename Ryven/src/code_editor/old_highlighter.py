"""
D E P R E C A T E D !!
"""






from qtpy.QtCore import QRegExp
from qtpy.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont, QColor

import keyword
import re


class CodePreview_Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(CodePreview_Highlighter, self).__init__(parent)

        self.highlighting_rules = []

        """
        some nodes on the regex rules 
        
        - use [...] for literals, not (...)
        - neg. lookBEHIND: (?<!...)
        - neg. lookAHEAD: (?!...)
        - start: ^..., stop: ...$
        - re'(?![...])sth' won't work for 'sth'!
        
        """

        # KEYWORDS --------------------------------------------

        keyword_format = QTextCharFormat()
        # keyword_format.setFontWeight(QFont.Bold)
        keyword_format.setForeground(QColor(180, 180, 240))

        keyword_patterns = keyword.kwlist

        # for pattern in keyword_patterns:
        #     self.highlighting_rules += [
        #         {
        #             'pattern':                          # the pattern to find the expression in
        #                 f'(?<!\w){pattern}(?!\w)',
        #                 # f'(^{pattern}(?!{words}))|'     # in case the code block starts with the keyword
        #                 # f'((?!{words}){pattern}$)|'     # in case the code block ends with the keyword
        #                 # f'(^{pattern}$)',               # in case the code block starts and ends with the keyword
        #             'fmt expression': pattern,          # what is actually being styled
        #             'fmt': keyword_format               # the style
        #         },
        #     ]

        # for p in keyword_patterns:
        #     print(f'(?!{words}){p}(?!{words})')

        # -----------------------------------------------------

        variable_assignment_format = QTextCharFormat()
        variable_assignment_format.setForeground(QColor(224, 108, 117))
        self.highlighting_rules.append({
            'pattern': r"(.+)( +)=( +)(.+)",
            'fmt expression': r"(.+)( +)=( +)(.+)",
            'fmt': variable_assignment_format
        })

        # parameter_format = QTextCharFormat()
        # parameter_format.setForeground(QColor(229, 192, 123))
        # self.highlighting_rules.append({
        #     'pattern': '[a-z_]+[a-zA-Z0-9_]*\(.*\)',
        #     'fmt expression': '[a-z_]+[a-zA-Z0-9_]*\(.*\)',
        #     'fmt': parameter_format
        # })
        #
        function_call_format = QTextCharFormat()
        function_call_format.setForeground(QColor(204, 204, 255))
        self.highlighting_rules.append({
            'pattern': r"[A-Za-z0-9_]+(?=\()",
            'fmt expression': r"[A-Za-z0-9_]+(?=\()",
            'fmt': function_call_format
        })

        # attribute_format = QTextCharFormat()
        # attribute_format.setForeground(QColor(229, 192, 123))
        # self.highlighting_rules.append({
        #     'pattern': r"[a-z_]+[a-zA-Z0-9_]*\(.*\)",
        #     'fmt expression': r"[a-z_]+[a-zA-Z0-9_]*\(.*\)",
        #     'fmt': attribute_format
        # })
        #
        # string_format = QTextCharFormat()
        # string_format.setFontItalic(False)
        # string_format.setForeground(QColor(235, 195, 52))
        # self.highlighting_rules.append({
        #     'pattern': r"('([a-zA-Z0-9_\-\[\]\(\){} ]*)\')|(\"(?!\"*)\")",
        #     'fmt expression': r"('([a-zA-Z0-9_\-\[\]\(\){} ]*)\')|(\"(?!\"*)\")",
        #     'fmt': string_format
        # })

        self_format = QTextCharFormat()
        self_format.setForeground(QColor(204, 204, 255))
        self.highlighting_rules.append({
            'pattern': r"(?<!\w)self(.|(?!\w))",
            'fmt expression': r"(?<!\w)self(.|(?!\w))",
            'fmt': self_format
        })

        comment_format = QTextCharFormat()
        comment_format.setFontItalic(True)
        comment_format.setForeground(QColor(92, 99, 112))
        self.highlighting_rules.append({
            'pattern': r"#[^\n]*",
            'fmt expression': r"#[^\n]*",
            'fmt': comment_format
        })

    def highlightBlock(self, text):

        for d in self.highlighting_rules:
            pattern, expression, _format = d['pattern'], d['fmt expression'], d['fmt']

            p_index = 0

            while p_index < len(text):

                # find new expr index
                pattern_match = re.search(pattern, text[p_index:])
                if pattern_match:

                    p_index += pattern_match.start()
                    expr_match = re.search(expression, text[p_index:])

                    if expr_match:
                        length = expr_match.end()-expr_match.start()

                        if p_index+expr_match.start() < pattern_match.end():
                            self.setFormat(p_index+expr_match.start(), length, _format)

                        p_index = p_index + length

                        continue

                p_index += len(expression)
