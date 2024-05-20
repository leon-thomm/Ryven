# prevent circular imports
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ryven.gui.main_window import MainWindow

from dataclasses import dataclass
from typing import Type, Optional, List

from qtpy.QtCore import Qt
from qtpy.QtWidgets import (
    QWidget, 
    QHBoxLayout, 
    QVBoxLayout, 
    QRadioButton, 
    QLabel, 
    QCheckBox, 
    QGridLayout,
    QPushButton
)

from ryven.gui.code_editor.EditSrcCodeInfoDialog import EditSrcCodeInfoDialog
from ryven.gui.code_editor.CodeEditorWidget import CodeEditorWidget
from ryven.gui.code_editor.SourceCodeUpdater import SrcCodeUpdater
from ryven.gui.code_editor.codes_storage import (
    class_codes, 
    mod_codes, 
    modif_codes, 
    NodeTypeCodes,
    Inspectable, 
    NodeInspectable, 
    MainWidgetInspectable, 
    CustomInputWidgetInspectable,
    load_src_code,
)

from ryvencore import Node
from ryvencore_qt.src.flows.FlowView import FlowView


class LoadSrcCodeButton(QPushButton):
    def __init__(self):
        super().__init__('load source code')
        self._node = None
    
    @property
    def node(self):
        return self._node
    
    @node.setter
    def node(self, node):
        self._node = node


class LinkedRadioButton(QRadioButton):
    """Represents a button linked to one particular inspectable object."""

    def __init__(self, name, obj: Inspectable):
        super().__init__(name)
        self.representing: Inspectable = obj


