# prevent circular imports
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ryven.main.packages.nodes_package import NodesPackage

import os
from os.path import basename, normpath
from typing import Type, Tuple, List, Optional, Dict

from ryven.main.utils import in_gui_mode, load_from_file

from ryvencore import Node, NodeInputType, NodeOutputType, Data, serialize, deserialize


def init_node_env():
    # Note 1:
    #   Because the wrapper classes were removed from ryvencore-qt recently, we don't need to import from
    #   difference ryvencore sources here anymore depending on the mode, ryvencore stuff comes from ryvencore
    #   directly now.

    # Note 2:
    #   I removed the NodeWrp class, which just added the actions dict to the Node base class, because it
    #   should be moved to ryvencore soon.

    # Note 3:
    #   I removed dtypes imports, they are currently not supported and are expected to become a new add-on
    #   some time in the future.

    # Note 4:
    #   I removed the import of NodeBase, because it's messy to override the Node class in the first place.

    if os.environ['RYVEN_MODE'] == 'gui':
        import ryvencore_qt


def import_guis(origin_file: str, gui_file_name='gui.py'):
    raise Exception(
        'The function import_guis is deprecated and should not be used anymore. '
        'Please use the on_gui_load decorator instead. '
        'See the example nodes packages that Ryven comes with for reference. '
    )


class NodesEnvRegistry:
    """
    Statically stores custom `ryvencore.Node` and `ryvencore.Data` subclasses
    exported via export_nodes on import of a nodes package.
    After running the imported nodes.py module (which needs to call
    `export_nodes()` to run), Ryven can then retrieve the exported types from
    this class.
    """

    # stores, for each nodes package or subpackage a tuple of exported node types and data
    exported_package_metadata: Dict[str, Tuple[List[Type[Node]], List[Type[Data]]]] = {}
    # the last exported package to be consumed for loading
    last_exported_package: List[Tuple[List[Type[Node]], List[Type[Data]]]] = []

    # stores, for each nodes package separately, a list of exported node types
    exported_nodes_legacy: List[List[Type[Node]]] = []

    # stores, for each nodes package separately, a list of exported data types
    exported_data_types_legacy: List[List[Type[Data]]] = []

    # stores the package that is currently being imported; set by the nodes package
    # loader ryven.main.packages.nodes_package.import_nodes_package;
    # needed for extending the identifiers of node types to include the package name
    current_package: Optional[NodesPackage] = None

    @classmethod
    def current_package_id(cls):
        if cls.current_package is None:
            raise Exception(
                f'Unexpected nodes export. '
                f'Nodes export is only allowed when the nodes package is imported. '
            )
        return cls.current_package.name

    @classmethod
    def consume_last_exported_package(cls) -> Tuple[List[Type[Node]], List[Type[Data]]]:
        """
        Returns and forgets the content of the last call to `export_nodes`.
        """
        result: Tuple[List[Type[Node]], List[Type[Data]]] = ([], [])
        node_types, data_types = result
        for nodes, data in cls.last_exported_package:
            node_types.extend(nodes)
            data_types.extend(data)
        cls.last_exported_package.clear()
        return result


def export_nodes(
    node_types: List[Type[Node]], 
    data_types: Optional[List[Type[Data]]] = None,
    sub_pkg_name: Optional[str] = None
):
    """
    Exports/exposes the specified nodes to Ryven for use in flows. Nodes will have the same identifier, since they come as a package.
    This function will fail if the NodesEnvRegistry package is not set.
    """

    if data_types is None:
        data_types = []

    pkg_name: str = NodesEnvRegistry.current_package_id()
    if sub_pkg_name is not None:
        full_pkg_name = f"{pkg_name}.{sub_pkg_name}"
    else:
        full_pkg_name = pkg_name
    
    # extend identifiers of node types to include the package name
    for n_cls in node_types:
        if not hasattr(n_cls, 'identifier') or n_cls.identifier is None:
            n_cls._build_identifier()

        # fallbacks for older versions
        n_cls.legacy_identifiers = [
            *n_cls.legacy_identifiers,
            n_cls.identifier,
            f"{pkg_name}.{n_cls.identifier}",
        ]
    
        # store the package id as identifier prefix, which will be added
        # by ryvencore when registering the node type
        n_cls.identifier_prefix = full_pkg_name

    # same for data types
    for d_cls in data_types:
        d_cls.identifier = f'{full_pkg_name}.{d_cls.identifier}'

    NodesEnvRegistry.exported_nodes_legacy.append(node_types)
    NodesEnvRegistry.exported_data_types_legacy.append(data_types)

    nodes_datas = (node_types, data_types)
    NodesEnvRegistry.exported_package_metadata[full_pkg_name] = nodes_datas
    NodesEnvRegistry.last_exported_package.append(nodes_datas)


__gui_loaders: list = []


def on_gui_load(func):
    """
    Use this decorator to register a function which imports all gui
    modules of the nodes package.
    Do not import any gui modules outside of this function.
    When Ryven is running in headless mode, this function will not
    be called, and your nodes package should function without any.

    Example `nodes.py`:
    ```
    from ryven.node_env import *

    # <node types> definitions
    # <data types> definitions

    export_nodes(<node types>, <data types>)

    @on_gui_load
    def load_guis():
        import .gui
    ```
    """
    __gui_loaders.append(func)


def load_current_guis():
    """
    Calls the functions registered via `~ryven.main.gui_env.on_gui_load`.
    """
    if not in_gui_mode():
        return
    for func in __gui_loaders:
        func()
    __gui_loaders.clear()
