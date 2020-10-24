from NIENV import *

import random

# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output
# self.create_new_input(type_, label, widget_name=None, widget_pos='under')
# self.delete_input(input or index)
# self.create_new_output(type_, label, append=True)
# self.delete_output(output or index)



class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        self.special_actions['reset'] = {'method': M(self.action_reset)}
        self.weights = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.feeding_log = self.new_log('Perception Feeding Log')
        self.fixing_log = self.new_log('Perceptron Fixing Log')


    def action_reset(self):
        self.weights = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.fixing_log.clear()
        self.fixing_log.log('new weights created:')
        self.fixing_log.log('x1:',str(self.weights[0]))
        self.fixing_log.log('x2:',str(self.weights[1]))
        self.feeding_log.clear()


    def guess(self, x1, x2):
        return x1*self.weights[0]+x2*self.weights[1]

    def sign(self, val):
        return -1 if val < 0 else +1

    def update_event(self, input_called=-1):
        if input_called == 0:  # guess
            x1 = self.input(1)
            x2 = self.input(2)
            guess = self.guess(x1, x2)
            signed_guess = self.sign(guess)
            self.outputs[1].set_val(signed_guess)
            self.feeding_log.log('input:',str(x1),',',str(x2),'   guess:',signed_guess)
            self.exec_output(0)

        elif input_called == 3:  # correct
            fix_factor = self.input(5)
            x1 = self.input(1)
            x2 = self.input(2)
            err = self.input(4)
            self.fixing_log.log('----------------------------')
            self.fixing_log.log('err:',err)
            self.fixing_log.log('old x1:',str(self.weights[0]))
            self.fixing_log.log('old x2:',str(self.weights[1]))
            d_w1 = x1*err*fix_factor
            self.weights[0] += d_w1
            d_w2 = x2*err*fix_factor
            self.weights[1] += d_w2
            self.fixing_log.log('new x1:',str(self.weights[0]))
            self.fixing_log.log('new x2:',str(self.weights[1]))

    def get_data(self):
        data = {'weights': self.weights}
        return data

    def set_data(self, data):
        self.weights = data['weights']


    def removed(self):
        pass
