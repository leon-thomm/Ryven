import code
import re

from PySide2.QtWidgets import QWidget, QLineEdit, QGridLayout, QPlainTextEdit, QLabel, QPushButton
from PySide2.QtCore import Signal, QEvent, Qt
from PySide2.QtGui import QTextCharFormat, QBrush, QColor, QFont


class MainConsole(QWidget):
    """Complete console interpreter.
    One instance will be created at the end of this file, when being imported in Ryven.py."""

    def __init__(
            self,
            history: int = 100,     # max lines in history buffer
            blockcount: int = 5000  # max lines in output buffer
    ):

        super(MainConsole, self).__init__()

        # self.main_window = None  # set manually after initialization

        self.init_ui(history, blockcount)


    def init_ui(self, history, blockcount):
        self.content_layout = QGridLayout(self)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # reset scope button
        self.reset_scope_button = QPushButton('reset console scope')
        self.reset_scope_button.clicked.connect(self.reset_scope_clicked)
        self.content_layout.addWidget(self.reset_scope_button, 0, 0, 1, 2)
        self.reset_scope_button.hide()

        # display for output
        self.out_display = ConsoleDisplay(blockcount, self)
        self.content_layout.addWidget(self.out_display, 1, 0, 1, 2)

        # colors to differentiate input, output and stderr
        self.inpfmt = self.out_display.currentCharFormat()
        self.inpfmt.setForeground(QBrush(QColor('white')))
        self.outfmt = QTextCharFormat(self.inpfmt)
        self.outfmt.setForeground(QBrush(QColor('#A9D5EF')))
        self.errfmt = QTextCharFormat(self.inpfmt)
        self.errfmt.setForeground(QBrush(QColor('#B55730')))

        # display input prompt left besides input edit
        self.prompt_label = QLabel('> ', self)
        self.prompt_label.setFixedWidth(15)
        self.content_layout.addWidget(self.prompt_label, 2, 0)

        # command line
        self.inpedit = ConsoleInputLineEdit(max_history=history)
        self.inpedit.returned.connect(self.push)
        self.content_layout.addWidget(self.inpedit, 2, 1)


        self.interp = None
        self.reset_interpreter()

        self.buffer = []
        self.num_added_object_contexts = 0


    def setprompt(self, text: str):
        self.prompt_label.setText(text)

    def reset_scope_clicked(self):
        self.reset_interpreter()

    def add_obj_context(self, context_obj):
        """adds the new context to the current context by initializing a new interpreter with both"""

        old_context = {} if self.interp is None else self.interp.locals
        name = 'obj' + (str(self.num_added_object_contexts+1) if self.num_added_object_contexts > 0 else '')
        new_context = {name: context_obj}
        context = {**old_context, **new_context}  # merge dicts
        self.interp = code.InteractiveConsole(context)
        print('added as ' + name)

        self.num_added_object_contexts += 1
        self.reset_scope_button.show()

    def reset_interpreter(self):
        """Initializes a new plain interpreter"""

        # # --------------------------------------
        # # def generate_code():
        # #     return print('generating code...')
        # def script():
        #     return self.main_window.get_current_script()
        # # --------------------------------------

        context = {**locals()}
        self.num_added_object_contexts = 0
        self.reset_scope_button.hide()
        self.interp = code.InteractiveConsole(context)

    def push(self, commands: str) -> None:
        """execute entered command which may span multiple lines when code was pasted"""

        if commands == 'clear':
            self.out_display.clear()
        else:
            lines = commands.split('\n')  # usually just one entry

            # clean and print commands
            for line in lines:

                # remove '> '-and '. ' prefixes which may remain from copy&paste
                if re.match('^[\>\.] ', line):
                    line = line[2:]

                # print input
                self.writeoutput(self.prompt_label.text() + line, self.inpfmt)

                # prepare for multi-line input
                self.setprompt('. ')
                self.buffer.append(line)

            # merge commands
            source = '\n'.join(self.buffer)
            more = self.interp.runsource(source, '<console>')

            if not more:  # no more input required
                self.setprompt('> ')
                self.buffer = []  # reset buffer

    def write(self, line: str) -> None:
        """capture stdout and print to outdisplay"""
        if len(line) != 1 or ord(line[0]) != 10:
            self.writeoutput(line.rstrip(), self.outfmt)

    def errorwrite(self, line: str) -> None:
        """capture stderr and print to outdisplay"""
        self.writeoutput(line, self.errfmt)

    def writeoutput(self, line: str, fmt: QTextCharFormat = None) -> None:
        """prints to outdisplay"""
        if fmt is not None:
            self.out_display.setCurrentCharFormat(fmt)
        self.out_display.appendPlainText(line.rstrip())


class ConsoleInputLineEdit(QLineEdit):
    """Input line edit with a history buffer for recalling previous lines."""

    returned = Signal(str)

    def __init__(self, max_history: int = 100):
        super().__init__()

        self.setObjectName('ConsoleInputLineEdit')
        self.max_hist = max_history
        self.hist_index = 0
        self.hist_list = []
        self.prompt_pattern = re.compile('^[>\.]')
        self.setFont(QFont('Consolas', 12))

    def event(self, ev: QEvent) -> bool:
        """
        Tab: Insert 4 spaces
        Arrow Up/Down: select a line from the history buffer
        Newline: Emit returned signal
        """
        if ev.type() == QEvent.KeyPress:
            if ev.key() == Qt.Key_Tab:
                self.insert(' '*4)
                return True
            elif ev.key() == Qt.Key_Up:
                self.recall(self.hist_index - 1)
                return True
            elif ev.key() == Qt.Key_Down:
                self.recall(self.hist_index + 1)
                return True
            elif ev.key() == Qt.Key_Return:
                self.returnkey()
                return True

        return super().event(ev)

    def returnkey(self) -> None:
        text = self.text()
        self.record(text)
        self.returned.emit(text)
        self.setText('')

    def recall(self, index: int) -> None:
        """select a line from the history list"""

        if len(self.hist_list) > 0 and 0 <= index < len(self.hist_list):
            self.setText(self.hist_list[index])
            self.hist_index = index

    def record(self, line: str) -> None:
        """store line in history buffer and update hist_index"""

        while len(self.hist_list) >= self.max_hist - 1:
            self.hist_list.pop()
        self.hist_list.append(line)

        if self.hist_index == len(self.hist_list)-1 or line != self.hist_list[self.hist_index]:
            self.hist_index = len(self.hist_list)



class ConsoleDisplay(QPlainTextEdit):
    def __init__(self, max_block_count, parent=None):
        super(ConsoleDisplay, self).__init__(parent)

        self.setObjectName('ConsoleDisplay')
        self.setMaximumBlockCount(max_block_count)
        self.setReadOnly(True)
        self.setFont(QFont('Consolas', 12))


class RedirectOutput:
    """Just redirects 'write()'-calls to a specified method."""

    def __init__(self, func):
        self.func = func

    def write(self, line):
        self.func(line)





main_console = None


def init_main_console():
    global main_console
    main_console = MainConsole()

    console_stdout_redirect = RedirectOutput(main_console.write)
    console_errout_redirect = RedirectOutput(main_console.errorwrite)

    return console_stdout_redirect, console_errout_redirect
