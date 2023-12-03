from ryven.gui_env import *
from .nodes import *

from qtpy.QtWidgets import QLabel


class Sub1NodeLabelWidget(NodeMainWidget, QLabel):
    def __init__(self, node):
        QLabel.__init__(self, "Sub1 Node's main widget")
        NodeMainWidget.__init__(self, node)


@node_gui(Sub1Node)
class MatrixNodeBaseGui(NodeGUI):
    main_widget_class = Sub1NodeLabelWidget
    main_widget_pos = 'below ports'
