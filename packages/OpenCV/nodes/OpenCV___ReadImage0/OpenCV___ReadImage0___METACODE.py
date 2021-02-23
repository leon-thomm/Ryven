from NENV import *

import cv2

# USEFUL
# self.input(index)                     <- access to input data
# self.outputs[index].set_val(val)      <- set output data port value
# self.main_widget()                      <- access to main widget


class %CLASS%(Node):

    main_widget_message = Signal(str)

    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        self.image_filepath = ''
        self.img = None
    
    def place_event(self):
        self.input_widget(0).path_chosen.connect(self.path_chosen)
        self.main_widget_message.connect(self.main_widget().show_path)


    def update_event(self, input_called=-1):
        try:
            self.log_message('loading image, fpath: '+
                                self.image_filepath,
                             target='Global')
            self.img = cv2.imread(self.image_filepath)
            self.set_output_val(0, self.img)
            # self.main_widget().set_path_text(self.image_filepath)
            self.main_widget_message.emit(self.image_filepath)
        except Exception as e:
            # self.main_widget().setText('couldn\'t open file')
            self.main_widget_message.emit('couldn\'t open file')
            self.log_message(e, 'error')

    def get_data(self):
        data = {'image file path': self.image_filepath}
        return data

    def set_data(self, data):
        self.image_filepath = data['image file path']

    def path_chosen(self, file_path):
        self.image_filepath = file_path
        self.update()


    def remove_event(self):
        pass
