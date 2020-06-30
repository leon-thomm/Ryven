from PySide2.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton


class EditSourceCode_Dialog(QDialog):
    def __init__(self, parent):
        super(EditSourceCode_Dialog, self).__init__(parent)

        self.setLayout(QVBoxLayout())

        # info text edit
        info_text_edit = QTextEdit()
        info_text_edit.setHtml('''
            <h2 style="font-family: Poppins; font-size: xx-large; color: #a9d5ef;">Info</h2>
            <div style="font-family: Corbel; font-size: x-large;">

            <p>This is an extremely useful feature! You should be a bit careful though, it's not exactly bulletproof.
            This is what you can do:
            <ul>
                <li>You can edit the implementation of existing custom methods</li>
                <li>And you can add new methods</li>
                <li>Note that changing a method that has been connected as a slot to the event of a Qt object will not 
                change the behavior when this event is being called. In other words: you cannot change a slot after it
                has been connected to an event (PySide2 behavior).</li>
            </ul>
            </p>
            <p>
            <b>You can write any code that would be valid in the class's original source file.</b> If you defined some further
            classes in the metacode file, for example, you can still totally use them here.
            </p>
            </div>
        ''')
        info_text_edit.setReadOnly(True)
        self.layout().addWidget(info_text_edit)

        ok_button = QPushButton('Got it')
        ok_button.clicked.connect(self.accept)
        self.layout().addWidget(ok_button)
        ok_button.setFocus()

        self.setWindowTitle('Editing Source Code Info')
        self.resize(560, 366)