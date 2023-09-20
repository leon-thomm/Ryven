from qtpy.QtCore import Qt
from qtpy.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton, QScrollArea

from .FlowsList_FlowWidget import FlowsList_FlowWidget


class FlowsListWidget(QWidget):
    """Convenience class for a QWidget to easily manage the flows of a session."""

    def __init__(self, session_gui):
        super().__init__()

        self.session_gui = session_gui
        self.list_widgets = []
        self.ignore_name_line_edit_signal = False  # because disabling causes firing twice otherwise

        self.setup_UI()

        self.session_gui.flow_view_created.connect(self.add_new_flow)
        self.session_gui.flow_deleted.connect(self.recreate_list)


    def setup_UI(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        # list scroll area

        self.list_scroll_area = QScrollArea(self)
        self.list_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list_scroll_area.setWidgetResizable(True)
        self.list_scroll_area.setContentsMargins(0, 0, 0, 0)

        self.scroll_area_widget = QWidget()
        self.scroll_area_widget.setContentsMargins(0, 0, 0, 0)
        self.list_scroll_area.setWidget(self.scroll_area_widget)

        self.list_layout = QVBoxLayout()
        self.list_layout.setContentsMargins(0, 0, 0, 0)
        self.list_layout.setAlignment(Qt.AlignTop)
        self.scroll_area_widget.setLayout(self.list_layout)

        self.layout().addWidget(self.list_scroll_area)

        # line edit

        self.new_flow_title_lineedit = QLineEdit()
        self.new_flow_title_lineedit.setPlaceholderText('new flow\'s title')
        self.new_flow_title_lineedit.returnPressed.connect(self.create_flow)

        main_layout.addWidget(self.new_flow_title_lineedit)


        self.recreate_list()


    def recreate_list(self):
        # remove flow widgets
        for i in reversed(range(self.list_layout.count())):
            self.list_layout.itemAt(i).widget().setParent(None)
        self.list_widgets.clear()

        # re-create flow widgets
        for s in self.session_gui.core_session.flows:
            new_widget = FlowsList_FlowWidget(self, self.session_gui, s)
            self.list_widgets.append(new_widget)

        # add flow widgets to layout
        for w in self.list_widgets:
            self.list_layout.addWidget(w)

    def create_flow(self):
        title = self.new_flow_title_lineedit.text()

        if self.session_gui.core_session.flow_title_valid(title):
            self.session_gui.core_session.create_flow(title=title)

    def add_new_flow(self, flow, flow_view):
        self.recreate_list()

    def del_flow(self, flow, flow_widget):
        msg_box = QMessageBox(QMessageBox.Warning, 'sure about deleting flow?',
                              'You are about to delete a flow. This cannot be undone, all content will be lost. '
                              'Do you want to continue?', QMessageBox.Cancel | QMessageBox.Yes, self)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        ret = msg_box.exec_()
        if ret != QMessageBox.Yes:
            return

        self.list_widgets.remove(flow_widget)
        flow_widget.setParent(None)
        self.session_gui.core_session.delete_flow(flow)
        # self.recreate_list()
