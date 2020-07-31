from PySide2.QtWidgets import QWidget, QPlainTextEdit, QRadioButton, QGridLayout, QPushButton, QComboBox, QLineEdit, \
    QGroupBox, QVBoxLayout


class NodeInput(QWidget):
    def __init__(self, content_widget):
        super(NodeInput, self).__init__()

        self.content_widget = content_widget
        self.widget_type = ''  # gets specified automatically when creating ui below (see self.widget_combo_box_changed)

        # create UI

        # create all layouts
        self.grid_layout = QGridLayout(self)

        # # move buttons TODO move buttons
        # self.up_button = QPushButton('<')
        # self.down_button = QPushButton('>')

        # type and label
        self.type_combo_box = QComboBox(self)
        self.type_combo_box.addItem('exec')
        self.type_combo_box.addItem('data')
        self.type_combo_box.currentTextChanged.connect(self.type_combo_box_changed)
        self.label_text_edit = QPlainTextEdit(self)
        self.label_text_edit.setPlaceholderText('Label')
        self.label_text_edit.setFixedWidth(self.type_combo_box.width())
        # self.label_text_edit.setMinimumHeight(20)
        self.label_text_edit.setMaximumHeight(92)

        # widget
        self.widget_grid_layout = QGridLayout()
        self.widget_yes_no_group_box = QGroupBox(self)
        self.widget_yes_no_group_box.setEnabled(False)
        self.widget_yes_no_group_box.setLayout(QVBoxLayout())
        self.widget_yes_radio_button = QRadioButton('Yes', self)
        self.widget_yes_radio_button.setChecked(True)
        self.widget_yes_radio_button.toggled.connect(self.widget_yes_set)
        self.widget_no_radio_button = QRadioButton('No', self)
        self.widget_yes_no_group_box.layout().addWidget(self.widget_yes_radio_button)
        self.widget_yes_no_group_box.layout().addWidget(self.widget_no_radio_button)
        self.widget_grid_layout.addWidget(self.widget_yes_no_group_box, 0, 0, 4, 1)

        self.widget_group_box = QGroupBox(self)
        self.widget_group_box.setEnabled(False)
        self.widget_group_box.setLayout(QVBoxLayout())
        self.std_widget_combo_box = QComboBox(self)
        self.std_widget_combo_box.addItem('std line edit s')
        self.std_widget_combo_box.addItem('std line edit m')
        self.std_widget_combo_box.addItem('std line edit l')
        self.std_widget_combo_box.addItem('std line edit s r')
        self.std_widget_combo_box.addItem('std line edit m r')
        self.std_widget_combo_box.addItem('std line edit l r')
        self.std_widget_combo_box.addItem('std line edit s r nb')
        self.std_widget_combo_box.addItem('std line edit m r nb')
        self.std_widget_combo_box.addItem('std line edit l r nb')
        self.std_widget_combo_box.addItem('std spin box')
        self.std_widget_combo_box.addItem('custom widget')
        self.std_widget_combo_box.setCurrentIndex(1)
        self.std_widget_combo_box.currentTextChanged.connect(self.widget_type_combo_box_changed)
        self.custom_widget_line_edit = QLineEdit()
        self.custom_widget_line_edit.setPlaceholderText('input widget name')
        self.custom_widget_line_edit.editingFinished.connect(self.widget_name_line_edit_edited)
        self.custom_widget_line_edit.setEnabled(False)

        self.widget_under_label_radio_button = QRadioButton('widget under label')
        self.widget_under_label_radio_button.setChecked(True)
        self.widget_besides_label_radio_button = QRadioButton('widget besides label')

        self.widget_group_box.layout().addWidget(self.std_widget_combo_box)
        self.widget_group_box.layout().addWidget(self.custom_widget_line_edit)
        self.widget_group_box.layout().addWidget(self.widget_under_label_radio_button)
        self.widget_group_box.layout().addWidget(self.widget_besides_label_radio_button)

        self.widget_grid_layout.addWidget(self.widget_group_box, 0, 3, 4, 1)

        # del button
        self.del_button = QPushButton(self)
        self.del_button.setText(' Del ')
        self.del_button.clicked.connect(self.delete_clicked)

        # create layout
        # self.grid_layout.addWidget(self.up_button, 0, 0, 1, 1)
        # self.grid_layout.addWidget(self.down_button, 3, 0, 1, 1)
        self.grid_layout.addWidget(self.type_combo_box, 0, 1)
        self.grid_layout.addWidget(self.label_text_edit, 1, 1, 3, 1)
        self.grid_layout.addLayout(self.widget_grid_layout, 0, 2, 4, 1)
        self.grid_layout.addWidget(self.del_button, 0, 4, 4, 1)






    def get_type(self):
        return self.type_combo_box.currentText()

    def get_label(self):
        return self.label_text_edit.toPlainText()

    def has_widget(self):
        return self.widget_yes_radio_button.isChecked()

    def set_has_widget(self, has_widget):
        if has_widget:
            self.widget_yes_radio_button.setChecked(True)
            self.widget_no_radio_button.setChecked(False)
        else:
            self.widget_yes_radio_button.setChecked(False)
            self.widget_no_radio_button.setChecked(True)

    def get_widget_name(self):
        if self.std_widget_combo_box.currentText() == 'custom widget':
            return self.content_widget.generate_class_name(self.custom_widget_line_edit.text())
        else:
            return self.std_widget_combo_box.currentText()

    def set_widget_name(self, name):
        if self.std_widget_combo_box.findText(name) != -1:
            self.std_widget_combo_box.setCurrentText(name)
        elif name == 'std line edit':  # 'std line edit' is an old name for 'std line edit m'
            self.std_widget_combo_box.setCurrentText('std line edit m')
        else:
            self.std_widget_combo_box.setCurrentText('custom widget')
            self.custom_widget_line_edit.setText(name)

    def get_widget_pos(self):
        under = self.widget_under_label_radio_button
        return 'under' if under.isChecked() else 'besides'

    def set_widget_pos(self, pos):
        if pos == 'under':
            self.widget_under_label_radio_button.setChecked(True)
            self.widget_besides_label_radio_button.setChecked(False)
        elif pos == 'besides':
            self.widget_under_label_radio_button.setChecked(False)
            self.widget_besides_label_radio_button.setChecked(True)

    def widget_yes_set(self):
        if self.widget_yes_radio_button.isChecked():
            self.widget_group_box.setEnabled(True)
        else:
            self.widget_group_box.setEnabled(False)

    def widget_name_line_edit_edited(self):
        self.custom_widget_line_edit.setText(self.content_widget.generate_class_name(self.custom_widget_line_edit.text()))


    def widget_type_combo_box_changed(self, new_text):
        self.widget_type = new_text
        if new_text == 'custom widget':
            self.custom_widget_line_edit.setEnabled(True)
        else:
            self.custom_widget_line_edit.setEnabled(False)

    def set_type(self, new_type):
        self.type_combo_box.setCurrentText(new_type)

    def type_combo_box_changed(self, new_type):
        if new_type == 'data':
            self.widget_yes_no_group_box.setEnabled(True)
            self.widget_group_box.setEnabled(True)
        elif new_type == 'exec':
            self.widget_yes_no_group_box.setEnabled(False)
            self.widget_group_box.setEnabled(False)

    def set_label(self, new_label):
        self.label_text_edit.setPlainText(new_label)

    def delete_clicked(self):
        self.content_widget.delete_input(self)