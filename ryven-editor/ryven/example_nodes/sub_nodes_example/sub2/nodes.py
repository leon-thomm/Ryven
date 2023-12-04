from ryven.node_env import *

class Sub2Node(Node):
    title = 'Node from sub-package 2'


export_nodes(
    sub_pkg_name='B',
    node_types=[Sub2Node],
)
