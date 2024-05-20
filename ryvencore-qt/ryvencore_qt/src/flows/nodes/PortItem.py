# prevent circular imports
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .NodeGUI import NodeGUI
    from .NodeItem import NodeItem
    from ..FlowView import FlowView

from typing import Tuple, Optional

from qtpy.QtWidgets import QGraphicsGridLayout, QGraphicsWidget, QGraphicsLayoutItem
from qtpy.QtCore import Qt, QRectF, QPointF, QSizeF
from qtpy.QtGui import QFontMetricsF, QFont

from ryvencore import serialize, Data
from ryvencore.NodePort import NodeOutput, NodeInput, NodePort
from ryvencore.utils import deserialize

from ...GUIBase import GUIBase
from ...utils import get_longest_line, shorten
from ..FlowViewProxyWidget import FlowViewProxyWidget
from .WidgetBaseClasses import NodeInputWidget

# utils


def is_connected(port):
    if isinstance(port, NodeOutput):
        is_connected = len(port.node.flow.connected_inputs(port)) > 0
    else:
        is_connected = port.node.flow.connected_output(port) is not None
    return is_connected


def val(port):
    if isinstance(port, NodeOutput):
        return port.val.payload if isinstance(port.val, Data) else None
    else:
        conn_out = port.node.flow.connected_output(port)
        if conn_out:
            return conn_out.val.payload if conn_out.val is not None else None
        else:
            return None


def connections(port):
    if isinstance(port, NodeOutput):
        return [(port, i) for i in port.node.flow.connected_inputs(port)]
    else:
        conn_out = port.node.flow.connected_output(port)
        if conn_out:
            return [(port.node.flow.connected_output(port), port)]
        else:
            return []


# main classes


class PortItem(GUIBase, QGraphicsWidget):
    """The GUI representative for ports of nodes, also handling mouse events for connections."""

    def __init__(self, node_gui: NodeGUI, node_item: NodeItem, port: NodePort, flow_view: FlowView):
        GUIBase.__init__(self, representing_component=port)
        QGraphicsWidget.__init__(self)

        self.setGraphicsItem(self)

        self.node_gui: NodeGUI = node_gui
        self.node_item: NodeItem = node_item
        self.port: NodePort = port
        self.flow_view: FlowView = flow_view

        # self.port.has_been_connected.connect(self.port_connected)
        # self.port.has_been_disconnected.connect(self.port_disconnected)

        self.pin = PortItemPin(self.port, self, self.node_gui, self.node_item)

        self.label = PortItemLabel(self.port, self, self.node_gui, self.node_item)

        self._layout = QGraphicsGridLayout()
        self._layout.setSpacing(0)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout)

    # >>> interaction boilerplate >>>
    def boundingRect(self):
        return QRectF(QPointF(0, 0), self.geometry().size())

    def setGeometry(self, rect):
        self.prepareGeometryChange()
        QGraphicsLayoutItem.setGeometry(self, rect)
        self.setPos(rect.topLeft())
    # <<< interaction boilerplate <<<

    def setup_ui(self):
        pass

    def port_connected(self):
        pass

    def port_disconnected(self):
        pass


