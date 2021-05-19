import os
import sys


def apply_stylesheet(style: str):

    from qtpy.QtCore import QDir
    d = QDir()
    d.setSearchPaths('icon', [os.path.abspath('../resources/stylesheets/icons')])

    from WindowTheme import WindowTheme_Dark, WindowTheme_Light

    if style == 'dark':
        window_theme = WindowTheme_Dark()

    else:
        window_theme = WindowTheme_Light()

    f = open('../resources/stylesheets/style_template.css')

    from jinja2 import Template
    jinja_template = Template(f.read())

    f.close()

    app.setStyleSheet(jinja_template.render(window_theme.rules))
    # print(app.styleSheet())

    return window_theme


if __name__ == '__main__':

    # change directory to current to this file's location
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    if len(sys.argv) > 1 and sys.argv[1] == 'console':

        # ryven console

        os.environ['RYVEN_MODE'] = 'no-gui'

        from ryven_console import run
        run()

    else:

        os.environ['RYVEN_MODE'] = 'gui'
        os.environ['QT_API'] = 'pyside2'

        sys.path.append(os.path.join(__file__, 'code_editor/pygments/dracula.py'))

        from MainConsole import init_main_console
        from startup_dialog.StartupDialog import StartupDialog
        from MainWindow import MainWindow
        from contextlib import redirect_stdout, redirect_stderr
        from qtpy.QtWidgets import QApplication

        # init application
        app = QApplication(sys.argv)

        # register fonts
        from qtpy.QtGui import QFontDatabase
        db = QFontDatabase()
        db.addApplicationFont('../resources/fonts/poppins/Poppins-Medium.ttf')
        db.addApplicationFont('../resources/fonts/source_code_pro/SourceCodePro-Regular.ttf')
        db.addApplicationFont('../resources/fonts/asap/Asap-Regular.ttf')

        window_theme = apply_stylesheet('dark' if 'light' not in sys.argv else 'light')

        # StartupDialog
        sw = StartupDialog()
        sw.exec_()

        # exit if dialog couldn't initialize
        if sw.editor_startup_configuration == {}:
            sys.exit()

        # init console and redirect all output
        console_stdout_redirect, console_errout_redirect = init_main_console(window_theme)
        with redirect_stdout(console_stdout_redirect), \
             redirect_stderr(console_errout_redirect):

            mw = MainWindow(sw.editor_startup_configuration, window_theme)
            mw.show()

            sys.exit(app.exec_())
