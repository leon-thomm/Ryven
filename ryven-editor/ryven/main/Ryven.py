import os
import sys

import ryven.main.packages.nodes_package
from ryven.main import utils
from ryven.main.config import Config
from ryven.main.args_parser import process_args


def check_pyside_available(qt_api: str):
    if qt_api == 'pyside2':
        if sys.version_info >= (3, 11):
            sys.exit(
                'You are trying to use PySide2 as the Qt API, but it is not available for Python 3.11 and later. '
                'Please use PySide6 instead (run `ryven -q pyside6`), or use Python 3.10 or earlier. '
            )
        try:
            import PySide2
        except ImportError:
            sys.exit(
                'You are trying to use PySide2 as the Qt API, but it is not available. '
                'Please install it, or use pyside6 as the Qt API. Either of those can '
                'installed through pip, e.g. `pip install pyside2` or `pip install \'pyside6<6.7\'`. '
            )
    elif qt_api == 'pyside6':
        try:
            import PySide6
        except ImportError:
            sys.exit(
                'You are trying to use PySide6 as the Qt API, but it is not available. '
                'please install it, or use pyside2 as the Qt API. Either of those can '
                'installed through pip, e.g. `pip install pyside2` or `pip install \'pyside6<6.7\'`. '
            )
    else:
        sys.exit(
            f'Error: Illegal Qt API: "{qt_api}". '
            f'Use either "pyside2" or "pyside6". '
        )


