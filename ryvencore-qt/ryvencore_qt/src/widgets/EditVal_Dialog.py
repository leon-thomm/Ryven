from qtpy.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QPlainTextEdit, QShortcut, QMessageBox
from qtpy.QtGui import QKeySequence


class EditVal_Dialog(QDialog):

    def __init__(self, parent, init_val):
        super(EditVal_Dialog, self).__init__(parent)

        # shortcut
        save_shortcut = QShortcut(QKeySequence.Save, self)
        save_shortcut.activated.connect(self.save_triggered)

        main_layout = QVBoxLayout()

        self.val_text_edit = QPlainTextEdit()
        val_str = ''
        try:
            val_str = str(init_val)
        except Exception as e:
            msg_box = QMessageBox(QMessageBox.Warning, 'Value parsing failed',
                                  'Couldn\'t stringify value', QMessageBox.Ok, self)
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec_()
            self.reject()

        self.val_text_edit.setPlainText(val_str)

        main_layout.addWidget(self.val_text_edit)

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout.addWidget(button_box)

        self.setLayout(main_layout)
        self.resize(450, 300)

        self.setWindowTitle('edit val')

    def save_triggered(self):
        self.accept()


    def get_val(self):
        val = self.val_text_edit.toPlainText()
        try:
            val = eval(val)
        except Exception as e:
            pass
        return val