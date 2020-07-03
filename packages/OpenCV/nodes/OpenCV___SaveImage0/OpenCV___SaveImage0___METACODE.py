from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node
from custom_src.retain import m

# API METHODS

# self.main_widget        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# set_output_val(self, index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, append=True, widget_type='', widget_name='', widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_new_output(type_, label, append=True, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')

# ------------------------------------------------------------------------------


import cv2

class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        self.image_filepath = ''
        self.img = None
        self.inputs[1].widget.path_chosen.connect(self.path_chosen)

        self.initialized()

    def update_event(self, input_called=-1):
        if input_called != 0:
            return

        self.img = self.input(2)
        try:
            self.log_message('Saving pic to '+self.image_filepath, 'global')
            cv2.imwrite(self.image_filepath, self.img)
            self.main_widget.set_path_text(self.image_filepath)
            self.main_widget.setText('Success')
        except Exception as e:
            self.main_widget.setText('Error')

    def get_data(self):
        data = {'image file path': self.image_filepath}
        return data

    def set_data(self, data):
        self.image_filepath = data['image file path']

    def path_chosen(self, file_path):
        self.image_filepath = file_path
        self.main_widget.setText('')
        self.update()



    # optional - important for threading - stop everything here
    def removing(self):
        pass
