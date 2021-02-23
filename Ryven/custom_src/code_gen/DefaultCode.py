# content from tools

import pickle
import base64


def serialize(data) -> str:
    return base64.b64encode(pickle.dumps(data)).decode('ascii')


def deserialize(data):
    return pickle.loads(base64.b64decode(data))


# flow

class FlowAlg:
    DATA = 1
    EXEC = 2


class Node:
    """Base node class with basic properties"""
    special_actions = {}

    def __init__(self, config):
        self.inputs, self.outputs = [], []

        for inp in config['inputs']:
            self.create_input(inp['type'], inp['label'], val=inp['val'])
        for out in config['outputs']:
            self.create_output(out['type'], out['label'])

    def create_input(self, type_: str, label: str, pos=-1, val=None):
        if pos==-1:
            pos = len(self.inputs)
        if type_ == 'data':
            self.inputs.insert(pos, DataInputPort(self, label, val))
        else:
            self.inputs.insert(pos, ExecInputPort(self, label))

    def delete_input(self, i):
        if type(i) == int:
            i = self.inputs[i]
        for c in i.connections:
            c.out.remove(c)
        self.inputs.remove(i)

    def create_output(self, type_: str, label: str, pos=-1):
        if pos==-1:
            pos = len(self.outputs)
        if type_ == 'data':
            self.outputs.insert(pos, DataOutputPort(self, label))
        else:
            self.outputs.insert(pos, ExecOutputPort(self, label))

    def remove_output(self, o):
        if type(o) == int:
            o = self.outputs[o]
        for c in o.connections:
            c.inp.remove(c)
        self.outputs.remove(o)

    def main_widget(self):
        return PlaceholderClass()

    def update(self, input_called=-1):
        self.update_event(input_called)

    def update_event(self, input_called=-1):
        pass

    def input(self, index: int):
        return self.inputs[index].get_val()

    def exec_output(self, index: int):
        self.outputs[index].exec()

    def set_output_val(self, index: int, val):
        self.outputs[index].set_val(val)

    def new_log(self):
        pass

    def disable_logs(self):
        pass

    def enable_logs(self):
        pass

    def log_message(self, msg: str, target: str):
        pass

    def update_shape(self):
        pass

    def set_data(self, data):
        pass

    def register_var_receiver(self, name: str, method):
        vars_manager.register_receiver(self, name, method)

    def unregister_var_receiver(self, name: str):
        vars_manager.unregister_receiver(self, name)


class NodePort:
    def __init__(self, node, label):
        self.node, self.label = node, label
        self.connections = []

class DataInputPort(NodePort):
    def __init__(self, node, label, val):
        super().__init__(node, label)
        self.val = deserialize(val) if val else None

    def update(self, data):
        self.val = data
        self.node.update(self.node.inputs.index(self))

    def get_val(self):
        return self.val

class ExecInputPort(NodePort):
    def update(self):
        self.node.update(self.node.inputs.index(self))

class DataOutputPort(NodePort):
    def __init__(self, node, label):
        super().__init__(node, label)
        self.val = None

    def set_val(self, val):
        self.val = val
        if flow_alg == FlowAlg.DATA:
            for c in self.connections:
                c.activate(val)

    def get_val(self):
        if flow_alg == FlowAlg.EXEC:
            self.node.update()
        return self.val

class ExecOutputPort(NodePort):
    def exec(self):
        for c in self.connections:
            c.activate()


class Connection:
    def __init__(self, out, inp):
        self.out, self.inp = out, inp

    def activate(self):
        pass

class ExecConnection(Connection):
    def activate(self):
        self.inp.update()

class DataConnection(Connection):
    def activate(self, data=None):
        self.inp.update(data)

    def get_val(self):
        return self.out.val


class M:
    """Replaces the retain mechanism from Ryven."""

    def __init__(self, method):
        self.method = method

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


class Variable:
    def __init__(self, name='', val=None):
        self.name, self.val = name, deserialize(val['serialized'])

    def serialize(self):
        return serialize(self.val)


class VarsManager:
    def __init__(self, config=None):
        self.variables = []
        self.var_receivers = {}

        if config is not None:
            for name in config.keys():
                self.create_new_var(name, val=config[name])

    def check_new_var_name_validity(self, name: str) -> bool:
        return name and len(name) != 0 and not any([v.name == name for v in self.variables])

    def create_new_var(self, name: str, val=None) -> Variable:
        v = Variable(name, val)
        self.variables.append(v)
        return v

    def get_var(self, name) -> Variable:
        for v in self.variables:
            if v.name == name:
                return v
        return None

    def get_var_val(self, name):
        var = self.get_var(name)
        return var.val if var is not None else None

    def set_var(self, name, val) -> bool:
        var_index = self.get_var_index_from_name(name)
        if var_index is None:
            return False

        self.variables[var_index].val = val

        # update receivers
        for receiver, var_name in self.var_receivers.keys():
            if var_name == name:
                self.var_receivers[receiver, var_name](var_name, val)
        return True

    def get_var_index_from_name(self, name: str) -> int:
        var_names_list = [v.name for v in self.variables]
        for i in range(len(var_names_list)):
            if var_names_list[i] == name:
                return i
        return None

    def register_receiver(self, receiver, var_name, method):
        self.var_receivers[(receiver, var_name)] = method

    def unregister_receiver(self, receiver, var_name):
        try:
            del self.var_receivers[(receiver, var_name)]
        except Exception:
            return

# ---------------------------------------------------------------------------
