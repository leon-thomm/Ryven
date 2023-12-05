from ryven.gui_env import *
from qtpy.QtWidgets import (
    QWidget, 
    QVBoxLayout, 
    QLabel,
    QCheckBox,
)
from .nodes import MyNode


class MyNodeInspector(NodeInspectorWidget, QWidget):
    def __init__(self, params):
        NodeInspectorWidget.__init__(self, params)
        QWidget.__init__(self)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(QLabel('This is a custom inspector for MyNode.'))
        self.cb = QCheckBox('This is an undoable checkbox.')
        self.cb.stateChanged.connect(self.on_cb_changed)
        self.layout().addWidget(self.cb)
    
    def on_cb_changed(self, state):
        def undo_fn():
            self.cb.stateChanged.disconnect(self.on_cb_changed)
            self.cb.setChecked(not state)
            self.cb.stateChanged.connect(self.on_cb_changed)
        
        def redo_fn():
            self.cb.stateChanged.disconnect(self.on_cb_changed)
            self.cb.setChecked(state)
            self.cb.stateChanged.connect(self.on_cb_changed)
        
        self.push_undo(
            text=f'{self.node.title} inspector checkbox: {state}',
            undo_fn=undo_fn,
            redo_fn=redo_fn,
        )


@node_gui(MyNode)
class MyNodeGui(NodeGUI):
    inspector_widget_class = MyNodeInspector
    wrap_inspector_in_default = True
