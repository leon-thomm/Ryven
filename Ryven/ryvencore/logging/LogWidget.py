from PySide2.QtGui import QFont
from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QPlainTextEdit

from ryvencore.logging.Log import Log


class LogWidget(QWidget):
    def __init__(self, log: Log):
        # super(QWidget, self).__init__()
        super().__init__()

        self.log = log
        log.enabled.connect(self.enable)
        log.disabled.connect(self.disable)
        log.wrote.connect(self.write)
        log.cleared.connect(self.clear)


        self.main_layout = QVBoxLayout()
        self.header_layout = QHBoxLayout()

        title_label = QLabel(self.log.title)
        title_label.setFont(QFont('Poppins', 13))
        self.header_layout.addWidget(title_label)

        self.remove_button = QPushButton('x')
        self.remove_button.clicked.connect(self.remove_clicked)
        self.header_layout.addWidget(self.remove_button)
        self.remove_button.hide()

        self.text_edit = QPlainTextEdit()
        self.text_edit.setReadOnly(True)

        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addWidget(self.text_edit)

        self.setLayout(self.main_layout)

        self.enabled_style_sheet = '''
            QLabel {
                border: None;
            }
            QWidget {
                color: #e9f4fb;
            }
        '''
        self.disabled_style_sheet = '''
            QLabel {
                border: None;
            }
            QWidget {
                color: #e9f4fb;
            }
            QPlainTextEdit {
                background: black; 
                color: grey;
            }
        '''
        self.setStyleSheet(self.enabled_style_sheet)

    def write(self, msg: str):
        self.text_edit.appendPlainText(msg)

    def clear(self):
        self.text_edit.clear()

    def disable(self):
        self.remove_button.show()
        self.setStyleSheet(self.disabled_style_sheet)

    def enable(self):
        self.remove_button.hide()
        self.setStyleSheet(self.enabled_style_sheet)
        self.show()

    def remove_clicked(self):
        self.hide()
