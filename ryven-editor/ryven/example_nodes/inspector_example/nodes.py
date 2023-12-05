from ryven.node_env import *


class MyNode(Node):
    title = 'My Node'


export_nodes(
    [MyNode],
)

@on_gui_load
def on_load():
    from . import gui
