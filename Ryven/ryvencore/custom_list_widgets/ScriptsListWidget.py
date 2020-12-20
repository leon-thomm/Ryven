from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLineEdit

from ryvencore.custom_list_widgets.ScriptsList_ScriptWidget import ScriptsList_ScriptWidget



class ScriptsListWidget(QWidget):
    """This is the list widget you can see on the left side in the editor, showing all existent scripts.
    This class equals VariablesListWidget by far, but I don't want to put them under the same base class since they
    actually represent very different things (scripts and variables) and therefore might develop quite differently
    in the future."""



    def __init__(self, session):
        super(ScriptsListWidget, self).__init__()

        self.session = session
        self.session.new_script_created.connect(self.add_new_script)

        self.list_widgets = []
        self.ignore_name_line_edit_signal = False  # because disabling causes firing twice otherwise

        self.setup_UI()


    def setup_UI(self):
        main_layout = QVBoxLayout()
        # main_layout.setAlignment(Qt.AlignBottom)

        self.list_layout = QVBoxLayout()
        self.list_layout.setAlignment(Qt.AlignTop)

        main_layout.addLayout(self.list_layout)

        self.new_script_title_lineedit = QLineEdit()
        self.new_script_title_lineedit.setPlaceholderText('new script\'s title')
        self.new_script_title_lineedit.returnPressed.connect(self.new_script_LE_return_pressed)

        main_layout.addWidget(self.new_script_title_lineedit)

        self.setLayout(main_layout)

        self.recreate_list()


    def recreate_list(self):
        for w in self.list_widgets:
            w.hide()
            del w

        self.list_widgets.clear()

        for s in self.session.scripts:
            new_widget = ScriptsList_ScriptWidget(self, self.session, s)
            self.list_widgets.append(new_widget)

        self.rebuild_list()


    def rebuild_list(self):
        for i in range(self.layout().count()):
            self.list_layout.removeItem(self.layout().itemAt(0))

        for w in self.list_widgets:
            self.list_layout.addWidget(w)


    def new_script_LE_return_pressed(self):
        title = self.new_script_title_lineedit.text()

        if not self.session.check_new_script_title_validity(title):
            return

        self.session.create_script(title=title)

    def add_new_script(self, script):
        self.recreate_list()


    def del_script(self, script, script_widget):
        msg_box = QMessageBox(QMessageBox.Warning, 'sure about deleting script?',
                              'You are about to delete a script. This cannot be undone, all content will be lost. '
                              'Do you want to continue?', QMessageBox.Cancel | QMessageBox.Yes, self)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        ret = msg_box.exec_()
        if ret != QMessageBox.Yes:
            return

        self.list_widgets.remove(script_widget)
        script_widget.setParent(None)
        self.session.delete_script(script)
        self.recreate_list()
