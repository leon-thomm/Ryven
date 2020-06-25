from PySide2.QtWidgets import QDialog, QWidget, QDialogButtonBox, QVBoxLayout, QHBoxLayout, QScrollArea, QGroupBox, QPushButton
from PySide2.QtGui import QGuiApplication, QClipboard
from CodeEditor import CodeEditor_Small
from NodeContentWidget import NodeContentWidget


class PreviewAllCodes_Dialog(QDialog):
    def __init__(self, nodes, parent=None):
        super(PreviewAllCodes_Dialog, self).__init__(parent)

        self.code_update_assignments = {}  # {CodeEditor_Small : CodeEditor from NodeContentWidget}
        self.copy_buttons = []

        main_vertical_layout = QVBoxLayout()

        # nodes scroll area
        nodes_scroll_area = QScrollArea(self)
        nodes_scroll_area_widget = QWidget()
        nodes_scroll_area_widget.setLayout(QVBoxLayout())

        # nodes
        for n in nodes:
            c_w: NodeContentWidget = n.content_widget

            # node_scroll_area = QScrollArea(nodes_scroll_area_widget)
            node_group_box = QGroupBox(c_w.get_title(), nodes_scroll_area_widget)
            node_group_box.setLayout(QHBoxLayout())

            # src code
            src_code_group_box = QGroupBox(self)
            src_code_group_box.setLayout(QVBoxLayout())
            src_code_editor = CodeEditor_Small()
            src_code_editor.setText(c_w.edit_src_code_dialog.get_code())
            src_code_group_box.layout().addWidget(src_code_editor)

            self.code_update_assignments[src_code_editor] = c_w.edit_src_code_dialog

            # copy button
            copy_button = QPushButton('copy')
            self.copy_buttons.append(copy_button)
            copy_button.clicked.connect(self.copy_clicked)
            src_code_group_box.layout().addWidget(copy_button)


            # main widget
            main_widget_group_box = None
            if c_w.has_main_widget:
                main_widget_code_editor = CodeEditor_Small()
                main_widget_code_editor.setText(c_w.edit_main_widget_dialog.get_code())
                main_widget_group_box = QGroupBox('main widget', self)
                main_widget_group_box.setLayout(QVBoxLayout())
                main_widget_group_box.layout().addWidget(main_widget_code_editor)

                self.code_update_assignments[main_widget_code_editor] = c_w.edit_main_widget_dialog

                # copy button
                copy_button = QPushButton('copy')
                self.copy_buttons.append(copy_button)
                copy_button.clicked.connect(self.copy_clicked)
                main_widget_group_box.layout().addWidget(copy_button)


            # inputs
            inputs_group_box = QGroupBox(self)
            inputs_group_box.setLayout(QHBoxLayout())

            for i_w in c_w.input_widgets:
                input_widget_code_editor = CodeEditor_Small()
                input_widget_code_editor.setText(i_w.edit_widget_dialog.get_code())
                input_widget_group_box = QGroupBox(i_w.get_name(), self)
                input_widget_group_box.setLayout(QVBoxLayout())
                input_widget_group_box.layout().addWidget(input_widget_code_editor)
                self.code_update_assignments[input_widget_code_editor] = i_w.edit_widget_dialog

                inputs_group_box.layout().addWidget(input_widget_group_box)

                # copy button
                copy_button = QPushButton('copy')
                self.copy_buttons.append(copy_button)
                copy_button.clicked.connect(self.copy_clicked)
                input_widget_group_box.layout().addWidget(copy_button)


            node_group_box.layout().addWidget(src_code_group_box)
            if c_w.has_main_widget:
                node_group_box.layout().addWidget(main_widget_group_box)
            node_group_box.layout().addWidget(inputs_group_box)
            # node_scroll_area.setWidget(node_group_box)
            nodes_scroll_area_widget.layout().addWidget(node_group_box)


        nodes_scroll_area.setWidget(nodes_scroll_area_widget)

        # button box
        self.button_box = QDialogButtonBox(self)
        self.button_box.setStandardButtons(QDialogButtonBox.Ok)
        self.button_box.button(QDialogButtonBox.Ok).clicked.connect(self.accepting)

        # merge layouts
        main_vertical_layout.addWidget(nodes_scroll_area)
        main_vertical_layout.addWidget(self.button_box)

        self.setLayout(main_vertical_layout)
        self.resize(1200, 800)


    def accepting(self):
        for small_editor in self.code_update_assignments.keys():
            self.code_update_assignments[small_editor].set_code(small_editor.toPlainText())

        self.accept()

    def copy_clicked(self):
        index = self.copy_buttons.index(self.sender())
        code_editor = list(self.code_update_assignments.keys())[index]
        code = code_editor.get_code()
        cb = QGuiApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(code)