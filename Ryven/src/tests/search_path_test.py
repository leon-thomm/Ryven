from PySide6.QtCore import QDir
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
import sys
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(QCheckBox('test'))


if __name__ == '__main__':

    app = QApplication(sys.argv)

    # the icon used below lies in the same dir as this file
    QDir.addSearchPath('icon', os.path.dirname(os.path.abspath(__file__)))

    app.setStyleSheet("""
QCheckBox::indicator:checked {
    image: url(icon:/checkbox_checked.svg);
}
    """)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
