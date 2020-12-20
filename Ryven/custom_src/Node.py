from PySide2.QtGui import QColor


class Node:
    def __init__(
            self,
            title: str,
            node_inst_class,
            inputs: list = [],
            input_widgets: dict = {},
            outputs: list = [],
            description: str = '',
            style: str = 'extended',
            color: str = '#A9D5EF',
            widget=None,
            widget_pos: str = 'under ports',
            type_: str = ''
    ):

        self.title = title
        self.node_inst_class = node_inst_class
        self.inputs = inputs
        self.outputs = outputs
        self.description = description
        self.design_style = style
        self.color = color
        self.main_widget_class = widget
        self.main_widget_pos = widget_pos
        self.type_ = type_
        self.custom_input_widgets = input_widgets  # {iw.__name__: iw for iw in input_widgets}  # {name: class}
        # print(self.custom_input_widgets)
        # self.type_ = type_  # just for clarity - grouping nodes (f.ex. 'http')
        # self.description = description

        # self.package = None  # everything else than 'built in' means that the node came from outside (important)

        # # self.has_main_widget = False
        # self.main_widget_class = widget
        # self.main_widget_pos = widget_pos
        # self.design_style = 'extended'  # default value just for testing
        # self.color = QColor(198, 154, 21)  # default value just for testing
        #
        # #   dynamic: (get copied and can be individually edited in NIs)
        # self.inputs = []
        # self.outputs = []


class NodePort:
    def __init__(self,
                 type_: str = 'data',
                 label: str = '',
                 widget: str = None,
                 widget_pos: str = 'under'):
        self.type_ = type_
        self.label = label
        self.widget_name = widget
        self.widget_pos = widget_pos
