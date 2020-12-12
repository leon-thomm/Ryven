from custom_src.script_variables.Variable import Variable
from custom_src.custom_list_widgets.VariablesListWidget import VariablesListWidget

from custom_src.global_tools.Debugger import Debugger


class VarsManager:
    """Manages script variables and triggers receivers when values of variables change"""

    def __init__(self, script, config=None):

        self.script = script

        self.variables = []
        self.list_widget = VariablesListWidget(self)
        self.var_receivers = {}

        if config is not None:
            for name in config.keys():  # variables
                # self.variables.append(Variable(name, config_vars[name]))
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
        Debugger.debug('getting variable with name:', name)

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

    def config_data(self):
        vars_dict = {}
        for v in self.variables:
            vars_dict[v.name] = {'serialized': v.serialize()}
        return vars_dict
