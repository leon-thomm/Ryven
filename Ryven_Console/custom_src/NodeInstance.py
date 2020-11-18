from custom_src.Node import Node
from custom_src.PlaceholderClass import PlaceholderClass
from custom_src.PortInstance import InputPortInstance, OutputPortInstance


class NodeInstance:
    def __init__(self, params):
        super(NodeInstance, self).__init__()

        self.parent_node, self.flow, config = params
        self.inputs = []
        self.outputs = []
        self.initializing = True
        self.init_config = config
        self.special_actions = {}
        self.main_widget = PlaceholderClass() if self.parent_node.has_main_widget else None


    def initialized(self):
        self.setup_ports(self.init_config['inputs'], self.init_config['outputs'])
        self.set_data(self.init_config['state data'])
        self.initializing = False
        self.update()

    def setup_ports(self, inputs_config, outputs_config):
        for inp in inputs_config:
            pi = InputPortInstance(self, inp['type'], inp['label'], inp['widget data'] if inp['has widget'] else None)
            self.inputs.append(pi)

        for out in outputs_config:
            pi = OutputPortInstance(self, out['type'], out['label'])
            self.outputs.append(pi)


    #   ALGORITHM

    def update(self, input_called=-1, output_called=-1):
        try:
            self.update_event(input_called)
        except Exception as e:
            print('EXCEPTION in', self.parent_node.title, e)

    def update_event(self, input_called=-1):
        pass

    def input(self, index):
        return self.inputs[index].get_val()

    def exec_output(self, index):
        self.outputs[index].exec()

    def set_output_val(self, index, val):
        self.outputs[index].set_val(val)

    def remove_event(self):
        pass

    #   FURTHER API

    def new_log(self, title):
        return PlaceholderClass()

    def log_message(self, message: str, target='global'):
        pass

    def update_shape(self):
        pass

    def get_data(self):
        pass

    def set_data(self, data):
        pass

    def get_default_stylesheet(self):
        return


    # VARIABLES

    def get_vars_handler(self):
        return self.flow.parent_script.variables_handler

    def get_var_val(self, name):
        return self.get_vars_handler().get_var_val(name)

    def set_var_val(self, name, val):
        return self.get_vars_handler().set_var(name, val)

    def register_var_receiver(self, name, method):
        self.get_vars_handler().register_receiver(self, name, method)

    def unregister_var_receiver(self, name):
        self.get_vars_handler().unregister_receiver(self, name)


    def is_active(self):
        for i in self.inputs:
            if i.type_ == 'exec':
                return True
        for o in self.outputs:
            if o.type_ == 'exec':
                return True
        return False