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
        self.img_unbright = None
        self.img_bright= None


    def update_event(self, input_called=-1):
        self.img_unbright = self.input(0)
        alpha= self.input(1)
        alpha=int(alpha)
        beta=self.input(2)
        beta=int(beta)
      

        self.img_bright = cv2.convertScaleAbs(self.img_unbright,alpha,beta)
        self.main_widget.show_image(self.img_bright)
        self.set_output_val(0, self.img_bright)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
