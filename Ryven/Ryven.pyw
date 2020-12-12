import os
import sys

from custom_src.Console.MainConsole import init_main_console

from custom_src.startup_dialog.StartupDialog import StartupDialog
from custom_src.MainWindow import MainWindow
from PySide2.QtWidgets import QApplication
from contextlib import redirect_stdout, redirect_stderr


if __name__ == '__main__':

    # change directory to current to this file's location
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # init application, StartupDialog
    app = QApplication(sys.argv)
    sw = StartupDialog()
    sw.exec_()

    # return if dialog couldn't initialize
    if sw.editor_startup_configuration == {}:
        sys.exit()

    # init console and redirect all output
    console_stdout_redirect, console_errout_redirect = init_main_console()
    with redirect_stdout(console_stdout_redirect), \
         redirect_stderr(console_errout_redirect):

        mw = MainWindow(sw.editor_startup_configuration)
        mw.show()

        sys.exit(app.exec_())
