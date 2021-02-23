from NENV import *


# API METHODS --------------

# self.main_widget()
# self.update_shape()

# Ports
# self.input(index)
# self.set_output_val(index, val)
# self.exec_output(index)

# self.create_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_output(type_, label, pos=-1)
# self.delete_output(index)

# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# --------------------------

from numpy import transpose, conjugate


class Herm_Node(Node):
    def __init__(self, params):
        super(Herm_Node, self).__init__(params)

        self.special_actions['hide preview'] = {'method': M(self.action_hide_mw)}
        self.main_widget_hidden = False

    def update_event(self, input_called=-1):
        m = transpose(conjugate(self.input(0)))
        self.set_output_val(0, m)
        self.main_widget().update_matrix(m)

    def action_hide_mw(self):
        self.main_widget().hide()
        del self.special_actions['hide preview']
        self.special_actions['show preview'] = {'method': M(self.action_show_mw)}
        self.main_widget_hidden = True
        self.update_shape()

    def action_show_mw(self):
        self.main_widget().show()
        del self.special_actions['show preview']
        self.special_actions['hide preview'] = {'method': M(self.action_hide_mw)}
        self.main_widget_hidden = False
        self.update_shape()

    def get_data(self):
        data = {'main widget hidden': self.main_widget_hidden}
        return data

    def set_data(self, data):
        self.main_widget_hidden = data['main widget hidden']
        if self.main_widget_hidden:
            self.action_hide_mw()
        # shown by default

    def removing(self):
        pass
