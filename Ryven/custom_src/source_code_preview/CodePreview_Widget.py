from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QRadioButton, QLabel, QCheckBox, QGridLayout, \
    QPushButton
from PySide2.QtGui import QFont
import inspect

from custom_src.NodeInstance import NodeInstance
from custom_src.source_code_preview.EditSrcCodeInfoDialog import EditSrcCodeInfoDialog
from custom_src.source_code_preview.CodePreview_TextEdit import CodePreview_TextEdit
from custom_src.global_tools.class_inspection import find_type_in_object
from custom_src.source_code_preview.SourceCodeUpdater import SrcCodeUpdater


class CodePreview_Widget(QWidget):
    def __init__(self):
        super(CodePreview_Widget, self).__init__()

        self.text_edit = CodePreview_TextEdit()
        self.node_instance = None
        self.buttons_obj_dict = {}
        self.active_class_index = -1
        self.edited_codes = {}

        settings_layout = QHBoxLayout()

        info_and_SH_layout = QVBoxLayout()

        # info label
        info_label = QLabel('Click on edit for more info!')
        info_label.setFont(QFont('Poppins', 8))
        info_and_SH_layout.addWidget(info_label)

        # syntax highlighting
        self.syntax_highlighting_check_box = QCheckBox('syntax highlighting (alpha)')
        self.syntax_highlighting_check_box.toggled.connect(self.syntax_highlighting_toggled)
        self.syntax_highlighting_check_box.setChecked(True)
        info_and_SH_layout.addWidget(self.syntax_highlighting_check_box)

        settings_layout.addLayout(info_and_SH_layout)

        # class radio buttons widget
        self.class_selection_layout = QGridLayout()

        settings_layout.addLayout(self.class_selection_layout)
        settings_layout.setAlignment(self.class_selection_layout, Qt.AlignRight)

        # edit source code buttons
        edit_buttons_layout = QVBoxLayout()
        self.edit_code_button = QPushButton('edit')
        self.edit_code_button.setMaximumWidth(100)
        self.edit_code_button.clicked.connect(self.edit_code_button_clicked)
        self.override_code_button = QPushButton('override')
        self.override_code_button.setMaximumWidth(100)
        self.override_code_button.setEnabled(False)
        self.override_code_button.clicked.connect(self.override_code_button_clicked)
        self.reset_code_button = QPushButton('reset')
        self.reset_code_button.setMaximumWidth(206)
        self.reset_code_button.setEnabled(False)
        self.reset_code_button.clicked.connect(self.reset_code_button_clicked)
        edit_buttons_top_layout = QHBoxLayout()
        edit_buttons_top_layout.addWidget(self.edit_code_button)
        edit_buttons_top_layout.addWidget(self.override_code_button)
        edit_buttons_layout.addLayout(edit_buttons_top_layout)
        edit_buttons_layout.addWidget(self.reset_code_button)

        settings_layout.addLayout(edit_buttons_layout)


        main_layout = QVBoxLayout()
        main_layout.addLayout(settings_layout)
        main_layout.addWidget(self.text_edit)
        self.setLayout(main_layout)

        self.set_new_NI(None)

    def set_new_NI(self, ni):
        self.disable_editing()

        self.rebuild_class_selection(ni)
        self.update_edit_status()

        self.node_instance = ni

        if ni is None:  # no NI selected
            self.text_edit.set_code('')
            self.edit_code_button.setEnabled(False)
            self.override_code_button.setEnabled(False)
            self.reset_code_button.setEnabled(False)
            return
        self.edit_code_button.setEnabled(True)

        self.update_code()

    def update_code(self):

        self.disable_editing()

        if self.active_class_index == -1 or self.node_instance is None:
            return

        if self.get_current_code_obj() not in self.edited_codes:
            self.text_edit.set_code(inspect.getsource(self.get_current_code_class()))
            self.reset_code_button.setEnabled(False)
        else:
            self.text_edit.set_code(self.edited_codes[self.get_current_code_obj()])
            self.reset_code_button.setEnabled(True)

    def get_current_code_class(self):
        return self.get_current_code_obj().__class__

    def get_current_code_obj(self):
        return list(self.buttons_obj_dict.values())[self.active_class_index]

    def rebuild_class_selection(self, obj):
        # clear layout
        for i in range(self.class_selection_layout.count()):
            item = self.class_selection_layout.itemAt(0)
            widget = item.widget()
            widget.hide()
            self.class_selection_layout.removeItem(item)

        self.buttons_obj_dict = {}
        self.active_class_index = -1

        if find_type_in_object(obj, NodeInstance):
            # NI class
            node_inst_class_RB = QRadioButton('NodeInstance')
            node_inst_class_RB.toggled.connect(self.class_RB_toggled)
            self.buttons_obj_dict[node_inst_class_RB] = obj
            self.class_selection_layout.addWidget(node_inst_class_RB, 0, 0)

            # main_widget class
            if obj.main_widget is not None:
                main_widget_class_RB = QRadioButton('MainWidget')
                main_widget_class_RB.toggled.connect(self.class_RB_toggled)
                self.buttons_obj_dict[main_widget_class_RB] = obj.main_widget
                self.class_selection_layout.addWidget(main_widget_class_RB, 1, 0)

            # data input widgets
            row_count = 0
            for inp in obj.inputs:
                if inp.widget is not None:
                    inp_widget_class_RB = QRadioButton('Input '+str(obj.inputs.index(inp)))
                    inp_widget_class_RB.toggled.connect(self.class_RB_toggled)
                    self.buttons_obj_dict[inp_widget_class_RB] = inp.widget
                    self.class_selection_layout.addWidget(inp_widget_class_RB, row_count, 1)
                    row_count += 1

            node_inst_class_RB.setChecked(True)

    def update_edit_status(self):
        for o in list(self.buttons_obj_dict.keys()):
            if self.edited_codes.keys().__contains__(self.buttons_obj_dict[o]):
                o.setStyleSheet('color: #3B9CD9;')
                f = o.font()
                f.setBold(True)
                o.setFont(f)
            else:
                o.setStyleSheet('color: white;')
                f = o.font()
                f.setBold(False)
                o.setFont(f)

    def class_RB_toggled(self, checked):
        if checked:
            self.active_class_index = list(self.buttons_obj_dict.keys()).index(self.sender())
            self.update_code()

    def syntax_highlighting_toggled(self):
        if self.syntax_highlighting_check_box.isChecked():
            self.text_edit.enable_highlighting()
        else:
            self.text_edit.disable_highlighting()

    def edit_code_button_clicked(self):
        if not EditSrcCodeInfoDialog.dont_show_again:
            info_dialog = EditSrcCodeInfoDialog(self)
            accepted = info_dialog.exec_()
            if not accepted:
                return
        self.enable_editing()

    def enable_editing(self):
        self.text_edit.enable_editing()
        self.override_code_button.setEnabled(True)

    def disable_editing(self):
        self.text_edit.disable_editing()
        self.override_code_button.setEnabled(False)

    def override_code_button_clicked(self):
        new_code = self.text_edit.get_code()
        SrcCodeUpdater.override_code(self.get_current_code_obj(), new_code)
        self.disable_editing()

        self.edited_codes[self.get_current_code_obj()] = new_code
        self.reset_code_button.setEnabled(True)
        self.update_edit_status()

    def reset_code_button_clicked(self):
        code = inspect.getsource(self.get_current_code_class())
        SrcCodeUpdater.override_code(self.get_current_code_obj(), code)
        del self.edited_codes[self.get_current_code_obj()]
        self.update_code()
        self.update_edit_status()