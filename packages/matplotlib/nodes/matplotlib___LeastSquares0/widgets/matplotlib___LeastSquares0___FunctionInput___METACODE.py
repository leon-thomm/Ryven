from NIWENV import *

from PySide2.QtWidgets import QLineEdit
# from PySide2.QtCore import ...
from PySide2.QtGui import QFont, QFontMetrics


class %CLASS%(QLineEdit, IWB):
    def __init__(self, params):
        IWB.__init__(self, params)
        QLineEdit.__init__(self)
        
        c = self.parent_node_instance.color.name()
        self.setStyleSheet('''
QLineEdit{
    color: '''+c+''';
    background: transparent;
    border: 1px solid '''+c+''';
    border-radius: 4px;
}
        ''')
        self.base_width = 50
        self.setFixedWidth(self.base_width)
        self.textChanged.connect(M(self.text_changed))
        self.setFont(QFont('source code pro'))


    def focusOutEvent(self, e):
        self.parent_node_instance.update()
        QLineEdit.focusOutEvent(self, e)

    def text_changed(self, t):
        fm = QFontMetrics(self.font())
        text_width = fm.width(t)
        text_width = text_width+25
        self.setFixedWidth(text_width if text_width > self.base_width else self.base_width)

        self.parent_node_instance.update_shape()

    def get_val(self):
        return self.text()


    def get_data(self):
        return self.get_val()

    def set_data(self, data):
        self.setText(data)

    def remove_event(self):
        pass # ...
