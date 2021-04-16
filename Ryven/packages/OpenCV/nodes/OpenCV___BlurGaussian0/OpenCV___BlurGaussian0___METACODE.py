from NENV import *

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget()                    <- access to main widget
from PySide2.QtCore import Signal


class %CLASS%(Node):

    new_img_computed = Signal(object)

    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        self.img_unblurred = None
        self.img_blurred = None

    def place_event(self):
        self.new_img_computed.connect(self.main_widget().show_image)

    def update_event(self, input_called=-1):
        self.img_unblurred = self.input(0)
        blur_val = self.input(1)
        blur_val = int(blur_val)
        self.img_blurred = cv2.GaussianBlur( self.img_unblurred, (blur_val, blur_val),0)
        # self.main_widget().show_image(self.img_blurred)
        self.new_img_computed.emit(self.img_blurred)
        self.set_output_val(0, self.img_blurred)

    def get_state(self):
        data = {}
        # ...
        return data

    def set_state(self, data):
        pass
        # ...


    def remove_event(self):
        pass
