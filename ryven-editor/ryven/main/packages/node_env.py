"""
This module automatically imports all requirements for custom nodes.
"""

import os
from os.path import basename, normpath
from typing import Type

from ryven.main.packages.nodes_package import load_from_file, NodesPackage

from ryvencore import Node, NodeInputType, NodeOutputType, Data, serialize, deserialize

import inspect

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
    # stores, for each nodes package or subpackage a tuple of exported node types and data
    exported_package_metadata: dict[str, tuple[list[Type[Node]], list[Type[Node]]]] = {}
    # the last exported package to be consumed for loading
    last_exported_package: list[tuple[list[Type[Node]], list[Type[Node]]]] = []
    
    # stores, for each nodes package separately, a list of exported node types
    exported_nodes_legacy: [[Type[Node]]] = []

    # stores, for each nodes package separately, a list of exported data types
    exported_data_types_legacy: [[Type[Data]]] = []

    # stores the package that is currently being imported; set by the nodes package
    # loader ryven.main.packages.nodes_package.import_nodes_package;
    # needed for extending the identifiers of node types to include the package name
    current_package: NodesPackage = None
    
    #set by export_sub_package, used in export_nodes
    current_sub_package:str = None
    
    @classmethod
    def current_package_id(cls):
        if cls.current_package is None:
            return
        return cls.current_package.name if cls.current_sub_package is None else f"{cls.current_package.name}.{cls.current_sub_package}"
    
    @classmethod
    def consume_last_exported_package(cls) -> tuple[list[Type[Node]], list[Type[Node]]]:
        result:tuple[list[Type[Node]], list[Type[Node]]] = ([], [])
        r_nodes, d_nodes = result
        for nodes, data in cls.last_exported_package:
            for n in nodes:
                r_nodes.append(n)
            for d in data:
                d_nodes.append(d)
        cls.last_exported_package.clear()
        return result

def export_nodes(node_types: [Type[Node]], data_types: [Type[Data]] = None):
    """
    Exports/exposes the specified nodes to Ryven for use in flows. Nodes will have the same identifier, since they come as a package.
    This function will fail if the NodesEnvRegistry package is not set.
    """

    if data_types is None:
        data_types = []

    pkg_name = NodesEnvRegistry.current_package_id()
    # extend identifiers of node types to include the package name
    for node_type in node_types:
        # store the package id as identifier prefix, which will be added
        # by ryvencore when registering the node type
        node_type.identifier_prefix = pkg_name
        
        # also add the identifier without the prefix as fallback for older versions
        node_type.legacy_identifiers = [
            *node_type.legacy_identifiers,
            node_type.identifier if node_type.identifier else node_type.__name__
        ]

    NodesEnvRegistry.exported_nodes_legacy.append(node_types)
    NodesEnvRegistry.exported_data_types_legacy.append(data_types)
    
    metadata = NodesEnvRegistry.exported_package_metadata
    nodes_datas = (node_types, data_types)
    metadata[pkg_name] = nodes_datas
    NodesEnvRegistry.last_exported_package.append(nodes_datas)

    if os.environ['RYVEN_MODE'] == 'gui':
        # store node sources for code inspection
        from ryven.gui.code_editor.codes_storage import register_node_type
        for node_type in node_types:
            register_node_type(node_type)

def export_sub_nodes(origin_file:str, node_types: [Type[Node]], data_types: [Type[Data]] = None, sub_pkg_name:str = None):
    """
    Exports / exposes nodes to Ryven as a subpackage of the currently loaded package for use in flows.
    Do not call this function in a node package's nodes.py file, call export_nodes instead.
    """
    
    #Fetch the module name
    if sub_pkg_name == None:
        head, tail = os.path.split(origin_file)
        if tail != "nodes.py":
            sub_pkg_name = tail.removeprefix(".py")
        else:
            sub_pkg_name = os.path.split(head)[1]
    
    #Apply the subpackage name
    NodesEnvRegistry.current_sub_package = sub_pkg_name
    export_nodes(node_types, data_types)
    NodesEnvRegistry.current_sub_package = None