from NWENV import *

from qtpy.QtGui import QFont, QFontMetrics, Qt
from qtpy.QtWidgets import QPushButton, QComboBox, QSlider, QTextEdit, QPlainTextEdit


class ButtonNode_MainWidget(QPushButton, MWB):

    def __init__(self, params):
        MWB.__init__(self, params)
        QPushButton.__init__(self)

        self.clicked.connect(self.update_node)


class ClockNode_MainWidget(QPushButton, MWB):

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

        f = QFont('Consolas', 9)
        self.setFont(f)
        self.setTabStopDistance(QFontMetrics(f).width(' ')*4)
    #
    #     self.lexer = get_lexer_by_name('python')
    #     self.formatter = get_formatter_by_name('html', noclasses=True, style=DraculaStyle)
    #     # self.formatter = get_formatter_by_name('html', noclasses=True, style=LightStyle)
    #
    #     self.textChanged.connect(self.text_changed)
    #
    # def text_changed(self):
    #
    #     self.setUpdatesEnabled(False)  # speed up, doesnt really seem to help though
    #
    #     cursor_pos = self.textCursor().position()
    #     scroll_pos = (self.horizontalScrollBar().sliderPosition(), self.verticalScrollBar().sliderPosition())
    #
    #     highlighted = """
    #     <style>
    #     * {
    #         font-family: Consolas;
    #     }
    #     </style>
    #             """ + highlight(self.toPlainText(), self.lexer, self.formatter)
    #
    #     self.setHtml(highlighted)
    #
    #     if self.hasFocus():
    #         c = QTextCursor(self.document())
    #         c.setPosition(cursor_pos)
    #         self.setTextCursor(c)
    #         self.horizontalScrollBar().setSliderPosition(scroll_pos[0])
    #         self.verticalScrollBar().setSliderPosition(scroll_pos[1])
    #     else:
    #         self.textCursor().setPosition(0)
    #
    #     self.setUpdatesEnabled(True)


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


export_widgets(
    ButtonNode_MainWidget,
    ClockNode_MainWidget,
    LogNode_MainWidget,
    SliderNode_MainWidget,
    CodeNode_MainWidget,
    EvalNode_MainWidget,
)
