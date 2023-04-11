import inspect
import os
import pathlib
from os.path import normpath, join, dirname, abspath, basename, expanduser
import importlib.util

from ryven.main.nodes_package import NodesPackage


def load_from_file(file: str = None, components_list: [str] = None) -> tuple:
    """
    Imports the specified components from a python module with given file path.
    """
    if components_list is None:
        components_list = []

    name = basename(file).split('.')[0]
    spec = importlib.util.spec_from_file_location(name, file)

    importlib.util.module_from_spec(spec)

    mod = spec.loader.load_module(name)
    # using load_module(name) instead of exec_module(mod) here,
    # because exec_module() somehow then registers it as "built-in"
    # which is wrong and prevents inspect from parsing the source

    comps = tuple([getattr(mod, c) for c in components_list])

    return comps


def import_nodes_package(package: NodesPackage = None, directory: str = None) -> list:
    """
    This function is an interface to the node packages system in Ryven.
    It loads nodes from a Ryven nodes package and returns them in a list.
    It can be used without a running Ryven instance, but you need to specify in which mode nodes should be loaded
    by setting the environment variable RYVEN_MODE to either 'gui' (gui imports enabled) or 'no-gui'.
    You can either pass a NodesPackage object or a path to the directory where the nodes.py file is located.
    """

    if package is None:
        package = NodesPackage(directory)

    if 'RYVEN_MODE' not in os.environ:
        raise Exception(
            "Please specify the environment variable RYVEN_MODE ('gui' or 'no-gui') before loading any packages. "
            "For example set os.environ['RYVEN_MODE'] = 'no-gui' for gui-less deployment."
        )

    from ryven import node_env
    load_from_file(package.file_path)

    node_types = node_env.NodesRegistry.exported_nodes[-1]

    return node_types


def read_project(project_path):
    """Read the project file and return its dictionary.

    Parameters
    ----------
    project_path : str|pathlib.Path
        The path to the project file.

    Returns
    -------
    dict
        The contents of the project file.

    """
    import io
    import json

    if isinstance(project_path, io.TextIOWrapper):
        project_dict = json.loads(project_path.read(), strict=False)
    else:
        with open(project_path) as f:
            import json
            # strict=False is needed to allow 'control characters' like '\n'
            # for newline when loading the json
            project_dict = json.load(f, strict=False)

    return project_dict


def find_project(project_path):
    """Find a project.

    The `project_path` is either the path to the project file (with or without
    the suffix '.json') or a path below `ryven_dir_path()/saves/`.

    Parameters
    ----------
    project_path : str|pathlib.Path
        The path to the project file or the subpath to `ryven_dir_path()/saves`.

    Returns
    -------
    pathlib.Path|None
        The full path to the project file or `None`, if it could not be found.

    """
    project_path = pathlib.Path(project_path)

    if project_path.exists():
        return project_path
    elif project_path.with_suffix('.json').exists():
        return project_path.with_suffix('.json')
    else:
        project_path = pathlib.Path(ryven_dir_path(), 'saves', project_path)
        if project_path.exists():
            return project_path
        elif project_path.with_suffix('.json').exists():
            return project_path.with_suffix('.json')
        else:
            return None


def find_config_file(cfg_file_path):
    """Find a config file.

    Parameters
    ----------
    cfg_file_path : str
        Either an absolute path, or relative to the ~/.ryven/ directory.
        The file extension '.cfg' can be omitted.

    Returns
    -------
    pathlib.Path|None
        The full path to the config file or `None`, if it could not be found.
    """

    config_file_path = pathlib.Path(cfg_file_path)

    if config_file_path.exists():
        return config_file_path
    else:
        config_file_path = pathlib.Path(ryven_dir_path(), cfg_file_path)
        if config_file_path.exists():
            return config_file_path
        else:
            return None


