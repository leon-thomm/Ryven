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
        self.img_unYUV_IYUV = None
        self.img_YUV_IYUV = None


    def update_event(self, input_called=-1):
        self.img_unYUV_IYUV = self.input(0)
      
        self.img_YUV_IYUV = cv2.cvtColor(self.img_unYUV_IYUV,cv2.COLOR_BGRA2YUV_IYUV)
        #self.cnvt=cv2.imshow('gray_image',self.img_YUV_I420)
        self.main_widget.show_image(self.img_YUV_IYUV)
        self.set_output_val(0, self.img_YUV_IYUV)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
