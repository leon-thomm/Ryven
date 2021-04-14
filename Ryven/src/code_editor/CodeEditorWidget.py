from PySide2.QtWidgets import QTextEdit
from PySide2.QtGui import QFont, QFontMetrics, QTextCursor, Qt

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
from resources.pygments.dracula import DraculaStyle


class CodeEditorWidget(QTextEdit):
    def __init__(self):
        super(CodeEditorWidget, self).__init__()

        self.highlighting = True
        self.editing = False

        self.setTabStopWidth(QFontMetrics(self.font()).width(' ')*4)

        self.textChanged.connect(self.text_changed)
        self.block_change_signal = False

        self.lexer = get_lexer_by_name('python')

        self.formatter = get_formatter_by_name('html', noclasses=True, style=DraculaStyle)

    def text_changed(self):
        if not self.block_change_signal:
            self.update_appearance()

    def set_code(self, new_code):
        self.setText(new_code.replace('    ', '\t'))
        self.update_appearance()

    def get_code(self):
        return self.toPlainText().replace('\t', '    ')

    def update_appearance(self):
        if not self.editing:
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
