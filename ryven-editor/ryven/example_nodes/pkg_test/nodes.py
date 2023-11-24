import os
from ryven.api import on_gui_load

from .std import nodes
from .linalg import nodes

@on_gui_load
def load_gui():
    from .std import gui
    from .linalg import gui