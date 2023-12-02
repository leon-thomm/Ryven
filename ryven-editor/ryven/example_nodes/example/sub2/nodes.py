from ryven.node_env import *

class Sub2Node(Node):
    title = 'Node from sub-package 2'


export_sub_nodes(__file__,
    node_types=[Sub2Node],
)
