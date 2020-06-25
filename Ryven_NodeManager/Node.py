from PySide2.QtCore import QObject, Signal


class Node(QObject):  # QObject inheritance for the Signal

    title_changed = Signal()

    def __init__(self, content_nodes_widget=None):
        super(Node, self).__init__()

        # IMPORTANT: the values of these attributes are only used for loading, after that, they won't be modified
        # anymore, all the information for saving then comes from the content_widget. This might seem stupid, but
        # updating everything here when anything changes in the content_widget would be a mess and a big source for
        # mistakes.
        # stored in NodeContentWidget and only important for imports:
        self.title = 'new node'
        self.type = ''
        self.description = ''
        self.module_name = ''
        self.class_name = ''
        self.meta_code = ''
        self.design_style = ''
        self.color = ''
        self.has_main_widget = True
        self.widget_position = ''
        self.main_widget_content = ''
        self.custom_input_widgets = []
        self.custom_input_widget_contents = []
        self.inputs = []
        self.outputs = []


        self.content_widget = content_nodes_widget
