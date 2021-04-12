import os
import sys


def apply_stylesheet(style='dark'):

    # from PySide2.QtCore import QDir
    # d = QDir()
    # d.setSearchPaths('icon', [os.path.abspath('../resources/stylesheets/icons')])

    if style == 'dark':
        colors = {
            'primaryColor': '#448aff',
            'primaryLightColor': '#83b9ff',
            'secondaryColor': '#1E242A',
            'secondaryLightColor': '#272d32',
            'secondaryDarkColor': '#0C1116',
            'primaryTextColor': '#E9E9E9',
            'secondaryTextColor': '#9F9F9F',
            'danger': '#dc3545',
            'warning': '#ffc107',
            'success': '#17a2b8',
        }
    else:
        colors = {
            'primaryColor': '#448aff',
            'primaryLightColor': '#508AD8',
            'secondaryColor': '#FFFFFF',
            'secondaryLightColor': '#E8EAEC',
            'secondaryDarkColor': '#ECEDEF',
            'primaryTextColor': '#1A1A1A',
            'secondaryTextColor': '#6E6E6E',
            'danger': '#dc3545',
            'warning': '#ffc107',
            'success': '#17a2b8',
        }

        # primary: primaryColor #448aff
        # secondary: secondaryColor #1E242A
        # disabled: secondaryLightColor #272d32

    f = open('../resources/stylesheets/style_template.css')
    style_sheet = f.read()
    f.close()

    for cname, c in colors.items():
        style_sheet = style_sheet.\
            replace('{{'+cname+'}}', c).\
            replace('{{rgb_inline_'+cname+'}}', ','.join([str(int(c[i+1:i+3], 16)) for i in (0, 2, 4)]))

    style_sheet = style_sheet\
        .replace('{{font_family}}', 'Roboto')\
        .replace('url(icon:/', 'url(' + os.path.abspath('../resources/stylesheets/icons').replace('\\', '/') + '/')\
        .replace('url("icon:/', 'url("' + os.path.abspath('../resources/stylesheets/icons').replace('\\', '/') + '/')
    # print(style_sheet)

    app.setStyleSheet(style_sheet)
    # print(style_sheet)


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

        from MainConsole import init_main_console
        from startup_dialog.StartupDialog import StartupDialog
        from MainWindow import MainWindow
        from contextlib import redirect_stdout, redirect_stderr
        from PySide2.QtWidgets import QApplication

        # init application
        app = QApplication(sys.argv)

        # register fonts
        from PySide2.QtGui import QFontDatabase
        db = QFontDatabase()
        db.addApplicationFont('../resources/fonts/poppins/Poppins-Medium.ttf')
        db.addApplicationFont('../resources/fonts/source_code_pro/SourceCodePro-Regular.ttf')
        db.addApplicationFont('../resources/fonts/asap/Asap-Regular.ttf')


        if 'light' in sys.argv:
            apply_stylesheet('light')
        else:
            apply_stylesheet('dark')


        # StartupDialog
        sw = StartupDialog()
        sw.exec_()

        # exit if dialog couldn't initialize
        if sw.editor_startup_configuration == {}:
            sys.exit()

        # init console and redirect all output
        console_stdout_redirect, console_errout_redirect = init_main_console()
        with redirect_stdout(console_stdout_redirect), \
             redirect_stderr(console_errout_redirect):

            mw = MainWindow(sw.editor_startup_configuration)
            mw.show()

            sys.exit(app.exec_())
