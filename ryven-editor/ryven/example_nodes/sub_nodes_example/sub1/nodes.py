from ryven.node_env import *

class Sub1Node(Node):
    title = 'Node from sub-package 1'


export_nodes(
    sub_pkg_name='A',
    node_types=[Sub1Node],
)
