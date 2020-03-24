from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        # ...

        if configuration:
            self.set_data(configuration['state data'])

    def video_picture_updated(self, img):
        self.outputs[0].set_val(img)
        self.update()


    def update(self, input_called=-1, token=None):
        self.handle_token(token)
        # ------------------------

        # your stuff here ...

        # ------------------------
        self.data_outputs_updated()

    def deleted(self):
        pass

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...