def process_nodes_packages(project_or_nodes, requested_packages: list = None):
    """Takes a project or list of node packages and additionally requested node
    packages and checks whether the node packages are valid.

    It also removes duplicates based on the name (and not the contents!).

    Parameters
    ----------
    project_or_nodes : str|pathlib.Path|list of (str|pathlib.Path|NodesPackage)
        Either a path to a Ryven project or a list of node packages.
        If a Ryven project is given, the required nodes packages specified
        in the project file are looked for.
        If a list is given, `NodesPackage` instances are  copied into the
        resulting list; paths are considered to direct to 'nodes.py'.
        If 'nodes.py' is found in the path,
        a `NodesPackage` instance is created and added to the resulting list.
        If 'nodes.py' cannot be found in the path, the package is searched in
        Ryven's example nodes dir, e.g. if "std" is given and not found
        locally, the "std" package included in Ryven is loaded.
    requested_packages : list of NodesPackage
        A list of additional node package, which were requested. These take
        precedence over `nodes`.
        The default is `[]`.

    Returns
    -------
    set of NodesPackage
        Set of available nodes required by the project or from list of nodes.
    set of NodesPackage
        Set of nodes required by the project or from list of nodes, which could
        not be found.
    dict
        Dictionary with the contents of the project or `None`.

    """
    from ryven.main.nodes_package import NodesPackage

    if requested_packages is None:
        requested_packages = []

    # Find nodes in the project file
    try:
        project_dict = read_project(project_or_nodes)
        node_pkg_paths = [p['dir'] for p in project_dict['required packages']]
    except TypeError:
        project_dict = None
        node_pkg_paths = project_or_nodes
    except KeyError:
        # No required packages found
        project_dict = None
        node_pkg_paths = []

    pkgs = set()
    pkgs_not_found = set()
    for pkg in node_pkg_paths:
        if isinstance(pkg, NodesPackage):
            pkgs.add(pkg)
        else:
            # For backward compatibility we have to deal with Windows and Posix
            # paths in the project's file
            pkg_windows_path = pathlib.PureWindowsPath(pkg)
            pkg_posix_path = pathlib.PurePosixPath(pkg)
            if len(pkg_windows_path.parts) > len(pkg_posix_path.parts):
                pkg_path = pathlib.Path(pkg_windows_path)
            else:
                pkg_path = pathlib.Path(pkg_posix_path)
            if pkg_path.joinpath('nodes.py').exists():
                pkgs.add(NodesPackage(str(pkg_path)))
                continue

            # Try to find the nodes package in Ryven's custom nodes dir
            pkg_custom_path = pathlib.Path(ryven_dir_path(), 'nodes', pkg)
            if pkg_custom_path.joinpath('nodes.py').exists():
                pkgs.add(NodesPackage(str(pkg_custom_path)))
                continue

            # Try to find in Ryven's example nodes
            pkg_example_path = pathlib.Path(abs_path_from_package_dir('example_nodes'), pkg)
            if pkg_example_path.joinpath('nodes.py').exists():
                pkgs.add(NodesPackage(str(pkg_example_path)))
                continue

            # Package could not be found
            pkgs_not_found.add(pkg_path)

    # Check, if nodes which could not be found are already available in
    # `requested_nodes`.
    # This check is done by comparing the path name to the nodes' names
    args_pkgs_names = [pkg.name for pkg in requested_packages]
    pkgs_not_found = [
        pkg_path
        for pkg_path in pkgs_not_found
        if pkg_path.name not in args_pkgs_names]

    return pkgs, pkgs_not_found, project_dict


def ryven_dir_path() -> str:
    """
    :return: absolute path the (OS-specific) '~/.ryven/' folder
    """
    return normpath(join(expanduser('~'), '.ryven/'))


def abs_path_from_package_dir(path_rel_to_ryven: str):
    """Given a path string relative to the ryven package, return the file/folder absolute path

    :param path_rel_to_ryven: path relative to ryven package (e.g. main/node_env.py)
    :type path_rel_to_ryven: str
    """
    ryven_path = dirname(dirname(__file__))
    return abspath(join(ryven_path, path_rel_to_ryven))


def abs_path_from_ryven_dir(path_rel_to_ryven_dir: str):
    """Given a path string relative to the ryven dir '~/.ryven/', return the file/folder absolute path

    :param path_rel_to_ryven_dir: path relative to ryven dir (e.g. saves)
    :return: file/folder absolute path
    """

    return abspath(join(ryven_dir_path(), path_rel_to_ryven_dir))
