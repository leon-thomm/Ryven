import os
import sys
import argparse
import pathlib

from ryven.main.utils import abs_path_from_package_dir
from ryven.NENV import init_node_env
from ryven.NWENV import init_node_widget_env


class CustomArgumentParser(argparse.ArgumentParser):
    """An `ArgumentParser` for 'key: value' configuration files.

    Configuration files can be specified on the command line with a prefixed
    at-sign '@'. Later command line arguments (or additional configuration
    files) override previous values.

    The format of the configuration files is 'key[:value]' and very similar to
    the long command line arguments, e.g.
        - '--example=basics' (or '--example basics') on the command line
          becomes 'example: basics' (or 'example=basics') in the configuration
          file.
        - '--debug' on the command line simply becomes 'debug' in the
          configuration file.

    Some more comments on the file format:
        - The key is always the long format of the command line argument to be
          set.
        - Spaces before the key are allowed.
        - Spaces after the value are stripped.
        - Spaces are allowed on either side of ':' (or '=').
        - Empty lines are allowed.
        - Comments can be added after a the hash sign '#'; either on a line on
          its own or as inline comments after 'key[:value]'.

    https://tricksntweaks.blogspot.com/2013_05_01_archive.html
    """

    def __init__(self, *args, **kwargs):
        # Inject `fromfile_prefix_char='@'` to the keyword arguments
        kwargs['fromfile_prefix_chars'] = '@'
        super().__init__(*args, **kwargs)

    def convert_arg_line_to_args(self, line):
        """
        Convert 'key: value' lines to the long command line arguments.

        The following line formats are allowed:
            - 'key': A simple switch; becomes '--key'.
            - 'key: value': An argument with a value; becomes '--key=value'.
            - 'key=value': Equivalent to 'key: value'; becomes '--key=value'.
            - 'key value': Equivalent to 'key: value'; becomes '--key value'.
            - Comments behind '#' are removed
            - Empty lines are removed

        See:
            https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.convert_arg_line_to_args

        Parameters
        ----------
        line : str
            One complete line from the configuration line.

        Returns
        -------
        list
            The parsed line from the configuration file as a list with just
            one item.

        """

        # Remove comments and white spaces around remaining line
        args = line.split('#', maxsplit=1)[0].strip()
        if not args:
            # Empty line
            return []

        # Generate long command line argument
        # Replace ':' after the key with '='
        args = args.replace(':', '=', 1)
        # Remove any spaces around '='
        args = '='.join([a.strip() for a in args.split('=', maxsplit=1)])
        # Return long command line argument
        return [f'--{args}']


