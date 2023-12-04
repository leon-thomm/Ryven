from ryven.gui_env import *
from qtpy.QtWidgets import (
    QWidget, 
    QVBoxLayout, 
    QLabel, 
)
from .nodes import MyNode


class MyNodeInspector(NodeInspectorWidget, QWidget):
    def __init__(self, params):
        NodeInspectorWidget.__init__(self, params)
        QWidget.__init__(self)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(QLabel('This is a custom inspector for MyNode.'))


@node_gui(MyNode)
class MyNodeGui(NodeGUI):
    inspector_widget_class = MyNodeInspector
    wrap_inspector_in_default = True
