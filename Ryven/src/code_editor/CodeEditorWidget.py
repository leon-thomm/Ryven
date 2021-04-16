from PySide2.QtWidgets import QTextEdit, QShortcut
from PySide2.QtGui import QFont, QFontMetrics, QTextCursor, Qt, QKeySequence

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
# from resources.pygments.dracula import DraculaStyle
from .pygments.dracula import DraculaStyle
from .pygments.light import LightStyle


class CodeEditorWidget(QTextEdit):
    def __init__(self, theme):
        super(CodeEditorWidget, self).__init__()

        self.editing = False
        self.highlighting = self.editing

        f = QFont('Consolas')
        self.setFont(f)
        self.update_tab_stop_width()

        # also not working:
        # copy_shortcut = QShortcut(QKeySequence.Copy, self)
        # copy_shortcut.activated.connect(self.copy)
        # https://forum.qt.io/topic/121474/qshortcuts-catch-external-shortcuts-from-readonly-textedit/4

        self.textChanged.connect(self.text_changed)
        self.block_change_signal = False

        self.lexer = get_lexer_by_name('python')

        if theme == 'dark':
            self.formatter = get_formatter_by_name('html', noclasses=True, style=DraculaStyle)
        else:
            self.formatter = get_formatter_by_name('html', noclasses=True, style=LightStyle)

    def update_tab_stop_width(self):
        self.setTabStopWidth(QFontMetrics(self.font()).width('_')*4)

    def wheelEvent(self, e) -> None:
        super().wheelEvent(e)
        if e.modifiers() == Qt.CTRL:  # for some reason this also catches touch pad zooming
            self.update_tab_stop_width()
            # and for some reason QTextEdit doesn't seem to zoom using zoomIn()/zoomOut(), but by changing the font size
            # so I need to update the (pixel measured) tab stop width

    def text_changed(self):
        if not self.block_change_signal:
            self.update_appearance()

    def set_code(self, new_code):
        self.highlighting = self.editing
        self.setText(new_code.replace('    ', '\t'))
        self.update_appearance()

    def get_code(self):
        return self.toPlainText().replace('\t', '    ')

    def highlight_now(self):
        self.highlighting = True
        self.update_appearance()

    def update_appearance(self):
        if not self.editing and not self.highlighting:
            return

        self.setUpdatesEnabled(False)  # speed up, doesnt really seem to help though

        cursor_pos = self.textCursor().position()
        scroll_pos = (self.horizontalScrollBar().sliderPosition(), self.verticalScrollBar().sliderPosition())

        self.block_change_signal = True

        highlighted = """
<style>
* {
    font-family: Consolas;
}
</style>
        """ + highlight(self.toPlainText(), self.lexer, self.formatter)

        self.setHtml(highlighted)

        self.block_change_signal = False

        if self.hasFocus():
            c = QTextCursor(self.document())
            c.setPosition(cursor_pos)
            self.setTextCursor(c)
            self.horizontalScrollBar().setSliderPosition(scroll_pos[0])
            self.verticalScrollBar().setSliderPosition(scroll_pos[1])
        else:
            self.textCursor().setPosition(0)

        self.setUpdatesEnabled(True)

    def enable_editing(self):
        self.editing = True
        self.setReadOnly(False)
        self.update_appearance()

    def disable_editing(self):
        self.editing = False
        self.setReadOnly(True)
        self.update_appearance()
