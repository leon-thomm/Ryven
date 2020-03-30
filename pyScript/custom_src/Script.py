from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import QObject, Signal

from custom_src.GlobalAccess import GlobalStorage
from custom_src.Log import Logger

from ui.w_ui_script import WUIScript

# from custom_src.VyMain_DetailsWidget import VyMain_DetailsWidget
from custom_src.Flow import Flow
from custom_src.VariablesHandler import VariablesHandler
from custom_src.custom_nodes.GetVar_NodeInstance import GetVar_NodeInstance


class Script(QObject):

    name_changed = Signal(str)

    def __init__(self, main_window, name, config=None):
        super(Script, self).__init__()

        self.main_window = main_window
        self.widget = WUIScript()

        # general attributes
        self.logger = Logger(self)
        self.variables = []
        self.variables_handler = None
        self.name = name
        self.details_widget = QPushButton('HELO HELOO!!')  # None
        self.set_details_widget(self, self.details_widget)
        self.flow = None
        self.thumbnail_source = ''  # URL to the thumbnail picture

        if config:
            self.name = config['name']
            self.variables_handler = VariablesHandler(self, config['variables'])
            self.flow = Flow(main_window, self, config['flow'])
            self.variables_handler.flow = self.flow
        else:
            self.flow = Flow(main_window, self)
            self.variables_handler = VariablesHandler(self)

        # variables list widget
        self.widget.ui.variables_scrollArea.setWidget(self.variables_handler.list_widget)
        # I connect the events between UI and the var handler here, because there are only a few actions over UI
        self.widget.ui.add_variable_push_button.clicked.connect(self.add_var_clicked)
        self.widget.ui.new_var_name_lineEdit.returnPressed.connect(self.new_var_line_edit_return_pressed)


        self.widget.ui.splitter.insertWidget(0, self.flow)
        # self.widget.ui.logs_scrollArea.setWidgetResizable(False)
        self.widget.ui.logs_scrollArea.setWidget(self.logger)
        self.widget.ui.splitter.setSizes([700, 0])


    def set_details_widget(self, provider, w):
        pass


    # I connect the events between UI and the var handler here, because there are only a few actions over UI
    def add_var_clicked(self):
        self.variables_handler.create_new_var(self.widget.ui.new_var_name_lineEdit.text())

    def new_var_line_edit_return_pressed(self):
        self.variables_handler.create_new_var(self.widget.ui.new_var_name_lineEdit.text())


    def get_json_data(self):
        script_dict = {'name': self.name,
                       'variables': self.variables_handler.get_json_data(),
                       'flow': self.flow.get_json_data()}

        return script_dict