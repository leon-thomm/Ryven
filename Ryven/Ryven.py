import os
import sys

from custom_src.startup_dialog.StartupDialog import StartupDialog
from custom_src.MainWindow import MainWindow
from PySide2.QtWidgets import QApplication

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    app = QApplication(sys.argv)

    sw = StartupDialog()
    sw.exec_()

    if not sw.editor_startup_configuration == {}:
        mw = MainWindow(sw.editor_startup_configuration)
        mw.show()

        sys.exit(app.exec_())