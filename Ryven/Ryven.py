import os
import sys

from custom_src.Console.MainConsole import MainConsole, RedirectOutput
from custom_src.startup_dialog.StartupDialog import StartupDialog
from custom_src.MainWindow import MainWindow
from PySide2.QtWidgets import QApplication
from contextlib import redirect_stdout, redirect_stderr

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    app = QApplication(sys.argv)

    sw = StartupDialog()
    sw.exec_()

    if not sw.editor_startup_configuration == {}:

        # initialize console
        console = MainConsole()
        console_stdout_redirect = RedirectOutput(console.write)
        console_errout_redirect = RedirectOutput(console.errorwrite)

        with redirect_stdout(console_stdout_redirect), \
             redirect_stderr(console_errout_redirect):

            # init whole UI
            mw = MainWindow(console, sw.editor_startup_configuration)
            mw.show()
            sys.exit(app.exec_())
