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
        self.vid_uncaptured= None
        self.vid_captured = None

        self.initialized()


    def update_event(self, input_called=-1):
        self.vid_uncaptured= self.input(0)
        self.vid_captured = cv2.VideoCapture(vid_uncaptured)
        while(1):
            ret,frame=self.vid_captured.read()
       # if (self.vid_captured.isOpened()== False): 
       # print("Error opening video stream or file")
       # while(self.vid_captured.isOpened()):
        # ret, frame = self.vid_captured.read()
        #if ret == True:
        self.play=cv2.imshow('Frame',frame)
   

  

        

      
      #  self.vid_captured = cv2.VideoCapture(showvid)
        #self.cnvt=cv2.imshow('gray_image',self.img_grayed)
        self.main_widget.show_image(self.play)
        self.outputs[0].set_val(selfplay )

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
