from ryven.node_env import on_gui_load

from . import special_nodes
from . import basic_operators
from . import control_structures


@on_gui_load
def load_gui():
    from . import gui
