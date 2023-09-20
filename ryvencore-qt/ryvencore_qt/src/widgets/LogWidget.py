from qtpy.QtGui import QFont
from qtpy.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QPlainTextEdit

from ryvencore.addons.Logging import Logger
import logging


class LogWidget(QWidget):
    """Convenience class for a QWidget representing a log."""

    def __init__(self, logger: Logger):
        super().__init__()

        self.logger = logger
        self.logger.addHandler(logging.StreamHandler(self))
        self.logger.sig_disabled.sub(self.disable)
        self.logger.sig_enabled.sub(self.enable)

        self.main_layout = QVBoxLayout()
        self.header_layout = QHBoxLayout()

        title_label = QLabel(self.logger.name)
        title_label.setFont(QFont('Poppins', 12))
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

    def write(self, msg: str):
        self.text_edit.appendPlainText(msg)

    def flush(self):
        pass

    # def clear(self):
    #     self.text_edit.clear()

    def disable(self):
        self.remove_button.show()

    def enable(self):
        self.remove_button.hide()
        self.show()

    def remove_clicked(self):
        self.hide()
