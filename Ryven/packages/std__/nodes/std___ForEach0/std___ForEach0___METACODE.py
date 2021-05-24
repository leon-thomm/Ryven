from NENV import *


# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget()                    <- access to main widget
# self.exec_output(index)             <- executes an execution output
# self.create_new_input(type_, label, widget_name=None, widget_pos='under')
# self.delete_input(input or index)
# self.create_new_output(type_, label, append=True)
# self.delete_output(output or index)



class %CLASS%(Node):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)


    def update_event(self, inp=-1):
        if inp == 0:
            for obj in self.input(1):
                self.set_output_val(1, obj)
                self.exec_output(0)

            self.exec_output(2)

    def get_state(self):
        data = {}
        # ...
        return data

    def set_state(self, data):
        pass
        # ...


    def remove_event(self):
        pass
