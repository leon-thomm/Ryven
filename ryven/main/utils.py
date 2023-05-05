import os
from os.path import normpath, join, dirname, abspath, basename, expanduser
import pathlib
import importlib.util
from typing import List, Tuple, Type, Union, Optional, Set

from ryven.main.nodes_package import NodesPackage
from ryvencore import Node, Data


def load_from_file(file: str = None, components_list: [str] = None) -> tuple:
    """
    Imports specified components from a python module with given file path.
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


def import_nodes_package(package: NodesPackage = None, directory: str = None) -> \
        Tuple[List[Type[Node]], List[Type[Data]]]:
    """Loads nodes from a Ryven nodes package and returns them in a list.

    Can be used without a running Ryven instance, but you need to specify in which mode nodes should be loaded
    by setting the environment variable RYVEN_MODE to either 'gui' (gui imports enabled) or 'no-gui'.

    :param package: The NodesPackage object.
    :param directory: The path to the directory where the nodes.py file is located, used if package is None.
    :return: A tuple containing node types (classes) first, and the data types exported by the package second.
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

    node_types = node_env.NodesEnvRegistry.exported_nodes[-1]
    data_types = node_env.NodesEnvRegistry.exported_data_types[-1]

    return node_types, data_types


def read_project(project_path: Union[str, pathlib.Path]) -> dict:
    """Read the project file and return its dictionary.

    :param project_path: The path to the project file.
    :return: The contents of the project file.
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


def find_project(project_path: Union[str, pathlib.Path]) -> Optional[pathlib.Path]:
    """Resolves a possibly *~/.ryven/saves/*-relative path to a nodes package to an absolute path.

    :param project_path: The path to the project file or the subpath to :code:`ryven_dir_path()/saves`.
        The file extension '.json' can be omitted.
    :return: The absolute and resolved path to the project file, or `None` if it could not be found.

    """
    project_path = pathlib.Path(project_path)

    if project_path.exists():
        return project_path.resolve()
    elif project_path.with_suffix('.json').exists():
        return project_path.with_suffix('.json').resolve()
    else:
        project_path = pathlib.Path(ryven_dir_path(), 'saves', project_path)
        if project_path.exists():
            return project_path.resolve()
        elif project_path.with_suffix('.json').exists():
            return project_path.with_suffix('.json').resolve()
        else:
            return None


def find_config_file(cfg_file_path: str) -> Optional[pathlib.Path]:
    """Resolves a possibly *~/.ryven/*-relative path of a config file to an absolute path.

    :param cfg_file_path: Either an absolute path, or relative to the *~/.ryven/* directory.
        The file extension '.cfg' can be omitted.
    :return: The full path to the config file or `None`, if it could not be found.
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


def process_nodes_packages(
    project_or_nodes: Union[
        Union[str, pathlib.Path],                       # path to Ryven project
        List[Union[str, pathlib.Path, NodesPackage]]    # list of node packages
    ],
    requested_packages: List[NodesPackage] = None
) -> Tuple[Set[NodesPackage], List[pathlib.Path], Optional[dict]]:
    """Takes a project or list of node packages and additionally requested node
    packages and checks whether the node packages are valid.

    It also removes duplicates based on the name (and not the contents!).

    :param project_or_nodes:
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
    :param requested_packages:
        A list of additional node package, which were requested. These take
        precedence over `nodes`.
        The default is `[]`.

    :return:
        A tuple of three elements:
            - Set of available nodes required by the project or from list of nodes.
            - Set of nodes required by the project or from list of nodes, which could not be found.
            - Dictionary with the contents of the project or `None`.
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
