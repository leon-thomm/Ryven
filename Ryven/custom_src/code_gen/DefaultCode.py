"""All required static components for building the flow in the target source"""


class Flow_AlgorithmMode:
    mode_data_flow = '''+str(self.flow_algorithm_mode.mode_data_flow)+'''


class Node:
    """Base node class with very basic properties"""

    def __init__(self, title, inputs, outputs):
        self.title = title
        self.inputs = inputs
        self.outputs = outputs


class NodePort:
    """Inputs and outputs for nodes"""

    def __init__(self, type_, label):
        self.type_ = type_
        self.label = label


class M:
    """Replaces the retain mechanism from Ryven, which isn't needed in the
    target source, as no source code will be edited live."""

    def __init__(self, method):
        self.method = method  # retain(method)

    def __call__(self, *args, **kwargs):
        self.method(*args, **kwargs)


class PlaceholderClass:
    """Placeholder class, used for widgets here, to automatically block all
    communication to a NodeInstance's main_widget"""

    def __getattr__(self, item):
        def method(*args):
            pass
        return method

    def __setattr__(self, key, value):
        if not hasattr(self, key):
            return
        super(PlaceholderClass, self).__setattr__(key, value)


class VarsManager:
    def __init__(self, config=None):

        self.variables = []
        self.list_widget = PlaceholderClass()
        self.var_receivers = {}

        if config is not None:
            for name in config.keys():
                self.create_new_var(name, val=config[name])
            self.list_widget.recreate_ui()

    def create_new_var_and_update(self, name):
        """Also updates the GUI"""

        self.create_new_var(name)
        self.list_widget.recreate_ui()

    def create_new_var(self, name, val=None):

        if len(name) == 0:
            return

        # search for name issues
        for v in self.variables:
            if v.name == name:
                return

        self.variables.append(Variable(name, val))

    def get_var(self, name):
        for v in self.variables:
            if v.name == name:
                return v
        return None

    def get_var_val(self, name):
        var = self.get_var(name)
        return var.val if var is not None else None

    def set_var(self, name, val):
        var_index = self.get_var_index_from_name(name)
        if var_index is None:
            return False

        self.variables[var_index].val = val

        # update all variable usages by calling all registered object's methods on updated variable with the new val
        for receiver, var_name in self.var_receivers.keys():
            if var_name == name:
                self.var_receivers[receiver, var_name](var_name, val)  # calling the slot method

        return True

    def get_var_index_from_name(self, name):
        var_names_list = [v.name for v in self.variables]
        for i in range(len(var_names_list)):
            if var_names_list[i] == name:
                return i

        return None

    def register_receiver(self, receiver, var_name, method):
        """A registered receiver (method) gets triggered every time the
        value of a variable changes"""

        self.var_receivers[(receiver, var_name)] = method

    def unregister_receiver(self, receiver, var_name):
        try:
            del self.var_receivers[(receiver, var_name)]
        except Exception:
            return

import pickle
import base64
class Variable:
    def __init__(self, name='', val=None):
        super(Variable, self).__init__()

        self.name = name
        self.val = None
        if type(val) != dict:  # backwards compatibility
            try:
                self.val = pickle.loads(base64.b64decode(val))
            except Exception:
                self.val = val

        elif 'serialized' in val.keys():
            self.val = pickle.loads(base64.b64decode(val['serialized']))

    def serialize(self):
        pickled = pickle.dumps(self.val)
        serialized = base64.b64encode(pickled).decode('ascii')
        return serialized


class PortInstance:
    def __init__(self, parent_node_instance, type_, label):
        self.parent_node_instance = parent_node_instance
        self.type_ = type_
        self.label = label
        self.connected_port_instances = []


    def get_val(self):
        pass


class OutputPortInstance(PortInstance):
    def __init__(self, parent_node_instance, type_, label):
        super(OutputPortInstance, self).__init__(parent_node_instance, type_, label)

        self.val = None

    def exec(self):
        for cpi in self.connected_port_instances:
            cpi.update()

    def set_val(self, val):
        self.val = val

        if Flow_AlgorithmMode.mode_data_flow and not self.parent_node_instance.initializing:
            for cpi in self.connected_port_instances:
                cpi.update()

    def get_val(self):
        if not Flow_AlgorithmMode.mode_data_flow:
            self.parent_node_instance.update()
        return self.val


class InputPortInstance(PortInstance):
    def __init__(self, parent_node_instance, type_: str, label: str, widget_data: str):
        super(InputPortInstance, self).__init__(parent_node_instance, type_, label)

        self.val = None
        try:
            self.val = eval(widget_data)
        except Exception as e:
            self.val = widget_data

    def get_val(self):
        if len(self.connected_port_instances) == 0:
            return self.val
        else:
            return self.connected_port_instances[0].get_val()

    def update(self):
        if (self.parent_node_instance.is_active() and self.type_ == 'exec') or not self.parent_node_instance.is_active():
            self.parent_node_instance.update(self.parent_node_instance.inputs.index(self))


class NodeInstance:
    """NodeInstance base class with functionality required for executing the flow"""

    def __init__(self, params):
        super(NodeInstance, self).__init__()

        self.parent_node, self.flow, config = params
        self.inputs = []
        self.outputs = []
        self.initializing = True
        self.init_config = config
        self.special_actions = {}
        self.main_widget = PlaceholderClass()


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

    def get_vars_manager(self):
        return vars_manager

    def get_var_val(self, name):
        return self.get_vars_manager().get_var_val(name)

    def set_var_val(self, name, val):
        return self.get_vars_manager().set_var(name, val)

    def register_var_receiver(self, name, method):
        self.get_vars_manager().register_receiver(self, name, method)

    def unregister_var_receiver(self, name):
        self.get_vars_manager().unregister_receiver(self, name)

    def is_active(self) -> bool:
        for i in self.inputs:
            if i.type_ == 'exec':
                return True
        for o in self.outputs:
            if o.type_ == 'exec':
                return True
        return False
