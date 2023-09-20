"""
This module automatically imports all requirements for custom nodes.
"""

import os
from typing import Type

from ryven.main.packages.nodes_package import load_from_file, NodesPackage

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
    """
    Import all exported GUI classes from gui_file_name with respect to the origin_file location.
    Returns an object with all exported gui classes as attributes for direct access.
    """

    caller_location = os.path.dirname(origin_file)

    # alternative solution without __file__ argument; does not work with debugging, so it's not the best idea
    #   caller_location = os.path.dirname(stack()[1].filename)  # getting caller file path from stack frame

    abs_path = os.path.join(caller_location, gui_file_name)

    if os.environ['RYVEN_MODE'] == 'gui':

        # import the gui module
        load_from_file(abs_path)

        # in GUI mode, import the gui classes container from gui_env containing all the exported gui classes
        from ryven import gui_env
        gui_classes_container = gui_env.GuiClassesRegistry.exported_guis[-1]

    else:
        # in non-gui mode, return an object that just returns None for all accessed attributes
        # so guis.MyGUI in the nodes file just returns None then
        class PlaceholderGuisContainer:
            def __getattr__(self, item):
                return None
        gui_classes_container = PlaceholderGuisContainer()

    return gui_classes_container


class NodesEnvRegistry:
    """
    Statically stores custom `ryvencore.Node` and `ryvencore.Data` subclasses
    exported via export_nodes on import of a nodes package.
    After running the imported nodes.py module (which needs to call
    `export_nodes()` to run), Ryven can then retrieve the exported types from
    this class.
    """

    # stores, for each nodes package separately, a list of exported node types
    exported_nodes: [[Type[Node]]] = []

    # stores, for each nodes package separately, a list of exported data types
    exported_data_types: [[Type[Data]]] = []

    # stores the package that is currently being imported; set by the nodes package
    # loader ryven.main.packages.nodes_package.import_nodes_package;
    # needed for extending the identifiers of node types to include the package name
    current_package: NodesPackage = None


def export_nodes(node_types: [Type[Node]], data_types: [Type[Data]] = None):
    """
    Exports/exposes the specified nodes to Ryven for use in flows.
    """

    if data_types is None:
        data_types = []

    # extend identifiers of node types to include the package name
    for node_type in node_types:
        # store the package name as identifier prefix, which will be added
        # by ryvencore when registering the node type
        node_type.identifier_prefix = NodesEnvRegistry.current_package.name

        # also add the identifier without the prefix as fallback for older versions
        node_type.legacy_identifiers = [
            *node_type.legacy_identifiers,
            node_type.identifier if node_type.identifier else node_type.__name__
        ]

    NodesEnvRegistry.exported_nodes.append(node_types)
    NodesEnvRegistry.exported_data_types.append(data_types)

    if os.environ['RYVEN_MODE'] == 'gui':
        # store node sources for code inspection
        from ryven.gui.code_editor.codes_storage import register_node_type
        for node_type in node_types:
            register_node_type(node_type)
