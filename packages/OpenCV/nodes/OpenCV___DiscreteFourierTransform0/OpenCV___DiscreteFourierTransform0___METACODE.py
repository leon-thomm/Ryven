from NIENV import *
import numpy as np
import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        self.img_unfourier = None
        self.img_fourier= None


    def update_event(self, input_called=-1):
        self.img_unfourier = self.input(0)
        #= self.input(1)
        #Nonzero=int(alpha)
        #beta=self.input(2)
        #beta=int(beta)
        
       # self.img_fourier = cv2.log(np.float(self.img_unfourier),np.float(self.img_unfourier),0,0)
        self.img_fourier = cv2.dft(self.img_unfourier)

        self.main_widget.show_image(self.img_fourier)
        self.set_output_val(0, self.img_fourier)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
