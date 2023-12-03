from ryven.node_env import *

class Sub1Node(Node):
    title = 'Node from sub-package 1'


export_sub_nodes(__file__,
    node_types=[Sub1Node],
)