def run(*args_,
        qt_app=None, gui_parent=None, use_sysargs: bool = True,
        **kwargs):
    """Start the Ryven window.

    The `*args_` and `**kwargs` arguments correspond to their positional and
    optional command line equivalents, respectively (see `parse_args()`).
    Optional keyword arguments are specified without the leading double hyphens
    '--'. As a name, the corresponding 'dest' value of `add_argument` has to
    be used. E.g. the command line:
        ryven --window-theme=light --nodes=std --nodes=linalg myproject.json
    becomes:
        run('myproject.json', window_theme='light', nodes=['std', 'linalg'])

    Note 1
    ------
    The `*args_` and `**kwargs` takes predecence and overwrites the values
    specified on the command line (or the default values, if
    `use_sysargs=False` is given). The exception are lists, which are appended,
    e.g. in the example from above, the two nodes 'std' and 'linalg' are added
    at the end of the nodes supplied at the command line.

    Note 2
    ------
    The positional command line argument to specify the project file also
    checks `utils.ryven_dir_path()/saves`, if it can find the project file.
    The `*args_` does not perform this check. This is up to the developer
    calling `run()`. The developer can always use `utils.find_project()` to
    find projects in this additional directory.

    Parameters
    ----------
    qt_app : QApplication, optional
        The `QApplication` to be used. If `None` a `QApplication` is generated.
        The default is `None`.
    gui_parent : QWidget, optional
        The parent `QWidget`.
        The default is `None`.
    use_sysargs : bool, optional
        Whether the command line arguments should be used.
        The default is `True`.
    *args_ : str
        Corresponding to the positional command line argument(s).
    **kwargs : any
        Corresponding to the keyword command line arguments.

    Raises
    ------
    TypeError
        Raised, if keyword argument is not specified by the argument parser or
        the wrong number of positional arguments are specified.

    Returns
    -------
    None|Main Window
    """
                
    # Process command line and method's arguments
    conf: Config = process_args(use_sysargs, *args_, **kwargs)

    #
    # Qt application setup
    #

    # Init environment
    check_pyside_available(conf.qt_api)
    os.environ['RYVEN_MODE'] = 'gui'
    os.environ['QT_API'] = conf.qt_api
    from ryven.node_env import init_node_env
    from ryven.gui_env import init_node_guis_env  # Qt dependency
    init_node_env()
    init_node_guis_env()

    # Import GUI sources (must come after setting `os.environ['QT_API']`)
    from ryven.gui.main_console import init_main_console
    from ryven.gui.main_window import MainWindow
    from ryven.gui.styling.window_theme import apply_stylesheet

    # Init Qt application
    if qt_app is None:
        from qtpy.QtWidgets import QApplication
        if conf.window_geometry:
            # Pass '--geometry' argument to Qt
            qt_args = [sys.argv[0], '-geometry', conf.window_geometry]
        else:
            qt_args = [sys.argv[0]]
        app = QApplication(qt_args)
    else:
        app = qt_app

    # Register fonts
    from qtpy.QtGui import QFontDatabase
    db = QFontDatabase()
    db.addApplicationFont(
        utils.abs_path_from_package_dir('resources/fonts/poppins/Poppins-Medium.ttf'))
    db.addApplicationFont(
        utils.abs_path_from_package_dir('resources/fonts/source_code_pro/SourceCodePro-Regular.ttf'))
    db.addApplicationFont(
        utils.abs_path_from_package_dir('resources/fonts/asap/Asap-Regular.ttf'))

    #
    # Editor configuration
    #

    # editor_config = {}

    # Startup dialog
    if conf.show_dialog:
        from ryven.gui.startup_dialog.StartupDialog import StartupDialog

        # Get packages and project file interactively and update arguments accordingly

        sw = StartupDialog(config=conf, parent=gui_parent)
        # Exit if dialog couldn't initialize or is exited
        if sw.exec_() <= 0:
            sys.exit('Start-up screen dismissed')

    # Replace node directories with `NodePackage` instances
    if len(conf.nodes) > 0:
        conf.nodes, pkgs_not_found, _ = ryven.main.packages.nodes_package.process_nodes_packages(list(conf.nodes))
        if pkgs_not_found:
            sys.exit(
                f'Error: Nodes packages not found: {", ".join([str(p) for p in pkgs_not_found])}')

        # editor_config['requested packages'] = conf.nodes

    # Store WindowTheme object
    assert isinstance(conf.window_theme, str)
    conf.window_theme = apply_stylesheet(conf.window_theme)

    # Adjust flow theme if not set
    if conf.flow_theme is None:
        if conf.window_theme.name == 'dark':
            conf.flow_theme = 'pure dark'
        else:
            conf.flow_theme = 'pure light'

    # Note:
    #   At this point, the Config is fully populated with exact types
    #   (e.g. `conf.nodes` is a list of `NodePackage` instances, and
    #   not a list of `str` anymore).

    # Get packages required by the project
    if conf.project:
        pkgs, pkgs_not_found, project_dict = ryven.main.packages.nodes_package.process_nodes_packages(
            conf.project,
            requested_packages=list(conf.nodes)  # type: ignore
        )

        if pkgs_not_found:
            str_missing_pkgs = ', '.join([str(p.name) for p in pkgs_not_found])
            plural = len(pkgs_not_found) > 1
            sys.exit(
                f'The package{"s" if plural else ""} {str_missing_pkgs} '
                f'{"were" if plural else "was"} requested, '
                f'but {"they are" if plural else "it is"} not available.\n'
                f'Update the project file or supply the missing package{"s" if plural else ""} '
                f'{str_missing_pkgs} on the command line with the "-n" switch.')

        requested_packages = conf.nodes
        required_packages = pkgs
        project_content = project_dict

    else:
        requested_packages = conf.nodes
        required_packages = None
        project_content = None

    #
    # Launch editor
    #

    # Init main console
    (console_stdout_redirect, console_errout_redirect) = \
        init_main_console(conf.window_theme)

    # Init main window
    editor = MainWindow(
        config=conf,
        requested_packages=requested_packages,
        required_packages=required_packages,
        project_content=project_content,
        parent=gui_parent
    )
    editor.show()

    # Start application
    if qt_app is None:
        if conf.verbose:
            # Run application
            editor.print_info()
            sys.exit(app.exec_())

        else:
            # Redirect console output
            import contextlib

            with contextlib.redirect_stdout(console_stdout_redirect), \
                    contextlib.redirect_stderr(console_errout_redirect):
                # Run application
                editor.print_info()
                sys.exit(app.exec_())

    else:
        return editor


if __name__ == '__main__':

    run()
