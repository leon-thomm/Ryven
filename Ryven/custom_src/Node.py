from PySide2.QtGui import QColor


class Node:
    def __init__(self):
        # GENERAL ATTRIBUTES
        #   static:
        self.title = ''
        self.type_ = ''  # just for clarity - grouping nodes (f.ex. 'http')
        self.description = ''
        self.package = None  # everything else than 'built in' means that the node came from outside (important)
        self.has_main_widget = False
        self.main_widget_class = None
        self.main_widget_pos = ''
        self.design_style = 'extended'  # default value just for testing
        self.color = QColor(198, 154, 21)  # default value just for testing

        #   dynamic: (get copied and can be individually edited in NIs)
        self.inputs = []
        self.outputs = []


class NodePort:
    def __init__(self):
        # general attributes
        self.type_ = ''
        self.label = ''
        self.widget_name = None
        self.widget_pos = 'under'