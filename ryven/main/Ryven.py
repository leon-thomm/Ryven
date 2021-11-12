import os
import sys
from ryven.main.utils import abs_path_from_package_dir
from ryven.NENV import init_node_env
from ryven.NWENV import init_node_widget_env

# change directory to this file's location
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# PyQt5 doesn't seem to work properly due to crucial inheritance issues
os.environ['QT_API'] = 'pyside2'

# turn off for debugging
REDIRECT_CONSOLE_OUTPUT = False


def run():
    os.environ['RYVEN_MODE'] = 'gui'
    init_node_env()
    init_node_widget_env()

    # import windows
    from ryven.gui.main_console import init_main_console
    from ryven.gui.startup_dialog.StartupDialog import StartupDialog
    from ryven.gui.main_window import MainWindow

    # init application
    from qtpy.QtWidgets import QApplication
    app = QApplication(sys.argv)

    # register fonts
    from qtpy.QtGui import QFontDatabase
    db = QFontDatabase()
    db.addApplicationFont(abs_path_from_package_dir('resources/fonts/poppins/Poppins-Medium.ttf'))
    db.addApplicationFont(abs_path_from_package_dir('resources/fonts/source_code_pro/SourceCodePro-Regular.ttf'))
    db.addApplicationFont(abs_path_from_package_dir('resources/fonts/asap/Asap-Regular.ttf'))

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


if __name__ == '__main__':
    run()
