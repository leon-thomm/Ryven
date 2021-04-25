"""This file automatically imports all requirements for custom nodes.
It should lie in the same location as Ryven.py so it can get imported directly from the custom sources."""
import sys
import os

# dependent on gui mode:
Node, NodeInputBP, NodeOutputBP, dtypes = None, None, None, None

if os.environ['RYVEN_MODE'] == 'gui':
    from ryvencore_qt import NodeInputBP as _NodeInputBP, NodeOutputBP as _NodeOutputBP, dtypes as _dtypes
    from nodes.NodeBase import NodeBase as _Node

    Node, NodeInputBP, NodeOutputBP, dtypes = _Node, _NodeInputBP, _NodeOutputBP, _dtypes
else:
    # import sources directly from backend if not running in gui mode
    from ryvencore_qt.src.ryvencore import Node as _Node, NodeInputBP as _NodeInputBP, NodeOutputBP as _NodeOutputBP, \
        dtypes as _dtypes

    Node, NodeInputBP, NodeOutputBP, dtypes = _Node, _NodeInputBP, _NodeOutputBP, _dtypes


from tools import load_from_file
from inspect import stack


def import_widgets(origin_file: str, rel_file_path='widgets.py'):

    caller_location = os.path.dirname(origin_file)

    # alternative solution without __file__ argument; does not work with debugging, so it's not the best idea
    #   caller_location = os.path.dirname(stack()[1].filename)  # getting caller file path from stack frame

    abs_path = os.path.join(caller_location, rel_file_path)
    # origin_dir = os.path.dirname(abs_path)
    # rem = origin_dir not in sys.path
    # sys.path.append(origin_dir)

    if os.environ.get('RYVEN_MODE') == 'gui':

        # import the widgets module
        load_from_file(abs_path)

        # in GUI mode, import the widgets container from NWENV containing all the exported widget classes
        import NWENV
        widgets_container = NWENV.WidgetsRegistry.exported_widgets[-1]

    else:
        # in non-gui mode, return an object that just returns None for all accessed attributes
        # so widgets.MyWidget in the nodes file just returns None then
        class PlaceholderWidgetsContainer:
            def __getattr__(self, item):
                return None
        widgets_container = PlaceholderWidgetsContainer()

    # if rem:
    #     sys.path.remove(origin_dir)

    return widgets_container


# def load_from_file(file: str, caller_file, components_list: [str], gui=False):
#     if os.environ['RYVEN_MODE'] == 'gui' or not gui:
#         comps = _load_from_file(file, caller_file, components_list)
#     else:
#         comps = tuple([None for i in range(len(components_list))])
#
#     return comps


# ------------------------------------------------------


class NodesRegistry:
    exported_nodes: [[Node]] = []


def export_nodes(*args):
    NodesRegistry.exported_nodes.append(list(args))


# ------------------------------------------------------
