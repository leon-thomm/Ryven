from ryven.node_env import on_gui_load

from .sub1 import nodes
from .sub2 import nodes

@on_gui_load
def load_gui():
    # this function will be called by Ryven once GUI can be imported
    # when running in headless mode, this function will not be called
    from .sub1 import gui
    from .sub2 import gui