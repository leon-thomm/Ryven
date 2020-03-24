from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        self.img_unblurred = None
        self.img_blurred = None

        if configuration:
            self.set_data(configuration['state data'])


    def update(self, input_called=-1, token=None):
        self.handle_token(token)
        # ------------------------

        self.img_unblurred = self.input(0)
        blur_val = self.input(1)
        try:
            blur_val = int(blur_val)
        except ValueError and TypeError:
            return
        try:
            self.img_blurred = cv2.blur(self.img_unblurred, (blur_val, blur_val))
            self.main_widget.show_image(self.img_blurred)
            self.outputs[0].set_val(self.img_blurred)
        except Exception as e:
            return

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
