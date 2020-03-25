from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node


# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output
# self.create_new_input(type_, label, append=True, widget_type='', widget_name='', widget_pos='under')
# self.delete_input(input or index)
# self.create_new_output(type_, label, append=True)
# self.delete_output(output or index)
# self.update_shape()


class Button_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(Button_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        self.main_widget.clicked.connect(self.button_clicked)

        if configuration:
            self.set_data(configuration['state data'])

    def button_clicked(self):
        self.update()

    def updating(self, token, input_called=-1):
        self.exec_output(0)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...



    # optional - important for threading - stop everything here
    def removing(self):
        pass
