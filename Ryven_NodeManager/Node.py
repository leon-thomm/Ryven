from PySide2.QtCore import QObject, Signal


class Node(QObject):  # QObject inheritance for the Signal
    """All values are initial! They get set when nodes are imported but do not get synchronized yet when the
    NodeContentWidget is being changed. When exporting, all info comes from the NodeContentWidget."""

    title_changed = Signal()

    def __init__(self, content_nodes_widget=None):
        super(Node, self).__init__()

        self.title = 'new node'
        self.type = ''
        self.description = ''
        self.module_name = ''
        self.class_name = None
        self.design_style = ''
        self.color = ''
        self.has_main_widget = False
        self.widget_position = ''
        self.custom_input_widgets = []
        self.custom_input_widget_metacodes = []
        self.custom_input_widget_metacodes_file_paths = []
        self.inputs = []
        self.outputs = []

        # src code
        f = open('template files/node_instance_default_template.txt', 'r')
        self.meta_code = f.read()
        f.close()
        self.meta_code_file_path = None
        # main widget code
        f = open('template files/main_widget_default_template.txt', 'r')
        self.main_widget_meta_code = f.read()
        f.close()
        self.main_widget_meta_code_file_path = None

        self.content_widget = content_nodes_widget