def parse_args(just_defaults=False):
    """Parse the command line arguments.

    Parameters
    ----------
    just_defaults : bool, optional
        Whether the command line arguments are to be parsed or just the
        defaults are returned.
        The default is `False`, which parses the command line arguments.

    Returns
    -------
    args : argparse.Namespace
        The parsed command line arguments or the default values.

    """

    # Get available examples
    exampledir = abs_path_from_package_dir('examples_projects')
    examples = [e.stem for e in pathlib.Path(exampledir).glob('*.json')]

    #
    # The parser
    #

    parser = CustomArgumentParser(
        description='''
            Flow-based visual scripting with Python with absolute freedom for
            your nodes. See https://ryven.org/guide/ for a guide how to
            program them.
            ''',
        epilog='Copyright (C) 2020-2022 Leon Thomm, licensed under MIT')

    parser.add_argument(
        nargs='?',
        dest='project',
        metavar='PROJECT',
        help='the project file or example to be loaded; '
             'use "-" for standard input')

    # Optional arguments

    parser.add_argument(
        '-s', '--show-dialog',
        action='store_true',
        dest='show_dialog',
        help='show start-up dialog '
             '(disables "--example", "--flow-theme" '
             'and the loading of the project file)')

    # Project

    group = parser.add_argument_group('projects')

    group.add_argument(
        '-n', '--nodes',
        action='append',
        default=[],
        dest='nodes',
        metavar='NODE',
        help='load a nodes packages; '
             'nodes packages loaded here take precedence over nodes packages '
             'with the same name specified in the project file! '
             '(%(metavar)s is the path to the nodes package without "/nodes.py")')

    group.add_argument(
        '-x', '--example',
        choices=examples,
        dest='example',
        help='load an example project '
             '(do not give PROJECT argument)')

    # Display

    group = parser.add_argument_group('display')

    group.add_argument(
        '-w', '--window-theme',
        choices=['dark', 'light'],
        default='dark',
        dest='window_theme',
        help='set the window theme '
             '(default: %(default)s)')

    group.add_argument(
        '-f', '--flow-theme',
        choices=[
            'toy', 'tron', 'ghost', 'blender', 'simple', 'ueli',
            'pure dark', 'colorful dark',
            'pure light', 'colorful light', 'industrial', 'fusion'],
        dest='flow_theme',
        help='set the theme of the flow view '
             '(default: {pure dark|pure light}, depending on the window theme)')

    # Debug

    group = parser.add_argument_group('debug')

    group.add_argument(
        '-d', '--debug',
        action='store_true',
        dest='debug',
        help='display messages on the console')

    # FIXME: Is there a way to get the version dynamically?
    # Could also be used in `MainWindow.save_project()`
    group.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 3.1')

    group.add_argument(
        '-q', '--qt-api',
        default='pyside2',
        dest='qt_api',
        help='the QT API to be used '
             '(default: %(default)s)')

    group.add_argument(
        '-t', '--title',
        default='Ryven',
        dest='title',
        help="changes the window's title "
             '(default: %(default)s)')

    # Configuration files

    parser.add_argument_group(
        'configuration files',
        description='''
            One or more configuration files can be used at any position.
            • To mark an argument to be used as a configuration files, the file
            name must be preceded with the @-sign, e.g. "@ryven.cfg".
            The later command line arguments or configuration file takes
            precedence over earlier specified arguments.
            • The format is like the long command line argument, but with the
            leading two hyphens removed. If the argument takes a value, this
            comes after a colon, e.g. these three lines are identical:
            "example: basics" and "example=basics".
            • Comments can be inserted after the hash sign "#".
        ''')


    #
    # Process the arguments
    #

    # Parse the arguments
    if just_defaults:
        args = parser.parse_args([])
    else:
        args = parser.parse_args()

    # Check, if project file exists
    if args.project:
        project = pathlib.Path(args.project)
        if project.exists():
            args.project = project
        else:
            parser.error(
                'project file does not exist')

    # Put example into 'project' argument
    if args.example:
        if args.project:
            parser.error(
                'when loading an example, no argument PROJECT is allowed')

        args.project = pathlib.Path(exampledir, args.example).with_suffix('.json')

    return args


def process_nodes(nodes):
    """Take a list of nodes, check it and convert it to `[NodesPackage]`.

    It also removes duplicates based on the name (and not the contents!).

    Parameters
    ----------
    nodes : list of str|pathlib.Path|NodesPackage
        A list of nodes. The node can a `NodesPackage` instance, in which case
        the node is copied into the resulting list; otherwise the node is
        considered as a path to 'nodes.py'. If 'nodes.py' is found in the path,
        a `NodesPackage` instance is created and added to the resulting list.
        If 'nodes.py' cannot be found in the path, the package is searchd in
        Ryven's directory, e.g. if "std" is given and not found locally, the
        "std" package included in Ryven is loaded.

    Returns
    -------
    list of NodesPackage
        unique nodes DESCRIPTION.

    """
    from ryven.main.nodes_package import NodesPackage

    node_packages = []
    missing_nodes = []
    for node in nodes:
        if isinstance(node, NodesPackage):
            node_packages.append(node)
        else:
            node_path = pathlib.Path(node)
            if node_path.joinpath('nodes.py').exists():
                node_packages.append(NodesPackage(str(node_path)))
            else:
                # Try to find the node in Ryven's dirs
                for name in ('package', 'example_nodes'):
                    sys_node = pathlib.Path(abs_path_from_package_dir(name)).joinpath(node)
                    if sys_node.joinpath('nodes.py').exists():
                        node_packages.append(NodesPackage(str(sys_node)))
                        break
                else:
                    missing_nodes.append(node)

    if missing_nodes:
        sys.exit(f'Error: Nodes packages not found: {", ".join(missing_nodes)}')

    # Remove duplicate nodes
    seen = set()
    unique_nodes = []
    for node in node_packages:
        if node.name not in seen:
            unique_nodes.append(node)
            seen.add(node.name)

    return unique_nodes


