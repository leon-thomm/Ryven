from PySide2.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton, QCheckBox, QHBoxLayout, QGridLayout


class EditSrcCodeInfoDialog(QDialog):

    dont_show_again = False

    def __init__(self, parent):
        super(EditSrcCodeInfoDialog, self).__init__(parent)

        self.setLayout(QGridLayout())

        # info text edit
        info_text_edit = QTextEdit()
        info_text_edit.setHtml('''
            <h2 style="font-family: Poppins; font-size: xx-large; color: #a9d5ef;">Some info before you delete the
            universe</h2>
            <div style="font-family: Corbel; font-size: x-large;">
                <p>
                    Yes, you can change method implementations of objects.
                    This can be quite useful for understanding a node's implementation, for designing new nodes 
                    and for debugging. But since changing an instance's implementation at runtime is kinda sketchy, 
                    you should be a bit careful, this feature is not exactly bulletproof, and doesnt <i>always</i> work.
                    You can override implementations of methods and add new methods to a single node object
                    or its custom widgets.
                    Other nodes of the same type won't be affected.
                    Changes made to the source code are temporary and don't get saved.
                </p>
                <p>
                    Have fun.
                </p>
            </div>
        ''')
        info_text_edit.setReadOnly(True)
        self.layout().addWidget(info_text_edit, 0, 0, 1, 2)

        dont_show_again_button = QPushButton('Stop being annoying')
        dont_show_again_button.clicked.connect(self.close_and_dont_show_again)
        self.layout().addWidget(dont_show_again_button, 1, 0)

        ok_button = QPushButton('Got it')
        ok_button.clicked.connect(self.accept)
        self.layout().addWidget(ok_button, 1, 1)

        ok_button.setFocus()

        self.setWindowTitle('Editing Source Code Info')
        self.resize(560, 366)

    def close_and_dont_show_again(self):
        EditSrcCodeInfoDialog.dont_show_again = True
        self.accept()
