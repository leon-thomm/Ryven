from NENV import *


# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget()                    <- access to main widget
# self.exec_output(index)             <- executes an execution output
# self.create_input(type_, label, widget_name=None, widget_pos='under')
# self.delete_input(input or index)
# self.create_output(type_, label, append=True)
# self.delete_output(output or index)



class While_Node(Node):
    def __init__(self, params):
        super(While_Node, self).__init__(params)


    def update_event(self, input_called=-1):
        if input_called == 0:
            while(self.input(1)):
                self.exec_output(0)

    def get_state(self):
        data = {}
        # ...
        return data

    def set_state(self, data):
        pass
        # ...


    def remove_event(self):
        pass
