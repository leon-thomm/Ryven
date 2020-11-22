from NIWENV import *

from PySide2.QtWidgets import QTextEdit
# from PySide2.QtCore import ...
from PySide2.QtGui import QFont, QFontMetrics


class %CLASS%(QTextEdit, IWB):
    def __init__(self, params):
        IWB.__init__(self, params)
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
        self.base_width = 200
        self.base_height = 30
        self.setFixedSize(self.base_width, self.base_height)
        self.textChanged.connect(M(self.text_changed))
        self.setFont(QFont('source code pro'))


    def focusOutEvent(self, e):
        self.parent_node_instance.update()
        QTextEdit.focusOutEvent(self, e)

    def text_changed(self):
        t = self.toPlainText()
        fm = QFontMetrics(self.font())
        text_width = fm.width(self.get_longest_line(t))
        text_width = text_width+25
        text_height = fm.height()*(t.count('\n')+1)+12
        self.setFixedWidth(text_width if text_width > self.base_width else self.base_width)
        self.setFixedHeight(text_height if text_height > self.base_height else self.base_height)

        self.parent_node_instance.update_shape()

    def get_longest_line(self, s: str):
        lines = s.split('\n')
        lines = [line.replace('\n', '') for line in lines]
        longest_line_found = ''
        for line in lines:
            if len(line) > len(longest_line_found):
                longest_line_found = line
        return line

    def get_val(self):
        return self.toPlainText()


    def get_data(self):
        return self.get_val()

    def set_data(self, data):
        self.setText(data)

    def remove_event(self):
        pass # ...
