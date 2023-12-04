# import math
from typing import Type, List
from qtpy.QtCore import QPointF, Qt, QTimeLine, QPropertyAnimation, QParallelAnimationGroup, QAbstractAnimation
from qtpy.QtGui import QPainter, QColor, QRadialGradient, QPainterPath, QPen, QBrush
from qtpy.QtWidgets import (
    QGraphicsPathItem,
    QGraphicsItem,
    QStyleOptionGraphicsItem,
    QGraphicsEllipseItem,
    QGraphicsObject,
)

from ...GUIBase import GUIBase, QGraphicsItemAnimated
from ...utils import sqrt
from ...utils import pythagoras

from ...flows.nodes.PortItem import PortItem

from enum import Enum

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
            QGraphicsEllipseItem(-diam / 2, -diam / 2, diam, diam, self) for i in range(40)
        ]
        for dot in self.dots:
            dot.setVisible(False)

        self.items_animation = ConnectionItemsAnimation(self.dots, self)
        self.connection_animation = ConnectionAnimation(self.items_animation)

        self.recompute()

    def __str__(self):
        out, inp = self.connection
        node_in_name = f'{inp.node.gui.item}'
        node_in_index = inp.node.inputs.index(inp)
        node_out_name = f'{out.node.gui.item}'
        node_out_index = out.node.outputs.index(out)
        return f'{node_out_index}->{node_in_index} ({node_out_name}, {node_in_name})'

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget):
        # draw path
        painter.setBrush(self.brush())
        painter.setPen(self.pen())
        painter.drawPath(self.path())
        # return super().paint(painter, option, widget)

    def recompute(self):
        """Updates scene position and recomputes path, pen, gradient and dots"""
        # dots
        self.items_animation.recompute()

        # position
        self.setPos(self.out_pos())

        # path
        p1 = QPointF(self.out_item.pin.width_no_padding() * 0.5, 0)
        p2 = self.inp_pos() - self.scenePos() - QPointF(self.inp_item.pin.width_no_padding() * 0.5, 0)
        self.setPath(self.connection_path(p1, p2))

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
        pass

    def pen_width(self) -> int:
        pass

    def get_style_color(self):
        pass

    def flow_theme(self):
        return self.session_design.flow_theme

    def hoverEnterEvent(self, event):
        self.set_highlighted(True)
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        if not self.isSelected():
            self.set_highlighted(False)
        super().hoverLeaveEvent(event)

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


def default_cubic_connection_path(p1: QPointF, p2: QPointF):
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


class ConnectionItemsAnimation(QGraphicsObject):
    """Animates items over the path"""

    def __init__(
        self,
        items: List[QGraphicsItem],
        connection: ConnectionItem,
        frames=100,
        duration=2500,
        between=125,
        speed=0.15,
    ):
        super().__init__()
        
        self.items:List[QGraphicsItemAnimated] = [QGraphicsItemAnimated(item, self) for item in items]
        self.connection = connection
        self._frames = frames
        self._duration = duration
        self.between = between
        self.speed = speed
        self.visible_items = []
        
        self.setParentItem(self.connection)
            
        self.timeline = QTimeLine(duration)
        self.timeline.setFrameRange(0, frames)
        self.timeline.setCurveShape(QTimeLine.LinearCurve)
        self.timeline.valueChanged.connect(self.update_items)
        self.timeline.setLoopCount(0)
        

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, new_duration):
        self._duration = new_duration
        self.timeline.setDuration(new_duration)

    @property
    def frames(self):
        return self.frames

    @frames.setter
    def frames(self, new_frames):
        self.frames = new_frames
        self.timeline.setFrameRange(0, new_frames)

    def boundingRect(self):
        return self.connection.boundingRect()
    
    def paint(self, painter, option, widget):
        pass
    
    def update_items(self, percent):
        for item, item_percent in self.visible_items:
            p = percent + item_percent
            if p > 1:
                p = p - 1
            item.setPos(self.connection.path().pointAtPercent(p))

    def toggle(self, recompute: bool = False):
        """Toggles the path animation. Returns True if toggled on, otherwise False"""
        state = self.timeline.state()
        running = False
        if state == QTimeLine.NotRunning:
            self.timeline.start()
            running = True
        elif state == QTimeLine.Paused:
            self.timeline.resume()
            running = True
        else:
            running = False
            self.timeline.setPaused(True)
        
        if recompute:
            self.recompute()
        return running
    
    def state(self):
        return self.timeline.state()
        
    def start(self, recompute: bool = True):
        self.timeline.start()
        if recompute:
            self.recompute()

    def setPaused(self, paused: bool, recompute: bool = True):
        self.timeline.setPaused(paused)
        if recompute:
            self.recompute()

    def stop(self, recompute: bool = True):
        self.timeline.stop()
        if recompute:
            self.recompute()

    def recompute(self):
        for item in self.items:
            item.setVisible(False)

        if (
            self.timeline.state() == QTimeLine.State.NotRunning
        ):
            return

        path_len = self.connection.path().length()
        num_points = max(3, min(self.connection.num_dots, int(path_len / self.between)))

        self.timeline.setDuration(path_len / self.speed)
        self.visible_items = []

        for i in range(num_points + 1):
            percent = i / num_points
            item = self.items[i - 1]
            self.visible_items.append((item, percent))
            item.setVisible(True)
            item.item.setPen(QPen(self.connection.get_style_color(), self.connection.pen_width()))
            item.item.setBrush(QBrush(self.connection.get_style_color()))


