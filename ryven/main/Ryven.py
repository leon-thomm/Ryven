import os
import sys
import argparse
import re
import pathlib

from ryven.main import utils
from ryven.NENV import init_node_env
from ryven.NWENV import init_node_widget_env
from ryven import __version__


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
        - '--verbose' on the command line simply becomes 'verbose' in the
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

    # Regular expression to split on spaces except within quotes - returns a
    # tuple with three values:
    #     (<inside double quotes>, < inside single quotes>, <without quotes>)
    value_re = r'''"([^"]*)"|'([^']*)'|([\S]+)'''

    def __init__(self, *args, **kwargs):
        # Inject `fromfile_prefix_char='@'` to the keyword arguments
        kwargs['fromfile_prefix_chars'] = '@'
        super().__init__(*args, **kwargs)
        # Speed up regular expression
        self.value_re = re.compile(self.value_re)

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
            The parsed line from the configuration file with the key (including
            the leading '--') as first element and then all values, where
            quoted items their quotes stripped.

        """

        # Remove comments and white spaces around remaining line
        args = line.split('#', maxsplit=1)[0].strip()
        if not args:
            # Empty line
            return []

        # Generate long command line argument

        # Replace first ':' with a '='
        args = args.replace(':', '=', 1)

        # Split line into keyword and argument
        args = args.split('=', maxsplit=1)

        if len(args) == 1:
            # A key without argument is a switch
            args = [f'--{args[0]}']
        else:
            key, values = args
            # Assemble long command line
            args = [f'--{key.strip()}']
            # Split values into a list of tokens taking care of quotes
            # `self.value_re.findall()` returns a list of tuples
            for value in self.value_re.findall(values.replace("'", '"')):
                # Each tuple has three elements - either all elements are empty
                # or exactly one non-empty element, look for this element and
                # add it to your list of element.
                args.extend([v for v in value if v])
        return args


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
    exampledir = utils.abs_path_from_package_dir('examples_projects')
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

    # Optional arguments

    parser.add_argument(
        nargs='?',
        dest='project',
        metavar='PROJECT',
        help=f'''
            the project file to be loaded (the suffix ".json" can be omitted);
            if the project file cannot be found, it is searched for under the
            directory "{pathlib.PurePath(utils.ryven_dir_path(), "saves")}";
            if the project file immediately follows nodes packages, separate
            the project file with " -- ";
            use "-" for standard input
            ''')

    parser.add_argument(
        '-s', '--show-dialog',
        action='store_true',
        dest='show_dialog',
        help='''
            show the start-up dialog,
            where project files, examples, nodes packages can be loaded and
            some settings changed
            ''')

    parser.add_argument(
        '-V', '--version',
        action='version',
        version=f'%(prog)s {__version__}')

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        dest='verbose',
        help='display messages on the terminal console')

    # Project

    group = parser.add_argument_group('projects')

    group.add_argument(
        '-n', '--nodes',
        nargs='+', action='extend',
        default=[],
        dest='nodes',
        metavar='NODES_PKG',
        help='''
            load one or more nodes packages;
            nodes packages loaded here take precedence over nodes packages
            with the same name specified in the project file!
            Nodes package names containing spaces must be enclosed in quotes.
            If the nodes are immediately followed by the project file,
            separate the project file with a " -- ";
            (%(metavar)s is the path to the nodes package without "/nodes.py")
            ''')

    group.add_argument(
        '-x', '--example',
        choices=examples,
        dest='example',
        help='load an example project (do not give PROJECT argument)')

    # Display

    group = parser.add_argument_group('display')

    group.add_argument(
        '-w', '--window-theme',
        choices=['dark', 'light', 'plain'],
        default='dark',
        dest='window_theme',
        help='''
            set the window theme
            (default: %(default)s)
            ''')

    group.add_argument(
        '-f', '--flow-theme',
        choices=[
            'toy', 'tron', 'ghost', 'blender', 'simple', 'ueli',
            'pure dark', 'colorful dark',
            'pure light', 'colorful light', 'industrial', 'fusion'],
        dest='flow_theme',
        help='''
            set the theme of the flow view; the theme's name must be put
            between quotation marks, if it contains spaces
            (default: {pure dark|pure light}, depending on the window theme)
            ''')

    group.add_argument(
        '--performance',
        choices=['pretty', 'fast'],
        default='pretty',
        dest='performance',
        help='''
            select performance mode
            (default: %(default)s)
            ''')

    # TODO: Python >= 3.9
    # group.add_argument(
    #     '--animations',
    #     action=argparse.BooleanOptionalAction,
    #     dest='animations',
    #     help='en/disable animations '
    #          '(default: %(default)s)')
    exclusive_group = group.add_mutually_exclusive_group()
    exclusive_group.add_argument(
        '--no-animations',
        action='store_false',
        dest='animations',
        help='''
            do not use animations
            (default: use animations)
            ''')
    exclusive_group.add_argument(
        '--animations',
        action='store_true',
        dest='animations',
        help='''
            use animations
            (default: use animations)
            ''')

    # TODO: Python >= 3.9
    # group.add_argument(
    #     '--info-messages',
    #     action=argparse.BooleanOptionalAction,
    #     dest='info_messages',
    #     help='en/disable info messages '
    #          '(default: %(default)s)')
    exclusive_group = group.add_mutually_exclusive_group()
    exclusive_group.add_argument(
        '--info-messages',
        action='store_true',
        dest='info_messages',
        help='''
            show info messages
            (default: do not show info messages)
            ''')
    exclusive_group.add_argument(
        '--no-info-messages',
        action='store_false',
        dest='info_messages',
        help='''
            do not show info messages
            (default: do not show info messages)
            ''')

    group.add_argument(     # Passed to Qt
        '--geometry',
        dest='geometry',
        metavar='[WxH][{+,-}X{+,-}Y]',
        help='''
            change the size of the window to WxH and
            position it at X,Y on the screen
            ''')

    group.add_argument(
        '-t', '--title',
        default='Ryven',
        dest='title',
        help='''
            changes the window's title
            (default: %(default)s)
            ''')

    group.add_argument(
        '-q', '--qt-api',
        default='pyside2',
        dest='qt_api',
        help='''
            the QT API to be used
            (default: %(default)s)
            ''')

    # Configuration files

    parser.add_argument_group(
        'configuration files',
        description=f'''
            One or more configuration files can be used at any position.
            • To mark an argument to be used as a configuration files, the file
            name must be preceded with the @-sign, e.g. "@ryven.cfg".
            The later command line arguments or configuration file takes
            precedence over earlier specified arguments.
            • The format is like the long command line argument, but with the
            leading two hyphens removed. If the argument takes a value, this
            comes after a colon or an equal sign,
            e.g. these three lines are identical:
            "example: basics" and "example=basics".
            • Values containing spaces must be enclosed in quotes as on the
            command line.
            • Comments can be inserted after the hash sign "#".
            • If the file
            "{pathlib.Path(utils.ryven_dir_path()).joinpath("ryven.cfg")}
            exists, it will always be read as the very first configuration file.
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
        if args.project == '-':
            args.project = sys.stdin
        else:
            project = utils.find_project(args.project)
            if project is None:
                parser.error(
                    'project file does not exist')
            args.project = project

    # Put example into 'project' argument
    if args.example:
        if args.project:
            parser.error(
                'when loading an example, no argument PROJECT is allowed')

        args.project = pathlib.Path(exampledir, args.example).with_suffix('.json')

    # Make a `set` of nodes
    args.nodes = set(args.nodes)

    return args


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

    #
    # Process command line and method's arguments
    #

    # Inject default configuration file in user's directory as first argument!
    config_file = pathlib.Path(utils.ryven_dir_path()).joinpath('ryven.cfg')
    if config_file.exists():
        sys.argv.insert(1, f'@{config_file}')

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
        elif isinstance(getattr(args, key), set):
            setattr(args, key, getattr(args, key).union(set(value)))
        else:
            setattr(args, key, value)

    # Update the 'project' argument with the positional arguments to run()
    # Note, this is intentionally generic, so that changes in `parse_args`
    # does not require changes here!

    # TODO: multiple project files
    # though currently unsupported, multiple 'project' arguments might be possible eventually
    # to enable passing multiple project files after adapting the editor accordingly:
    #   change nargs of project parameter in the argument parser
    if isinstance(args.project, list):
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
    # Ryven main window set up
    #

    editor_config = {}

    # Replace node directories with `NodePackage` instances
    if args.nodes:
        args.nodes, nodes_not_found, _ = utils.process_nodes_packages(args.nodes)
        if nodes_not_found:
            sys.exit(
                f'''Error: Nodes packages not found: '''
                f'''{", ".join(['"'+str(n)+'"' for n in nodes_not_found])}''')

        editor_config['requested packages'] = args.nodes

    # Get packages and project file interactively and update arguments accordingly
    if args.show_dialog:
        # Startup dialog
        from ryven.gui.startup_dialog.StartupDialog import StartupDialog

        sw = StartupDialog(vars(args), parent=gui_parent)
        # Exit if dialog couldn't initialize or is exited
        if sw.exec_() <= 0:
            sys.exit('Start-up screen dismissed')

        # Update `args` with `sw.configs`
        for key, value in sw.configs.items():
            # A little safeguard
            if hasattr(args, key):
                setattr(args, key, value)
            else:
                raise KeyError(
                    f'The startup dialog set an unknown argument. '
                    f'Got: {key}={value}')

    else:
        # This is needed, because the stylesheet is applied in `StartupDialog`
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
        editor_config['content'] = project_dict

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

    # FIXME? `window_theme` is of type `WindowTheme`, but `flow_theme` is a `str`

    # Init main console
    (console_stdout_redirect, console_errout_redirect
     ) = init_main_console(args.window_theme)

    # Project setup
    editor_config['info messages enabled'] = args.info_messages
    editor_config['performance mode'] = args.performance
    editor_config['animations enabled'] = args.animations

    # Init main window
    editor = MainWindow(
        editor_config,
        args.title, args.window_theme, args.flow_theme,
        parent=gui_parent)
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
