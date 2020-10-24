from NIENV import *


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        self.log = self.new_log('Webcam Feed log')

    def video_picture_updated(self, img):
        self.log.log('video picture updated')
        self.set_output_val(0, img)
        # self.update()


    def update_event(self, input_called=-1):
        pass  # no central updating here

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        self.log_message('Webcam feed node instance successfully removed. Have a good day.', target='global')
