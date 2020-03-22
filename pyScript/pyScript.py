import sys

from custom_src.StartupDialog import StartupDialog
from custom_src.MainWindow import MainWindow
from PySide2.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    sw = StartupDialog()
    sw.exec_()

    if not sw.editor_startup_configuration == {}:
        mw = MainWindow(sw.editor_startup_configuration)
        mw.show()

        sys.exit(app.exec_())