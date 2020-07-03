# QT
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QFileDialog
from PySide2.QtCore import Qt
# parent UI
from ui_node_manager_mainwindow import Ui_MainWindow
# custom content
from Node import Node
from Node_ListWidget import Node_ListWidget
from NodeContentWidget import NodeContentWidget
from SaveDialog import SaveDialog

import json
import os


class MainWindow(QMainWindow):

    nodes = []
    node_list_widgets = []

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.nodes_list_widget.setFixedWidth(200)
        self.setWindowTitle('Ryven NodeManager')
        self.setWindowIcon(QIcon('resources/pics/program_icon2.png'))
        self.load_stylesheet('dark')

        self.ui.add_new_node_pushButton.clicked.connect(self.add_new_node_pushButton_clicked)
        self.ui.import_nodes_pushButton.clicked.connect(self.import_button_clicked)
        self.ui.save_pushButton.clicked.connect(self.save_button_clicked)




    def add_new_node_pushButton_clicked(self):
        node_content_widget = NodeContentWidget()
        new_node = Node(node_content_widget)
        node_content_widget.load_node(new_node)
        new_node.title_changed.connect(self.update_nodes_list_names)  # this will update the list view
        self.nodes.append(new_node)

        self.rebuild_nodes_list()

        self.set_current_node(self.nodes[-1])


    def rebuild_nodes_list(self):
        if self.ui.nodes_scrollArea.widget().layout().count() != 0:
            # clear nodes layout
            for i in reversed(range(self.ui.nodes_scrollArea.widget().layout().count())):
                #  'The new widget is deleted when its parent is deleted' - Docs
                self.ui.nodes_scrollArea.widget().layout().itemAt(i).widget().setParent(None)

        scroll_area_content_widget = QWidget()  # create new widget and layout for the scroll area
        nodes_layout = QVBoxLayout()
        nodes_layout.setAlignment(Qt.AlignTop)

        for n in self.nodes:  # create a new node list widget for every node
            node_widget = Node_ListWidget(n)
            node_widget.double_clicked.connect(self.node_widget_double_clicked)

            nodes_layout.addWidget(node_widget)
            self.node_list_widgets.append(node_widget)

        scroll_area_content_widget.setLayout(nodes_layout)
        self.ui.nodes_scrollArea.setWidget(scroll_area_content_widget)


    def update_nodes_list_names(self):
        for node_list_widget in self.node_list_widgets:
            node_list_widget.update_display_title()


    def set_current_node(self, node: Node):
        # clear node_content_placeholder_widget
        layout = self.ui.node_content_placeholder_widget.layout()
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            item.widget().setParent(self)  # removing the widget from the layout without deleting the widget

        layout.addWidget(node.content_widget)
        node.content_widget.show()


    def node_widget_double_clicked(self, node):
        self.set_current_node(node)


    def load_stylesheet(self, ss):
        ss_content = ''
        try:
            f = open('resources/stylesheets/'+ss+'.txt')
            ss_content = f.read()
            f.close()
        finally:
            self.setStyleSheet(ss_content)


    def import_nodes(self, j_nodes, dir):
        print('importing nodes')
        o_nodes = json.loads(j_nodes)
        nodes_list = o_nodes['nodes']

        for n in nodes_list:
            # print('parsing node', n['title'])
            new_node = Node()
            new_node.title = n['title']
            new_node.description = n['description']
            new_node.type = n['type']
            new_node.module_name = n['module name']
            new_node.class_name = n['class name']
            new_node.design_style = n['design style']
            new_node.color = n['color']
            new_node.has_main_widget = n['has main widget']
            if new_node.has_main_widget:
                new_node.widget_position = n['widget position']
            new_node.custom_input_widgets = n['custom input widgets']
            new_node.inputs = n['inputs']
            new_node.outputs = n['outputs']

            # load custom files
            module_name_separator = '___'

            node_path = dir+'/'+new_node.module_name

            #   main code
            node_metacode_file_path = node_path+'/'+new_node.module_name+module_name_separator+'METACODE.py'
            new_node.meta_code_file_path = node_metacode_file_path
            f = open(node_metacode_file_path)
            new_node.meta_code = f.read()
            f.close()

            node_widgets_path = node_path + '/widgets'

            #   main widget code
            if new_node.has_main_widget:
                main_widget_metacode_file_path = node_widgets_path+'/'+new_node.module_name+module_name_separator + \
                                                 'main_widget'+module_name_separator+'METACODE.py'
                new_node.main_widget_meta_code_file_path = main_widget_metacode_file_path
                f = open(main_widget_metacode_file_path)
                new_node.main_widget_meta_code = f.read()
                f.close()

            #   custom input widgets
            for ciw in new_node.custom_input_widgets:
                custom_input_widget_file_path = node_widgets_path+'/'+new_node.module_name+module_name_separator+ciw + \
                                                module_name_separator+'METACODE.py'
                f = open(custom_input_widget_file_path)
                new_node.custom_input_widget_metacodes.append(f.read())
                new_node.custom_input_widget_metacodes_file_paths.append(custom_input_widget_file_path)
                f.close()

            new_node_content_widget = NodeContentWidget()
            new_node.title_changed.connect(self.update_nodes_list_names)  # this will update the list view
            new_node_content_widget.load_node(new_node)
            new_node.content_widget = new_node_content_widget
            self.nodes.append(new_node)
            # print('finished parsing')

        print(self.nodes)
        self.rebuild_nodes_list()


    def import_button_clicked(self):
        file_path = QFileDialog.getOpenFileName(self, 'select the json file you want to import', '../packages')[0]
        f_content = ''
        try:
            f = open(file_path)
            f_content = f.read()
            f.close()
        except Exception as e:
            return

        self.import_nodes(f_content, os.path.dirname(file_path) + '/nodes')


    def save_button_clicked(self):
        # the dialog does the whole saving process
        save_dialog = SaveDialog(self, self.nodes)
        save_dialog.exec_()