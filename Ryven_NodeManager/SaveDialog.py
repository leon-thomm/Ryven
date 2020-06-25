from PySide2.QtWidgets import QSizePolicy, QDialog, QVBoxLayout, QHBoxLayout, QGroupBox, QScrollArea, QWidget, QCheckBox, QPushButton, QLabel, QLineEdit, QFileDialog, QDialogButtonBox
from PySide2.QtCore import Qt

from Node import Node
from NodeContentWidget import NodeContentWidget
from InputWidget import InputWidget
from NodeOutput import NodeOutput
from PreviewAllCodesDialog import PreviewAllCodes_Dialog

import json
import os  # for creating directories
import re
import shutil
import time


class SaveDialog(QDialog):
    def __init__(self, parent, nodes):
        super(SaveDialog, self).__init__(parent)

        self.all_nodes = nodes
        self.export_nodes = []
        self.nodes_check_box_list = []
        self.export_dir = ''
        self.package_name = ''

        # create UI

        # main layouts and widgets
        self.main_vertical_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout(self)
        self.nodes_vertical_layout = QVBoxLayout(self)
        self.nodes_vertical_layout.setAlignment(Qt.AlignTop)
        self.export_widget = QWidget(self)
        self.export_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.export_layout = QVBoxLayout(self)
        self.export_layout.setAlignment(Qt.AlignTop)
        self.export_widget.setLayout(self.export_layout)

        # nodes selection section
        self.nodes_group_box = QGroupBox(self)


        self.nodes_group_box.setLayout(QVBoxLayout(self))
        self.nodes_group_box.setTitle('Select nodes to export')

        self.nodes_scroll_area = QScrollArea(self)
        nodes_list_widget = QWidget()
        nodes_list_widget.setLayout(self.nodes_vertical_layout)

        for i in range(len(nodes)):
            n = nodes[i]
            node_check_box = QCheckBox(n.title)
            node_check_box.setObjectName('node_check_box_'+str(i))
            node_check_box.setChecked(True)
            self.nodes_vertical_layout.addWidget(node_check_box)
            self.nodes_check_box_list.append(node_check_box)

        self.nodes_scroll_area.setWidget(nodes_list_widget)
        self.nodes_group_box.layout().addWidget(self.nodes_scroll_area)

        # preview codes dialog
        self.preview_codes_button = QPushButton('preview codes')
        self.preview_codes_button.clicked.connect(self.preview_codes_clicked)

        # export settings section
        self.select_package_dir_button = QPushButton('Select package dir', self)
        self.select_package_dir_button.clicked.connect(self.select_package_dir)

        self.package_dir_label = QLabel('package dir: -')

        self.export_button = QPushButton('export', self)
        self.export_button.clicked.connect(self.export)

        self.export_layout.addWidget(self.preview_codes_button)
        self.export_layout.addWidget(self.select_package_dir_button)
        self.export_layout.addWidget(self.package_dir_label)
        self.export_layout.addWidget(self.export_button)

        # button box
        self.button_box = QDialogButtonBox(self)
        self.button_box.setStandardButtons(QDialogButtonBox.Ok)
        self.button_box.button(QDialogButtonBox.Ok).clicked.connect(self.close)


        # merge layouts
        self.horizontal_layout.addWidget(self.nodes_group_box)
        self.horizontal_layout.addWidget(self.export_widget)
        self.main_vertical_layout.addLayout(self.horizontal_layout)
        self.main_vertical_layout.addWidget(self.button_box)


        self.setWindowTitle('Export Nodes')
        self.resize(500, 300)


    def preview_codes_clicked(self):
        accepted = PreviewAllCodes_Dialog(self.all_nodes, self).exec_()

    def select_package_dir(self):
        self.export_dir = QFileDialog.getExistingDirectory(
                                            self,
                                            'Select the package folder where your nodes shall be exported at',
                                            '../packages')
        self.package_name = os.path.basename(self.export_dir)
        self.package_dir_label.setText('package dir: '+self.export_dir)


    def update_export_nodes(self):
        self.export_nodes.clear()

        for i in range(len(self.nodes_check_box_list)):
            check_box: QCheckBox = self.nodes_check_box_list[i]
            if check_box.isChecked():
                self.export_nodes.append(self.all_nodes[int(check_box.objectName()[15:])])



    def export(self):
        self.update_export_nodes()



        # prevent duplicates
        # EXPLANATION: different Nodes should be able to have same names inside a package. Also two different nodes
        # should both be able to have a custom input widget f.ex. 'InputWidget1' (same name again) although these are
        # different widgets. There is a problem when importing the modules (the python files) in the editor - if an
        # earlier imported module has the same name, then the old one will be used to import f.ex. a widget class which
        # leads of course to errors. In fact, all my modules I use in the editor have to have individual names. That's
        # what I do here. The only convention that has to be followed by the user now would be not to create multiple
        # packages with same name -> which isn't possible!! (two folders with the same name are impossible)
        node_module_names = {}  # Node : Name
        module_name_separator = '___'
        for n in self.export_nodes:
            module_node_title = n.content_widget.get_intern_title()
            pattern = self.package_name + module_name_separator + module_node_title + '\\d+'
            node_module_names[n] = self.package_name + module_name_separator + \
                                   module_node_title + \
                                   str(len([x for x in node_module_names.values() if re.match(pattern, x)]))



        nodes_dict = {}

        nodes_list = []
        for i in range(len(self.export_nodes)):
            n: Node = self.export_nodes[i]

            c_w: NodeContentWidget = n.content_widget

            # save general node info
            node_data = {'title': c_w.get_title(), 'description': c_w.get_description(), 'type': c_w.get_type(),
                         'module name': node_module_names[n],
                         'class name': c_w.get_intern_title(),
                         'design style': c_w.get_design_style(),
                         'color': c_w.node_color.name(),
                         'has main widget': c_w.has_main_widget}
            if c_w.has_main_widget:
                node_data['widget position'] = c_w.get_main_widget_pos()
                         # 'DSL code': c_w.get_dsl_code() if c_w.programming_type == 'DSL' else None}

            input_widgets_list = []
            for i_w in c_w.input_widgets:
                input_widgets_list.append(i_w.get_name())
            node_data['custom input widgets'] = input_widgets_list

            inputs = []  # save inputs
            for inp in c_w.inputs:
                input_data = {'type': inp.get_type(),
                              'label': inp.get_label()}
                if inp.get_type() == 'data':
                    input_data['has widget'] = inp.has_widget()
                    if inp.has_widget():
                        input_data['widget type'] = inp.get_widget_type()
                        if inp.get_widget_type() == 'custom widget':
                            input_data['widget name'] = inp.get_widget_name()
                        input_data['widget position'] = inp.get_widget_pos()
                inputs.append(input_data)

            outputs = []  # save outputs
            for out in c_w.outputs:
                output_data = {'type': out.get_type(),
                               'label': out.get_label()}
                outputs.append(output_data)

            node_data['inputs'] = inputs
            node_data['outputs'] = outputs

            nodes_list.append(node_data)

        nodes_dict['nodes'] = nodes_list

        info_dict = {'type': 'vyScriptFP nodes package'}

        whole_dict = {**info_dict, **nodes_dict}  # merges single two dictionaries to one

        json_data = json.dumps(whole_dict)
        print(json_data)


        # try:
        #     # create main package folder
        #     self.export_dir = self.export_dir+'/'+self.get_package_name()
        #     os.mkdir(self.export_dir)
        #
        #     f = open(self.export_dir+'/'+self.get_package_name()+'.txt', 'w')
        #     f.write(json_data)
        #     f.close()
        # except FileExistsError:
        #     print('File already exists! Please select another location')

        # # clear directory if it already exitsts
        # if len(self.export_dir) > 12 and self.export_dir.find('packages') != -1:
        #     if len(os.listdir(self.export_dir)) > 0:
        #         shutil.rmtree(self.export_dir + '/', ignore_errors=True)
        #         time.sleep(0.001)
        #         os.mkdir(self.export_dir)



        # create dirs and save files
        if not os.path.isdir(self.export_dir+'/nodes'):
            os.mkdir(self.export_dir+'/nodes')

        self.save_file(self.export_dir + '/' + self.package_name + '.rypac', json_data)


        for n in self.export_nodes:
            c_w: NodeContentWidget = n.content_widget
            module_name = node_module_names[n]
            module_node_title = c_w.get_title()
            node_class_name = c_w.get_intern_title()

            # create node folder
            node_dir = self.export_dir+'/nodes/'+module_name
            if not os.path.isdir(node_dir):
                os.mkdir(node_dir)

            # create widgets folder
            widgets_dir = node_dir+'/widgets'
            if not os.path.isdir(widgets_dir):
                os.mkdir(widgets_dir)


            # save source files
            src_code_file_path = node_dir+'/'+module_name+module_name_separator+'METACODE.py'
            if not os.path.isfile(src_code_file_path):
                meta_code = c_w.get_src_code()
                self.save_file(node_dir+'/'+module_name+module_name_separator+'METACODE.py', meta_code)  # the NI file's name is just the 'module name'

            if c_w.has_main_widget:
                main_widget_src_code_file_path = widgets_dir + '/' + module_name + module_name_separator + 'main_widget' + module_name_separator + 'METACODE.py'
                if not os.path.isfile(main_widget_src_code_file_path):
                    meta_code = c_w.get_main_widget_code()
                    self.save_file(widgets_dir+'/'+module_name+module_name_separator+'main_widget'+module_name_separator+'METACODE.py', meta_code)

            for iw in c_w.input_widgets:
                iw: InputWidget = iw
                iw_file_path = widgets_dir+'/'+module_name+module_name_separator+iw.get_name()+module_name_separator+'METACODE.py'
                if not os.path.isfile(iw_file_path):
                    meta_code = iw.get_code()
                    self.save_file(widgets_dir+'/'+module_name+module_name_separator+iw.get_name()+module_name_separator+'METACODE.py', meta_code)


    def save_file(self, file_path, content):
        try:
            os.remove(file_path)
        except OSError:
            pass

        f = open(file_path, 'w')
        f.write(content)
        f.close()