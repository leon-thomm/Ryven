from typing import Union, Type, List, Optional, Tuple, TypeVar

from qtpy.QtWidgets import (
    QWidget, 
    QVBoxLayout, 
    QLabel, 
    QTextEdit,
    QSplitter,
)

from qtpy.QtCore import Qt
from ryvencore import Node

from .WidgetBaseClasses import NodeInspectorWidget


class InspectorView(QWidget):
    """
    A widget that can display the inspector of the currently selected node.
    """

    def __init__(self, flow_view, parent: Optional[QWidget] = None):
        super().__init__(parent=parent)
        self.node: Optional[Node] = None
        self.inspector_widget: Optional[NodeInspectorWidget] = None
        self.flow_view = flow_view

        self.setup_ui()
        self.flow_view.nodes_selection_changed.connect(self.set_selected_nodes)

    def setup_ui(self):
        self.setLayout(QVBoxLayout())

    def set_selected_nodes(self, nodes: List[Node]):
        if len(nodes) == 0:
            self.set_node(None)
        else:
            self.set_node(nodes[-1])

    def set_node(self, node: Optional[Node]):
        """Sets a node for inspection, if it exists. Otherwise clears the inspector"""

        if self.node == node:
            return

        if self.inspector_widget is not None:
            assert isinstance(self.inspector_widget, QWidget)
            self.inspector_widget.setVisible(False)
            self.inspector_widget.setParent(None)  # type: ignore
            self.inspector_widget.unload()
            
        self.node = None
        self.inspector_widget = None

        if node is not None:
            self.node = node
            assert hasattr(self.node, 'gui')
            self.inspector_widget = self.node.gui.inspector_widget
            assert isinstance(self.inspector_widget, QWidget)
            self.layout().addWidget(self.inspector_widget)
            self.inspector_widget.load()
            self.inspector_widget.setVisible(True)


class NodeInspectorDefaultWidget(NodeInspectorWidget, QWidget):
    """
    Default node inspector widget implementation.
    Can also be extended by embedding a custom widget.
    """
    
    @staticmethod
    def _big_bold_text(txt: str):
        return f'<b><bold>{txt}</bold></b>'
    
    def __init__(self, params, child: Optional[NodeInspectorWidget] = None):
        QWidget.__init__(self)
        NodeInspectorWidget.__init__(self, params)

        self.child = child
        self.setLayout(QVBoxLayout())

        self.title_label: QLabel = QLabel()
        self.title_label.setText(
            f'<h2>{self.node.title}</h2> '
            f'<h4>id: {self.node.global_id}, pyid: {id(self.node)}</h4>'
        )
        # title
        self.layout().addWidget(self.title_label)
        
        # content splitter
        self.content_splitter = QSplitter()
        self.content_splitter.setOrientation(Qt.Orientation.Vertical)
        self.layout().addWidget(self.content_splitter)
        
        if child is not None:
            assert isinstance(child, QWidget)
            self.content_splitter.addWidget(child)

        desc = self.node.__doc__ if self.node.__doc__ and self.node.__doc__ != "" else "No description given"
        bbt = NodeInspectorDefaultWidget._big_bold_text
        
        self.description_area: QTextEdit = QTextEdit()
        self.description_area.setReadOnly(True)
        self.description_area.setText(f"""
<html>
    <body>
        {bbt('Title:')} {self.node.title}<br>
        {bbt('Version:')} {self.node.version}<br><br>
        {bbt('Description:')}<br><br>
        {desc}
    </body>
</html>
        """)
    
        self.content_splitter.addWidget(self.description_area)
    
    def load(self):
        super().load()
        if self.child:
            self.child.load()
    
    def unload(self):
        if self.child:
            self.child.unload()
        super().unload()
