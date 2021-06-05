import os
import sys

# change directory to this file's location
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# PyQt5 doesn't seem to work properly due to crucial inheritance issues
os.environ['QT_API'] = 'pyside2'

# turn off for debugging
REDIRECT_CONSOLE_OUTPUT = True


def start_ryven():

    # import windows
    from MainConsole import init_main_console
    from startup_dialog.StartupDialog import StartupDialog
    from MainWindow import MainWindow

    # init application
    from qtpy.QtWidgets import QApplication
    app = QApplication(sys.argv)

    # register fonts
    from qtpy.QtGui import QFontDatabase
    db = QFontDatabase()
    db.addApplicationFont('../resources/fonts/poppins/Poppins-Medium.ttf')
    db.addApplicationFont('../resources/fonts/source_code_pro/SourceCodePro-Regular.ttf')
    db.addApplicationFont('../resources/fonts/asap/Asap-Regular.ttf')

    # StartupDialog
    sw = StartupDialog()
    sw.exec_()

    # exit if dialog couldn't initialize
    if sw.editor_startup_configuration == {}:
        sys.exit()

    window_theme = sw.window_theme

    # init main console
    console_stdout_redirect, \
    console_errout_redirect = init_main_console(window_theme)

    # init main window
    mw = MainWindow(sw.editor_startup_configuration, window_theme)
    mw.show()

    if REDIRECT_CONSOLE_OUTPUT:  # redirect console output
        from contextlib import redirect_stdout, redirect_stderr

        with redirect_stdout(console_stdout_redirect), \
                redirect_stderr(console_errout_redirect):

            # run
            mw.print_info()
            sys.exit(app.exec_())

    else:

        # run
        mw.print_info()
        sys.exit(app.exec_())


def start_ryven_console():
    from ryven_console import run
    run()


def main():

    if len(sys.argv) > 1 and sys.argv[1] == 'console':
        os.environ['RYVEN_MODE'] = 'no-gui'
        start_ryven_console()
    else:
        os.environ['RYVEN_MODE'] = 'gui'
        start_ryven()


if __name__ == '__main__':
    main()