class CodePreviewWidget(QWidget):
    def __init__(self, main_window: MainWindow, flow_view: FlowView):
        super().__init__()

        self.edits_enabled = main_window.config.src_code_edits_enabled
        self.current_insp: Optional[Inspectable] = None

        # widgets
        self.radio_buttons: List[QRadioButton] = []
        self.text_edit = CodeEditorWidget(main_window.theme)

        self.setup_ui()
        self._set_node(None)
        flow_view.nodes_selection_changed.connect(self.set_selected_nodes)

    def setup_ui(self):

        secondary_layout = QHBoxLayout()

        # load source code button
        self.load_code_button = LoadSrcCodeButton()
        self.load_code_button.setProperty('class', 'small_button')
        secondary_layout.addWidget(self.load_code_button)
        self.load_code_button.hide()
        self.load_code_button.clicked.connect(self._load_code_button_clicked)

        # class radio buttons widget
        self.class_selection_layout = QHBoxLayout()  # QGridLayout()

        secondary_layout.addLayout(self.class_selection_layout)
        self.class_selection_layout.setAlignment(Qt.AlignLeft)
        # secondary_layout.setAlignment(self.class_selection_layout, Qt.AlignLeft)

        # edit source code buttons
        if self.edits_enabled:
            self.edit_code_button = QPushButton('edit')
            self.edit_code_button.setProperty('class', 'small_button')
            self.edit_code_button.setMaximumWidth(100)
            self.edit_code_button.clicked.connect(self._edit_code_button_clicked)
            self.override_code_button = QPushButton('override')
            self.override_code_button.setProperty('class', 'small_button')
            self.override_code_button.setMaximumWidth(100)
            self.override_code_button.setEnabled(False)
            self.override_code_button.clicked.connect(self._override_code_button_clicked)
            self.reset_code_button = QPushButton('reset')
            self.reset_code_button.setProperty('class', 'small_button')
            self.reset_code_button.setMaximumWidth(206)
            self.reset_code_button.setEnabled(False)
            self.reset_code_button.clicked.connect(self._reset_code_button_clicked)

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
            self._set_node(None)
        else:
            self._set_node(nodes[-1])

    def _set_node(self, node: Optional[Node]):
        self.node = node

        if node is None:
            # clear view
            if self.edits_enabled:
                self.edit_code_button.setEnabled(False)
                self.override_code_button.setEnabled(False)
                self.reset_code_button.setEnabled(False)
            self.text_edit.set_code('')
            self._clear_class_layout()
        else:
            if class_codes.get(node.__class__) is None:
                # source code not loaded yet
                self.load_code_button.node = node
                self.load_code_button.show()
                self._clear_class_layout()
                self._update_code(NodeInspectable(node, 'source not loaded'))
            else:
                self._process_node_src(node)

    def _process_node_src(self, node: Node):
        self._rebuild_class_selection(node)
        codes = class_codes[node.__class__]
        assert codes is not None
        code = codes.node_cls
        if self.edits_enabled and node in modif_codes:
            code = modif_codes[node]
        self._update_code(NodeInspectable(node, code))

    def _update_code(self, insp: Inspectable):
        if self.edits_enabled:
            self._disable_editing()
            self._update_radio_buttons_edit_status()
            self.edit_code_button.setEnabled(True)
            self.reset_code_button.setEnabled(insp.obj in modif_codes)

        self.text_edit.disable_highlighting()

        self.current_insp = insp
        self.text_edit.set_code(insp.code)


    def _rebuild_class_selection(self, node: Node):
        assert hasattr(node, 'gui')

        self.load_code_button.hide()
        self._clear_class_layout()
        self.radio_buttons.clear()

        codes = class_codes[node.__class__]
        assert codes is not None

        def register_rb(rb: QRadioButton):
           rb.toggled.connect(self._class_rb_toggled)
           self.class_selection_layout.addWidget(rb)
           self.radio_buttons.append(rb)

        # node radio button
        code = codes.node_cls
        code = modif_codes.get(node, code)
        register_rb(LinkedRadioButton('node', NodeInspectable(node, code)))

        # main widget radio button
        if codes.main_widget_cls is not None:
            mw = node.gui.main_widget()
            code = codes.main_widget_cls
            code = modif_codes.get(mw, code)
            register_rb(LinkedRadioButton(
                'main widget',
                MainWidgetInspectable(node, node.gui.main_widget(), code)
            ))

        # custom input widgets
        for i in range(len(node.inputs)):
            inp = node.inputs[i]
            if inp in node.gui.input_widgets:
                name = node.gui.input_widgets[inp]['name']
                widget = node.gui.item.inputs[i].widget
                code = codes.custom_input_widget_clss[name]
                code = modif_codes.get(widget, code)
                register_rb(LinkedRadioButton(
                    f'input {i}', CustomInputWidgetInspectable(node, widget, code)
                ))

        self.radio_buttons[0].setChecked(True)

    def _clear_class_layout(self):
        # clear layout
        for i in range(self.class_selection_layout.count()):
            item = self.class_selection_layout.itemAt(0)
            widget = item.widget()
            widget.hide()
            self.class_selection_layout.removeItem(item)
    
    def _load_code_button_clicked(self) -> None:
        node: Node = self.sender().node
        load_src_code(node.__class__)
        self.load_code_button.hide()
        self._process_node_src(node)

    def _update_radio_buttons_edit_status(self):
        """Draws radio buttons referring to modified objects bold."""

        for br in self.radio_buttons:
            if modif_codes.get(br.representing.obj) is not None:
                # o.setStyleSheet('color: #3B9CD9;')
                f = br.font()
                f.setBold(True)
                br.setFont(f)
            else:
                # o.setStyleSheet('color: white;')
                f = br.font()
                f.setBold(False)
                br.setFont(f)

    def _class_rb_toggled(self, checked: bool) -> None:
        if checked:
            rb: LinkedRadioButton = self.sender()
            self._update_code(rb.representing)

    def _edit_code_button_clicked(self):
        if not EditSrcCodeInfoDialog.dont_show_again:
            info_dialog = EditSrcCodeInfoDialog(self)
            accepted = info_dialog.exec_()
            if not accepted:
                return
        self._enable_editing()

    def _enable_editing(self):
        self.text_edit.enable_editing()
        self.override_code_button.setEnabled(True)

    def _disable_editing(self):
        self.text_edit.disable_editing()
        self.override_code_button.setEnabled(False)

    def _override_code_button_clicked(self):
        new_code = self.text_edit.get_code()
        err = SrcCodeUpdater.override_code(
            obj=self.current_insp.obj,
            new_class_src=new_code,
        )
        if err is None:
            self.current_insp.code = new_code
            modif_codes[self.current_insp.obj] = new_code
            self._disable_editing()
            self.reset_code_button.setEnabled(True)
            self._update_radio_buttons_edit_status()
        else:
            # TODO: show error message
            ...

    def _reset_code_button_clicked(self):

        insp = self.current_insp
        o = insp.obj
        orig_code = ''
        if isinstance(insp, NodeInspectable):
            orig_code = class_codes[o.__class__].node_cls
        elif isinstance(insp, MainWidgetInspectable):
            orig_code = class_codes[o.__class__].main_widget_cls
        elif isinstance(insp, CustomInputWidgetInspectable):
            orig_code = class_codes[o.__class__].custom_input_widget_clss[o.__class__]

        err = SrcCodeUpdater.override_code(
            obj=self.current_insp.obj,
            new_class_src=orig_code
        )

        if err is None:
            self.current_insp.code = orig_code
            del modif_codes[self.current_insp.obj]
            self._update_code(self.current_insp)
        else:
            # TODO: show error message
            ...
