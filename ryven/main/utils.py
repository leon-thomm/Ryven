import inspect
import os
import pathlib
from os.path import normpath, join, dirname, abspath, basename, expanduser
import importlib.util

from ryven.main.nodes_package import NodesPackage


def load_from_file(file: str = None, components_list: [str] = []) -> tuple:
    """
    Imports the specified components from a python module with given file path.
    """

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

    from ryven import NENV
    load_from_file(package.file_path)

    nodes = NENV.NodesRegistry.exported_nodes[-1]

    if os.environ['RYVEN_MODE'] == 'gui':

        # ADD SOURCES

        # because all the node package modules are named 'nodes.py' now, we need to retrieve the sources via inspect here
        # since inspect will be unable to do so once we imported another 'nodes' module.

        node_cls_sources = NENV.NodesRegistry.exported_node_sources[-1]
        node_mod_sources = [inspect.getsource(inspect.getmodule(n)) for n in nodes]

        for i in range(len(nodes)):
            n = nodes[i]

            mw_cls_src = inspect.getsource(n.main_widget_class) if n.main_widget_class else None
            mw_mod_src = inspect.getsource(inspect.getmodule(n.main_widget_class)) if n.main_widget_class else None

            n.__class_codes__ = {
                'node cls': node_cls_sources[i],
                'node mod': node_mod_sources[i],
                'main widget cls': mw_cls_src,
                'main widget mod': mw_mod_src,
                'custom input widgets': {
                    name: {
                        'cls': inspect.getsource(inp_cls),
                        'mod': inspect.getsource(inspect.getmodule(inp_cls))
                    } for name, inp_cls in n.input_widget_classes.items()
                }
            }

    # -----------

    # add package name to identifiers and define custom types

    for n in nodes:
        n.identifier_prefix = package.name  #  + '.' + (n.identifier if n.identifier else n.__name__)
        n.type_ = package.name if not n.type_ else f'{package.name}[{n.type_}]'

    return nodes


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


def process_nodes_packages(project_or_nodes, requested_nodes=[]):
    """Takes a project or list of node packages and additionally requested node
    packages and checks whether the node packages are valid.

    It also removes duplicates based on the name (and not the contents!).

    Parameters
    ----------
    project_or_nodes : str|pathlib.Path|list of (str|pathlib.Path|NodesPackage)
        Either a path to a Ryven project or a list of nodes.
        If a Ryven project is given, the required nodes packages specified
        in the project file are looked for.
        If a list is given, `NodesPackage` instances are  copied into the
        resulting list; paths are considered to direct to 'nodes.py'.
        If 'nodes.py' is found in the path,
        a `NodesPackage` instance is created and added to the resulting list.
        If 'nodes.py' cannot be found in the path, the package is searched in
        Ryven's example nodes dir, e.g. if "std" is given and not found
        locally, the "std" package included in Ryven is loaded.
    requested_nodes : list of NodesPackage
        A list of additional node package, which were requested. These take
        precedence over `nodes`.
        The default is `[]`.

    Returns
    -------
    set of NodesPackage
        Set of available nodes required by the project or from list of nodes.
    set of NodesPackage
        Set of nodes required by the project or from list of nodes, which could
        no be found.
    dict
        Dictionary with the contents of the project or `None`.

    """
    from ryven.main.nodes_package import NodesPackage

    # Find nodes in the project file
    try:
        project_dict = read_project(project_or_nodes)
        nodes = [p['dir'] for p in project_dict['required packages']]
    except TypeError:
        project_dict = None
        nodes = project_or_nodes

    node_packages = set()
    nodes_not_found = set()
    for node in nodes:
        if isinstance(node, NodesPackage):
            node_packages.add(node)
        else:
            # For backward compatibility we have to deal with Windows and Posix
            # paths in the project's file
            node_windows_path = pathlib.PureWindowsPath(node)
            node_posix_path = pathlib.PurePosixPath(node)
            if len(node_windows_path.parts) > len(node_posix_path.parts):
                node_path = pathlib.Path(node_windows_path)
            else:
                node_path = pathlib.Path(node_posix_path)
            if node_path.joinpath('nodes.py').exists():
                node_packages.add(NodesPackage(str(node_path)))
                continue

            # Try to find the nodes package in Ryven's custom nodes dir
            node_custom_path = pathlib.Path(ryven_dir_path(), 'nodes', node)
            if node_custom_path.joinpath('nodes.py').exists():
                node_packages.add(NodesPackage(str(node_custom_path)))
                continue

            # Try to find in Ryven's example nodes
            node_example_path = pathlib.Path(abs_path_from_package_dir('example_nodes'), node)
            if node_example_path.joinpath('nodes.py').exists():
                node_packages.add(NodesPackage(str(node_example_path)))
                continue

            # Package could not be found
            nodes_not_found.add(node_path)

    # Check, if nodes which could not be found are already available in
    # `requested_nodes`.
    # This check is done by comparing the path name to the nodes' names
    args_nodes_names = [node.name for node in requested_nodes]
    nodes_not_found = [
        node_path
        for node_path in nodes_not_found
        if node_path.name not in args_nodes_names]

    return node_packages, nodes_not_found, project_dict


def ryven_dir_path() -> str:
    """
    :return: absolute path the (OS-specific) '~/.ryven/' folder
    """
    return normpath(join(expanduser('~'), '.ryven/'))


def abs_path_from_package_dir(path_rel_to_ryven: str):
    """Given a path string relative to the ryven package, return the file/folder absolute path

    :param path_rel_to_ryven: path relative to ryven package (e.g. main/NENV.py)
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
