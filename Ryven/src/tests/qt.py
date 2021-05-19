from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


def foo():
    print('clicked!')


if __name__ == '__main__':

    app = QApplication()

    mw = QMainWindow()
    b = QPushButton('click me!')
    b.clicked.connect(foo)
    mw.setCentralWidget(b)
    mw.show()

    sys.exit(app.exec_())
