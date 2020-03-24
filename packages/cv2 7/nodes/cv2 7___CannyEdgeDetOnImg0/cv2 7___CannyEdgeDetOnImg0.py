from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class CannyEdgeDetOnImg_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(CannyEdgeDetOnImg_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        self.img_normal = None
        self.img_canny = None

        if configuration:
            self.set_data(configuration['state data'])


    def update(self, input_called=-1, token=None):
        self.handle_token(token)
        # ------------------------

        self.img_normal = self.input(0)
        canny_min_val = self.input(1)
        canny_max_val = self.input(2)
        print('a')
        try:
            canny_min_val = int(canny_min_val)
            canny_max_val = int(canny_max_val)
        except ValueError:
            return
        print('b')
        try:
            self.img_canny = cv2.Canny(self.img_normal, canny_min_val, canny_max_val)
            print('c')
            self.main_widget.show_image(self.img_canny)
            print('d')
            self.outputs[0].set_val(self.img_canny)
        except Exception as e:
            print(e)
            return

        # ------------------------
        self.data_outputs_updated()

    def deleted(self):
        pass
    
    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...
