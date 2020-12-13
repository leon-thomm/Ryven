from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QMessageBox, QVBoxLayout

from custom_src.custom_list_widgets.ScriptsList_ScriptWidget import ScriptsList_ScriptWidget



class ScriptsListWidget(QWidget):
    """This is the list widget you can see on the left side in the editor, showing all existent scripts.
    This class equals VariablesListWidget by far, but I don't want to put them under the same base class since they
    actually represent very different things (scripts and variables) and therefore might develop quite differently
    in the future."""

    def __init__(self, main_window, scripts):
        super(ScriptsListWidget, self).__init__()

        self.main_window = main_window
        self.scripts = scripts
        self.widgets = []
        self.currently_edited_script = ''
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

        for s in self.scripts:
            new_widget = ScriptsList_ScriptWidget(self, s)
            new_widget.name_LE_editing_finished.connect(self.name_line_edit_editing_finished)
            self.widgets.append(new_widget)

        self.rebuild_ui()


    def rebuild_ui(self):
        for i in range(self.layout().count()):
            self.layout().removeItem(self.layout().itemAt(0))

        for w in self.widgets:
            self.layout().addWidget(w)



    def name_line_edit_editing_finished(self):
        script_widget: ScriptsList_ScriptWidget = self.sender()
        script_widget.name_line_edit.setEnabled(False)

        # search for name problems
        new_script_name = script_widget.name_line_edit.text()
        for s in self.scripts:
            if s.name == new_script_name:
                script_widget.name_line_edit.setText(self.currently_edited_script.name)
                return

        self.main_window.rename_script(script_widget.script, new_script_name)


    def del_script(self, script, script_widget):
        msg_box = QMessageBox(QMessageBox.Warning, 'sure about deleting script?',
                              'You are about to delete a script. This cannot be undone, all content will be lost. '
                              'Do you want to continue?', QMessageBox.Cancel | QMessageBox.Yes, self)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        ret = msg_box.exec_()
        if ret != QMessageBox.Yes:
            return

        self.widgets.remove(script_widget)
        script_widget.setParent(None)
        self.main_window.delete_script(script)
        self.recreate_ui()