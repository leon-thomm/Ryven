import re

from PySide2.QtWidgets import QWidget, QSizePolicy, QLineEdit, QColorDialog
from PySide2.QtCore import Qt
from PySide2.QtGui import QFontMetrics, QColor

from ui_node_manager_node_content_widget import Ui_Form
from Node import Node
from NodeInput import NodeInput
from NodeOutput import NodeOutput
from InputWidget import InputWidget


class NodeContentWidget(QWidget):
    def __init__(self):
        super(NodeContentWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.input_widgets_scrollArea.widget().layout().setAlignment(Qt.AlignTop)
        self.ui.inputs_scrollArea.widget().layout().setAlignment(Qt.AlignTop)
        self.ui.outputs_scrollArea.widget().layout().setAlignment(Qt.AlignTop)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # textEdit.setTabStopWidth(QFontMetrics(self.ui.textEdit.font()).width(' ') * 4)

        self.node: Node = None
        self.programming_type = ''
        self.has_main_widget = True
        self.inputs = []
        self.input_widgets = []
        self.outputs = []
        self.node_color = QColor(59, 156, 217)
        
        # src code
        f = open('template files/node_instance_default_template.txt', 'r')
        self.src_code = f.read()
        f.close()
        # main widget code
        f = open('template files/main_widget_default_template.txt', 'r')
        self.main_widget_code = f.read()
        f.close()

        self.ui.title_lineEdit.editingFinished.connect(self.title_lineEdit_edited)
        self.ui.intern_name_lineEdit.editingFinished.connect(self.intern_name_line_edit_edited)
        self.ui.use_title_as_intern_name_checkBox.toggled.connect(self.internal_name_check_box_toggled)
        self.ui.type_comboBox.currentTextChanged.connect(self.type_changed)
        self.ui.main_widget_checkBox.toggled.connect(self.main_widget_toggled)
        self.ui.select_color_pushButton.clicked.connect(self.select_node_color_clicked)
        self.ui.add_new_input_widget_pushButton.clicked.connect(self.add_new_input_widget_clicked)
        self.ui.add_new_input_pushButton.clicked.connect(self.add_new_input_clicked)
        self.ui.add_new_output_pushButton.clicked.connect(self.add_new_output_clicked)


    def load_node(self, node):
        self.node = node

        # synchronise with node
        self.ui.title_lineEdit.setText(node.title)
        if self.prepare_class_name(node.title) == node.class_name:
            self.ui.use_title_as_intern_name_checkBox.setChecked(True)
        else:
            self.ui.use_title_as_intern_name_checkBox.setChecked(False)
            self.ui.intern_name_lineEdit.setText(node.class_name)
        self.ui.description_textEdit.setText(node.description)
        print(node.type, node.title)
        if self.ui.type_comboBox.findText(node.type) != -1:
            self.ui.type_comboBox.setCurrentText(node.type)
        else:
            self.ui.type_comboBox.setCurrentText('custom')
            self.ui.custom_type_lineEdit.setText(node.type)
        self.src_code = node.meta_code

        # get all possible node types from the UI
        node_types_list = [self.ui.type_comboBox.itemText(i) for i in range(self.ui.type_comboBox.count())]
        try:
            if node_types_list.index(node.type) != len(node_types_list)-1:
                self.ui.type_comboBox.setCurrentText(node.type)
        except ValueError:
            pass

        if node.design_style == 'extended':
            self.ui.design_style_extended_radioButton.setChecked(True)
            self.ui.design_style_minimalistic_radioButton.setChecked(False)
        elif node.design_style == 'minimalistic':
            self.ui.design_style_extended_radioButton.setChecked(False)
            self.ui.design_style_minimalistic_radioButton.setChecked(True)

        self.node_color = QColor(node.color)

        print('setting has main widget to', node.has_main_widget)
        self.set_has_main_widget_manual(node.has_main_widget)
        if node.has_main_widget:
            widget_pos = node.widget_position
            if widget_pos == 'under ports':
                self.ui.main_widget_under_ports_radioButton.setChecked(True)
                self.ui.main_widget_between_ports_radioButton.setChecked(False)
            elif widget_pos == 'between ports':
                self.ui.main_widget_under_ports_radioButton.setChecked(False)
                self.ui.main_widget_between_ports_radioButton.setChecked(True)
            self.main_widget_code = node.main_widget_content

        for i in range(len(node.custom_input_widgets)):
            iw = node.custom_input_widgets[i]
            iw_content = node.custom_input_widget_contents[i]
            new_input_widget = InputWidget(self)
            new_input_widget.set_name(iw)
            new_input_widget.code = iw_content
            self.ui.input_widgets_scrollArea.widget().layout().addWidget(new_input_widget)
            self.input_widgets.append(new_input_widget)

        for i in node.inputs:
            i_type = i['type']
            i_label = i['label']
            i_has_widget = i['has widget'] if i_type == 'data' else None
            i_widget_type = i['widget type'] if i_has_widget else None
            i_widget_name = i['widget name'] if i_widget_type=='custom widget' else None
            i_widget_pos = i['widget position'] if i_has_widget else None
            self.add_new_input(i_type, i_label, i_has_widget, i_widget_type, i_widget_name, i_widget_pos)

        for o in node.outputs:
            self.add_new_output(o['type'], o['label'])


    def title_lineEdit_edited(self):  # only necessary for the title, the rest is stored here or in NodeInput/-Output
        line_edit: QLineEdit = self.sender()
        self.node.title = line_edit.text()
        self.node.title_changed.emit()

    def intern_name_line_edit_edited(self):
        line_edit: QLineEdit = self.sender()
        line_edit.setText(self.prepare_class_name(line_edit.text()))
        self.node.class_name = line_edit.text()

    def internal_name_check_box_toggled(self):
        if self.ui.use_title_as_intern_name_checkBox.isChecked():
            self.ui.intern_name_lineEdit.setEnabled(False)
        else:
            self.ui.intern_name_lineEdit.setEnabled(True)

    def type_changed(self, new_type):
        if new_type == 'custom':
            self.ui.custom_type_lineEdit.setEnabled(True)
        else:
            self.ui.custom_type_lineEdit.setEnabled(False)
            self.ui.custom_type_lineEdit.clear()


    def main_widget_toggled(self, checked):
        self.set_has_main_widget(not checked)

    def set_has_main_widget_manual(self, has_main_widget):
        self.ui.main_widget_checkBox.setChecked(not has_main_widget)
        self.set_has_main_widget(has_main_widget)

    def set_has_main_widget(self, has_main_widget):
        if not has_main_widget:
            self.ui.main_widget_position_widget.setEnabled(False)
            self.has_main_widget = False
        else:
            self.ui.main_widget_position_widget.setEnabled(True)
            self.has_main_widget = True


    def select_node_color_clicked(self):
        self.node_color = QColorDialog.getColor(self.node_color)
        ss = 'background-color: '+self.node_color.name()
        self.ui.color_sample_pushButton.setStyleSheet(ss)


    def add_new_input_widget_clicked(self):
        new_input_widget = InputWidget(self)
        self.ui.input_widgets_scrollArea.widget().layout().addWidget(new_input_widget)
        self.input_widgets.append(new_input_widget)

    def delete_input_widget(self, input_widget):
        input_widget.setParent(None)
        self.input_widgets.remove(input_widget)


    def add_new_input_clicked(self):
        self.add_new_input()

    def add_new_input(self, _type=None, label=None, has_widget=None, widget_type=None, widget_name=None, widget_pos=None):
        new_input = NodeInput(self)
        if _type:
            new_input.set_type(_type)
        if label:
            new_input.set_label(label)
        if has_widget != None:
            new_input.set_has_widget(has_widget)
            if has_widget:
                new_input.set_widget_type(widget_type)
                if widget_type == 'custom widget':
                    new_input.set_widget_name(widget_name)
                new_input.set_widget_pos(widget_pos)

        self.inputs.append(new_input)

        self.ui.inputs_scrollArea.widget().layout().addWidget(new_input)

    def delete_input(self, inp):
        self.inputs.remove(inp)
        inp.setParent(None)


    def add_new_output_clicked(self):
        self.add_new_output()

    def add_new_output(self, _type=None, label=None):
        new_output = NodeOutput(self)
        if _type:
            new_output.set_type(_type)
        if label:
            new_output.set_label(label)

        self.outputs.append(new_output)

        self.ui.outputs_scrollArea.widget().layout().addWidget(new_output)


    def delete_output(self, out):
        out.setParent(None)
        self.outputs.remove(out)


    def get_title(self):
        return self.ui.title_lineEdit.text()

    def get_intern_title(self):
        if self.ui.use_title_as_intern_name_checkBox.isChecked():
            return self.prepare_class_name(self.ui.title_lineEdit.text())
        else:
            return self.ui.intern_name_lineEdit.text()

    def get_description(self):
        return self.ui.description_textEdit.toPlainText()

    def get_type(self):
        node_type = self.ui.type_comboBox.currentText()
        if node_type == 'custom':
            node_type = self.ui.custom_type_lineEdit.text()
        return node_type
    
    def get_src_code(self):
        return self.src_code
    
    def get_main_widget_code(self):
        return self.main_widget_code

    def get_design_style(self):
        return 'extended' if self.ui.design_style_extended_radioButton.isChecked() else 'minimalistic'

    def get_main_widget_pos(self):
        under = self.ui.main_widget_under_ports_radioButton
        # between = self.ui.main_widget_between_ports_radioButton
        return 'under ports' if under.isChecked() else 'between ports'

    def prepare_class_name(self, s: str):
        # make upper
        s = ''.join([a if a.isupper() else b for a, b in zip(s, s.title())])

        # Remove invalid characters
        s = re.sub('[^0-9a-zA-Z_]', '', s)

        # Remove leading characters until we find a letter or underscore
        s = re.sub('^[^a-zA-Z_]+', '', s)

        return s