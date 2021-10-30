import re

from ryven.NWENV import *

from qtpy.QtGui import QFont
from qtpy.QtCore import Qt, Signal, QEvent
from qtpy.QtWidgets import QPushButton, QComboBox, QSlider, QTextEdit, QPlainTextEdit, QWidget, QVBoxLayout, QLineEdit


class ButtonNode_MainWidget(QPushButton, MWB):

    def __init__(self, params):
        MWB.__init__(self, params)
        QPushButton.__init__(self)

        self.clicked.connect(self.update_node)


class ClockNode_MainWidget(MWB, QPushButton):

    def __init__(self, params):
        MWB.__init__(self, params)
        QPushButton.__init__(self)

        self.clicked.connect(self.node.toggle)


class LogNode_MainWidget(MWB, QComboBox):
    def __init__(self, params):
        MWB.__init__(self, params)
        QComboBox.__init__(self)

        self.addItems(self.node.targets)

        self.currentTextChanged.connect(self.text_changed)
        self.set_target(self.node.target)

    def text_changed(self, t):
        self.node.target = t

    def set_target(self, t):
        self.setCurrentText(t)


class SliderNode_MainWidget(MWB, QSlider):
    def __init__(self, params):
        MWB.__init__(self, params)
        QSlider.__init__(self, Qt.Horizontal)

        self.setRange(0, 1000)
        self.valueChanged.connect(self.value_changed)

    def value_changed(self, v):
        self.node.val = v/1000
        self.update_node()

    def get_state(self) -> dict:
        return {
            'val': self.value(),
        }

    def set_state(self, data: dict):
        self.setValue(data['val'])


class CodeNode_MainWidget(MWB, QTextEdit):
    def __init__(self, params):
        MWB.__init__(self, params)
        QTextEdit.__init__(self)

        self.setFont(QFont('Consolas', 9))
        self.textChanged.connect(self.text_changed)
        self.setFixedHeight(150)
        self.setFixedWidth(300)

    def text_changed(self):
        self.node.code = self.toPlainText()
        self.update_node()

    def get_state(self) -> dict:
        return {
            'text': self.toPlainText(),
        }

    def set_state(self, data: dict):
        self.setPlainText(data['text'])


class EvalNode_MainWidget(MWB, QPlainTextEdit):
    def __init__(self, params):
        MWB.__init__(self, params)
        QPlainTextEdit.__init__(self)

        self.setFont(QFont('Consolas', 9))
        self.textChanged.connect(self.text_changed)
        self.setMaximumHeight(50)
        self.setMaximumWidth(200)

    def text_changed(self):
        self.node.expression_code = self.toPlainText()
        self.update_node()

    def get_state(self) -> dict:
        return {
            'text': self.toPlainText(),
        }

    def set_state(self, data: dict):
        self.setPlainText(data['text'])


class InterpreterConsole(MWB, QWidget):
    def __init__(self, params):
        MWB.__init__(self, params)
        QWidget.__init__(self)

        self.inp_line_edit = ConsoleInpLineEdit()
        self.output_text_edit = ConsoleOutDisplay()

        self.inp_line_edit.returned.connect(self.node.process_input)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.output_text_edit)
        self.layout().addWidget(self.inp_line_edit)

        self.last_hist_len = 0

    def interp_updated(self):

        if self.last_hist_len < len(self.node.hist):
            self.output_text_edit.appendPlainText('\n'.join(self.node.hist[self.last_hist_len:]))
        else:
            self.output_text_edit.clear()
            self.output_text_edit.setPlainText('\n'.join(self.node.hist))

        self.last_hist_len = len(self.node.hist)


class ConsoleInpLineEdit(QLineEdit):

    returned = Signal(str)

    def __init__(self):
        super().__init__()

        self.hist_index = 0
        self.hist = []

    def event(self, ev: QEvent) -> bool:

        if ev.type() == QEvent.KeyPress:

            if ev.key() == Qt.Key_Tab:
                self.insert(' '*4)
                return True

            elif ev.key() == Qt.Key_Backtab:
                ccp = self.cursorPosition()
                text_left = self.text()[:ccp]
                text_right = self.text()[ccp:]
                ends_with_tab = re.match(r"(.*)\s\s\s\s$", text_left)
                if ends_with_tab:
                    self.setText(text_left[:-4]+text_right)
                    self.setCursorPosition(ccp-4)
                    return True

            elif ev.key() == Qt.Key_Up:
                self.recall(self.hist_index - 1)
                return True

            elif ev.key() == Qt.Key_Down:
                self.recall(self.hist_index + 1)
                return True

            elif ev.key() == Qt.Key_Return:
                self.return_key()
                return True

        return super().event(ev)

    def return_key(self) -> None:
        text = self.text()
        for line in text.splitlines():
            self.record(line)
        self.returned.emit(text)
        self.clear()

    def record(self, line: str) -> None:
        """store line in history buffer and update hist_index"""

        self.hist.append(line)

        if self.hist_index == len(self.hist)-1 or line != self.hist[self.hist_index]:
            self.hist_index = len(self.hist)

    def recall(self, index: int) -> None:
        """select a line from the history list"""

        if len(self.hist) > 0 and 0 <= index < len(self.hist):
            self.setText(self.hist[index])
            self.hist_index = index


class ConsoleOutDisplay(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        self.setReadOnly(True)
        self.setFont(QFont('Source Code Pro', 9))


export_widgets(
    ButtonNode_MainWidget,
    ClockNode_MainWidget,
    LogNode_MainWidget,
    SliderNode_MainWidget,
    CodeNode_MainWidget,
    EvalNode_MainWidget,
    InterpreterConsole,
)
