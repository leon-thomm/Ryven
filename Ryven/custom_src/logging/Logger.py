from PySide2.QtCore import QObject, Signal
from PySide2.QtWidgets import QWidget, QHBoxLayout, QLayout

from custom_src.logging.Log import Log


class Logger(QObject):
    """Manages all logs that belong to the script"""

    new_log_created = Signal(Log)

    def __init__(self, script):
        super(Logger, self).__init__()

        # # UI
        # main_layout = QHBoxLayout()
        # main_layout.setSizeConstraint(QLayout.SetMinimumSize)

        self.script = script
        self.logs: [Log] = []
        # self.custom_log_holders = {}  # sender (NodeInstance) : Log
        # self.global_log: Log = None
        # main_layout.addWidget(self.global_log)
        # self.error_log: Log = None
        # main_layout.addWidget(self.error_log)
        #
        # self.setLayout(main_layout)
        #
        # self.setStyleSheet('''
        # QScrollArea {
        #     background-color: grey;
        # }
        # ''')

    def create_default_logs(self):
        self.logs.append(self.new_log(title='Global'))
        self.logs.append(self.new_log(title='Errors'))

    def log_message(self, msg: str, target: str = ''):
        for log in self.logs:
            if log.title == target:
                log.write(msg)
        # if target == 'global':
        #     self.global_log.write(message)
        # elif target == 'error':
        #     self.error_log.write(message)

    def new_log(self, title: str) -> Log:
        # new_log = Log(title)
        # self.custom_log_holders[new_sender] = new_log
        # self.layout().addWidget(new_log)

        log = Log(title=title)
        self.new_log_created.emit(log)
        return log
