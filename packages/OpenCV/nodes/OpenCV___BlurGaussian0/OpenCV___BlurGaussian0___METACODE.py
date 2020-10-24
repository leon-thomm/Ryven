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
        self.img_unblurred = None
        self.img_blurred = None


    def update_event(self, input_called=-1):
        self.img_unblurred = self.input(0)
        blur_val = self.input(1)
        blur_val = int(blur_val)
        self.img_blurred = cv2.GaussianBlur( self.img_unblurred, (blur_val, blur_val),0)
        self.main_widget.show_image(self.img_blurred)
        self.set_output_val(0, self.img_blurred)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
