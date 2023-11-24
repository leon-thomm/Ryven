"""
This module automatically imports all requirements for Gui definitions of a nodes package.
"""

import inspect
from typing import Type

import ryven.gui.std_input_widgets as inp_widgets

from ryvencore_qt import NodeInputWidget, NodeMainWidget, NodeGUI

from ryvencore import Data, Node, serialize, deserialize
from ryvencore.InfoMsgs import InfoMsgs
from ryven.main.utils import in_gui_mode

__gui_loaders: list = []
__explicit_nodes: set = set() # for protection against setting the gui twice on the same node

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


def load_current_guis():
    """
    Calls the functions registered via `~ryven.main.gui_env.on_gui_load`.
    """
    if not in_gui_mode():
        return
    for func in __gui_loaders:
        func()
    __gui_loaders.clear()


def on_gui_load(func):
    """
    Defers a parameterless function to be called for package loading when
    the GUIs are loaded.
    """
    if in_gui_mode():
        __gui_loaders.append(func)


def node_gui(node_cls: Type[Node]):
    """
    Registers a node widget as the GUI for a specific node.
    """
    if not issubclass(node_cls, Node):
        raise Exception(f"{node_cls} is not of type {Node}")

    def register_gui(gui_cls: Type[NodeGUI]):
        if node_cls in __explicit_nodes:
            InfoMsgs.write(f'{node_cls.__name__} has defined an explicit gui {node_cls.GUI.__name__}')
            return
        
        node_cls.GUI = gui_cls
        __explicit_nodes.add(node_cls)
        InfoMsgs.write(f"Registered node gui: {node_cls} for {gui_cls}")
        # legacy
        GuiClassesRegistry.exported_guis.append(gui_cls)
        GuiClassesRegistry.exported_guis_sources.append(inspect.getsource(gui_cls))
        return gui_cls

    return register_gui
