from abc import ABC, abstractmethod
import PySide2.QtCore
from qtpy.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QScrollArea
from ryvencore import Node
from typing import Union
from ryvencore_qt.src.flows.FlowView import FlowView
from ryvencore_qt.src.flows.nodes.NodeItem import NodeItem
from typing import Type, List


class InspectorWidget(QWidget):
    """The widget that handles the inspecting"""

    def __init__(self, flow_view: FlowView, parent: QWidget = None):
        super().__init__(parent=parent)
        self.node: Node = None
        self.inspector: BaseNodeInspector = None
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

    def set_node(self, node: Node):
        """Sets a node for inspection, if it exists. Otherwise clears the inspector"""
        if self.node == node:
            return

        if self.inspector:
            self.inspector.unload()
        self.node = None
        self.inspector = None
        self.clear()

        node_cls = type(node)
        if not node:
            return

        self.node = node
        if hasattr(node_cls, 'inspector'):
            inspect_cls: Type[BaseNodeInspector] = node_cls.inspector
            self.inspector = inspect_cls(node, self.flow_view)
        else:
            self.inspector = NodeInspector(node, self.flow_view)

        inspect_gui = self.inspector.create_inspector(self)
        if inspect_gui:
            self.layout().addWidget(inspect_gui)

    def clear(self):
        """
        A typical method for clearing a layout. This does not
        delete the widgets. This is left to the InspectorGUI.
        Ideally, one would want to handle the removal there as
        well, if the widget is not deleted.
        """
        layout = self.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
            else:
                layout.removeItem(item)


class BaseNodeInspector(ABC):
    """Abstract class for an inspector. Requires the node."""

    def __init__(self, node: Node, flow_view: FlowView):
        self.node: Node = node
        self.flow_view: FlowView = flow_view

    @abstractmethod
    def create_inspector(
        self, parent: QWidget
    ) -> Union[QWidget, None]:  # should be QWidget | None in 3.10+
        """
        Creates the inspector. The parent is also provided. If the
        function returns None, it means parenting has been applied
        here. Otherwise, it must be applied externally within the
        corresponding application.

        The implementation is left for the user
        """
        pass

    def unload(self):
        """
        VIRTUAL
        This is called when the inspector widget changes the internal
        GUI. Should be used for clearing up any Widgets in order to
        free up memory.
        """
        pass

    def node_item(self):
        return self.flow_view.node_items__cache.get(self.node)


class NodeInspector(BaseNodeInspector):
    """
    This is a basic implementation. Will be used if there is no inspector
    provided. Can also be subclassed for easier inspector building.
    """

    def __init__(self, node: Node, flow_view: FlowView):
        super().__init__(node, flow_view)
        self.inspection_widget = NodeInspectorWidget()
        self.inspection_widget.populate(node, self.node_item())

    def create_inspector(self, parent: QWidget):
        parent.layout().addWidget(self.inspection_widget)
        self.attach_inspector(self.inspection_widget.inspect_area)

    def attach_inspector(self, parent: QScrollArea):
        pass
    
    def unload(self):
        self.inspection_widget.deleteLater()
        pass


class NodeInspectorWidget(QWidget):
    """The basic implementation widget"""

    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

        self.title_label: QLabel = QLabel()
        self.layout().addWidget(self.title_label)

        self.inspect_area: QWidget = QWidget()
        self.inspect_area.setLayout(QVBoxLayout())
        self.layout().addWidget(self.inspect_area)

        self.description_area: QTextEdit = QTextEdit()
        self.description_area.setReadOnly(True)
        self.layout().addWidget(self.description_area)

    def populate(self, node: Node, node_item: NodeItem):
        # self.title_label.setText(node_item.widget.title_label.title_str)
        self.title_label.setText(node.title)
        
        desc = "No description given"
        if hasattr(node, 'description'):
            desc = node.description
        self.description_area.setText(
            f"""Title: {node.title}, Version: {node.version}
                
Description:\n{node.__doc__ if node.__doc__ else "No description provided"}
            """
        )
