from NIWENV import *

from PySide2.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QFileDialog
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...


class %CLASS%(QWidget, IWB):
    def __init__(self, params):
        super(%CLASS%, self).__init__()

        self.file_path = ''

        # UI
        self.setLayout(QVBoxLayout())
        self.path_line_edit = QLineEdit()
        self.path_line_edit.setPlaceholderText('file path...')
        self.path_line_edit.textChanged.connect(M(self.set_file_path))
        self.select_file_button = QPushButton('select')
        self.select_file_button.clicked.connect(M(self.select_file_button_clicked))
        self.layout().addWidget(self.path_line_edit)
        self.layout().addWidget(self.select_file_button)

        self.setStyleSheet('''
            QWidget {
                background: transparent;
            }
            QLineEdit {
                border-radius: 10px;
                background-color: transparent;
                border: 1px solid #202020;
                color: #aaaaaa;
                padding: 3px;
            }
            QPushButton {
                background-color: #36383B;
                padding-top: 5px;
                padding-bottom: 5px;
                padding-left: 22px;
                padding-right: 22px;
                border: 1px solid #666666;
                border-radius: 5px;
            }
        ''')
        self.setFixedWidth(150)


    def select_file_button_clicked(self):
        file_path = QFileDialog.getOpenFileName(self, 'Select File')[0]
        if len(file_path) > 0:
            self.set_file_path(file_path)

    def set_file_path(self, new_file_path):
        self.file_path = new_file_path
        self.path_line_edit.setText(self.file_path)

    def get_val(self):
        return self.file_path


    def get_data(self):
        # data = {'file path': self.file_path}
        return self.get_val()

    def set_data(self, data):
        # self.set_file_path(data['file path'])
        self.set_file_path(data)


    # remove logs and stop threads and timers here
    def remove_event(self):
        pass
