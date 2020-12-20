from PySide2.QtCore import QObject, Signal


class Log(QObject):

    enabled = Signal()
    disabled = Signal()
    wrote = Signal(str)
    cleared = Signal()
    # redisplay = Signal()

    def __init__(self, title: str):
        super(Log, self).__init__()

        self.title: str = title
        self.lines: [str] = []
        self.enabled_: bool = True

        # self.main_layout = QVBoxLayout()
        # self.header_layout = QHBoxLayout()
        #
        # title_label = QLabel(title)
        # title_label.setFont(QFont('Poppins', 13))
        # self.header_layout.addWidget(title_label)
        #
        # self.remove_button = QPushButton('x')
        # self.remove_button.clicked.connect(self.remove_clicked)
        # self.header_layout.addWidget(self.remove_button)
        # self.remove_button.hide()
        #
        # holder_label = QLabel(shorten(str(sender), 76))
        # holder_label.setWordWrap(True)
        # self.log_view = QPlainTextEdit()
        # self.log_view.setReadOnly(True)
        #
        #
        # self.main_layout.addLayout(self.header_layout)
        # self.main_layout.addWidget(holder_label)
        # self.main_layout.addWidget(self.log_view)
        #
        # self.setLayout(self.main_layout)
        #
        # self.enabled_style_sheet = '''
        #     QLabel {
        #         border: None;
        #     }
        #     QWidget {
        #         color: #e9f4fb;
        #     }
        # '''
        # self.disabled_style_sheet = '''
        #     QLabel {
        #         border: None;
        #     }
        #     QWidget {
        #         color: #e9f4fb;
        #     }
        #     QPlainTextEdit {
        #         background: black;
        #         color: grey;
        #     }
        # '''
        # self.setStyleSheet(self.enabled_style_sheet)


    def write(self, *args):
        if not self.enabled_:
            return

        s = ''
        for arg in args:
            s += ' '+str(arg)
        self.lines.append(s)
        self.wrote.emit(s)
        # self.log_view.appendPlainText('>  '+s)

    def clear(self):
        self.cleared.emit()
        # self.log_view.clear()

    def disable(self):
        self.enabled_ = False
        self.disabled.emit()
        # self.remove_button.show()
        # self.setStyleSheet(self.disabled_style_sheet)

    def enable(self):
        self.enabled_ = True
        self.enabled.emit()
        # self.remove_button.hide()
        # self.setStyleSheet(self.enabled_style_sheet)
        # self.show()

    # def remove_clicked(self):
    #     self.hide()


# class ErrorLog(Log):
#     def __init__(self):
#         super(ErrorLog, self).__init__('Error Log')
#
#
# class GlobalLog(Log):
#     def __init__(self):
#         super(GlobalLog, self).__init__('Global Messages')
