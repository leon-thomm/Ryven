# import math
from qtpy.QtCore import QMarginsF
from qtpy.QtCore import QRectF, QPointF, Qt
from qtpy.QtGui import QPainter, QColor, QRadialGradient, QPainterPath, QPen
from qtpy.QtWidgets import QGraphicsPathItem, QGraphicsItem, QStyleOptionGraphicsItem

from ...GUIBase import GUIBase
from ...utils import sqrt
from ...utils import pythagoras


class ConnectionItem(GUIBase, QGraphicsPathItem):
    """The GUI representative for a connection. The classes ExecConnectionItem and DataConnectionItem will be ready
    for reimplementation later, so users can add GUI for the enhancements of DataConnection and ExecConnection,
    like input fields for weights."""

    def __init__(self, connection, session_design):
        QGraphicsPathItem.__init__(self)

        self.setAcceptHoverEvents(True)

        self.connection = connection
        out, inp = self.connection

        out_port_index = out.node.outputs.index(out)
        inp_port_index = inp.node.inputs.index(inp)
        self.out_item = out.node.gui.item.outputs[out_port_index]
        self.inp_item = inp.node.gui.item.inputs[inp_port_index]

        self.session_design = session_design
        self.session_design.flow_theme_changed.connect(self.recompute)
        self.session_design.performance_mode_changed.connect(self.recompute)

        # for rendering flow pictures
        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

        self.recompute()

    def recompute(self):
        """Updates scene position and recomputes path, pen and gradient"""

        # position
        self.setPos(self.out_pos())

        # path
        self.setPath(
            self.connection_path(
                QPointF(0, 0),
                self.inp_pos()-self.scenePos()
            )
        )

        # pen
        pen = self.get_pen()

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

            c_r = c.red()
            c_g = c.green()
            c_b = c.blue()

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

    def set_highlighted(self, b: bool):
        pen: QPen = self.pen()

        if b:
            pen.setWidthF(self.pen_width() * 2)
        else:
            pen.setWidthF(self.pen_width())
            self.recompute()

        self.setPen(pen)

    def get_pen(self) -> QPen:
        pass

    def pen_width(self) -> int:
        pass

    def flow_theme(self):
        return self.session_design.flow_theme

    def hoverEnterEvent(self, event):
        self.set_highlighted(True)
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.set_highlighted(False)
        super().hoverLeaveEvent(event)

    @staticmethod
    def dist(p1: QPointF, p2: QPointF) -> float:
        """Returns the diagonal distance between the points using pythagoras"""

        dx = p2.x()-p1.x()
        dy = p2.y()-p1.y()
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


class DataConnectionItem(ConnectionItem):

    def pen_width(self):
        return self.flow_theme().data_conn_width

    def get_pen(self):
        theme = self.flow_theme()
        pen = QPen(theme.data_conn_color, theme.data_conn_width)
        pen.setStyle(theme.data_conn_pen_style)
        pen.setCapStyle(Qt.RoundCap)
        return pen


def default_cubic_connection_path(p1: QPointF, p2: QPointF):
    """Returns the nice looking QPainterPath from p1 to p2"""

    path = QPainterPath()

    path.moveTo(p1)

    dx = p2.x() - p1.x()
    adx = abs(dx)
    dy = p2.y() - p1.y()
    ady = abs(dy)
    distance = sqrt((dx ** 2) + (dy ** 2))
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
