from qtpy.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QShortcut, QPushButton
from qtpy.QtGui import QKeySequence, QGuiApplication
import sys


class CatchingWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        copy_shortcut = QShortcut(QKeySequence.Copy, self)
        copy_shortcut.activated.connect(self.copy)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(QPushButton())

    def copy(self):
        print('copy in widget!')
        QGuiApplication.clipboard().setText(self.hasFocus())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        l = QVBoxLayout()
        l.addWidget(CatchingWidget(self))
        textedit = QPlainTextEdit('some text I would like to copy', self)
        textedit.setReadOnly(True)
        l.addWidget(textedit)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)


if __name__ == '__main__':
    app = QApplication()
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
