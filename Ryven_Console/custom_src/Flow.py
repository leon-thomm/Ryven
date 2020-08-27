import inspect

from class_inspection import find_type_in_object
from custom_src.GlobalAttributes import Flow_AlgorithmMode
from custom_src.Node import Node
from custom_src.PortInstance import PortInstance
from custom_src.builtin_nodes.GetVar_NodeInstance import GetVar_NodeInstance


class Flow:
    def __init__(self, parent_script, config: dict, nodes, node_instance_classes):

        self.parent_script = parent_script
        self.all_nodes = nodes
        self.node_instance_classes = node_instance_classes
        if config.__contains__('algorithm mode'):
            if config['algorithm mode'] == 'data flow':
                Flow_AlgorithmMode.mode_data_flow = True
            else:
                Flow_AlgorithmMode.mode_data_flow = False

        self.all_node_instances = self.load_node_instances(config['nodes'])
        self.get_var_node_instances = [ni for ni in self.all_node_instances if find_type_in_object(ni, GetVar_NodeInstance)]
        self.connect_nodes(config['connections'])


    def load_node_instances(self, config: dict):
        node_instances = []

        for n_c in config:
            # find parent node by title, type, package name and description as identifiers
            parent_node_title = n_c['parent node title']
            parent_node_package_name = n_c['parent node package']
            parent_node = None
            for pn in self.all_nodes:
                pn: Node
                if pn.title == parent_node_title and \
                        pn.package == parent_node_package_name:
                    parent_node = pn
                    break
            new_NI = self.create_node_instance(parent_node, n_c)
            node_instances.append(new_NI)

        return node_instances


    def create_node_instance(self, parent_node: Node, config: dict):
        return self.get_node_instance_class_from_node(parent_node)(parent_node, self, config)


    def get_node_instance_class_from_node(self, node: Node):
        return self.node_instance_classes[node]


    def connect_nodes(self, config: dict):
        for c in config:
            parent_node_instance = self.all_node_instances[c['parent node instance index']]
            connected_node_instance = self.all_node_instances[c['connected node instance']]

            self.connect_ports(parent_node_instance.outputs[c['output port index']],
                               connected_node_instance.inputs[c['connected input port index']])


    def connect_ports(self, parent_port: PortInstance, child_port: PortInstance):
        parent_port.connected_port_instances.append(child_port)
        child_port.connected_port_instances.append(parent_port)