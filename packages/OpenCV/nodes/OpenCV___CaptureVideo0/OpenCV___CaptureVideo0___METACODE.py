from NIENV import *

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        self.vid_uncaptured= None
        self.vid_captured = None


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
        self.set_output_val(0, self.play)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