class InputPortItem(PortItem):
    def __init__(self, node_gui, node_item, port, input_widget: Optional[Tuple[type, str]] = None):
        self.port: NodeInput
        super().__init__(node_gui, node_item, port, node_gui.flow_view())

        self.proxy = None  # widget proxy
        self.widget: Optional[NodeInputWidget] = None  # widget
        if input_widget is not None:
            self.create_widget(input_widget[0], input_widget[1])

        self.update_widget_value = (
            self.widget is not None
        )  # modified by FlowView when performance mode changes

        # catch up to missed connections
        if self.port.node.flow.connected_output(self.port) is not None:
            self.port_connected()

        if (
            self.port.type_ == 'data'
            and self.port.load_data is not None
            and self.port.load_data['has widget']
        ):
            c_d = self.port.load_data['widget data']
            if c_d is not None:
                assert self.widget is not None
                self.widget.set_state(deserialize(c_d))
            else:
                # this is a little feature that lets us prevent loading of input widgets
                # which is occasionally useful, e.g. when changing an input widget class:
                # to prevent loading of the input widget, 'widget data' must be None
                pass

        self.setup_ui()

    def setup_ui(self):
        l = self._layout

        # l.setSpacing(0)
        l.addItem(self.pin, 0, 0)
        l.setAlignment(self.pin, Qt.AlignVCenter | Qt.AlignLeft)
        l.addItem(self.label, 0, 1)
        l.setAlignment(self.label, Qt.AlignVCenter | Qt.AlignLeft)
        if self.widget:
            if self.widget.position == 'below':
                l.addItem(self.proxy, 1, 0, 1, 2)
            elif self.widget.position == 'besides':
                l.addItem(self.proxy, 0, 2)
            else:
                print('Unknown input widget position:', self.widget.position)

            l.setAlignment(self.proxy, Qt.AlignCenter)

    def create_widget(self, widget_class, widget_pos):
        if widget_class is None:
            return

        if self.port.type_ != 'data':
            # TODO: how about input widgets for exec inputs?
            return

        params = (self.port, self, self.node_gui.node, self.node_gui, widget_pos)

        # custom input widget
        self.widget = widget_class(params)
        self.proxy = FlowViewProxyWidget(self.flow_view, parent=self.node_item)
        self.proxy.setWidget(self.widget)

    def port_connected(self):
        """Disables the widget"""
        if self.widget:
            self.widget.setEnabled(False)

        # https://github.com/leon-thomm/Ryven/pull/137#issuecomment-1433783052
        # if self.port.type_ == 'data':
        #     self.port.connections[0].activated.connect(self._port_val_updated)
        #
        # self._port_val_updated(self.port.val)

    def port_disconnected(self):
        """Enables the widget again"""
        if self.widget:
            self.widget.setEnabled(True)

    def complete_data(self, data: dict) -> dict:
        if self.port.type_ == 'data':
            if self.widget:
                data['has widget'] = True
                data['widget name'] = self.node_gui.input_widgets[self.port]['name']
                data['widget pos'] = self.node_gui.input_widgets[self.port]['pos']
                data['widget data'] = serialize(self.widget.get_state())
            else:
                data['has widget'] = False

        return data


class OutputPortItem(PortItem):
    def __init__(self, node_gui, node_item, port):
        super().__init__(node_gui, node_item, port, node_gui.flow_view())
        # super(OutputPortItem, self).__init__(parent_node_instance, PortObjPos.OUTPUT, type_, label_str)

        self.setup_ui()

    def setup_ui(self):
        l = self._layout

        # l.setSpacing(5)
        l.addItem(self.label, 0, 0)
        l.setAlignment(self.label, Qt.AlignVCenter | Qt.AlignRight)
        l.addItem(self.pin, 0, 1)

        l.setAlignment(self.pin, Qt.AlignVCenter | Qt.AlignRight)


# contents


