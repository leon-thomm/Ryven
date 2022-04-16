import os
import sys

from ryven.main import utils
from ryven.NENV import init_node_env
from ryven.NWENV import init_node_widget_env
from ryven.main.args_parser import process_args


def run(*args_,
        qt_app=None, gui_parent=None, use_sysargs=True,
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
    args = process_args(use_sysargs, *args_, **kwargs)

    #
    # Qt application setup
    #

    # QtPy API
    os.environ['QT_API'] = args.qt_api

    # Init environment
    os.environ['RYVEN_MODE'] = 'gui'
    init_node_env()
    init_node_widget_env()

    # Import GUI sources (must come after setting `os.environ['QT_API']`)
    from ryven.gui.main_console import init_main_console
    from ryven.gui.main_window import MainWindow
    from ryven.gui.styling.window_theme import apply_stylesheet

    # Init Qt application
    if qt_app is None:
        from qtpy.QtWidgets import QApplication
        if args.geometry:
            # Pass '--geometry' argument to Qt
            qt_args = [sys.argv[0], '-geometry', args.geometry]
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
    # Ryven editor setup
    #

    editor_config = {}

    # Startup dialog
    if args.show_dialog:
        from ryven.gui.startup_dialog.StartupDialog import StartupDialog

        # Get packages and project file interactively and update arguments accordingly

        sw = StartupDialog(args, parent=gui_parent)
        # Exit if dialog couldn't initialize or is exited
        if sw.exec_() <= 0:
            sys.exit('Start-up screen dismissed')

    # Replace node directories with `NodePackage` instances
    if args.nodes:
        args.nodes, nodes_not_found, _ = utils.process_nodes_packages(args.nodes)
        if nodes_not_found:
            sys.exit(
                f'''Error: Nodes packages not found: '''
                f'''{", ".join(['"' + str(n) + '"' for n in nodes_not_found])}''')

        editor_config['requested packages'] = args.nodes

    # Store WindowTheme object
    args.window_theme = apply_stylesheet(args.window_theme)

    # Get packages required by the project
    if args.project:
        nodes, nodes_not_found, project_dict = utils.process_nodes_packages(
            args.project, requested_nodes=args.nodes)

        if nodes_not_found:
            sys.exit(
                f'The package{"s" if len(nodes_not_found)>1 else ""} '
                f''''{"', '".join([str(p) for p in nodes_not_found])}' '''
                f'{"were" if len(nodes_not_found)>1 else "was"} requested, '
                f'but {"they are" if len(nodes_not_found)>1 else "it is"} not available.'
                f'\n'
                f'Update the project file or supply the missing package{"s" if len(nodes_not_found)>1 else ""} '
                f''''{"', '".join([p.name for p in nodes_not_found])}' '''
                f'on the command line with the "-n" switch.')

        editor_config['action'] = 'open project'
        editor_config['requested packages'] = args.nodes
        editor_config['required packages'] = nodes
        editor_config['project content'] = project_dict

    else:
        editor_config['action'] = 'create project'
        editor_config['requested packages'] = args.nodes

    # Adjust flow theme if not set
    if args.flow_theme is None:
        if args.window_theme.name == 'dark':
            args.flow_theme = 'pure dark'
        else:
            args.flow_theme = 'pure light'

    #
    # Start and run application
    #

    # Init main console
    (console_stdout_redirect, console_errout_redirect
     ) = init_main_console(args.window_theme)

    # Init main window
    editor = MainWindow(
        window_title=args.title,
        window_theme=args.window_theme,
        flow_theme=args.flow_theme,

        action=editor_config['action'],
        requested_packages=editor_config['requested packages'],
        required_packages=editor_config.get('required packages'),
        project_content=editor_config.get('project content'),
        info_msgs_enabled=args.info_messages,
        performance_mode=args.performance,
        animations_enabled=args.animations,

        # editor_config,
        # args.title, args.window_theme, args.flow_theme,
        parent=gui_parent
    )
    editor.show()

    # Start application
    if qt_app is None:
        if args.verbose:
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
