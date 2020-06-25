from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class Rectangle_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(Rectangle_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        self.img_unrectangled = None
        self.img_rectangled = None
       

        self.initialized()


    def update_event(self, input_called=-1):
        self.img_unrectangled = self.input(0)
        startpoint = self.input(1)
        endpoint=self.input(2)
        color=self.input(3) #COLOR is in BGR
        thickness=self.input(4)
        
        self.img_rectangled = cv2.rectangle( self.img_unrectangled,startpoint,endpoint,color,thickness)
        self.main_widget.show_image(self.img_rectangled)
        self.outputs[0].set_val(self.img_rectangled)

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
