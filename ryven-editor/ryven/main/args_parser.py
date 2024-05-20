import argparse
import pathlib
import sys

from ryven.main.utils import find_config_file

from ryven.main.utils import ryven_version
from ryven.main import utils
from ryven.main.config import Config


class CustomHelpFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        text = self._whitespace_matcher.sub(' ', text).strip()
        # The textwrap module is used only for formatting help.
        # Delay its import for speeding up the common usage of argparse.
        import textwrap
        r = []
        for t in text.split('\\'):
            r.extend(textwrap.wrap(t.strip(), width))
        return r

    def _fill_text(self, text, width, indent):
        text = self._whitespace_matcher.sub(' ', text).strip()
        import textwrap
        return '\n'.join([
            textwrap.fill(
                t.strip(), width,
                initial_indent=indent, subsequent_indent=indent)
            for t in text.split('\\')])


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


def parse_sys_args(just_defaults=False) -> Config:
    """Parse the command line arguments into a `Config` instance.

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
    exampledir = utils.abs_path_from_package_dir('example_projects')
    examples = [e.stem for e in pathlib.Path(exampledir).glob('*.json')]

    #
    # The parser
    #

    parser = CustomArgumentParser(
        description='''
            Flow-based visual scripting for Python.\\
            \\
            See https://ryven.org/guide/ for a guide on developing nodes.
            ''',
        formatter_class=CustomHelpFormatter)

    # Positional arguments

    parser.add_argument(
        nargs='?',
        dest='project',
        metavar='PROJECT',
        help=f'''
            the project file to be loaded (the suffix ".json" can be omitted)\\
            • If the project file cannot be found, it is searched for under the
            directory "{pathlib.PurePath(utils.ryven_dir_path(), "saves")}".\\
            • use "-" for standard input.
            ''')

    # Optional arguments

    parser.add_argument(
        '-s', '--skip-dialog',
        action='store_false',
        dest='show_dialog',
        help='''
            skip the start-up dialog
            ''')

    parser.add_argument(
        '-V', '--version',
        action='version',
        version=f'%(prog)s {ryven_version()}')

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help=f'''
            prevents redirect of stderr and stdout to the in-editor console\\
            and prints lots of debug information to the default stderr and stdout
            ''')

    parser.add_argument(
        '--enable-code-editing',
        action='store_true',
        dest='src_code_edits_enabled',
        help=f'''
            • Enables a (highly unstable and hacky) feature that allows temporary\\ 
            editing of the source code of nodes in the source code preview panel\\
            (useful for debugging)\\
            • When enabled, Ryven might consume much more memory than usual
            ''')

    parser.add_argument(
        '--defer-code-loading',
        action='store_true',
        dest='defer_code_loading',
        help=f'''
            • When using deferred code loading, Ryven will load the source code of\\
            nodes only once the user wants to inspect it.\\
            • Deferred code loading decreases package loading time.\\
            ''')

    # Project configuration

    group = parser.add_argument_group('project configuration')

    group.add_argument(
        '-n', '--nodes',
        action='append',
        # nargs='+', action='extend',
        default=Config.nodes,
        dest='nodes',
        metavar='NODES_PKG',
        help='''
            load a nodes package\\
            • If you want to load multiple packages, use the option again.\\
            • Packages loaded here take precedence over packages
            with the same name specified in the project file!\\
            • Package names containing spaces must be enclosed in quotes.
            ''')

    group.add_argument(
        '-x', '--example',
        choices=examples,
        dest='example',
        help='load an example project (do not give the PROJECT argument)')

    # Display

    group = parser.add_argument_group('display')
    
    group.add_argument(
        '-w', '--window-theme',
        choices=Config.get_available_window_themes(),
        default=Config.window_theme,
        dest='window_theme',
        help='''
            set the window theme\\
            Default: %(default)s
            ''')

    group.add_argument(
        '-f', '--flow-theme',
        choices=Config.get_available_flow_themes(),
        dest='flow_theme',
        help='''
            set the theme of the flow view\\
            • The theme's name must be put between quotation marks, if it
            contains spaces.\\
            Default: {pure dark|pure light}, depending on the window theme
            ''')

    group.add_argument(
        '--performance',
        choices=Config.get_available_performance_modes(),
        default=Config.performance_mode,
        dest='performance_mode',
        help='''
            select performance mode\\
            Default: %(default)s
            ''')

    exclusive_group = group.add_mutually_exclusive_group()
    exclusive_group.add_argument(
        '--no-animations',
        action='store_false',
        dest='animations',
        help=f'''
            do not use animations\\
            Default: {'Use' if Config.animations else 'Do not use'} animations
            ''')
    exclusive_group.add_argument(
        '--animations',
        action='store_true',
        dest='animations',
        help=f'''
            use animations\\
            Default: {'Use' if Config.animations else 'Do not use'} animations
            ''')

    group.add_argument(
        '--geometry',
        dest='window_geometry',
        metavar='[WxH][{+,-}X{+,-}Y]',
        help='''
            change the size of the window to WxH and
            position it at X,Y on the screen
            ''')

    group.add_argument(
        '-t', '--title',
        default=Config.window_title,
        dest='window_title',
        help='''
            changes the window's title\\
            Default: %(default)s
            ''')

    group.add_argument(
        '-q', '--qt-api',
        default=Config.qt_api,
        dest='qt_api',
        help='''
            the QT API to be used\\
            • Notice that only PySide versions are allowed, Ryven does not work with PyQt.\\
            Default: %(default)s
            ''')

    # Configuration files

    parser.add_argument_group(
        'configuration files',
        description=f'''
            One or more configuration files for automatically loading optional
            arguments can be used at any position.\\
            • If the file
            "{pathlib.Path(utils.ryven_dir_path()).joinpath("ryven.cfg")}"
            exists, it will always be read as the very first configuration
            file.\\
            • This default configuration file is created with an example during 
            installation.\\
            • To explicitly load a configuration file from a given location,
            the file name must be preceded with the @-sign, e.g. "@ryven.cfg".\\
            • The later command line arguments or configuration files take
            precedence over earlier specified arguments.\\
            • The format is like the long command line argument, but with the
            leading two hyphens removed. If the argument takes a value, this
            comes after a colon or an equal sign, e.g. "example: basics" or
            "example=basics".\\
            • There is no need to enclose values containing spaces in quotes as
            on the command line, but they can be enclosed if preferred.\\
            • Symmetric single or double quotes around values are removed.\\
            • Comments can be inserted after the hash sign "#" inline or on
            a line on their own.
            ''')

    #
    # Process the arguments
    #

    # Parse the arguments
    if just_defaults:
        args = parser.parse_args([], namespace=Config())
    else:
        args = parser.parse_args(namespace=Config())

    # Check, if project file exists
    if args.project:
        if args.project == '-':
            args.project = pathlib.Path(str(sys.stdin))
        project = utils.find_project(args.project)
        if project is None:
            parser.error(
                'project file does not exist')
        args.project = project

    # Make a `set` of paths to node packages
    args.nodes = set([pathlib.Path(nodes_pkg) for nodes_pkg in args.nodes])  # type: ignore

    # Put example into 'project' argument
    if args.example:
        if args.project:
            parser.error(
                'when loading an example, no argument PROJECT is allowed')

        args.project = pathlib.Path(exampledir, args.example).with_suffix('.json')

    return args


def quote(s):
    """Puts strings with spaces in quotes; strings without spaces remain unchanged"""

    if ' ' in s:
        # Values with spaces must be enclosed in quotes
        return f'"{s}"'
    else:
        return s


def unparse_sys_args(args: Config):
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

    cmd_line = ['ryven']
    cfg_file = []

    for key, value in vars(args).items():

        key = key.replace('_', '-')

        if value is True:
            # A positive switch
            cmd_line.append(f'--{key}')
            cfg_file.append(key)
        elif value is False:
            # A negative switch
            cmd_line.append(f'--no-{key}')
            cfg_file.append(f'no-{key}')
            # TODO: not all switches have a negative form; e.g. --verbose does not
        else:
            # An argument with a value

            if value is None:
                continue

            if isinstance(value, pathlib.Path):
                value = str(value)

            value_quoted = quote(value)

            if key == 'nodes':
                for n in value:
                    value_quoted = quote(str(n))

                    cmd_line.append(f'-n {value_quoted}')
                    cfg_file.append(f'nodes: {n}')

            elif key == 'project':
                continue

            else:
                cmd_line.append(f'--{key}={value_quoted}')
                cfg_file.append(f'{key}: {value}')

    if args.project:
        cmd_line.append(f'{quote(str(args.project))}')

        # The config file should not contain a project.

    return ' '.join(cmd_line), '\n'.join(cfg_file)


def process_args(use_sysargs, *args_, **kwargs) -> Config:
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

    # Inject default configuration file in user's directory as first argument
    config_file = pathlib.Path(utils.ryven_dir_path()).joinpath('ryven.cfg')
    if config_file.exists():
        sys.argv.insert(1, f'@{config_file}')

    # Locate config files
    if use_sysargs:
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
    if len(args_) > 1:                 # Just one argument, but more given
        raise TypeError(
            f'run() takes 1 positional argument, but {len(args_)} were given')
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
