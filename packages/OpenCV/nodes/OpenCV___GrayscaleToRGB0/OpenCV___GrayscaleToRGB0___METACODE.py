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
        self.img_unRgba = None
        self.img_Rgba = None


    def update_event(self, input_called=-1):
        self.img_unRgba= self.input(0)
      
        self.img_Rgba= cv2.cvtColor(self.img_unRgba,cv2.COLOR_BGRA2RGBA)
        #self.cnvt=cv2.imshow('gray_image',self.img_Rgb)
        self.main_widget.show_image(self.img_Rgba)
        self.set_output_val(0, self.img_Rgba)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
