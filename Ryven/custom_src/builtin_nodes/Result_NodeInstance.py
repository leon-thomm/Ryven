from custom_src.retain import M
from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node


class Result_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(Result_NodeInstance, self).__init__(parent_node, flow, configuration)

        self.initialized()

    def update_event(self, input_called=-1):
        self.main_widget.show_val(self.input(0))

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass
