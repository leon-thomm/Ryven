from PySide2.QtWidgets import QVBoxLayout, QWidget
from PySide2.QtCore import Qt

from custom_src.custom_list_widgets.VarsList_VarWidget import VarsList_VarWidget


class VariablesListWidget(QWidget):
    """This is the list widget you can see on the right side in the editor, showing all existent variables of a script.
    This class equals ScriptsListWidget by far, but I don't want to put them under the same base class since they
    actually represent very different things (scripts and variables) and therefore might develop quite differently
    in the future."""

    def __init__(self, vars_manager):
        super(VariablesListWidget, self).__init__()

        self.vars_manager = vars_manager
        self.widgets = []
        self.currently_edited_var = ''
        self.ignore_name_line_edit_signal = False  # because disabling causes firing twice otherwise
        # self.data_type_line_edits = []  # same here

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        self.recreate_ui()


    def recreate_ui(self):
        for w in self.widgets:
            w.hide()
            del w

        self.widgets.clear()
        # self.data_type_line_edits.clear()

        for v in self.vars_manager.variables:
            new_widget = VarsList_VarWidget(self, self.vars_manager, v)
            new_widget.name_LE_editing_finished.connect(self.name_line_edit_editing_finished)
            self.widgets.append(new_widget)

        self.rebuild_ui()


    def rebuild_ui(self):
        for i in range(self.layout().count()):
            self.layout().removeItem(self.layout().itemAt(0))

        for w in self.widgets:
            self.layout().addWidget(w)


    def name_line_edit_editing_finished(self):
        var_widget: VarsList_VarWidget = self.sender()
        var_widget.name_line_edit.setEnabled(False)

        # search for name problems
        new_var_name = var_widget.name_line_edit.text()
        for v in self.vars_manager.variables:
            if v.name == new_var_name:
                var_widget.name_line_edit.setText(self.currently_edited_var.name)
                return

        var_widget.var.name = new_var_name


    def del_variable(self, var, var_widget):
        self.widgets.remove(var_widget)
        var_widget.setParent(None)
        del self.vars_manager.variables[self.vars_manager.variables.index(var)]
        self.recreate_ui()