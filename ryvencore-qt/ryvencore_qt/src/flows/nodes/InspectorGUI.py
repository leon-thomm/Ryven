from abc import ABC, abstractmethod
from qtpy.QtWidgets import QWidget, QVBoxLayout
from ryvencore import Node
from typing import Union
from ryvencore_qt.src.flows.FlowView import FlowView
from typing import Type, List


class InspectorWidget(QWidget):
    """The widget that handles the inspecting"""
    
    def __init__(self, flow_view: FlowView, parent: QWidget = None):
        super().__init__(parent = parent)
        self.node: Node = None
        self.inspector: InspectorGUI = None
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
        if not node or not hasattr(node_cls, 'inspector'):
            return
        
        self.node = node
        inspect_cls: Type[InspectorGUI] = node_cls.inspector
        self.inspector: InspectorGUI = inspect_cls(node)
        
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
                
            

class InspectorGUI(ABC):
    """Abstract class for an inspector. Requires the node."""
    
    def __init__(self, node: Node):
        self.node: Node = node
    
    
    @abstractmethod
    def create_inspector(self, parent: QWidget) -> Union[QWidget, None]: # should be QWidget | None in 3.10+
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