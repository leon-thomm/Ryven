from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QMessageBox, QRadioButton, QSizePolicy
from PySide2.QtCore import Qt


class InputWidget(QWidget):
    def __init__(self, content_widget):
        super(InputWidget, self).__init__()

        self.content_widget = content_widget

        self.main_grid_layout = QGridLayout()

        self.name_line_edit = QLineEdit()
        self.name_line_edit.setPlaceholderText('widget name')
        self.name_line_edit.editingFinished.connect(self.name_line_edit_edited)
        self.main_grid_layout.addWidget(self.name_line_edit, 0, 0, 1, 2)

        self.del_button = QPushButton()
        self.del_button.setText('delete')
        self.del_button.clicked.connect(self.delete_clicked)

        self.main_grid_layout.addWidget(self.del_button, 1, 1)


        self.setLayout(self.main_grid_layout)

        f = open('template files/input_widget_default_template.txt', 'r')
        self.code = f.read()
        f.close()


    def delete_clicked(self):
        ret = QMessageBox.warning(self, 'Input Widget', 'Do you really want to delete this input widget? All changes'
                                                        'will be lost.',
                                  QMessageBox.Yes, QMessageBox.No)
        if ret == QMessageBox.Yes:
            self.content_widget.delete_input_widget(self)

    def set_name(self, new_name):
        self.name_line_edit.setText(new_name)

    def get_name(self):
        return self.content_widget.prepare_class_name(self.name_line_edit.text())
    
    def get_code(self):
        return self.code

    def name_line_edit_edited(self):
        self.name_line_edit.setText(self.content_widget.prepare_class_name(self.name_line_edit.text()))