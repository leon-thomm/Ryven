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
        self.img_unTexed = None
        self.img_Texed = None


    def update_event(self, input_called=-1):
        self.img_unTexed = self.input(0).copy()
        text = self.input(1)
        org=self.input(2)
        #font=cv2.FONT_HERSHEY_SIMPLEX
       # line=cv2.LINE_AA
        fontScale=self.input(3)
        color=self.input(4)
        thickness=self.input(5)

        self.img_Texed = cv2.putText( self.img_unTexed,text,org,cv2.FONT_HERSHEY_SIMPLEX,fontScale,color,thickness,cv2.LINE_AA)
        self.main_widget.show_image(self.img_Texed)
        self.set_output_val(0, self.img_Texed)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
