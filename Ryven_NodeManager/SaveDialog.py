from PySide2.QtWidgets import QSizePolicy, QDialog, QVBoxLayout, QHBoxLayout, QGroupBox, QScrollArea, QWidget, QCheckBox, QPushButton, QLabel, \
    QFileDialog, QDialogButtonBox
from PySide2.QtCore import Qt

from Node import Node
from NodeContentWidget import NodeContentWidget

import json
import os  # for creating directories

from files_manager import save_file


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

        # export settings section
        self.select_package_dir_button = QPushButton('Select package dir', self)
        self.select_package_dir_button.clicked.connect(self.select_package_dir)

        self.package_dir_label = QLabel('package dir: -')

        self.export_button = QPushButton('export', self)
        self.export_button.clicked.connect(self.export)

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


        nodes_dict = {}
        module_name_separator = '___'

        nodes_list = []
        node_titles_count = {}  # title (str) : number (int)
        for i in range(len(self.export_nodes)):
            n: Node = self.export_nodes[i]

            c_w: NodeContentWidget = n.content_widget

            node_number = 0
            title = c_w.get_node_title()
            if title in node_titles_count.values():
                node_number = node_titles_count[title]  # index
                node_titles_count[title] += 1
            else:
                node_titles_count[title] = 1

            node_data = c_w.get_json_data(package_name=self.package_name,
                                          module_name_separator=module_name_separator,
                                          number=node_number)

            nodes_list.append(node_data)

        nodes_dict['nodes'] = nodes_list

        info_dict = {'type': 'Ryven nodes package'}

        whole_dict = {**info_dict, **nodes_dict}  # merges single two dictionaries to one

        json_data = json.dumps(whole_dict)
        print(json_data)


        # create dirs and save files
        if not os.path.isdir(self.export_dir+'/nodes'):
            os.mkdir(self.export_dir+'/nodes')

        save_file(self.export_dir + '/' + self.package_name + '.rpc', json_data)


        for i in range(len(self.export_nodes)):
            n = self.export_nodes[i]
            module_name = nodes_list[i]['module name']

            # create node folder
            node_dir = self.export_dir+'/nodes/'+module_name
            if not os.path.isdir(node_dir):
                os.mkdir(node_dir)

            # create widgets folder
            widgets_dir = node_dir+'/widgets'
            if not os.path.isdir(widgets_dir):
                os.mkdir(widgets_dir)

            n.content_widget.save_metacode_files(node_dir=node_dir, widgets_dir=widgets_dir,
                                                 module_name_separator=module_name_separator, module_name=module_name)