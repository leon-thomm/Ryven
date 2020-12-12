from PySide2.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton, QMessageBox

from CodeEditor.CodeEditor_Dialog import CodeEditor_Dialog
from EditSrcCode_PushButton import EditSrcCode_PushButton


class CustomInputWidget(QWidget):
    def __init__(self, content_widget, metacode_file_path=None):
        super(CustomInputWidget, self).__init__()

        self.content_widget = content_widget
        self.edit_input_widget_metacode_dialog = CodeEditor_Dialog(self)
        if metacode_file_path is None:
            f = open('template files/input_widget_default_template.txt', 'r')
            self.edit_input_widget_metacode_dialog.set_code(f.read())
            f.close()
        else:
            f = open(metacode_file_path)
            self.edit_input_widget_metacode_dialog.set_code(f.read(), metacode_file_path)
            f.close()

        self.main_grid_layout = QGridLayout()

        self.name_line_edit = QLineEdit()
        self.name_line_edit.setPlaceholderText('widget name')
        self.name_line_edit.editingFinished.connect(self.name_line_edit_edited)
        self.main_grid_layout.addWidget(self.name_line_edit, 0, 0, 1, 2)

        edit_metacode_button = EditSrcCode_PushButton('edit metacode')
        edit_metacode_button.clicked.connect(self.edit_metacode_button_clicked)
        self.main_grid_layout.addWidget(edit_metacode_button, 1, 0, 1, 1)

        self.del_button = QPushButton()
        self.del_button.setText('delete')
        self.del_button.clicked.connect(self.delete_clicked)

        self.main_grid_layout.addWidget(self.del_button, 1, 1)


        self.setLayout(self.main_grid_layout)



    def edit_metacode_button_clicked(self):
        self.edit_input_widget_metacode_dialog.exec_()

    def delete_clicked(self):
        ret = QMessageBox.warning(self, 'Deleting custom input widget',
                                  'Do you really want to delete this input widget? All changes '
                                  'will be lost including any edited code.',
                                  QMessageBox.Yes, QMessageBox.No)
        if ret == QMessageBox.Yes:
            self.content_widget.delete_input_widget(self)

    def get_name(self):
        return self.content_widget.generate_class_name(self.name_line_edit.text())

    def set_name(self, new_name):
        self.name_line_edit.setText(new_name)

    def get_code(self):
        return self.edit_input_widget_metacode_dialog.get_code()

    def name_line_edit_edited(self):
        self.name_line_edit.setText(self.content_widget.generate_class_name(self.name_line_edit.text()))