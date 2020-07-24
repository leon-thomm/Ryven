from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QPlainTextEdit, QLabel, QLayout
from PySide2.QtGui import QFont

from custom_src.global_tools.strings import shorten


class Logger(QWidget):

    def __init__(self, script):
        super(Logger, self).__init__()

        # UI
        main_layout = QHBoxLayout()
        main_layout.setSizeConstraint(QLayout.SetMinimumSize)

        self.script = script
        self.custom_log_holders = {}  # sender (NodeInstance) : Log
        self.global_log = GlobalLog(self.script)
        main_layout.addWidget(self.global_log)
        self.error_log = ErrorLog(self.script)
        main_layout.addWidget(self.error_log)

        self.setLayout(main_layout)

        self.setStyleSheet('''
        QScrollArea {
            background-color: grey;
        }
        ''')


    def log_message(self, message: str, target=''):
        if target == 'global':
            self.global_log.log(message)
        elif target == 'error':
            self.error_log.log(message)

    def new_log(self, new_sender, title):
        new_log = Log(new_sender, title)
        self.custom_log_holders[new_sender] = new_log
        self.layout().addWidget(new_log)
        return new_log


class Log(QWidget):
    def __init__(self, sender, title=''):
        super(Log, self).__init__()


        self.main_layout = QVBoxLayout()
        self.header_layout = QHBoxLayout()

        title_label = QLabel(title)
        title_label.setFont(QFont('Poppins', 13))
        self.header_layout.addWidget(title_label)

        self.remove_button = QPushButton('x')
        self.remove_button.clicked.connect(self.remove_clicked)
        self.header_layout.addWidget(self.remove_button)
        self.remove_button.hide()

        holder_label = QLabel(shorten(str(sender), 76))
        holder_label.setWordWrap(True)
        self.log_view = QPlainTextEdit()
        self.log_view.setReadOnly(True)


        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addWidget(holder_label)
        self.main_layout.addWidget(self.log_view)

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


    def log(self, *args):
        s = ''
        for arg in args:
            s += ' '+str(arg)
        self.log_view.appendPlainText('>  '+s)

    def clear(self):
        self.log_view.clear()

    def disable(self):
        self.remove_button.show()
        self.setStyleSheet(self.disabled_style_sheet)

    def enable(self):
        self.remove_button.hide()
        self.setStyleSheet(self.enabled_style_sheet)
        self.show()

    def remove_clicked(self):
        self.hide()


class ErrorLog(Log):
    def __init__(self, sender):
        super(ErrorLog, self).__init__(sender, 'Error Log')



class GlobalLog(Log):
    def __init__(self, sender):
        super(GlobalLog, self).__init__(sender, 'Global Messages')
