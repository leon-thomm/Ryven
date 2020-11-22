import os
import sys

import custom_src.Console.MainConsole as MainConsole
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

        if MainConsole.main_console_enabled:
            # initialize console
            MainConsole.init_main_console()
            console_stdout_redirect = MainConsole.RedirectOutput(MainConsole.main_console.write)
            console_errout_redirect = MainConsole.RedirectOutput(MainConsole.main_console.errorwrite)

            with redirect_stdout(console_stdout_redirect), \
                 redirect_stderr(console_errout_redirect):

                # init whole UI
                mw = MainWindow(sw.editor_startup_configuration)
                mw.show()
                sys.exit(app.exec_())

        else:  # just for some debugging
            # init whole UI
            mw = MainWindow(sw.editor_startup_configuration)
            mw.show()
            sys.exit(app.exec_())
