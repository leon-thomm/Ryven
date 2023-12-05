"""
This module automatically imports all requirements for Gui definitions of a nodes package.
"""

from typing import Type

from ryvencore import Data, Node, serialize, deserialize
from ryvencore.InfoMsgs import InfoMsgs

from ryvencore_qt import NodeInputWidget, NodeMainWidget, NodeGUI, NodeInspectorWidget

import ryven.gui.std_input_widgets as inp_widgets
from ryven.main.utils import in_gui_mode


__explicit_nodes: set = set() # for protection against setting the gui twice on the same node

def init_node_guis_env():
    pass


class GuiClassesRegistry:
    """
    Used for statically keeping the gui classes specified in export_guis to access them through node_env.import_guis().
    """

    exported_guis = []


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


def node_gui(node_cls: Type[Node]):
    """
    Registers a node gui for a node class. The gui of a node is inherited to its sub-classes,
    but can be overridden by specifying a new gui for the sub-class.
    """
    if not issubclass(node_cls, Node):
        raise Exception(f"{node_cls} is not of type {Node}")

    def register_gui(gui_cls: Type[NodeGUI]):
        if node_cls in __explicit_nodes:
            InfoMsgs.write(f'{node_cls.__name__} has defined an explicit gui {node_cls.GUI.__name__}')
            return
        
        node_cls.GUI = gui_cls
        __explicit_nodes.add(node_cls)
        InfoMsgs.write(f"Registered node gui: {gui_cls} for {node_cls}")
        return gui_cls

    return register_gui
