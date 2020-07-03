from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton, QComboBox, QLineEdit, QMessageBox


class NodeOutput(QWidget):
    def __init__(self, content_widget):
        super(NodeOutput, self).__init__()

        self.content_widget = content_widget

        # create UI

        # create all layouts
        self.grid_layout = QGridLayout(self)

        # # move buttons TODO move buttons
        # self.up_button = QPushButton(self, '')
        # self.down_button = QPushButton(self, '')

        # type and label
        self.type_combo_box = QComboBox(self)
        self.type_combo_box.addItem('exec')
        self.type_combo_box.addItem('data')
        self.label_line_edit = QLineEdit(self)
        self.label_line_edit.setPlaceholderText('Label')

        # del button
        self.del_button = QPushButton(self)
        self.del_button.setText(' Del ')
        self.del_button.clicked.connect(self.delete_clicked)

        # merge layouts
        # self.grid_layout.addWidget(self.up_button, 0, 0)
        # self.grid_layout.addWidget(self.down_button, 1, 0)
        self.grid_layout.addWidget(self.type_combo_box, 0, 1)
        self.grid_layout.addWidget(self.label_line_edit, 1, 1)
        self.grid_layout.addWidget(self.type_combo_box, 0, 1)
        self.grid_layout.addWidget(self.del_button, 0, 2, 2, 1)




    def get_type(self):
        return self.type_combo_box.currentText()

    def get_label(self):
        return self.label_line_edit.text()


    def set_type(self, new_type):
        self.type_combo_box.setCurrentText(new_type)

    def set_label(self, new_label):
        self.label_line_edit.setText(new_label)

    def delete_clicked(self):
        self.content_widget.delete_output(self)