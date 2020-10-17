from PySide2.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QScrollArea
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont

from custom_src.global_tools.Debugger import Debugger
from custom_src.global_tools.stuff import sort_nodes
from custom_src.node_choice_widget.NodeWidget import NodeWidget


class NodeChoiceWidget(QWidget):
    def __init__(self, flow, nodes):
        super(NodeChoiceWidget, self).__init__()

        self.flow = flow

        self.all_nodes = sort_nodes(nodes)  # copy, no ref

        self.nodes = []

        # 'current_nodes' are the currently selectable ones, they get recreated every time update_view() is called
        self.current_nodes = []
        self.all_current_node_widgets = []
        self.active_node_widget_index = -1
        self.active_node_widget = None

        self.reset_list()

        self.node_widget_index_counter = 0

        self.setMinimumWidth(260)
        self.setFixedHeight(450)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.main_layout)

        # adding all stuff to the layout
        self.search_line_edit = QLineEdit(self)
        self.search_line_edit.setPlaceholderText('search for node...')
        self.search_line_edit.textChanged.connect(self.update_view)
        self.layout().addWidget(self.search_line_edit)


        self.list_scroll_area = QScrollArea(self)
        self.list_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list_scroll_area.setWidgetResizable(True)

        self.list_scroll_area_widget = QWidget()
        self.list_scroll_area.setWidget(self.list_scroll_area_widget)

        self.list_layout = QVBoxLayout()
        self.list_layout.setAlignment(Qt.AlignTop)
        self.list_scroll_area_widget.setLayout(self.list_layout)

        self.layout().addWidget(self.list_scroll_area)

        self.setFixedHeight(400)


        self.update_view('')

        try:
            f = open('../resources/stylesheets/dark_node_choice_widget.txt')
            self.setStyleSheet(f.read())
            f.close()
        except FileNotFoundError:
            pass

        self.search_line_edit.setFocus()


    def mousePressEvent(self, event):
        QWidget.mousePressEvent(self, event)
        event.accept()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.flow.hide_node_choice_widget()

        elif event.key() == Qt.Key_Down:
            index = self.active_node_widget_index+1 if \
                self.active_node_widget_index+1 < len(self.all_current_node_widgets) else 0
            self.set_active_node_widget_index(index)
        elif event.key() == Qt.Key_Up:
            index = self.active_node_widget_index-1 if \
                self.active_node_widget_index-1 > -1 else len(self.all_current_node_widgets)-1
            self.set_active_node_widget_index(index)

        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if len(self.all_current_node_widgets) > 0:
                self.place_node(self.active_node_widget_index)
        else:
            event.setAccepted(False)


    def wheelEvent(self, event):
        QWidget.wheelEvent(self, event)
        event.accept()


    def refocus(self):
        self.search_line_edit.setFocus()
        self.search_line_edit.selectAll()


    def update_list(self, nodes):
        self.nodes = sort_nodes(nodes)

    def reset_list(self):
        self.nodes = self.all_nodes


    def update_view(self, text=''):
        text = text.lower()
        for i in reversed(range(self.list_layout.count())):
            self.list_layout.itemAt(i).widget().setParent(None)

        self.current_nodes.clear()
        self.all_current_node_widgets.clear()

        self.node_widget_index_counter = 0

        # select valid elements from text
        # nodes
        nodes_names_dict = {}
        for n in self.nodes:
            nodes_names_dict[n] = n.title.lower()
        sorted_indices = self.get_sorted_dict_matching_search(nodes_names_dict, text)
        for n, index in sorted_indices.items():
            self.current_nodes.append(n)


        # nodes
        if len(self.current_nodes) > 0:
            nodes_label = QLabel('Hover for description')
            nodes_label_font = QFont('Poppins')
            nodes_label_font.setPixelSize(15)
            nodes_label.setStyleSheet('color: #9bbf9dff; border: none;')
            nodes_label.setFont(nodes_label_font)
            self.list_layout.addWidget(nodes_label)

            for n in self.current_nodes:
                node_widget = self.create_list_item_widget(n)
                self.list_layout.addWidget(node_widget)
                self.all_current_node_widgets.append(node_widget)

        if len(self.all_current_node_widgets) > 0:
            self.set_active_node_widget_index(0)

        # self.setFixedWidth(self.minimumWidth())
        # print(self.list_scroll_area_widget.width())


    def get_sorted_dict_matching_search(self, items_dict, text):
        indices_dict = {}
        for item, name in items_dict.items():  # the strings are already lowered here
            Debugger.debug(item, name, text)
            if name.__contains__(text):
                index = name.index(text)
                indices_dict[item] = index
        return {k: v for k, v in sorted(indices_dict.items(), key=lambda i: i[1])}


    def create_list_item_widget(self, node):
        node_widget = NodeWidget(self, node)  # , self.node_images[node])
        node_widget.custom_focused_from_inside.connect(self.node_widget_focused_from_inside)
        node_widget.setObjectName('node_widget_' + str(self.node_widget_index_counter))
        self.node_widget_index_counter += 1
        node_widget.chosen.connect(self.node_widget_chosen)
        
        return node_widget

    
    def node_widget_focused_from_inside(self):
        self.set_active_node_widget_index(self.all_current_node_widgets.index(self.sender()))

    def set_active_node_widget_index(self, index):
        self.active_node_widget_index = index
        node_widget = self.all_current_node_widgets[index]

        if self.active_node_widget:
            self.active_node_widget.set_custom_focus(False)

        node_widget.set_custom_focus(True)
        self.active_node_widget = node_widget
        self.list_scroll_area.ensureWidgetVisible(self.active_node_widget)


    def node_widget_chosen(self):  # gets called when the user clicks on a node widget with the mouse
        self.flow.ignore_mouse_event = True  # otherwise, it will receive a mouse press event

        index = int(self.sender().objectName()[self.sender().objectName().rindex('_')+1:])
        self.place_node(index)


    def place_node(self, index):
        node_index = index
        node = self.current_nodes[node_index]
        self.flow.place_node__cmd(node)

        self.flow.hide_node_choice_widget()