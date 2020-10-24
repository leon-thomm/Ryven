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
        self.img_unfiltered = None
        self.img_filtered = None


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
        self.set_output_val(0, self.img_filtered)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
