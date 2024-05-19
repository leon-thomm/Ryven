"""
This module, together with the node_env and gui_env defines Ryven's nodes
package system. It can be used outside of Ryven as well.
"""

import importlib.util
import os, sys
import pathlib
from os.path import basename, dirname, splitext, normpath, join
from typing import Tuple, List, Type, Union, Set, Optional, Dict
import pkgutil

from ryvencore import Node, Data

from ryven.main.utils import (
    read_project, 
    ryven_dir_path, 
    abs_path_from_package_dir, 
    in_gui_mode,
    load_from_file,
)
from ryven.main.packages.node_env import load_current_guis

class NodesPackage:
    """
    A small container to store meta data about imported node packages.
    """

    def __init__(self, directory: str):
        self.name = basename(normpath(directory))
        self.directory = directory

        self.file_path = normpath(join(directory, 'nodes.py'))

    def __str__(self):
        return f'{self.__class__.__name__}({self.name})'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.directory})'

    def __eq__(self, other):
        if isinstance(other, NodesPackage):
            return self.name == other.name
        else:
            return self.name == str(other)

    def __hash__(self):
        return hash(self.name)

    def config_data(self):
        return {
            'name': self.name,
            'dir': self.directory,
        }


# should be Tuple[list[Type[Node]], list[Type[Data]] in 3.9+
def import_nodes_package(
    package: Optional[NodesPackage] = None, directory: Optional[str] = None
) -> Tuple[List[Type[Node]], List[Type[Data]]]:
    """Loads node and data classes from a Ryven nodes package and returns both in separate lists.

    Can be used without a running Ryven instance, but you need to specify in which mode nodes should be loaded
    by setting the environment variable RYVEN_MODE to either 'gui' (gui imports enabled) or 'no-gui'.

    :param package: The NodesPackage object.
    :param directory: The path to the directory where the nodes.py file is located, used if package is None.
    :return: A tuple containing node types (classes) first, and the data types exported by the package second.
    """

    if package is None:
        assert directory is not None, 'Either package or directory must be specified.'
        package = NodesPackage(directory)

    if 'RYVEN_MODE' not in os.environ:
        raise Exception(
            """Please specify the environment variable RYVEN_MODE ('gui' or 'no-gui') before loading any packages. 
            For example, set os.environ['RYVEN_MODE'] = 'no-gui' for gui-less deployment.
            Ryven and RyvenConsole should do this automatically.
            """
        )

    from ryven import node_env

    node_env.NodesEnvRegistry.current_package = package
    load_from_file(package.file_path)

    # load guis
    if in_gui_mode():
        load_current_guis()
    
    node_types, data_types = node_env.NodesEnvRegistry.consume_last_exported_package()
    
    # load source codes
    if in_gui_mode():
        from ryven.gui.code_editor.codes_storage import register_node_type
        for node_type in node_types:
            register_node_type(node_type)
    
    return node_types, data_types

def process_nodes_packages(
    project_or_nodes: Union[
        Union[str, pathlib.Path],  # path to Ryven project
        List[Union[str, pathlib.Path, NodesPackage]],  # list of node packages
    ],
    requested_packages: Optional[List[NodesPackage]] = None,
) -> Tuple[Set[NodesPackage], Set[pathlib.Path], Optional[Dict]]:
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
    # from ryven.main.packages.nodes_package import NodesPackage

    if requested_packages is None:
        requested_packages = []

    pkgs: Set[NodesPackage] = set()
    pkgs_not_found: Set[pathlib.Path] = set()
    project_dict: Optional[Dict]

    # Find nodes in the project file
    if isinstance(project_or_nodes, (str, pathlib.Path)):
        project_dict = read_project(project_or_nodes)
        node_pkg_paths = [p['dir'] for p in project_dict['required packages']]
    else:
        project_dict = None
        node_pkg_paths = project_or_nodes

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
    pkgs_not_found = set(
        pkg_path for pkg_path in pkgs_not_found if pkg_path.name not in args_pkgs_names
    )

    return pkgs, pkgs_not_found, project_dict
