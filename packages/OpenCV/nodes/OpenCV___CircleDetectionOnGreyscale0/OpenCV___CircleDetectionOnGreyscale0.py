from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node
from custom_src.retain import M


# API METHODS

# self.main_widget        <- access to main widget


# Ports
# self.input(index)                   <- access to input data
# set_output_val(self, index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, widget_type='', widget_name='', widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')

# ------------------------------------------------------------------------------

import cv2
import numpy as np

class CircleDetectionOnGreyscale_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(CircleDetectionOnGreyscale_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

        self.initialized()

    # don't call self.update_event() directly, use self.update() instead
    def update_event(self, input_called=-1):
        self.image = self.input(0).copy()
        self.grayImage = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        circles = cv2.HoughCircles(self.grayImage, cv2.HOUGH_GRADIENT, self.input(1), self.input(2))

        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(self.image,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(self.image,(i[0],i[1]),2,(0,0,255),3)

        self.main_widget.show_image(self.image)
        self.set_output_val(0, self.image)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...



    # optional - important for threading - stop everything here
    def removing(self):
        pass
