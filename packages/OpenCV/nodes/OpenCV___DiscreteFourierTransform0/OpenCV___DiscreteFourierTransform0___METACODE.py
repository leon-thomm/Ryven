from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node
import numpy as np
import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        self.img_unfourier = None
        self.img_fourier= None
        
        self.initialized()


    def update_event(self, input_called=-1):
        self.img_unfourier = self.input(0)
        #= self.input(1)
        #Nonzero=int(alpha)
        #beta=self.input(2)
        #beta=int(beta)
        
       # self.img_fourier = cv2.log(np.float(self.img_unfourier),np.float(self.img_unfourier),0,0)
        self.img_fourier = cv2.dft(self.img_unfourier)

        self.main_widget.show_image(self.img_fourier)
        self.outputs[0].set_val(self.img_fourier)

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