class PortItemPin(QGraphicsWidget):
    def __init__(self, port, port_item, node_gui, node_item):
        super(PortItemPin, self).__init__(node_item)

        self.port = port
        self.port_item = port_item
        self.node_gui = node_gui
        self.node_item = node_item
        self.flow_view = self.node_item.flow_view

        self.setGraphicsItem(self)
        self.setAcceptHoverEvents(True)
        self.hovered = False
        self.setCursor(Qt.CrossCursor)
        self.tool_tip_pos = None

        self.padding = 2
        # self.painting_width = 17
        # self.painting_height = 17
        # self.width = self.painting_width+2*self.padding
        # self.height = self.painting_height+2*self.padding
        self.width = 17
        self.height = 17
        self.port_local_pos = None

    def boundingRect(self):
        return QRectF(QPointF(0, 0), self.geometry().size())

    def setGeometry(self, rect):
        self.prepareGeometryChange()
        QGraphicsLayoutItem.setGeometry(self, rect)
        self.setPos(rect.topLeft())

    def sizeHint(self, which, constraint=...):
        return QSizeF(self.width, self.height)

    def paint(self, painter, option, widget=None):
        self.node_item.session_design.flow_theme.paint_PI(
            node_gui=self.node_gui,
            painter=painter,
            option=option,
            node_color=self.node_gui.color,
            type_=self.port.type_,
            connected=is_connected(self.port),
            rect=QRectF(
                self.padding, self.padding, self.width_no_padding(), self.height_no_padding()
            ),
        )

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  # DRAG NEW CONNECTION
            self.flow_view.mouse_event_taken = True
            self.flow_view._selected_pin = self
            self.flow_view._dragging_connection = True
            event.accept()  # don't pass the ev ent to anything below
        else:
            return QGraphicsWidget.mousePressEvent(self, event)

    def moveEvent(self, event):
        super().moveEvent(event)

        # update connections
        conn_items = self.flow_view.connection_items
        for c in self.port.connections:
            i = conn_items[c]

            # if the items are grouped (which means they move together), don't recompute
            if i.out.group() is None or i.out.group() != i.inp.group():  # not entirely sure if this is working
                i.recompute()

    def hoverEnterEvent(self, event):
        if self.port.type_ == 'data':  # and self.parent_port_instance.io_pos == PortPos.OUTPUT:
            self.setToolTip(shorten(str(val(self.port)), 1000, line_break=True))

        # highlight connections
        items = self.flow_view.connection_items
        for c in connections(self.port):
            items[c].set_highlighted(True)

        self.hovered = True

        QGraphicsWidget.hoverEnterEvent(self, event)

    def hoverLeaveEvent(self, event):
        # un-highlight connections
        items = self.flow_view.connection_items
        for c in connections(self.port):
            items[c].set_highlighted(False)

        self.hovered = False

        QGraphicsWidget.hoverLeaveEvent(self, event)

    def width_no_padding(self):
        """The width without the padding"""
        return self.width - 2 * self.padding

    def height_no_padding(self):
        """The height without the padding"""
        return self.height - 2 * self.padding

    def get_scene_center_pos(self) -> QPointF:
        if not self.node_item.collapsed:
            return QPointF(
                self.scenePos().x() + self.boundingRect().width() / 2,
                self.scenePos().y() + self.boundingRect().height() / 2,
            )
        else:
            # mypy seems buggy here, it things below methods return Any,
            # but they are annotated to return QPointF
            if isinstance(self.port_item, InputPortItem):
                return self.node_item.get_left_body_header_vertex_scene_pos()  # type: ignore
            else:
                return self.node_item.get_right_body_header_vertex_scene_pos()  # type: ignore


class PortItemLabel(QGraphicsWidget):
    def __init__(self, port, port_item, node_gui, node_item):
        super(PortItemLabel, self).__init__(node_item)
        self.setGraphicsItem(self)

        self.port = port
        self.port_item = port_item
        self.node_gui = node_gui
        self.node_item = node_item

        self.font = QFont("Source Code Pro", 10, QFont.Bold)
        font_metrics = QFontMetricsF(
            self.font
        )  # approximately! the designs can use different fonts
        self.width = font_metrics.width(get_longest_line(self.port.label_str))
        self.height = font_metrics.height() * (self.port.label_str.count('\n') + 1)
        self.port_local_pos = None

    def boundingRect(self):
        return QRectF(QPointF(0, 0), self.geometry().size())

    def setGeometry(self, rect):
        self.prepareGeometryChange()
        QGraphicsLayoutItem.setGeometry(self, rect)
        self.setPos(rect.topLeft())

    def sizeHint(self, which, constraint=...):
        return QSizeF(self.width, self.height)

    def paint(self, painter, option, widget=None):
        self.node_item.session_design.flow_theme.paint_PI_label(
            self.node_gui,
            painter,
            option,
            self.port.type_,
            is_connected(self.port),
            self.port.label_str,
            self.node_gui.color,
            self.boundingRect(),
        )
