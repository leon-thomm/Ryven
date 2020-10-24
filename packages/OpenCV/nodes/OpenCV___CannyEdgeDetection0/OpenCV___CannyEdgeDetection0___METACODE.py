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
        self.img_normal = None
        self.img_canny = None


    def update_event(self, input_called=-1):
        self.img_normal = self.input(0)
        canny_min_val = self.input(1)
        canny_max_val = self.input(2)

        canny_min_val = int(canny_min_val)
        canny_max_val = int(canny_max_val)

        self.img_canny = cv2.Canny(self.img_normal, canny_min_val, canny_max_val)
        self.main_widget.show_image(self.img_canny)
        self.set_output_val(0, self.img_canny)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
