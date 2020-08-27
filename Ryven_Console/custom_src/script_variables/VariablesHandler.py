from custom_src.script_variables.Variable import Variable


class VariablesHandler:
    def __init__(self, script, config_vars):
        self.script = script
        self.flow = None
        self.variables = []
        for name in list(config_vars.keys()):  # variables
            self.variables.append(Variable(name, config_vars[name]))

    def get_var(self, name):
        for v in self.variables:
            if v.name == name:
                return v
        return None

    def set_var(self, name, val):
        for v in self.variables:
            if v.name == name:
                v.val = val
                self.update_variable_usages(v)
                return True
        return False

    def update_variable_usages(self, v):
        for ni in self.flow.get_var_node_instances:
            ni.update()