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
            <div style="font-family: Corbel; font-size: large;">

            <p>Yes, you can change method implementations of objects.
            This can be an extremely powerful feature! Especially when trying to understand nodes more 
            deeply, when creating new nodes and for debugging. But since changing an instance's implementation
            at runtime is pretty deep stuff, you should be a bit careful, this feature is not exactly bulletproof.
            This is what you can do:
            <ul>
                <li>You can edit the implementation of existing custom methods of...</li>
                <li>And you can add new methods to...</li>
            </ul>
            ... any <i>object</i> (a placed node and all its widgets). Other nodes of the same type won't be affected.
            </p>
            <p>
            <b>You can write any code that would be valid in the class's original source file.</b> If you defined some further
            classes in the metacode file, for example, you can still totally use them here.
            <br>
            There is just one issue that you may want to consider:
            <br>
            If you edit a method that gets called somewhere and you cannot see any effect, it may be due to a
            problem in the class's implementation that you are editing. Because whenever a reference of a <i>method</i>
            is used (like
            <i>self.print_something</i>, e.g. for connecting Qt signals to
            slots or in the <i>special_actions</i> dict),
            instead of directly using the object, it should be passed using M() (<i>M(self.print_something)</i>)
            which ensures that a referenced and edited method gets called correctly.
            Otherwise the method reference would always link to the original method, not the edited one.
            <br><br>
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
