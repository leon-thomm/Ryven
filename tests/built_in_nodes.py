import unittest
from os.path import join, dirname
import os
import unittest
from os.path import join, dirname

import ryvencore as rc
from ryven.node_env import init_node_env
from ryven.main.nodes_package import NodesPackage
from ryven.main.utils import import_nodes_package


class BuiltInNodesTestCase(unittest.TestCase):

    def test_load_builtin_nodes(self):
        os.environ['RYVEN_MODE'] = 'no-gui'
        init_node_env()
        session = rc.Session(gui=False)
        nodes, data_types = import_nodes_package(NodesPackage(
            directory=join(dirname(__file__), '../ryven/main/nodes/built_in/')
        ))
        session.register_data_types(data_types)
        session.register_node_types(nodes)
        print('registered nodes: ', nodes)



if __name__ == '__main__':
    unittest.main()
