from NIWENV import *

from PySide2.QtWidgets import QPlainTextEdit
from PySide2.QtCore import Qt
# from PySide2.QtGui import ...




class %CLASS%(QPlainTextEdit, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QPlainTextEdit.__init__(self)

        

        self.setStyleSheet(self.parent_node_instance.session_stylesheet())

        self.setFixedSize(250, 30)
        self.setPlainText('obj.')
        
        self.last_text = self.toPlainText()



    def focusOutEvent(self, event):
        txt = self.toPlainText()
        if txt != self.last_text:
            self.editing_finished(txt)
            self.last_text = txt
        QPlainTextEdit.focusOutEvent(self, event)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.editing_finished(self.toPlainText())
            self.last_text = self.toPlainText()
        else:
            QPlainTextEdit.keyPressEvent(self, event)
    
    def editing_finished(self, text):
        self.parent_node_instance.text = text
        self.parent_node_instance.update()

    def get_text(self):
        return self.toPlainText()


    def get_data(self):
        data = {'text': self.toPlainText()}
        return data

    def set_data(self, data):
        self.setPlainText(data['text'])

    def remove_event(self):
        pass
