import re, os

from PySide2.QtWidgets import QWidget, QSizePolicy, QLineEdit, QColorDialog, QMessageBox
from PySide2.QtCore import Qt
from PySide2.QtGui import QFontMetrics, QColor

from CodeEditor.CodeEditor_Dialog import CodeEditor_Dialog
from EditSrcCode_PushButton import EditSrcCode_PushButton
from files_manager import save_file
from ui_node_manager_node_content_widget import Ui_Form
from Node import Node
from NodeInput import NodeInput
from NodeOutput import NodeOutput
from CustomInputWidget import CustomInputWidget


class NodeContentWidget(QWidget):
    def __init__(self):
        super(NodeContentWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.input_widgets_scrollArea.widget().layout().setAlignment(Qt.AlignTop)
        self.ui.inputs_scrollArea.widget().layout().setAlignment(Qt.AlignTop)
        self.ui.outputs_scrollArea.widget().layout().setAlignment(Qt.AlignTop)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.node: Node = None
        self.programming_type = ''
        self.inputs = []
        self.input_widgets = []
        self.outputs = []
        self.node_color = QColor(59, 156, 217)
        self.edit_node_metacode_dialog = CodeEditor_Dialog(self)
        self.edit_main_widget_metacode_dialog = CodeEditor_Dialog(self)

        self.ui.title_lineEdit.editingFinished.connect(self.title_lineEdit_edited)
        self.ui.internal_name_lineEdit.editingFinished.connect(self.internal_name_line_edit_edited)
        self.ui.auto_generate_internal_name_checkBox.toggled.connect(self.internal_name_check_box_toggled)
        self.ui.type_comboBox.currentTextChanged.connect(self.type_changed)

        # replace src code placeholder buttons
        self.ui.edit_node_metacode_placeholderButton.setParent(None)
        edit_node_MC_button = EditSrcCode_PushButton('edit node metacode')
        self.ui.top_horizontalLayout.insertWidget(1, edit_node_MC_button)
        edit_node_MC_button.clicked.connect(self.edit_node_metacode_clicked)
        self.ui.edit_main_widget_metacode_placeholderButton.setParent(None)
        edit_MW_MC_button = EditSrcCode_PushButton('edit metacode')
        self.ui.main_widget_position_widget.layout().addWidget(edit_MW_MC_button)
        edit_MW_MC_button.clicked.connect(self.edit_main_widget_metacode_clicked)
        self.ui.main_widget_checkBox.toggled.connect(self.main_widget_toggled)
        # self.ui.edit_main_widget_metacode_pushButton.clicked.connect(self.edit_main_widget_metacode_clicked)

        self.ui.select_color_pushButton.clicked.connect(self.select_node_color_clicked)
        self.ui.add_new_input_widget_pushButton.clicked.connect(self.add_new_input_widget_clicked)
        self.ui.add_new_input_pushButton.clicked.connect(self.add_new_input_clicked)
        self.ui.add_new_output_pushButton.clicked.connect(self.add_new_output_clicked)

        self.ui.splitter.setSizes([80, 100, 300])


    def load_node(self, node):
        self.node = node

        # synchronise with node
        self.ui.title_lineEdit.setText(node.title)
        if node.class_name is not None:
            if self.generate_class_name(node.title) != node.class_name:
                self.ui.auto_generate_internal_name_checkBox.setChecked(False)
            self.ui.internal_name_lineEdit.setText(node.class_name)
        else:
            self.ui.internal_name_lineEdit.setText(self.generate_class_name(node.title))
        self.ui.description_textEdit.setText(node.description)

        if self.ui.type_comboBox.findText(node.type) != -1:
            self.ui.type_comboBox.setCurrentText(node.type)
        else:
            self.ui.type_comboBox.setCurrentText('custom')
            self.ui.custom_type_lineEdit.setText(node.type)
        self.edit_node_metacode_dialog.set_code(node.meta_code, node.meta_code_file_path)

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
        self.ui.color_sample_pushButton.setStyleSheet('background-color: '+node.color)

        self.set_has_main_widget(node.has_main_widget)
        if node.has_main_widget:
            widget_pos = node.widget_position
            if widget_pos == 'under ports':
                self.ui.main_widget_under_ports_radioButton.setChecked(True)
                self.ui.main_widget_between_ports_radioButton.setChecked(False)
            elif widget_pos == 'between ports':
                self.ui.main_widget_under_ports_radioButton.setChecked(False)
                self.ui.main_widget_between_ports_radioButton.setChecked(True)

        # also set the code when the node doesn't have a widget YET
        self.edit_main_widget_metacode_dialog.set_code(node.main_widget_meta_code,
                                                       node.main_widget_meta_code_file_path)

        for i in range(len(node.custom_input_widgets)):
            iw = node.custom_input_widgets[i]
            iw_metacode = node.custom_input_widget_metacodes[i]
            iw_metacode_file_path = node.custom_input_widget_metacodes_file_paths[i]
            new_input_widget = CustomInputWidget(self, iw_metacode_file_path)
            new_input_widget.set_name(iw)
            self.ui.input_widgets_scrollArea.widget().layout().addWidget(new_input_widget)
            self.input_widgets.append(new_input_widget)

        for i in node.inputs:
            i_type = i['type']
            i_label = i['label']
            i_has_widget = i['has widget'] if i_type == 'data' else None
            i_widget_name = i['widget name'] if i_has_widget else None
            i_widget_pos = i['widget position'] if i_has_widget else None
            self.add_new_input(i_type, i_label, i_has_widget, i_widget_name, i_widget_pos)

        for o in node.outputs:
            self.add_new_output(o['type'], o['label'])


    def title_lineEdit_edited(self):  # only necessary for the title, the rest is stored here or in NodeInput/-Output
        line_edit: QLineEdit = self.sender()
        self.node.title = line_edit.text()
        self.node.title_changed.emit()

        if self.ui.auto_generate_internal_name_checkBox.isChecked():
            if self.check_class_name_conformity(line_edit.text()):
                self.ui.internal_name_lineEdit.setText(self.generate_class_name(line_edit.text()))
            else:
                self.ui.title_lineEdit.blockSignals(True)  # Qt Bug
                ret = QMessageBox.warning(self, 'Classname Conformity',
                                          'Your title is not auto class name conform. If this is your final title, please '
                                          'provide a custom internal name.',
                                          QMessageBox.Ok)
                self.ui.internal_name_lineEdit.setText('')
                self.ui.title_lineEdit.blockSignals(False)  # Qt Bug

    def internal_name_line_edit_edited(self):
        line_edit: QLineEdit = self.sender()

        if not self.ui.auto_generate_internal_name_checkBox.isChecked():
            if self.check_class_name_conformity(line_edit.text()):
                line_edit.setText(self.generate_class_name(line_edit.text()))
                self.node.class_name = line_edit.text()
            else:
                self.ui.internal_name_lineEdit.blockSignals(True)  # Qt Bug
                ret = QMessageBox.warning(self, 'Classname Conformity',
                                          'Your custom internal name isn\'t class name conform.',
                                          QMessageBox.Ok)
                self.ui.internal_name_lineEdit.blockSignals(True)  # Qt Bug


    def internal_name_check_box_toggled(self):
        if self.ui.auto_generate_internal_name_checkBox.isChecked():
            self.ui.internal_name_lineEdit.setEnabled(False)
        else:
            self.ui.internal_name_lineEdit.setEnabled(True)

    def type_changed(self, new_type):
        if new_type == 'custom':
            self.ui.custom_type_lineEdit.setEnabled(True)
        else:
            self.ui.custom_type_lineEdit.setEnabled(False)
            self.ui.custom_type_lineEdit.clear()

    def edit_node_metacode_clicked(self):
        self.edit_node_metacode_dialog.exec_()

    def main_widget_toggled(self, checked):
        self.set_has_main_widget(not checked)

    def edit_main_widget_metacode_clicked(self):
        self.edit_main_widget_metacode_dialog.exec_()

    def set_has_main_widget(self, has_main_widget):
        self.ui.main_widget_checkBox.setChecked(not has_main_widget)
        if not has_main_widget:
            self.ui.main_widget_position_widget.setEnabled(False)
        else:
            self.ui.main_widget_position_widget.setEnabled(True)


    def select_node_color_clicked(self):
        self.node_color = QColorDialog.getColor(self.node_color, title='Select node color. Don\'t use too dark '
                                                                       'colors.')
        ss = 'background-color: '+self.node_color.name()
        self.ui.color_sample_pushButton.setStyleSheet(ss)


    def add_new_input_widget_clicked(self):
        new_input_widget = CustomInputWidget(self)
        self.ui.input_widgets_scrollArea.widget().layout().addWidget(new_input_widget)
        self.input_widgets.append(new_input_widget)

    def delete_input_widget(self, input_widget):
        input_widget.setParent(None)
        self.input_widgets.remove(input_widget)


    def add_new_input_clicked(self):
        self.add_new_input()

    def add_new_input(self, _type=None, label=None, has_widget=None, widget_name=None,
                      widget_pos=None):
        new_input = NodeInput(self)
        if _type:
            new_input.set_type(_type)
        if label:
            new_input.set_label(label)
        if has_widget is not None:
            new_input.set_has_widget(has_widget)
            if has_widget:

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


    def get_node_title(self):
        return self.ui.title_lineEdit.text()

    def get_node_class_name(self):
        return self.ui.internal_name_lineEdit.text()

        # if self.ui.auto_generate_internal_name_checkBox.isChecked():
        #     return self.generate_class_name(self.ui.title_lineEdit.text())
        # else:
        #     return self.ui.internal_name_lineEdit.text()

    def get_node_description(self):
        return self.ui.description_textEdit.toPlainText()

    def get_node_type(self):
        node_type = self.ui.type_comboBox.currentText()
        if node_type == 'custom':
            node_type = self.ui.custom_type_lineEdit.text()
        return node_type

    def node_has_main_widget(self):
        return not self.ui.main_widget_checkBox.isChecked()

    def get_node_design_style(self):
        return 'extended' if self.ui.design_style_extended_radioButton.isChecked() else 'minimalistic'

    def get_node_main_widget_pos(self):
        under = self.ui.main_widget_under_ports_radioButton
        return 'under ports' if under.isChecked() else 'between ports'

    def check_class_name_conformity(self, s: str):
        return re.match('[a-zA-Z_]+[0-9a-zA-Z_]*', self.generate_class_name(s))

    def generate_class_name(self, s: str):
        # make upper
        s = ''.join([a if a.isupper() else b for a, b in zip(s, s.title())])

        # Remove invalid characters
        s = re.sub('[^0-9a-zA-Z_]', '', s)

        # Remove leading characters until we find a letter or underscore
        s = re.sub('^[^a-zA-Z_]+', '', s)

        # Remove every occurrence of '___' since this is an anchor for Ryven for separation of components
        while s.__contains__('___'):
            s = s.replace('___', '__')

        return s

    def get_json_data(self, package_name, module_name_separator, number):
        node_module_name = package_name + module_name_separator + self.get_node_class_name() + str(number)

        node_data = {'title': self.get_node_title(),
                     'description': self.get_node_description(),
                     'type': self.get_node_type(),
                     'module name': node_module_name,
                     'class name': self.get_node_class_name(),
                     'design style': self.get_node_design_style(),
                     'color': self.node_color.name(),
                     'has main widget': self.node_has_main_widget()}
        if self.node_has_main_widget():
            node_data['widget position'] = self.get_node_main_widget_pos()

        input_widgets_list = []
        for i_w in self.input_widgets:
            input_widgets_list.append(i_w.get_name())
        node_data['custom input widgets'] = input_widgets_list

        inputs = []  # save inputs
        for inp in self.inputs:
            input_data = {'type': inp.get_type(),
                          'label': inp.get_label()}
            if inp.get_type() == 'data':
                input_data['has widget'] = inp.has_widget()
                if inp.has_widget():
                    input_data['widget name'] = inp.get_widget_name()
                    input_data['widget position'] = inp.get_widget_pos()
            inputs.append(input_data)

        outputs = []  # save outputs
        for out in self.outputs:
            output_data = {'type': out.get_type(),
                           'label': out.get_label()}
            outputs.append(output_data)

        node_data['inputs'] = inputs
        node_data['outputs'] = outputs

        return node_data

    def save_metacode_files(self, node_dir, widgets_dir, module_name_separator, module_name):

        # check if any code sources have been changed
        any_code_source_changed = self.edit_node_metacode_dialog.code_source_changed() or \
                              self.edit_main_widget_metacode_dialog.code_source_changed() or \
                              any([input_widget.edit_input_widget_metacode_dialog.code_source_changed() for
                                   input_widget in self.input_widgets])

        override_changed_source = True
        if any_code_source_changed:
            ret = QMessageBox.warning(self, 'An edited code source has changed',
                                      'You have edited the metacode of a class which\'s source '
                                      '(the metacode file) '
                                      'has changed! Do you want to override these changes from outside with the edited '
                                      'code from here?',
                                      QMessageBox.Yes, QMessageBox.No)
            if ret == QMessageBox.Close:
                return
            override_changed_source = ret == QMessageBox.Yes


        node_meta_code_file_path = node_dir + '/' + module_name + module_name_separator + 'METACODE.py'
        enmd = self.edit_node_metacode_dialog
        if not os.path.isfile(node_meta_code_file_path):
            metacode = enmd.get_code()
            save_file(node_meta_code_file_path, metacode)  # the NI file's name is just the 'module name'
            enmd.set_code(metacode)  # to reset 'initial code'
        else:
            # if enmd.code_edited():
            if not enmd.code_source_changed() or enmd.code_source_changed() and override_changed_source:
                metacode = enmd.get_code()
                save_file(node_meta_code_file_path, metacode)
                enmd.set_code(metacode)  # to reset 'initial code'


        if self.node_has_main_widget():
            main_widget_src_code_file_path = widgets_dir + '/' + module_name + module_name_separator + 'main_widget' + \
                                             module_name_separator + 'METACODE.py'
            emwmd = self.edit_main_widget_metacode_dialog
            if not os.path.isfile(main_widget_src_code_file_path):
                metacode = emwmd.get_code()
                save_file(main_widget_src_code_file_path, metacode)
                emwmd.set_code(metacode)  # to reset 'initial code'
            else:
                # if emwmd.code_edited():
                if not emwmd.code_source_changed() or emwmd.code_source_changed() and override_changed_source:
                    metacode = emwmd.get_code()
                    save_file(main_widget_src_code_file_path, metacode)
                    emwmd.set_code(metacode)  # to reset 'initial code'


        for iw in self.input_widgets:
            iw: CustomInputWidget = iw
            iw_file_path = widgets_dir + '/' + module_name + module_name_separator + iw.get_name() + \
                module_name_separator + 'METACODE.py'
            eiwmd = iw.edit_input_widget_metacode_dialog
            if not os.path.isfile(iw_file_path):
                metacode = iw.get_code()
                save_file(iw_file_path, metacode)
                eiwmd.set_code(metacode)  # to reset 'initial code'
            else:
                # if eiwmd.code_edited():
                if not eiwmd.code_source_changed() or eiwmd.code_source_changed() and override_changed_source:
                    metacode = eiwmd.get_code()
                    save_file(iw_file_path, metacode)
                    eiwmd.set_code(metacode)  # to reset 'initial code'