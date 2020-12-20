from PySide2.QtCore import QObject, Signal

from ryvencore.logging.Log import Log


class Logger(QObject):
    """Manages all logs that belong to the script"""

    new_log_created = Signal(Log)

    def __init__(self, script):
        super(Logger, self).__init__()

        self.script = script
        self.logs: [Log] = []

        self.create_default_logs()

    def create_default_logs(self):
        self.new_log(title='Global')
        self.new_log(title='Errors')

    def log_message(self, msg: str, target: str = ''):
        for log in self.logs:
            if log.title == target:
                log.write(msg)

    def new_log(self, title: str) -> Log:

        log = Log(title=title)
        self.logs.append(log)
        self.new_log_created.emit(log)
        return log
