from NENV import *


class GetVar_Node(Node):

    title = 'get var'
    description = 'get the value of a script variable'
    init_inputs = [
        NodeInputBP(add_config={'widget name': 'std line edit', 'widget pos': 'besides'}),
    ]
    init_outputs = [
        NodeOutputBP(label='val')
    ]
    style = 'extended'
    color = '#c69a15'

    def __init__(self, params):
        super(GetVar_Node, self).__init__(params)

        self.var_name = ''
        self.temp_var_val = None

    def place_event(self):
        self.update()

    def update_event(self, input_called=-1):
        if self.input(0) != self.var_name:

            if self.var_name != '':  # disconnect old var val update connection
                self.unregister_var_receiver(self.var_name)

            self.var_name = self.input(0)

            # create new var update connection
            self.register_var_receiver(self.var_name, self.var_val_changed)

            val = self.get_var_val(self.input(0))
            if val is not None:
                self.set_output_val(0, val)
            else:
                self.set_output_val(0, None)

        else:  # ->> value changed!
            self.set_output_val(0, self.get_var_val(self.var_name))


    def var_val_changed(self, name, val):
        self.update()

    def get_current_var_name(self):
        return self.input(0)
