from PySide2.QtWidgets import QGraphicsItem
from PySide2.QtGui import QPen, QPainter
from PySide2.QtCore import Qt, QRectF, QPointF, QLineF

from custom_src.GlobalAccess import GlobalStorage, MovementEnum


class DrawingObject(QGraphicsItem):
    def __init__(self, flow, config=None):
        super(DrawingObject, self).__init__()

        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable |
                      QGraphicsItem.ItemSendsScenePositionChanges)
        self.setAcceptHoverEvents(True)

        self.flow = flow
        self.points = []
        self.stroke_weights = []
        self.rect = None
        self.width = -1
        self.height = -1

        self.movement_state = None  # ugly - should get replaced later, see NodeInstance, same issue
        self.movement_pos_from = None

        if config:
            for p in config:  # config = 'points' array
                x = p['x']
                y = p['y']
                self.points.append(QPointF(x, y))
                self.stroke_weights.append(p['w'])


    def paint(self, painter, option, widget=None):
        for i in range(1, len(self.points)):
            pen = QPen(Qt.yellow)
            pen_width = (self.stroke_weights[i]+0.2)*3.0
            pen.setWidthF(pen_width)
            painter.setPen(pen)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setRenderHint(QPainter.HighQualityAntialiasing)
            painter.drawLine(self.points[i-1], self.points[i])

    def try_to_append_point(self, p):
        if len(self.points) > 0:
            line = QLineF(self.points[-1], p)
            if line.length() < 1.5:
                return
        self.points.append(p)

    def finished(self):
        # correct bounding rect (so far (0,0) is at the start of the line, but it should be in the middle)
        rect_center = self.get_points_rect_center()
        for p in self.points:
            p.setX(p.x()-rect_center.x())
            p.setY(p.y()-rect_center.y())
        self.setPos(self.pos()+rect_center)

        self.rect = self.get_points_rect()

    def get_points_rect(self):
        x_coords = [p.x() for p in self.points]
        y_coords = [p.y() for p in self.points]
        left = min(x_coords)
        right = max(x_coords)
        up = min(y_coords)
        down = max(y_coords)

        rect = QRectF(left=left,
                      top=up,
                      width=right - left,
                      height=down - up)

        self.width = rect.width()
        self.height = rect.height()

        return rect

    def get_points_rect_center(self):
        return self.get_points_rect().center()

    def boundingRect(self):
        if self.rect:
            return self.rect
        else:
            return self.get_points_rect()

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            self.flow.viewport().update()
            if self.movement_state == MovementEnum.mouse_clicked:
                self.movement_state = MovementEnum.position_changed

        return QGraphicsItem.itemChange(self, change, value)

    def mousePressEvent(self, event):
        """Used for Moving-Commands in Flow - may be replaced later with a nicer determination of a move action."""
        self.movement_state = MovementEnum.mouse_clicked
        self.movement_pos_from = self.pos()
        return QGraphicsItem.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event):
        """Used for Moving-Commands in Flow - may be replaced later with a nicer determination of a move action."""
        if self.movement_state == MovementEnum.position_changed:
            self.flow.selected_components_moved(self.pos()-self.movement_pos_from)
        self.movement_state = None
        return QGraphicsItem.mouseReleaseEvent(self, event)

    def get_json_data(self):
        paint_obj_data = {}
        for i in range(len(self.points)):
            p = self.points[i]
            sw = self.stroke_weights[i]
            point_data = {'x': p.x(),
                          'y': p.y(),
                          'stroke weight': sw}