from qtpy.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton


class GetTextDialog(QDialog):
    def __init__(self, window_title='', init_text='', placeholder_text='', parent=None):
        super().__init__(parent=parent)
        self.text = ''
        self.setLayout(QVBoxLayout())
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(placeholder_text)
        self.line_edit.setText(init_text)
        self.line_edit.returnPressed.connect(self.returned)
        self.layout().addWidget(self.line_edit)
        self.setWindowTitle(window_title)

    def returned(self):
        self.text = self.line_edit.text()
        self.accept()

    def get_text(self):
        self.exec_()
        return self.text


class ChooseFlowDialog(QDialog):
    def __init__(self, window_title, flows, parent=None):
        super().__init__(parent)

        self.flow = None
        self.button_flows = {}

        self.setLayout(QVBoxLayout())
        for s in flows:
            b = QPushButton(s.title)
            b.pressed.connect(self.button_pressed)
            self.button_flows[b] = s
            self.layout().addWidget(b)

        self.setWindowTitle(window_title)

    def button_pressed(self):
        self.flow = self.button_flows[self.sender()]
        self.accept()

    def get_flow(self):
        self.exec_()
        return self.flow
