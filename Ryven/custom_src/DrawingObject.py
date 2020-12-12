from PySide2.QtWidgets import QGraphicsItem
from PySide2.QtGui import QPen, QPainter, QColor
from PySide2.QtCore import Qt, QRectF, QPointF, QLineF

from custom_src.global_tools.MovementEnum import MovementEnum


class DrawingObject(QGraphicsItem):
    def __init__(self, flow, config=None):
        super(DrawingObject, self).__init__()

        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable |
                      QGraphicsItem.ItemSendsScenePositionChanges)
        self.setAcceptHoverEvents(True)

        self.flow = flow
        self.color = None
        self.base_stroke_weight = None
        self.type = 'pen'  # so far the only available, but I already save it so I could add more types in the future
        self.points = []
        self.stroke_weights = []
        self.rect = None
        self.width = -1
        self.height = -1

        # viewport_pos enables global floating points for precise pen positions
        self.viewport_pos: QPointF = config['viewport pos'] if 'viewport pos' in config else None
        # if the drawing gets loaded, its correct global floating pos is already correct (gets set by flow then)

        self.movement_state = None  # ugly - should get replaced later, see NodeInstance, same issue
        self.movement_pos_from = None

        if 'points' in config:
            p_c = config['points']
            for p in p_c:
                if type(p) == list:
                    x = p[0]
                    y = p[1]
                    w = p[2]
                    self.points.append(QPointF(x, y))
                    self.stroke_weights.append(w)
                elif type(p) == dict:  # old signature for older projects
                    x = p['x']
                    y = p['y']
                    w = p['w']
                    self.points.append(QPointF(x, y))
                    self.stroke_weights.append(w)
        self.color = QColor(config['color'])
        self.base_stroke_weight = config['base stroke weight']


    def paint(self, painter, option, widget=None):
        for i in range(1, len(self.points)):
            pen = QPen()
            pen.setColor(self.color)
            pen_width = (self.stroke_weights[i]+0.2)*self.base_stroke_weight
            pen.setWidthF(pen_width)
            if i == 1 or i == len(self.points)-1:
                pen.setCapStyle(Qt.RoundCap)
            painter.setPen(pen)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setRenderHint(QPainter.HighQualityAntialiasing)
            painter.drawLine(self.points[i-1], self.points[i])

    def append_point(self, posF_in_view: QPointF) -> bool:
        """Only used for active drawing.
        Appends a point (floating, in viewport coordinates),
        if the distance to the last one isn't oo small"""

        p: QPointF = (self.viewport_pos + posF_in_view) - self.pos()

        if len(self.points) > 0:
            line = QLineF(self.points[-1], p)
            if line.length() < 0.5:
                return False

        self.points.append(p)
        return True

    def finished(self):
        """correct bounding rect (so far (0,0) is at the start of the line, but it should be in the middle)"""
        rect_center = self.get_points_rect_center()
        for p in self.points:
            p.setX(p.x()-rect_center.x())
            p.setY(p.y()-rect_center.y())
        self.setPos(self.pos()+rect_center)

        self.rect = self.get_points_rect()

    def get_points_rect(self):
        if len(self.points) == 0:
            return QRectF(0, 0, 0, 0)
        x_coords = [p.x() for p in self.points]
        y_coords = [p.y() for p in self.points]
        left = min(x_coords)
        right = max(x_coords)
        up = min(y_coords)
        down = max(y_coords)

        rect = QRectF(left, up, right - left, down - up)

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

    def config_data(self):
        drawing_dict = {'pos x': self.pos().x(),
                        'pos y': self.pos().y(),
                        'color': self.color.name(),
                        'type': self.type,
                        'base stroke weight': self.base_stroke_weight}
        points_list = []
        for i in range(len(self.points)):
            p = self.points[i]
            points_list.append([p.x(), p.y(), self.stroke_weights[i]])
        drawing_dict['points'] = points_list
        return drawing_dict