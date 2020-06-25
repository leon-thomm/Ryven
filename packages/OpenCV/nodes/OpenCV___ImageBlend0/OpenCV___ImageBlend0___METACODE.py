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
        self.img_unblend1 = None
        self.img_unblend2 = None
        self.img_blend= None
        
        self.initialized()


    def update_event(self, input_called=-1):
        self.img_unblend1 = self.input(0)
        alpha= self.input(1)
        alpha=int(alpha)
        self.img_unblend2=self.input(2)
        beta=int(1.0-alpha)

        self.img_blend = cv2.addWeighted(self.img_unblend1,alpha,self.img_unblend2,beta,0.0)
        self.main_widget.show_image(self.img_blend)
        self.outputs[0].set_val(self.img_blend)

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
