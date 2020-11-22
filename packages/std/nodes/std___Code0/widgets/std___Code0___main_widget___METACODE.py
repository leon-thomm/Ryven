from NIWENV import *

from PySide2.QtWidgets import QWidget, QVBoxLayout, QPlainTextEdit
# from PySide2.QtCore import
from PySide2.QtGui import QFont




class %CLASS%(QWidget, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QWidget.__init__(self)

        

        self.code_text_edits = []

        # UI
        self.code_font = QFont('Courier New', 12)
        self.setLayout(QVBoxLayout())

        # self.setStyleSheet('''
        #     QWidget {
        #         background: transparent;
        #     }
        #     QTextPlainEdit {
        #         background-color: black;
        #         color: grey;
        #     }
        # ''')

        self.setStyleSheet('background: transparent;')

        self.add_new_script()


    def add_new_script(self):
        code_text_edit = QPlainTextEdit()
        code_text_edit.setPlainText('test code')
        code_text_edit.setFont(self.code_font)
        # code_text_edit.setStyleSheet('background: black; color: grey;')
        self.code_text_edits.append(code_text_edit)
        # print('before: ', self.height())
        self.layout().addWidget(code_text_edit)
        # print('after: ', self.height())
        self.parent_node_instance.update_shape()

    def delete_script(self):
        code_text_edit = self.code_text_edits[-1]
        self.layout().removeWidget(code_text_edit)
        code_text_edit.setParent(None)
        self.parent_node_instance.update_shape()

    def get_code(self, index):
        return self.code_text_edits[index].toPlainText()

    def set_code(self, index, code):
        self.code_text_edits[index].setPlainText(code)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass


    def remove_event(self):
        pass