def run(*args_,
        qt_app=None, gui_parent=None, use_sysargs=True,
        **kwargs):
    """Start the Ryven window.

    The `*args` and `**kwargs` arguments correspond to their positional and
    optional command line equivalents, respectively (see `parse_args()`).
    Optional keyword arguments are specified without the leading double hyphens
    '--'. As a name, the corresponding 'dest' value of `add_argument` has to
    be used. E.g. the command line:
        ryven --window-theme=light --nodes=std --nodes=linalg myproject.json
    becomes:
        run('myproject.json', window_theme='light', nodes=['std', 'linalg'])

    Note
    ----
    The `*args` and `**kwargs` takes predecence and overwrites the values
    specified on the command line (or the default values, if
    `use_sysargs=False` is given). The exception are lists, which are appended,
    e.g. in the example from above, the two nodes 'std' and 'linalg' are added
    at the end of the nodes supplied at the command line.

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

    #
    # Process command line and method's arguments
    #

    if use_sysargs:
        # Get parsed command line arguments
        args = parse_args()
    else:
        # Get default values
        args = parse_args(just_defaults=True)

    # Update command line arguments with keyword arguments to run()
    for key, value in kwargs.items():
        if not hasattr(args, key):
            raise TypeError(
                f"run() got an unexpected keyword argument '{key}'")
        if isinstance(getattr(args, key), list):
            getattr(args, key).extend(value)
        else:
            setattr(args, key, value)

    # Update the 'project' argument with the positional arguments to run()
    # Note, this is intentionally generic, so that changes in `parse_args`
    # does not require changes here!
    if isinstance(args.project, list):  # Multiple 'project' arguments possible
        args.project.extend(args)
    elif len(args_) > 1:                 # Just one argument, but more given
        raise TypeError(
            f'run() takes 1 positional argument, but {len(args)} were given')
    elif args_:                          # Exactly one argument given
        args.project = args_[0]

    #
    # Qt application set up
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
        app = QApplication(sys.argv)
    else:
        app = qt_app

    # Register fonts
    from qtpy.QtGui import QFontDatabase
    db = QFontDatabase()
    db.addApplicationFont(abs_path_from_package_dir('resources/fonts/poppins/Poppins-Medium.ttf'))
    db.addApplicationFont(abs_path_from_package_dir('resources/fonts/source_code_pro/SourceCodePro-Regular.ttf'))
    db.addApplicationFont(abs_path_from_package_dir('resources/fonts/asap/Asap-Regular.ttf'))

    #
    # Ryven main window set up
    #

    # Assemble `editor_config`
    if args.show_dialog:
        # Startup dialog
        from ryven.gui.startup_dialog.StartupDialog import StartupDialog

        sw = StartupDialog(args.window_theme, gui_parent)
        sw.exec_()

        # Exit if dialog couldn't initialize or is exited
        if sw.editor_startup_configuration == {}:
            sys.exit('Start-up screen dismissed')

        args.window_theme = sw.window_theme
        editor_config = sw.editor_startup_configuration

    else:
        args.window_theme = apply_stylesheet(args.window_theme)

        if args.project:
            # FIXME: This shadows `StartupDialog.open_project()`
            # Move its entire functionality here (and outside of the if clause?
            import json

            with open(args.project) as f:
                project_dict = json.load(f, strict=False)

            nodes = process_nodes(
                [p['dir'] for p in project_dict['required packages']])

            editor_config = {
                'action': 'open project',
                'required packages': nodes,
                'content': project_dict}

        else:
            editor_config = {'action': 'create project'}

    # Replace node directories with `NodePackage` instances
    if args.nodes:
        nodes = process_nodes(args.nodes)
        editor_config['requested packages'] = nodes

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
        editor_config,
        args.title, args.window_theme, args.flow_theme,
        parent=gui_parent)
    editor.show()

    # Start application
    if qt_app is None:
        if args.debug:
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
