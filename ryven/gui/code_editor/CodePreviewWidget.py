from qtpy.QtCore import Qt
from qtpy.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QRadioButton, QLabel, QCheckBox, QGridLayout, \
    QPushButton

from ryven.gui.code_editor.EditSrcCodeInfoDialog import EditSrcCodeInfoDialog
from ryven.gui.code_editor.CodeEditorWidget import CodeEditorWidget
from ryven.gui.code_editor.SourceCodeUpdater import SrcCodeUpdater


class LinkedRadioButton(QRadioButton):
    """Represents a button linked to one particular"""

    def __init__(self, name, node, obj):
        super().__init__(name)

        self.node = node
        self.obj = obj


class CodePreviewWidget(QWidget):
    def __init__(self, main_window, flow):
        super(CodePreviewWidget, self).__init__()

        self.codes = {
            # structure:
            #
            #   <node>: {
            #       <object>: {                 (the node instance or some widget instance)
            #           'title': str,           (for faster widget building)
            #           'original': str,        (original code comes from Node.__class_codes__)
            #           'edited': str(None),    (initially None)
            #       }
            #   }
        }
        self.node = None            # currently displayed node
        self.current_obj = None     # reference to the currently shown/edited object
        self.radio_buttons = []     # the radio buttons to select a source

        flow.nodes_selection_changed.connect(self.set_selected_nodes)

        self.text_edit = CodeEditorWidget(main_window.theme)
        self.setup_ui()

        self.set_node(None)

    def setup_ui(self):

        secondary_layout = QHBoxLayout()

        # class radio buttons widget
        self.class_selection_layout = QHBoxLayout()  # QGridLayout()

        secondary_layout.addLayout(self.class_selection_layout)
        self.class_selection_layout.setAlignment(Qt.AlignLeft)
        # secondary_layout.setAlignment(self.class_selection_layout, Qt.AlignLeft)

        # edit source code buttons
        self.edit_code_button = QPushButton('edit')
        self.edit_code_button.setProperty('class', 'small_button')
        self.edit_code_button.setMaximumWidth(100)
        self.edit_code_button.clicked.connect(self.edit_code_button_clicked)
        self.override_code_button = QPushButton('override')
        self.override_code_button.setProperty('class', 'small_button')
        self.override_code_button.setMaximumWidth(100)
        self.override_code_button.setEnabled(False)
        self.override_code_button.clicked.connect(self.override_code_button_clicked)
        self.reset_code_button = QPushButton('reset')
        self.reset_code_button.setProperty('class', 'small_button')
        self.reset_code_button.setMaximumWidth(206)
        self.reset_code_button.setEnabled(False)
        self.reset_code_button.clicked.connect(self.reset_code_button_clicked)

        edit_buttons_layout = QHBoxLayout()
        # edit_buttons_layout.addWidget(self.highlight_code_button)
        edit_buttons_layout.addWidget(self.edit_code_button)
        edit_buttons_layout.addWidget(self.override_code_button)
        edit_buttons_layout.addWidget(self.reset_code_button)
        # edit_buttons_layout.addWidget(self.highlight_code_button)

        secondary_layout.addLayout(edit_buttons_layout)
        edit_buttons_layout.setAlignment(Qt.AlignRight)

        main_layout = QVBoxLayout()
        main_layout.addLayout(secondary_layout)
        main_layout.addWidget(self.text_edit)
        self.setLayout(main_layout)

    def set_selected_nodes(self, nodes):
        if len(nodes) == 0:
            self.set_node(None)
        else:
            self.set_node(nodes[-1])

    def set_node(self, node):

        self.node = node

        if node is None or node.__class_codes__ is None:  # no node selected / only imported nodes have __class_codes__
            # clear view
            self.text_edit.set_code('')
            self.edit_code_button.setEnabled(False)
            self.override_code_button.setEnabled(False)
            self.reset_code_button.setEnabled(False)
            self.clear_class_layout()
            return


        if node not in self.codes:  # node not yet registered

            # save class sources for all objects (node, main_widget, custom input widgets)

            # saving it in this structure enables easy view updates and src code overrides

            node_objects = {
                node: {
                    'title': 'node',
                    'original cls': node.__class_codes__['node cls'],
                    'original mod': node.__class_codes__['node mod'],
                    'modified cls': None,
                },
            }

            if node.main_widget():
                node_objects[node.main_widget()] = {
                    'title': 'main widget',
                    'original cls': node.__class_codes__['main widget cls'],
                    'original mod': node.__class_codes__['main widget mod'],
                    'modified cls': None
                }

            for i in range(len(node.inputs)):
                iw = node.item.inputs[i].widget
                if iw:
                    # find code
                    code = ''
                    for name, cls in node.input_widget_classes.items():
                        if cls == iw.__class__:
                            code = node.__class_codes__['custom input widgets'][name]['cls']
                            break

                    else:  # no break -> no custom widget (builtin widget) -> ignore
                        continue

                    node_objects[iw] = {
                        'title': f'inp {i}',
                        'original cls': code,
                        'modified cls': None,
                    }

            self.codes[node] = node_objects

        self.rebuild_class_selection(node)
        self.update_edit_statuses()

        self.edit_code_button.setEnabled(True)

        self.update_code(node, node)

    def update_code(self, node, obj):
        """
        Updates the 'modified' field in the nodes dict
        """

        self.disable_editing()
        self.text_edit.disable_highlighting()

        self.current_obj = obj

        orig = self.codes[node][obj]['original cls']
        modf = self.codes[node][obj]['modified cls']

        if modf:
            code = modf
            self.reset_code_button.setEnabled(True)
        else:
            code = orig
            self.reset_code_button.setEnabled(False)

        self.text_edit.set_code(code)

    def rebuild_class_selection(self, node):

        self.clear_class_layout()

        self.radio_buttons.clear()

        for obj, d in self.codes[node].items():
            rb = LinkedRadioButton(d['title'], node, obj)
            rb.toggled.connect(self.class_RB_toggled)
            self.class_selection_layout.addWidget(rb)
            self.radio_buttons.append(rb)

        self.radio_buttons[0].setChecked(True)

    def clear_class_layout(self):

        # clear layout
        for i in range(self.class_selection_layout.count()):
            item = self.class_selection_layout.itemAt(0)
            widget = item.widget()
            widget.hide()
            self.class_selection_layout.removeItem(item)

    def update_edit_statuses(self):
        """
        Draws radio buttons referring to modified objects bold
        """

        for b in self.radio_buttons:
            if self.codes[b.node][b.obj]['modified cls']:
                # o.setStyleSheet('color: #3B9CD9;')
                f = b.font()
                f.setBold(True)
                b.setFont(f)
            else:
                # o.setStyleSheet('color: white;')
                f = b.font()
                f.setBold(False)
                b.setFont(f)

    def class_RB_toggled(self, checked):
        if checked:
            self.update_code(self.sender().node, self.sender().obj)

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

        SrcCodeUpdater.override_code(
            obj=self.current_obj,
            new_class_src=new_code,
        )

        self.codes[self.node][self.current_obj]['modified cls'] = new_code

        self.disable_editing()

        self.reset_code_button.setEnabled(True)
        self.update_edit_statuses()

    def reset_code_button_clicked(self):

        code = self.codes[self.node][self.current_obj]['original cls']

        SrcCodeUpdater.override_code(
            obj=self.current_obj,
            new_class_src=code
        )

        self.codes[self.node][self.current_obj]['modified cls'] = None

        self.update_code(self.node, self.current_obj)
        self.update_edit_statuses()
