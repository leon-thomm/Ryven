from NIENV import *


# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output
# self.create_new_input(type_, label, widget_name=None, widget_pos='under')
# self.delete_input(input or index)
# self.create_new_output(type_, label, append=True)
# self.delete_output(output or index)
from random import random


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        self.points = []


    def update_event(self, input_called=-1):
        if input_called == 1:
            self.randomize(self.input(0))
            self.set_output_val(0, self.points)

    def randomize(self, num_points):
        self.points.clear()

        for i in range(num_points):
            self.points.append([random(), random()])

        self.main_widget.draw_points(self.points)

    def get_data(self):
        data = {'points': self.points}
        return data

    def set_data(self, data):
        self.points = data['points']
        self.main_widget.draw_points(self.points)


    def remove_event(self):
        pass
