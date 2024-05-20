from typing import Type, List, Set

from ryvencore import Data, Node, serialize, deserialize
from ryvencore.InfoMsgs import InfoMsgs

from ryvencore_qt import NodeInputWidget, NodeMainWidget, NodeGUI, NodeInspectorWidget

from ryven.gui import std_input_widgets as inp_widgets
from ryven.main.utils import in_gui_mode


__explicit_nodes: Set = set()  # for protection against setting the gui twice on the same node

def init_node_guis_env():
    pass

def export_guis(guis: List[Type[NodeGUI]]):
    raise Exception(
        'The function export_guis is deprecated and should not be used anymore. '
        'Please use the node_gui decorator instead. '
        'See the example nodes packages that Ryven comes with for reference. '
    )


def node_gui(node_cls: Type[Node]):
    """
    Registers a node gui for a node class. The gui of a node is inherited to its sub-classes,
    but can be overridden by specifying a new gui for the sub-class.
    """
    if not issubclass(node_cls, Node):
        raise Exception(f"{node_cls} is not of type {Node}")

    def register_gui(gui_cls: Type[NodeGUI]):
        if node_cls in __explicit_nodes:
            assert hasattr(node_cls, 'GUI')
            InfoMsgs.write(f'{node_cls.__name__} has defined an explicit gui {node_cls.GUI.__name__}')
            return
        node_cls.GUI = gui_cls  # type: ignore
        __explicit_nodes.add(node_cls)
        InfoMsgs.write(f"Registered node gui: {gui_cls} for {node_cls}")
        return gui_cls

    return register_gui
