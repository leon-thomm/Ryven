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
        self.img_unlined = None
        self.img_lined = None


    def update_event(self, input_called=-1):
        self.img_unlined = self.input(0)
        startpoint = self.input(1)
        endpoint=self.input(2)
        color=self.input(3)
        thickness=self.input(4)
        
        self.img_lined = cv2.line( self.img_unlined,startpoint,endpoint,color,thickness)
        self.main_widget.show_image(self.img_lined)
        self.set_output_val(0, self.img_lined)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
