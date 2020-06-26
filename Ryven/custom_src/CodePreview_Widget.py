from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QRadioButton, QLabel, QCheckBox, QGridLayout
from PySide2.QtGui import QFont
import inspect

from custom_src.NodeInstance import NodeInstance
from custom_src.CodePreview_TextEdit import CodePreview_TextEdit
from custom_src.global_tools.class_inspection import find_type_in_object


class CodePreview_Widget(QWidget):
    def __init__(self):
        super(CodePreview_Widget, self).__init__()

        self.text_edit = CodePreview_TextEdit()
        self.code_obj = None
        self.buttons_class_dict = {}
        self.active_class_index = -1

        settings_widget = QWidget()
        settings_layout = QHBoxLayout()
        info_label = QLabel('You can zoom!')
        info_label.setFont(QFont('Poppins', 8))
        settings_layout.addWidget(info_label)

        # class radio buttons widget
        class_selection_widget = QWidget()
        self.class_selection_layout = QGridLayout()
        class_selection_widget.setLayout(self.class_selection_layout)

        settings_layout.addWidget(class_selection_widget)

        # syntax highlighting
        self.syntax_highlighting_check_box = QCheckBox('syntax highlighting (alpha)')
        self.syntax_highlighting_check_box.toggled.connect(self.syntax_highlighting_toggled)
        self.syntax_highlighting_check_box.setChecked(True)
        settings_layout.addWidget(self.syntax_highlighting_check_box)


        settings_widget.setLayout(settings_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(settings_widget)
        main_layout.addWidget(self.text_edit)
        self.setLayout(main_layout)

        self.setStyleSheet('border: none;')

    def set_new_code_obj(self, obj):
        self.rebuild_class_selection(obj)

        self.code_obj = obj

        if obj is None:  # no NI selected
            self.text_edit.setText('')
            return

        self.update_code()

    def update_code(self):
        if self.active_class_index == -1:
            return

        c = self.get_current_code_class()

        self.text_edit.setText(inspect.getsource(c))

    def get_current_code_class(self):
        return list(self.buttons_class_dict.values())[self.active_class_index]

    def rebuild_class_selection(self, obj):
        # clear layout
        for i in range(self.class_selection_layout.count()):
            item = self.class_selection_layout.itemAt(0)
            widget = item.widget()
            widget.hide()
            self.class_selection_layout.removeItem(item)

        self.buttons_class_dict = {}
        self.active_class_index = -1

        if find_type_in_object(obj, NodeInstance):
            # NI class
            node_inst_class_RB = QRadioButton('NodeInstance')
            node_inst_class_RB.toggled.connect(self.class_RB_toggled)
            self.buttons_class_dict[node_inst_class_RB] = obj.__class__
            self.class_selection_layout.addWidget(node_inst_class_RB, 0, 0)

            # main_widget class
            if obj.main_widget is not None:
                main_widget_class_RB = QRadioButton('MainWidget')
                main_widget_class_RB.toggled.connect(self.class_RB_toggled)
                self.buttons_class_dict[main_widget_class_RB] = obj.main_widget.__class__
                self.class_selection_layout.addWidget(main_widget_class_RB, 1, 0)

            # data input widgets
            row_count = 0
            for inp in obj.inputs:
                if inp.widget is not None:
                    inp_widget_class_RB = QRadioButton('Input '+str(obj.inputs.index(inp)))
                    inp_widget_class_RB.toggled.connect(self.class_RB_toggled)
                    self.buttons_class_dict[inp_widget_class_RB] = inp.widget.__class__
                    self.class_selection_layout.addWidget(inp_widget_class_RB, row_count, 1)
                    row_count += 1

            node_inst_class_RB.setChecked(True)


    def class_RB_toggled(self, checked):
        if checked:
            self.active_class_index = list(self.buttons_class_dict.keys()).index(self.sender())
            self.update_code()

    def syntax_highlighting_toggled(self):
        if self.syntax_highlighting_check_box.isChecked():
            self.text_edit.enable_highlighting()
        else:
            self.text_edit.disable_highlighting()
