from qtpy.QtWidgets import QTextEdit, QShortcut
from qtpy.QtGui import QFont, QFontMetrics, QTextCursor, QKeySequence
from qtpy.QtCore import Qt

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
# from resources.pygments.dracula import DraculaStyle
from ryven.gui.code_editor.pygments.dracula import DraculaStyle
from ryven.gui.code_editor.pygments.light import LightStyle


class CodeEditorWidget(QTextEdit):
    def __init__(self, theme, highlight=True, enabled=False):
        super(CodeEditorWidget, self).__init__()

        self.highlighting = highlight
        self.editing = enabled

        f = QFont('Consolas', 12)
        self.setFont(f)
        self.update_tab_stop_width()

        # also not working:
        # copy_shortcut = QShortcut(QKeySequence.Copy, self)
        # copy_shortcut.activated.connect(self.copy)
        # https://forum.qt.io/topic/121474/qshortcuts-catch-external-shortcuts-from-readonly-textedit/4

        self.textChanged.connect(self.text_changed)
        self.block_change_signal = False

        self.lexer = get_lexer_by_name('python')

        if theme.name == 'dark':
            self.formatter = get_formatter_by_name('html', noclasses=True, style=DraculaStyle)
        else:
            self.formatter = get_formatter_by_name('html', noclasses=True, style=LightStyle)

        if self.editing:
            self.enable_editing()
        else:
            self.disable_editing()

    def enable_editing(self):
        self.editing = True
        self.setReadOnly(False)
        self.update_appearance()

    def disable_editing(self):
        self.editing = False
        self.setReadOnly(True)
        self.update_appearance()

    def disable_highlighting(self):
        self.highlighting = False
        # self.update_appearance()

    def enable_highlighting(self):
        self.highlighting = True
        # self.update_appearance()

    def highlight(self):
        self.enable_highlighting()
        self.update_appearance()

    def mousePressEvent(self, e) -> None:
        if not self.highlighting and not self.editing:
            self.highlight()
        else:
            return super().mousePressEvent(e)

    def wheelEvent(self, e) -> None:
        super().wheelEvent(e)
        if e.modifiers() == Qt.CTRL:  # for some reason this also catches touch pad zooming
            self.update_tab_stop_width()
            # and for some reason QTextEdit doesn't seem to zoom using zoomIn()/zoomOut(), but by changing the font size
            # so I need to update the (pixel measured) tab stop width

    def set_code(self, new_code):
        # self.highlighting = self.editing
        self.setText(new_code.replace('    ', '\t'))
        self.update_appearance()

    def get_code(self):
        return self.toPlainText().replace('\t', '    ')

    def text_changed(self):
        if not self.block_change_signal:
            self.update_appearance()

    def update_tab_stop_width(self):
        self.setTabStopWidth(QFontMetrics(self.font()).width('_')*4)

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
