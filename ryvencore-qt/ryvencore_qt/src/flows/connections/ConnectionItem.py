# import math
from typing import List, Any, Tuple
from qtpy.QtCore import QPointF, Qt
from qtpy.QtGui import QPainter, QColor, QRadialGradient, QPainterPath, QPen
from qtpy.QtWidgets import (
    QGraphicsPathItem,
    QGraphicsItem,
    QStyleOptionGraphicsItem,
    QGraphicsEllipseItem,
)

from ...GUIBase import GUIBase
from ...utils import sqrt
from ...utils import pythagoras
from ...flows.nodes.PortItem import PortItem
from .ConnectionAnimation import ConnPathItemsAnimation, ConnPathItemsAnimationScaled

from ryvencore_qt.src.Design import Design
from ryvencore.NodePort import NodeInput, NodeOutput


class ConnectionItem(GUIBase, QGraphicsPathItem):
    """The GUI representative for a connection. The classes ExecConnectionItem and DataConnectionItem will be ready
    for reimplementation later, so users can add GUI for the enhancements of DataConnection and ExecConnection,
    like input fields for weights."""

    def __init__(self, connection: Tuple[NodeOutput, NodeInput], session_design: Design):
        QGraphicsPathItem.__init__(self)

        self.setAcceptHoverEvents(True)

        self.connection = connection
        out, inp = self.connection

        out_port_index = out.node.outputs.index(out)
        inp_port_index = inp.node.inputs.index(inp)
        assert hasattr(out.node, 'gui') and hasattr(inp.node, 'gui')
        self.out_item: PortItem = out.node.gui.item.outputs[out_port_index]
        self.inp_item: PortItem = inp.node.gui.item.inputs[inp_port_index]

        self.session_design = session_design
        self.session_design.flow_theme_changed.connect(self.recompute)
        self.session_design.performance_mode_changed.connect(self.recompute)

        # for rendering flow pictures
        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
        self.setFlag(QGraphicsItem.ItemIsSelectable)

        diam = 12.5
        self.num_dots = 40
        self.dots = [
            QGraphicsEllipseItem(-diam / 2, -diam / 2, diam, diam, self) 
            for _ in range(self.num_dots)
        ]
        for dot in self.dots:
            dot.setVisible(False)

        # TODO: the connection animation is currently unused because we need a 
        #       signel for when the node output is updated
        self.items_path_animation = ConnPathItemsAnimation(self.dots, self)
        self.connection_animation = ConnPathItemsAnimationScaled(self.items_path_animation)

        self.recompute()

    def __str__(self):
        out, inp = self.connection
        node_in_name = f'{inp.node.gui.item}'
        node_in_index = inp.node.inputs.index(inp)
        node_out_name = f'{out.node.gui.item}'
        node_out_index = out.node.outputs.index(out)
        return f'{node_out_index}->{node_in_index} ({node_out_name}, {node_in_name})'

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget = None):
        # draw path
        painter.setBrush(self.brush())
        painter.setPen(self.pen())
        painter.drawPath(self.path())
        # return super().paint(painter, option, widget)

    def recompute(self) -> None:
        """Updates scene position and recomputes path, pen, gradient and dots"""

        # dots
        self.items_path_animation.recompute()

        # position
        self.setPos(self.out_pos())

        # path
        p1: QPointF = QPointF(self.out_item.pin.width_no_padding() * 0.5, 0)
        p2: QPointF = self.inp_pos() - self.scenePos() - QPointF(self.inp_item.pin.width_no_padding() * 0.5, 0)
        self.setPath(self.connection_path(p1, p2))

        # pen
        pen: QPen = self.get_pen()

        # brush
        self.setBrush(Qt.NoBrush)

        #   gradient
        if self.session_design.performance_mode == 'pretty':
            c = pen.color()
            w = self.path().boundingRect().width()
            h = self.path().boundingRect().height()
            gradient = QRadialGradient(
                self.boundingRect().center(), 
                pythagoras(w, h) / 2
            )

            c_r: int = c.red()
            c_g: int = c.green()
            c_b: int = c.blue()

            # this offset will be 1 if inp.x >> out.x and 0 if inp.x < out.x
            # hence, no fade for the gradient if the connection goes backwards
            offset_mult: float = max(
                0,
                min(
                    (self.inp_pos().x() - self.out_pos().x()) / 200,
                    1
                )
            )

            # and if the input is very far away from the output, decrease the gradient fade so the connection
            # doesn't fully disappear at the ends and stays visible
            if self.inp_pos().x() > self.out_pos().x():
                offset_mult = min(
                    offset_mult,
                    2000 / (self.dist(self.inp_pos(), self.out_pos()))
                )
                # zucker.

            gradient.setColorAt(0.0, QColor(c_r, c_g, c_b, 255))
            gradient.setColorAt(0.75, QColor(c_r, c_g, c_b, 255 - round(55 * offset_mult)))
            gradient.setColorAt(0.95, QColor(c_r, c_g, c_b, 255 - round(255 * offset_mult)))

            pen.setBrush(gradient)

        self.setPen(pen)

    def out_pos(self) -> QPointF:
        """The current global scene position of the pin of the output port"""

        return self.out_item.pin.get_scene_center_pos()

    def inp_pos(self) -> QPointF:
        """The current global scene position of the pin of the input port"""

        return self.inp_item.pin.get_scene_center_pos()

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemSelectedHasChanged or (
            change == QGraphicsItem.ItemVisibleHasChanged and self.isVisible()
        ):
            self.set_highlighted(self.isSelected())
        return QGraphicsItem.itemChange(self, change, value)

    def set_highlighted(self, b: bool):
        pen: QPen = self.pen()

        if b:
            pen.setWidthF(self.pen_width() * 2)
        else:
            pen.setWidthF(self.pen_width())
            self.recompute()

        self.setPen(pen)

    def get_pen(self) -> QPen:
        raise NotImplementedError

    def pen_width(self) -> int:
        raise NotImplementedError

    def get_style_color(self):
        raise NotImplementedError

    def flow_theme(self):
        return self.session_design.flow_theme

    def hoverEnterEvent(self, event):
        self.set_highlighted(True)
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        if not self.isSelected():
            self.set_highlighted(False)
        super().hoverLeaveEvent(event)

    # uncomment to test connection animation:
    # 
    # def mouseReleaseEvent(self, event) -> None:
    #    self.connection_animation.toggle()
        
    @staticmethod
    def dist(p1: QPointF, p2: QPointF) -> float:
        """Returns the diagonal distance between the points using pythagoras"""

        dx = p2.x() - p1.x()
        dy = p2.y() - p1.y()
        return sqrt((dx**2) + (dy**2))

    @staticmethod
    def connection_path(p1: QPointF, p2: QPointF) -> QPainterPath:
        """Returns the painter path for drawing the connection, using the usual cubic connection path by default"""

        return default_cubic_connection_path(p1, p2)


