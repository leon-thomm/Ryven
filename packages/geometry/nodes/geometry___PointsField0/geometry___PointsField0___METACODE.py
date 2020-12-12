from NIENV import *


# API METHODS --------------

# self.main_widget
# self.update_shape()

# Ports
# self.input(index)
# self.set_output_val(index, val)
# self.exec_output(index)

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index)

# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# --------------------------


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        self.points = []

    def add_point(self, p):
        self.points.append(p)
        self.update()

    def update_event(self, input_called=-1):
        sclx = self.input(0)
        scly = self.input(1)
        points_scaled = [[p[0]*sclx, p[1]*scly] for p in self.points]
        self.set_output_val(0, points_scaled)

    def get_data(self):
        data = {'points': self.points}
        return data

    def set_data(self, data):
        self.points = data['points']
        self.main_widget.draw()

    def removing(self):
        pass
