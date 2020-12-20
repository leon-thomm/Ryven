from PySide2.QtCore import Signal, QObject

from ryvencore.script_variables.Variable import Variable

from ryvencore.global_tools.Debugger import Debugger


class VarsManager(QObject):
    """Manages script variables and triggers receivers when values of variables change"""

    new_var_created = Signal(Variable)
    var_deleted = Signal(Variable)

    def __init__(self, script, config=None):
        super().__init__()

        self.script = script

        self.variables = []
        # self.list_widget = VariablesListWidget(self)
        self.var_receivers = {}

        if config is not None:
            for name in config.keys():  # variables
                # self.variables.append(Variable(name, config_vars[name]))
                self.create_new_var(name, val=config[name])
            # self.list_widget.recreate_list()

    # def create_new_var_and_update(self, name):
    #     """Also updates the GUI"""
    #
    #     self.create_new_var(name)
    #     self.list_widget.recreate_ui()

    def check_new_var_name_validity(self, name: str) -> bool:
        if len(name) == 0:
            return False

        # search for name issues
        for v in self.variables:
            if v.name == name:
                return False

        return True


    def create_new_var(self, name: str, val=None):
        v = Variable(name, val)
        self.variables.append(v)
        self.new_var_created.emit(v)

    def get_var(self, name):
        Debugger.write('getting variable with name:', name)

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

    def delete_variable(self, var: Variable):
        self.variables.remove(var)
        self.var_deleted.emit(var)

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
