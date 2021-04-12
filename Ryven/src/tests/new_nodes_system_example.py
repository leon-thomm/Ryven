


class Session:
    def __init__(self):
        self.node_classes = []

    def register_node(self, node_class):
        self.node_classes.append(node_class)

    def register_nodes(self, node_classes):
        for nc in node_classes:
            self.register_node(nc)

    def print_nodes(self):
        for nc in self.node_classes:
            print(nc.title, nc.val)


class Node:
    title = ''
    val = 0


class Node1(Node):
    title = 'Node 1'
    val = 1


class Node2(Node):
    title = 'Node 2'
    val = 2


class SubGraph:
    def __init__(self, nodes, title, session):
        self.nodes = nodes

        # create private node class
        class MyNode(Node):
            pass
        # set static attributes
        MyNode.title = title

        self.node_class = MyNode

        # and register as new node
        session.register_node(self.node_class)


if __name__ == '__main__':
    session = Session()
    session.register_nodes([
        Node1,
        Node2
    ])

    # create some nodes
    n1 = Node1()
    n2 = Node2()
    n3 = Node2()

    subgraph1 = SubGraph([n2, n3], 'fancy subgraph', session)
    subgraph2 = SubGraph([n3], 'very fancy subgraph', session)
    subgraph2.node_class.val = 42

    session.print_nodes()
