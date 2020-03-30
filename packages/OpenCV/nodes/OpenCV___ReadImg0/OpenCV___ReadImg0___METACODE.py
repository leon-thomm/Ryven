from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node

import cv2


# USEFUL
# self.input(index)                     <- access to input data
# self.outputs[index].set_val(val)      <- set output data port value
# self.main_widget                      <- access to main widget


class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        self.image_filepath = ''
        self.img = None
        self.inputs[0].widget.path_chosen.connect(self.path_chosen)

        if configuration:
            self.set_data(configuration['state data'])

    def update_event(self, input_called=-1):
        try:
            print('image file path:', self.image_filepath)
            self.img = cv2.imread(self.image_filepath)
            self.outputs[0].set_val(self.img)
            self.main_widget.set_path_text(self.image_filepath)
        except Exception as e:
            self.main_widget.setText('couldn\'t open file')
            print(e)

    def get_data(self):
        data = {'image file path': self.image_filepath}
        return data

    def set_data(self, data):
        self.image_filepath = data['image file path']

    def path_chosen(self, file_path):
        self.image_filepath = file_path
        self.update()



    # optional - important for threading - stop everything here
    def removing(self):
        pass
