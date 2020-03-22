from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import QObject, Signal

from custom_src.GlobalAccess import GlobalStorage
from custom_src.Log import Logger

from ui.w_ui_script import WUIScript

# from custom_src.VyMain_DetailsWidget import VyMain_DetailsWidget
from custom_src.Flow import Flow
from custom_src.Variable import Variable
from custom_src.VariablesListWidget import VariablesCustomListWidget


class Script(QObject):

    name_changed = Signal(str)

    def __init__(self, main_window, name, config=None):
        super(Script, self).__init__()

        self.main_window = main_window
        self.widget = WUIScript()

        # general attributes
        self.logger = Logger(self)
        self.variables = []
        self.name = name
        self.details_widget = QPushButton('HELO HELOO!!')  # None
        self.set_details_widget(self, self.details_widget)
        self.flow = None
        self.thumbnail_source = ''  # URL to the thumbnail picture

        # variables list widget
        self.custom_variables_list_widget = VariablesCustomListWidget(self.variables)
        self.widget.ui.variables_scrollArea.setWidget(self.custom_variables_list_widget)
        # self.widget.ui.new_var_name_lineEdit.editingFinished.connect(self.create_new_var_triggered)
        self.widget.ui.add_variable_push_button.clicked.connect(self.add_var_clicked)
        self.widget.ui.new_var_name_lineEdit.returnPressed.connect(self.new_var_line_edit_return_pressed)


        if config:
            self.name = config['name']
            for name in list(config['variables'].keys()):  # variables
                self.variables.append(Variable(name, config['variables'][name]))
            self.custom_variables_list_widget.recreate_ui()
            self.flow = Flow(main_window, self, config['flow'])
        else:
            self.flow = Flow(main_window, self)

        self.widget.ui.splitter.insertWidget(0, self.flow)
        # self.widget.ui.logs_scrollArea.setWidgetResizable(False)
        self.widget.ui.logs_scrollArea.setWidget(self.logger)
        self.widget.ui.splitter.setSizes([700, 0])


    # def set_design_style(self, new_design):
    #     self.flow.set_design_style(new_design)

    def set_details_widget(self, provider, w):
        pass


    # def add_new_variable(self):
    #     self.create_variable()

    # def create_variable(self, data_type='', name=''):
    #     # create variable object
    #     new_variable = self.main_window.create_new_variable(self)
    #     new_variable.change_data_type(data_type)
    #     new_variable.change_name(name)
    #     self.add_existing_variable_and_update_ui(new_variable)

    # def add_existing_variable_and_update_ui(self, v):
    #     self.vy_variables.append(v)
    #
    #     # add new variable to list
    #     self.custom_variables_list_widget.recreate_ui()

    def add_var_clicked(self):
        self.create_new_var(self.widget.ui.new_var_name_lineEdit.text())

    def new_var_line_edit_return_pressed(self):
        self.create_new_var(self.widget.ui.new_var_name_lineEdit.text())

    # def create_new_var_triggered(self):
    #     self.create_new_var(self.widget.ui.new_var_name_lineEdit.text())

    def create_new_var(self, new_var_name):
        if len(new_var_name) == 0:
            return
        # search for name problems
        for v in self.variables:
            if v.name == new_var_name:
                return

        self.variables.append(Variable(new_var_name))
        self.custom_variables_list_widget.recreate_ui()


    def set_var(self, var_name, val):
        GlobalStorage.debug('setting var in script name:', var_name, 'to val:', val)

        var_index = self.get_var_index_from_name(var_name)
        if var_index is None:
            return False

        self.variables[var_index].val = val
        return True

    def get_var(self, var_name):
        GlobalStorage.debug('getting variable from script name:', var_name)

        var_index = self.get_var_index_from_name(var_name)
        if var_index is None:
            return

        return self.variables[var_index]

    def get_var_index_from_name(self, var_name):
        var_names_list = [v.name for v in self.variables]
        for i in range(len(var_names_list)):
            if var_names_list[i] == var_name:
                return i

        return None


    def get_json_data(self):
        vars_dict = {}
        for v in self.variables:
            vars_dict[v.name] = v.val

        script_dict = {'name': self.name,
                       'variables': vars_dict,
                       'flow': self.flow.get_json_data()}

        return script_dict