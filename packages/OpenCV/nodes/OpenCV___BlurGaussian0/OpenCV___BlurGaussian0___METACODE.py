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

        self.initialized()


    def update_event(self, input_called=-1):
        self.img_unblurred = self.input(0)
        blur_val = self.input(1)
        blur_val = int(blur_val)
        self.img_blurred = cv2.GaussianBlur( self.img_unblurred, (blur_val, blur_val),0)
        self.main_widget.show_image(self.img_blurred)
        self.outputs[0].set_val(self.img_blurred)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...



    # optional - important for threading - stop everything here
    def removing(self):
        pass