class ExecConnectionItem(ConnectionItem):
    def pen_width(self):
        return self.flow_theme().exec_conn_width

    def get_pen(self):
        theme = self.flow_theme()
        pen = QPen(theme.exec_conn_color, theme.exec_conn_width)
        pen.setStyle(theme.exec_conn_pen_style)
        pen.setCapStyle(Qt.RoundCap)
        return pen

    def get_style_color(self):
        return self.flow_theme().exec_conn_color


class DataConnectionItem(ConnectionItem):
    def pen_width(self):
        return self.flow_theme().data_conn_width

    def get_pen(self):
        theme = self.flow_theme()
        pen = QPen(theme.data_conn_color, theme.data_conn_width)
        pen.setStyle(theme.data_conn_pen_style)
        pen.setCapStyle(Qt.RoundCap)
        return pen

    def get_style_color(self):
        return self.flow_theme().data_conn_color


def default_cubic_connection_path(p1: QPointF, p2: QPointF) -> QPainterPath:
    """Returns the nice looking QPainterPath from p1 to p2"""

    path = QPainterPath()

    path.moveTo(p1)

    dx = p2.x() - p1.x()
    adx = abs(dx)
    dy = p2.y() - p1.y()
    ady = abs(dy)
    distance = sqrt((dx**2) + (dy**2))
    x1, y1 = p1.x(), p1.y()
    x2, y2 = p2.x(), p2.y()

    if ((x1 < x2 - 30) or distance < 100) and (x1 < x2):
        # STANDARD FORWARD
        path.cubicTo(x1 + ((x2 - x1) / 2), y1,
                     x1 + ((x2 - x1) / 2), y2,
                     x2, y2)
    elif x2 < x1 - 100 and adx > ady * 2:
        # STRONG BACKWARDS
        path.cubicTo(x1 + 100 + (x1 - x2) / 10, y1,
                     x1 + 100 + (x1 - x2) / 10, y1 + (dy / 2),
                     x1 + (dx / 2), y1 + (dy / 2))
        path.cubicTo(x2 - 100 - (x1 - x2) / 10, y2 - (dy / 2),
                     x2 - 100 - (x1 - x2) / 10, y2,
                     x2, y2)
    else:
        # STANDARD BACKWARDS
        path.cubicTo(x1 + 100 + (x1 - x2) / 3, y1,
                     x2 - 100 - (x1 - x2) / 3, y2,
                     x2, y2)

    return path
