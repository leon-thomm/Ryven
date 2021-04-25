from NWENV import *

from qtpy.QtWidgets import QTextEdit
# from qtpy.QtCore import ...
from qtpy.QtGui import QFontMetrics, QFont

import numpy as np


class MatrixWidget(QTextEdit, MWB):
    def __init__(self, params, base_width=50, base_height=50):
        MWB.__init__(self, params)
        QTextEdit.__init__(self)



        c = self.parent_node_instance.color.name()
        self.setStyleSheet('''
QTextEdit{
    color: '''+c+''';
    background: transparent;
    border: 1px solid '''+c+''';
    border-radius: 4px;
}
        ''')
        self.setFont(QFont('source code pro', 10))
        self.base_width = base_width
        self.base_height = base_height
        self.setFixedSize(self.base_width, self.base_height)
        self.setReadOnly(True)
        self.hidden_size = None

    #     self.textChanged.connect(M(self.text_changed))
    #
    #
    # def text_changed(self, new_text):
    #     fm = QFontMetrics(self.font())
    #     text_width = fm.width(new_text)
    #     new_width = text_width+15
    #     self.setFixedWidth(new_width if new_width > self.base_width else self.base_width)
    #
    #     self.parent_node_instance.update_shape()
    #     self.parent_node_instance.rebuild_ui()  # see rebuild_ui() for explanation

    def update_matrix(self, m):
        if m is None:
            self.setText('')
            return

        longest_exp_length = -1
        lines = []

        try:
            matrix = np.around(m, 4)
        except Exception:
            matrix = m
            # non computable matrix (expression matrix)

            # if matrix.ndim == 1:
            #     longest_exp_length = self.get_row_lxl(matrix)
            #     lines.append(self.format_row_to_str(matrix, longest_exp_length))
            # elif matrix.ndim == 2:
            #     for row in matrix:
            #         nlxl = self.get_row_lxl(row)
            #         if nlxl > longest_exp_length:
            #             longest_exp_length = nlxl
            #     for row in matrix:
            #         lines.append(self.format_row_to_str(row, longest_exp_length))
            #
            # self.setText('\n'.join(lines))
            # return
            pass

        if matrix.ndim == 0:    # can happen with scalars
            lines = [str(m)]

        elif matrix.ndim == 1:
            longest_exp_length = self.get_row_lxl(matrix)
            row = matrix
            lines.append(self.format_row_to_str(row, longest_exp_length))

        elif matrix.ndim == 2:
            for row in matrix:
                nlxl = self.get_row_lxl(row)
                if nlxl > longest_exp_length:
                    longest_exp_length = nlxl

            for row in matrix:
                lines.append(self.format_row_to_str(row, longest_exp_length))


        s = '\n'.join(lines)
        self.setText(s)
        self.resize_to_content(lines)

    def get_row_lxl(self, row):
        longest_exp_length = -1
        for exp in row:
            if type(exp) == str:
                if len(exp) > longest_exp_length:
                    longest_exp_length = len(exp)
            else:
                if len(str(exp)) > longest_exp_length:  # round(number, 4)
                    longest_exp_length = len(str(exp))
        return longest_exp_length

    def format_row_to_str(self, row, lxl):
        format_str = len(row) * ('{:>'+str(lxl)+'} ')
        format_str = format_str[:-1]
        return format_str.format(*row)

    def resize_to_content(self, lines):
        if len(lines) == 0:
            lines.append('')

        # resize properly
        fm = QFontMetrics(self.font())
        text_width = fm.width(lines[0]+'__')
        text_width = text_width+20  # some buffer
        text_height = fm.height()*(len(lines))+12  # also some vertical buffer
        self.setFixedWidth(text_width if text_width > self.base_width else self.base_width)
        self.setFixedHeight(text_height if text_height > self.base_height else self.base_height)
        self.parent_node_instance.update_shape()

        # if self.hidden_size is None:
        #     # resize properly
        #     fm = QFontMetrics(self.font())
        #     text_width = fm.width(lines[0]+'__')
        #     text_width = text_width+20  # some buffer
        #     text_height = fm.height()*(len(lines))+12  # also some vertical buffer
        #     self.setFixedWidth(text_width if text_width > self.base_width else self.base_width)
        #     self.setFixedHeight(text_height if text_height > self.base_height else self.base_height)
        #     self.parent_node_instance.update_shape()

    def hide(self):
        self.hidden_size = self.size()
        self.setFixedSize(0, 0)
        self.parent_node_instance.update_shape()

    def show(self):
        self.setFixedSize(self.hidden_size)
        self.parent_node_instance.update_shape()
        self.hidden_size = None


    def get_state(self):
        data = {'text': self.toPlainText(),
                'shown': self.hidden_size is None
                }
        return data

    def set_state(self, data):
        self.setText(data['text'])
        self.resize_to_content(data['text'].splitlines())
        if not data['shown']:
            self.hide()

    def remove_event(self):
        pass
