from PySide2.QtWidgets import QVBoxLayout, QWidget, QLineEdit
from PySide2.QtCore import Qt

from ryvencore.custom_list_widgets.VarsList_VarWidget import VarsList_VarWidget


class VariablesListWidget(QWidget):
    """This is the list widget you can see on the right side in the editor, showing all existent variables of a script.
    This class equals ScriptsListWidget by far, but I don't want to put them under the same base class since they
    actually represent very different things (scripts and variables) and therefore might develop quite differently
    in the future."""


    def __init__(self, vars_manager):
        super(VariablesListWidget, self).__init__()

        self.vars_manager = vars_manager
        self.vars_manager.new_var_created.connect(self.add_new_var)
        self.widgets = []
        self.currently_edited_var = ''
        self.ignore_name_line_edit_signal = False  # because disabling causes firing twice otherwise
        # self.data_type_line_edits = []  # same here

        self.setup_UI()


    def setup_UI(self):
        main_layout = QVBoxLayout()

        self.list_layout = QVBoxLayout()
        self.list_layout.setAlignment(Qt.AlignTop)

        # w = QWidget()
        # w.setLayout(self.list_layout)
        #
        # scroll_area = QScrollArea()
        # scroll_area.setLayout(QVBoxLayout())
        # scroll_area.setWidget(w)
        #
        # main_layout.addWidget(scroll_area)
        main_layout.addLayout(self.list_layout)

        self.new_var_name_lineedit = QLineEdit()
        self.new_var_name_lineedit.setPlaceholderText('new var\'s title')
        self.new_var_name_lineedit.returnPressed.connect(self.new_var_LE_return_pressed)

        main_layout.addWidget(self.new_var_name_lineedit)

        self.setLayout(main_layout)

        self.recreate_list()


    def recreate_list(self):
        for w in self.widgets:
            w.hide()
            del w

        self.widgets.clear()
        # self.data_type_line_edits.clear()

        for v in self.vars_manager.variables:
            new_widget = VarsList_VarWidget(self, self.vars_manager, v)
            # new_widget.name_LE_editing_finished.connect(self.name_line_edit_editing_finished)
            self.widgets.append(new_widget)

        self.rebuild_list()


    def rebuild_list(self):
        for i in range(self.layout().count()):
            self.list_layout.removeItem(self.layout().itemAt(0))

        for w in self.widgets:
            self.list_layout.addWidget(w)


    def new_var_LE_return_pressed(self):
        name = self.new_var_name_lineedit.text()

        if not self.vars_manager.check_new_var_name_validity(name=name):
            return

        self.vars_manager.create_new_var(name=name)


    def add_new_var(self, var):
        self.recreate_list()


    # def name_line_edit_editing_finished(self):
    #     var_widget: VarsList_VarWidget = self.sender()
    #     var_widget.name_line_edit.setEnabled(False)
    #
    #     # search for name issues
    #     new_var_name = var_widget.name_line_edit.text()
    #     for v in self.vars_manager.variables:
    #         if v.name == new_var_name:
    #             var_widget.name_line_edit.setText(self.currently_edited_var.name)
    #             return
    #
    #     var_widget.var.name = new_var_name


    def del_variable(self, var, var_widget):
        self.widgets.remove(var_widget)
        var_widget.setParent(None)
        self.vars_manager.delete_variable(var)
        # del self.vars_manager.variables[self.vars_manager.variables.index(var)]
        self.recreate_list()