class ConnectionAnimation:
    """
    Displays an output update by animating items over the path.
    This is toggle-able only
    """
    class State(Enum):
        NOT_RUNNING = 0
        RUNNING = 1
        TO_SCALE = 2
        TO_ZERO = 3
        
    
    def __init__(
        self, items_animation: ConnectionItemsAnimation, duration: int = 750, scale: int = 1
    ) -> None:
        self.con_items_anim = items_animation
        self.duration = duration
        self.scalar = scale
        self.to_scalar_group = QParallelAnimationGroup()
        self.to_zero_group = QParallelAnimationGroup()
        self.state = ConnectionAnimation.State.NOT_RUNNING
        
        for item in self.con_items_anim.items:
            item.setScale(0)
            # to scaler
            to_scalar_anim = QPropertyAnimation(item, b'scale')
            to_scalar_anim.setDuration(self.duration)
            self.to_scalar_group.addAnimation(to_scalar_anim)
            # to zero
            to_zero_anim = QPropertyAnimation(item, b'scale')
            to_zero_anim.setDuration(self.duration)
            self.to_zero_group.addAnimation(to_zero_anim)

        self.to_scalar_group.finished.connect(self.__on_scalar_ended)
        self.to_zero_group.finished.connect(self.__on_zero_ended)
        
    def toggle(self):
        if self.state == ConnectionAnimation.State.NOT_RUNNING:
            self.__run_scalar()
            self.con_items_anim.start()
            self.state = ConnectionAnimation.State.TO_SCALE
        elif self.state == ConnectionAnimation.State.RUNNING:
            self.__run_zero()
            self.state = ConnectionAnimation.State.TO_ZERO
        elif self.state == ConnectionAnimation.State.TO_SCALE:
            self.to_scalar_group.stop()
            self.__run_zero()
            self.state = ConnectionAnimation.State.TO_ZERO
        else:
            self.to_zero_group.stop()
            self.__run_scalar()
            self.state = ConnectionAnimation.State.TO_SCALE
    
    def __stop(self):
        self.to_zero_group.stop()
        self.to_scalar_group.stop()
    
    def __run_scalar(self):
        self.__run_animation(self.to_scalar_group, self.scalar)
    
    def __run_zero(self):
        self.__run_animation(self.to_zero_group, 0)
        
    def __run_animation(self, group: QParallelAnimationGroup, end_value):
        for i in range(group.animationCount()):
            anim: QPropertyAnimation = group.animationAt(i)
            target: QGraphicsItem = anim.targetObject()
            anim.setKeyValues([(0, target.scale()), (1, end_value)])
        group.start()
    
    def __on_scalar_ended(self):
        self.state = ConnectionAnimation.State.RUNNING
    
    def __on_zero_ended(self):
        if self.state == ConnectionAnimation.State.TO_ZERO:
            self.con_items_anim.stop()
        self.state = ConnectionAnimation.State.NOT_RUNNING
    