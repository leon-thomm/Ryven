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
        self.img_ungrayed = None
        self.img_grayed = None

        self.initialized()


    def update_event(self, input_called=-1):
        self.img_ungrayed = self.input(0)
      
        self.img_grayed = cv2.cvtColor(self.img_ungrayed,cv2.COLOR_BGRA2GRAY)
        #self.cnvt=cv2.imshow('gray_image',self.img_grayed)
        self.main_widget.show_image(self.img_grayed)
        self.outputs[0].set_val(self.img_grayed)

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
