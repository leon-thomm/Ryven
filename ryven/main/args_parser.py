import argparse
import pathlib
import sys

from ryven.main.utils import find_config_file

from ryven import __version__
from ryven.main import utils


def quote(s):
    """Puts double quotes around a string, if it contains one or more spaces.

    Parameters
    ----------
    s : str
        The string.

    Returns
    -------
    str
        If one or more spaces are found in the string, it is returned enclosed
        in double quotes; otherwise the original string is returned

    """

    if ' ' in s:
        # String with spaces must be enclosed in quotes
        return f'"{s}"'
    else:
        return s


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
        - Comments can be added after the hash sign '#'; either on a line on
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

    def convert_arg_line_to_args(self, line):
        """
        Convert 'key: value' lines to the long command line arguments.

        The following line formats are allowed:
            - 'key': A simple switch; becomes '--key'.
            - 'key: value': An argument with a value; becomes '--key=value'.
            - 'key=value': Equivalent to 'key: value'; becomes '--key=value'.
            - 'key value': Equivalent to 'key: value'; becomes '--key value'.
            - Quotes around values are removed.
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
        args = [a.strip() for a in args.split('=', maxsplit=1)]

        if len(args) == 1:
            # A key without argument is a switch
            key = args[0]
            return [f'--{key}']
        else:
            key, value = args
            # Remove optional quotes around the value
            if value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            elif value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            # Assemble long command line
            return [f'--{key}', value]


def parse_sys_args(just_defaults=False):
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
        action='append',
        # nargs='+', action='extend',
        default=[],
        dest='nodes',
        metavar='NODES_PKG',
        help='''
            load a nodes package;
            If you want to load multiple packages, use the option again;
            nodes packages loaded here take precedence over nodes packages
            with the same name specified in the project file!
            Nodes package names containing spaces must be enclosed in quotes.
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
            One or more configuration files for automatically loading optional
            arguments can be used at any position;
            • If the file
            "{pathlib.Path(utils.ryven_dir_path()).joinpath("ryven.cfg")}
            exists, it will always be read as the very first configuration file;
            • to explicitly load a configuration file from a given location, the file
            name must be preceded with the @-sign, e.g. "@ryven.cfg";
            the later command line arguments or configuration files take
            precedence over earlier specified arguments;
            • the format is like the long command line argument, but with the
            leading two hyphens removed. If the argument takes a value, this
            comes after a colon or an equal sign, e.g. "example: basics" or "example=basics".
            • There is no need to enclose values containing spaces in quotes as
            on the command line.
            • Symmetric single or double quotes around values are removed.
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
        if args.project == '-':
            args.project = sys.stdin
        else:
            project = utils.find_project(args.project)
            if project is None:
                parser.error(
                    'project file does not exist')
            args.project = project

    # Make a `set` of nodes
    args.nodes = set([pathlib.Path(nodes_pkg) for nodes_pkg in args.nodes])

    # Put example into 'project' argument
    if args.example:
        if args.project:
            parser.error(
                'when loading an example, no argument PROJECT is allowed')

        args.project = pathlib.Path(exampledir, args.example).with_suffix('.json')

    return args


def unparse_sys_args(args):
    """Generate command line and configuration file.

    Reverse parsing the args namespace into two strings:
        - a command representing the command line arguments
        - the content of the corresponding config file

    Parameters
    ----------
    args : argparse.Namespace
        The arguments containing the configuration, just like what
        `parse_sys_args()` returns.

    Returns
    -------
    command : string
        The command line argument that would generate the supplied
        configuration.
    config : string
        The contents of a config file that would generate the supplied
        configuration.

    """

    cmd_line = [sys.argv[0]]
    cfg_file = []
    project = None

    for key, value in vars(args).items():
        if value is True:
            # A positive switch
            cmd_line.append(f'--{key}')
            cfg_file.append(key)
        elif value is False:
            # A negative switch
            cmd_line.append(f'--no-{key}')
            cfg_file.append(f'no-{key}')
        elif isinstance(value, list):
            for v in value:
                # Values with spaces must be enclosed in quotes
                cmd_line.append(f'--{key}={quote(v)}')
                cfg_file.append(f'{key}: {v}')
        elif key == 'project':
            # Save the project, because it has to be the last argument
            project = quote(value)
        else:
            # An argument with a value
            cmd_line.append(f'--{key}={quote(v)}')
            cfg_file.append(f'{key}: {value}')

    # Append project
    if project:
        cmd_line.append(project)
        cfg_file.append(f'project: {project}')

    return ' '.join(cmd_line), '\n'.join(cfg_file)


def process_args(use_sysargs, *args_, **kwargs):
    """Completely processes all arguments given either through sys args,
    or through function arguments. Performs checks on argument correctness,
    and injects the arguments from the default config file

    Parameters
    ----------
    use_sysargs : bool, optional
        Whether the command line arguments should be used.
        The default is `True`.
    *args_
        Corresponding to the positional command line argument(s).
    **kwargs
        Corresponding to the keyword command line arguments.

    Returns
    -------
    args : argparse.Namespace
        The parsed command line arguments or the default values, merged with
        config file arguments.
    """

    # Inject default configuration file in user's directory as first argument!
    config_file = pathlib.Path(utils.ryven_dir_path()).joinpath('ryven.cfg')
    if config_file.exists():
        sys.argv.insert(1, f'@{config_file}')

    if use_sysargs:
        # locate '@' config files
        for val in sys.argv:
            if val.startswith('@'):
                i = sys.argv.index(val)
                sys.argv.remove(val)
                path = str(find_config_file(val.strip('@')))
                if path is None:
                    sys.exit(f"Error: could not find config file: {val}")
                sys.argv.insert(i, '@'+path)

        # Get parsed command line arguments
        args = parse_sys_args()
    else:
        # Get default values
        args = parse_sys_args(just_defaults=True)

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

    # Check project
    if isinstance(args.project, list):
        # TODO: multiple project files
        # though currently unsupported, multiple 'project' arguments might be possible eventually
        # to enable passing multiple project files after adapting the editor accordingly:
        #   change nargs of project parameter in the argument parser
        args.project.extend(args)
    elif len(args_) > 1:                 # Just one argument, but more given
        raise TypeError(
            f'run() takes 1 positional argument, but {len(args)} were given')
    elif args_:                          # Exactly one argument given
        # Update the 'project' argument with the positional arguments to run()
        # Note, this is intentionally generic, so that changes in `parse_args`
        # does not require changes here!
        project = utils.find_project(args_[0])
        if project is None:
            raise IOError(f'project "{args_[0]}" not found')
        else:
            args.project = project

    return args