from custom_src.script_variables.Variable import Variable
from custom_src.custom_list_widgets.VariablesListWidget import VariablesListWidget
from custom_src.custom_nodes.GetVar_NodeInstance import GetVar_NodeInstance

from custom_src.global_tools.Debugger import Debugger
from custom_src.global_tools.class_inspection import find_type_in_object


class VariablesHandler:
    def __init__(self, script, config_vars=None):

        self.script = script
        self.flow = None  # for get var node instances - gets set by Script manually

        self.variables = []
        self.list_widget = VariablesListWidget(self.variables)

        if config_vars is not None:
            for name in list(config_vars.keys()):  # variables
                self.variables.append(Variable(name, config_vars[name]))
            self.list_widget.recreate_ui()


    def create_new_var(self, name):
        if len(name) == 0:
            return
        # search for name problems
        for v in self.variables:
            if v.name == name:
                return

        self.variables.append(Variable(name))
        self.update_variable_usages(self.variables[-1])
        self.list_widget.recreate_ui()

    def get_var(self, name):
        Debugger.debug('getting variable from script name:', name)

        for v in self.variables:
            if v.name == name:
                return v
        return None

    def set_var(self, name, val):
        var_index = self.get_var_index_from_name(name)
        if var_index is None:
            return False

        var = self.variables[var_index]
        var.val = val
        self.update_variable_usages(var)
        return True

    def get_var_index_from_name(self, name):
        var_names_list = [v.name for v in self.variables]
        for i in range(len(var_names_list)):
            if var_names_list[i] == name:
                return i

        return None

    def update_all_var_usages(self):
        for v in self.variables:
            self.update_variable_usages(v)

    def update_variable_usages(self, v):
        get_var_NIs = []
        for ni in self.flow.all_node_instances:
            if find_type_in_object(ni, GetVar_NodeInstance):
                get_var_NIs.append(ni)

        for ni in get_var_NIs:
            if ni.get_current_var_name() == v.name:
                ni.update()


    def get_json_data(self):
        vars_dict = {}
        for v in self.variables:
            vars_dict[v.name] = v.val
        return vars_dict