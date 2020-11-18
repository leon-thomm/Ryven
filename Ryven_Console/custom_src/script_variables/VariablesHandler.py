import sys
sys.path.append('../Ryven/custom_src/script_variables/')
from Variable import Variable

import pickle
import base64


class VariablesHandler:
    def __init__(self, script, config_vars=None):

        self.script = script

        self.variables = []
        self.var_receivers = {}

        if config_vars is not None:
            for name in list(config_vars.keys()):  # variables
                self.variables.append(Variable(name, config_vars[name]))


    def create_new_var(self, name):
        if len(name) == 0:
            return
        # search for name problems
        for v in self.variables:
            if v.name == name:
                return

        self.variables.append(Variable(name))
        self.set_var(name, None)

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
        self.var_receivers[(receiver, var_name)] = method

    def unregister_receiver(self, receiver, var_name):
        try:
            del self.var_receivers[(receiver, var_name)]
        except Exception:
            return

    def get_json_data(self):
        vars_dict = {}
        for v in self.variables:
            pickled = pickle.dumps(v.val)
            vars_dict[v.name] = {'serialized': base64.b64encode(pickled).decode('ascii')}
        return vars_dict