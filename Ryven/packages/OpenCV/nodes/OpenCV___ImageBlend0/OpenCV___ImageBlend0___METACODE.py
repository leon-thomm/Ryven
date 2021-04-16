from NENV import *

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget()                    <- access to main widget


class %CLASS%(Node):

    new_img = Signal(object)

    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        self.img_unblend1 = None
        self.img_unblend2 = None
        self.img_blend= None

    def place_event(self):
        self.new_img.connect(self.main_widget().show_image)


    def update_event(self, input_called=-1):
        self.img_unblend1 = self.input(0)
        alpha= self.input(1)
        alpha=int(alpha)
        self.img_unblend2=self.input(2)
        beta=int(1.0-alpha)

        self.img_blend = cv2.addWeighted(self.img_unblend1,alpha,self.img_unblend2,beta,0.0)
        # self.main_widget().show_image(self.img_blend)
        self.new_img.emit(self.img_blend)
        self.set_output_val(0, self.img_blend)

    def get_state(self):
        data = {}
        # ...
        return data

    def set_state(self, data):
        pass
        # ...


    def remove_event(self):
        pass
