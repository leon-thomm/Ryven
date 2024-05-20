# prevent circular imports
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .FlowView import FlowView

from qtpy.QtWidgets import QGraphicsProxyWidget, QGraphicsSceneHoverEvent


class FlowViewProxyWidget(QGraphicsProxyWidget):
    """Ensures easy controls event handling for QProxyWidgets in the flow."""

    def __init__(self, flow_view, parent=None):
        super(FlowViewProxyWidget, self).__init__(parent)

        self.flow_view = flow_view

    def mousePressEvent(self, arg__1):
        QGraphicsProxyWidget.mousePressEvent(self, arg__1)
        if arg__1.isAccepted():
            self.flow_view.mouse_event_taken = True

    def mouseReleaseEvent(self, arg__1):
        self.flow_view.mouse_event_taken = True
        QGraphicsProxyWidget.mouseReleaseEvent(self, arg__1)

    def wheelEvent(self, event):
        QGraphicsProxyWidget.wheelEvent(self, event)

    def keyPressEvent(self, arg__1):
        QGraphicsProxyWidget.keyPressEvent(self, arg__1)
        if arg__1.isAccepted():
            self.flow_view.ignore_key_event = True


class FlowViewProxyHoverWidget(FlowViewProxyWidget):
    """Additional hover controls for QProxyWidgets in the flow."""

    def __init__(self, flow_view: FlowView, parent=None):
        super(FlowViewProxyHoverWidget, self).__init__(flow_view, parent)
        self._is_hovered: bool = False

    def hoverEnterEvent(self, event: QGraphicsSceneHoverEvent):
        super().hoverEnterEvent(event)
        self._is_hovered = True

    def hoverLeaveEvent(self, event: QGraphicsSceneHoverEvent):
        super().hoverLeaveEvent(event)
        self._is_hovered = False

    def is_hovered(self) -> bool:
        return self._is_hovered
