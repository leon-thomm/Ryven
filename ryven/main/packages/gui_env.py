"""
This module automatically imports all requirements for Gui definitions of a nodes package.
"""

import inspect
from typing import Type

import ryven.gui.std_input_widgets as inp_widgets

from ryvencore_qt import \
    NodeInputWidget, NodeMainWidget, NodeGUI

from ryvencore import Data, Node, serialize, deserialize

def init_node_guis_env():
    pass


class GuiClassesRegistry:
    """
    Used for statically keeping the gui classes specified in export_guis to access them through node_env.import_guis().
    """
    exported_guis = []
    exported_guis_sources: [[str]] = []


class GuiClassesContainer:
    pass


def export_guis(guis: [Type[NodeGUI]]):
    """
    Exports/exposes the specified node gui classes to the nodes file importing them via import_guis().
    Returns an object with all exported gui classes as attributes for direct access.
    """

    gcc = GuiClassesContainer()
    for w in guis:
        setattr(gcc, w.__name__, w)
    GuiClassesRegistry.exported_guis.append(gcc)

    # get sources
    gui_sources = [inspect.getsource(g) for g in guis]
    GuiClassesRegistry.exported_guis_sources.append(gui_sources)
