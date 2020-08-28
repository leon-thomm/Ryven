class Node:
    def __init__(self):
        self.title = ''
        self.type_ = ''
        self.inputs = []
        self.outputs = []
        self.has_main_widget = False


class NodePort:
    def __init__(self):
        self.type_ = ''
        self.label = ''