from NWENV import *

from qtpy.QtWidgets import QLineEdit
# from qtpy.QtCore import ...
from qtpy.QtGui import QFont, QFontMetrics


class %CLASS%(QLineEdit, IWB):
    def __init__(self, params):
        IWB.__init__(self, params)
        QLineEdit.__init__(self)
        
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
        self.setFixedWidth(self.base_width)
        self.textChanged.connect(self.text_changed)
        self.setFont(QFont('source code pro'))


    def focusOutEvent(self, e):
        self.parent_node_instance.update()
        QTextEdit.focusOutEvent(self, e)

    def text_changed(self):
        t = self.toPlainText()
        fm = QFontMetrics(self.font())
        text_width = fm.width(t)
        text_width = text_width+25
        self.setFixedWidth(text_width if text_width > self.base_width else self.base_width)

        self.parent_node_instance.update_shape()

    def get_val(self):
        return self.text()


    def get_state(self):
        return self.get_val()

    def set_state(self, data):
        self.setText(data)

    def remove_event(self):
        pass # ...
