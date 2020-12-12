# QT
from PySide2.QtGui import QIcon, QKeySequence, QFontDatabase
from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QFileDialog, QMessageBox, QShortcut
from PySide2.QtCore import Qt
# parent UI
from NodesListWidget import NodesListWidget
from ui_node_manager_mainwindow import Ui_MainWindow
# custom content
from Node import Node
from NodeContentWidget import NodeContentWidget
from SaveDialog import SaveDialog

import json
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont('../resources/fonts/source code pro/SourceCodePro-Regular.ttf')

        self.nodes = []

        # convenience features for exporting
        self.nodes_at_last_export = []
        self.last_exported_nodes = []
        self.last_export_path = ''

        self.nodes_list_widget = NodesListWidget(self)
        self.ui.nodes_scrollArea.setWidget(self.nodes_list_widget)

        # shortcuts
        save_shortcut = QShortcut(QKeySequence.Save, self)
        save_shortcut.activated.connect(self.save_triggered)
        import_nodes_shortcut = QShortcut(QKeySequence('Ctrl+i'), self)
        import_nodes_shortcut.activated.connect(self.import_nodes_triggered)

        # UI
        self.ui.splitter.setSizes([200, 850])
        self.setWindowTitle('Ryven NodeManager')
        self.setWindowIcon(QIcon('resources/pics/program_icon2.png'))
        self.load_stylesheet('dark')

        self.ui.add_new_node_pushButton.clicked.connect(self.add_new_node_pushButton_clicked)
        self.ui.import_nodes_pushButton.clicked.connect(self.import_nodes_triggered)
        self.ui.clear_nodes_pushButton.clicked.connect(self.clear_button_clicked)
        self.ui.save_pushButton.clicked.connect(self.save_triggered)


    def add_new_node_pushButton_clicked(self):
        node_content_widget = NodeContentWidget()
        new_node = Node(node_content_widget)
        node_content_widget.load_node(new_node)
        new_node.title_changed.connect(self.update_node_name)  # this will update the list view
        self.nodes.append(new_node)

        self.nodes_list_widget.add_node(new_node)

        self.set_current_node(-1)


    def update_node_name(self):
        node: Node = self.sender()
        index = self.nodes.index(node)
        self.nodes_list_widget.node_renamed(index, node.content_widget.get_node_title())


    def set_current_node(self, index: int):
        node = self.nodes[index]

        self.remove_node_content_widget()
        self.add_node_content_widget(node.content_widget)

        node.content_widget.show()

        self.nodes_list_widget.set_current_index(index)

    def remove_node_content_widget(self):
        # clear node_content_placeholder_widget
        layout = self.ui.node_content_placeholder_widget.layout()
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            item.widget().setParent(self)  # removing the widget from the layout without deleting the widget

    def add_node_content_widget(self, w):
        self.ui.node_content_placeholder_widget.layout().addWidget(w)

    def clear_button_clicked(self):
        msg_box = QMessageBox(QMessageBox.Warning, 'Clearing nodes',
                              'You are about to remove all present nodes. Unsaved changes will be lost. '
                              'Do you want to proceed?', QMessageBox.Cancel | QMessageBox.Yes, self)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        ret = msg_box.exec_()
        if ret != QMessageBox.Yes:
            return
        self.clear_nodes()

    def clear_nodes(self):
        self.remove_node_content_widget()
        self.nodes_list_widget.clear_list()
        self.nodes.clear()

    def delete_node(self, index: int):
        del self.nodes[index]
        self.remove_node_content_widget()


    def load_stylesheet(self, ss):
        ss_content = ''
        try:
            f = open('resources/stylesheets/'+ss+'.txt')
            ss_content = f.read()
            f.close()
        finally:
            self.setStyleSheet(ss_content)


    def import_nodes(self, j_nodes, dir):
        # print('importing nodes')
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
            new_node.title_changed.connect(self.update_node_name)  # this will update the list view
            new_node_content_widget.load_node(new_node)
            new_node.content_widget = new_node_content_widget
            self.nodes.append(new_node)
            self.nodes_list_widget.add_node(new_node)
            # print('finished parsing')

        print(self.nodes)


    def import_nodes_triggered(self):
        file_path = QFileDialog.getOpenFileName(self, 'select the json file you want to import', '../packages',
                                                '(*.rpc *.rypac)')[0]
        f_content = ''
        try:
            f = open(file_path)
            f_content = f.read()
            f.close()
        except Exception as e:
            return

        self.import_nodes(f_content, os.path.dirname(file_path) + '/nodes')


    def save_triggered(self):
        """creates the dialog that manages the whole saving process"""

        selected_nodes = []
        if len(self.nodes_at_last_export) == 0:
            selected_nodes = self.nodes
        elif self.nodes_at_last_export == self.nodes:
            # no nodes added or removed
            selected_nodes = self.last_exported_nodes
        else:
            selected_nodes = self.nodes

        nodes_dict = {}         # {node: selected}
        for n in self.nodes:    # add all nodes, unselected
            nodes_dict[n] = False
        for n in selected_nodes:    # select
            nodes_dict[n] = True

        save_dialog = SaveDialog(self,
                                 nodes_dict=nodes_dict,
                                 last_export_dir=self.last_export_path)
        save_dialog.exec_()

        self.nodes_at_last_export = self.nodes.copy()
