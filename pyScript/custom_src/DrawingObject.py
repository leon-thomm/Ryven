from PySide2.QtWidgets import QGraphicsItem
from PySide2.QtGui import QPen, QPainter
from PySide2.QtCore import Qt, QRectF, QPointF, QLineF

from custom_src.GlobalAccess import GlobalStorage


class DrawingObject(QGraphicsItem):
    def __init__(self, config=None):
        super(DrawingObject, self).__init__()

        self.points = []
        self.stroke_weights = []
        self.rect = None
        self.width = -1
        self.height = -1

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
        rect = QRectF()
        left = 1
        right = -1
        up = 1
        down = -1
        for p in self.points:
            if p.x() < left:
                left = p.x()
            if p.x() > right:
                right = p.x()
            if p.y() < up:
                up = p.y()
            if p.y() > down:
                down = p.y()
        rect.setLeft(left)
        rect.setRight(right)
        rect.setTop(up)
        rect.setBottom(down)
        self.width = rect.width()
        self.height = rect.height()
        # rect.setLeft(-self.width/2)
        # rect.setRight(self.width/2)
        # rect.setTop(-self.height/2)
        # rect.setBottom(self.height/2)
        return rect

    def get_points_rect_center(self):
        return self.get_points_rect().center()

    def boundingRect(self):
        if self.rect:
            return self.rect
        else:
            return self.get_points_rect()


    def get_json_data(self):
        paint_obj_data = {}
        for i in range(len(self.points)):
            p = self.points[i]
            sw = self.stroke_weights[i]
            point_data = {'x': p.x(),
                          'y': p.y(),
                          'stroke weight': sw}