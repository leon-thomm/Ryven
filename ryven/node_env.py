"""This module automatically imports all requirements for custom nodes.
It should lie in the same location as Ryven.py so it can get imported directly from the custom sources
without path modifications which caused issues in the past."""

import inspect
import sys
import os

from ryven.main.utils import load_from_file

from ryvencore import \
    Node, NodeInputType, NodeOutputType, Data


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

# ------------------------------------------------------


class NodesRegistry:
    """
    Statically stores the nodes exported via export_nodes on import of a nodes package.
    After running the imported nodes.py module (which causes export_nodes() to run),
    Ryven can find the exported nodes in exported_nodes.
    """
    exported_nodes: [[Node]] = []
    exported_node_sources: [[str]] = []


def export_nodes(*args):
    """
    Exports/exposes the specified nodes to Ryven for use in flows.
    """

    if not isinstance(args, tuple):
        if issubclass(args, Node):
            nodes = tuple(args)
        else:
            return
    else:
        nodes = list(args)

    NodesRegistry.exported_nodes.append(nodes)

    # get sources
    node_sources = [inspect.getsource(n) for n in nodes]
    NodesRegistry.exported_node_sources.append(node_sources)


# ------------------------------------------------------
