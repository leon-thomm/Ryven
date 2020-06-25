from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class BilateralFilter_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(BilateralFilter_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        self.img_unfiltered = None
        self.img_filtered = None
       

        self.initialized()


    def update_event(self, input_called=-1):
        self.img_unfiltered = self.input(0)
        d_val = self.input(1)
        d_val = int(d_val)
        sigmaColor_val=self.input(2)
        sigmaColor_val=int(sigmaColor_val)
        sigmaSpace_val=self.input(3)
        sigmaSpace_val=int(sigmaSpace_val)
    
        self.img_filtered = cv2.bilateralFilter( self.img_unfiltered, d_val, sigmaColor_val,sigmaSpace_val)
        self.main_widget.show_image(self.img_filtered)
        self.outputs[0].set_val(self.img_filtered)

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
