from PySide2.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QPlainTextEdit, QShortcut
from PySide2.QtGui import QKeySequence


class EditVarVal_Dialog(QDialog):
    def __init__(self, parent, var):
        super(EditVarVal_Dialog, self).__init__(parent)

        # shortcut
        save_shortcut = QShortcut(QKeySequence.Save, self)
        save_shortcut.activated.connect(self.save_triggered)

        main_layout = QVBoxLayout()

        self.val_text_edit = QPlainTextEdit()
        var_val_str = ''
        try:
            var_val_str = str(var.val)
        except Exception as e:
            var_val_str = 'couldn\'nt stringify value'
        self.val_text_edit.setPlainText(var_val_str)

        main_layout.addWidget(self.val_text_edit)

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout.addWidget(button_box)

        self.setLayout(main_layout)
        self.resize(450, 300)

        self.setWindowTitle('edit var val \''+var.name+'\'')

    def save_triggered(self):
        self.accept()


    def get_val(self):
        val = self.val_text_edit.toPlainText()
        try:
            val = eval(val)
        except Exception as e:
            pass
        return val