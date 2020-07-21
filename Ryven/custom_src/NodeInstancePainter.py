from PySide2.QtCore import Qt, QPointF, QRectF
from PySide2.QtGui import QColor, QPainter, QBrush, QRadialGradient, QLinearGradient, QPen, QPainterPath
from PySide2.QtWidgets import QStyle

from custom_src.GlobalAttributes import Design
from custom_src.global_tools.math import pythagoras


class NodeInstancePainter:
    def __init__(self, node_instance):
        self.ni = node_instance


    def paint(self, painter, option,
              c: QColor, w: int, h: int, bounding_rect,
              widget):

        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(QColor(100, 100, 100, 150))  # QBrush(QColor('#3B9CD9'))
        painter.setBrush(brush)

        if self.ni.parent_node.design_style == 'extended':

            if Design.flow_style == 'dark std':
                self.draw_dark_extended_background(painter, c, w, h, bounding_rect)

            elif Design.flow_style == 'dark tron':
                self.draw_tron_extended_background(painter, c, w, h, bounding_rect)

            elif Design.flow_style == 'ghostly':
                self.draw_ghostly_extended_background(painter, c, w, h, bounding_rect)

            elif Design.flow_style == 'blender':
                self.draw_blender_extended_background(painter, c, w, h, bounding_rect)

        elif self.ni.parent_node.design_style == 'minimalistic':

            if Design.flow_style == 'dark std':
                self.draw_dark_minimalistic(painter, c, w, h, bounding_rect)

            elif Design.flow_style == 'dark tron':
                if option.state & QStyle.State_MouseOver:  # use special dark background color when mouse hovers
                    self.draw_tron_minimalistic(painter, 10, c, w, h, background_color=c.darker())
                else:
                    self.draw_tron_minimalistic(painter, 10, c, w, h)

            elif Design.flow_style == 'ghostly':
                if option.state & QStyle.State_MouseOver:  # use special dark background color when mouse hovers
                    self.draw_ghostly_minimalistic(painter, 15, c, w, h, background_color=c.darker())
                else:
                    self.draw_ghostly_minimalistic(painter, 15, c, w, h)

            elif Design.flow_style == 'blender':
                self.draw_blender_minimalistic(painter, 20, c, w, h, bounding_rect)

    def draw_dark_extended_background(self, painter, c, w, h, bounding_rect):
        """
        :param painter: painter from paint event
        :param c: NodeInstance's theme color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        """

        # main rect
        body_gradient = QRadialGradient(bounding_rect.topLeft(), pythagoras(h, w))
        body_gradient.setColorAt(0, QColor(c.red() / 10 + 100, c.green() / 10 + 100, c.blue() / 10 + 100, 200))
        body_gradient.setColorAt(1, QColor(c.red() / 10 + 100, c.green() / 10 + 100, c.blue() / 10 + 100, 0))

        painter.setBrush(body_gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, 12, 12)

        header_gradient = QLinearGradient(self.get_header_rect(w, h).topRight(),
                                          self.get_header_rect(w, h).bottomLeft())
        header_gradient.setColorAt(0, QColor(c.red(), c.green(), c.blue(), 255))
        header_gradient.setColorAt(1, QColor(c.red(), c.green(), c.blue(), 0))
        painter.setBrush(header_gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.get_header_rect(w, h), 12, 12)

    def draw_tron_extended_background(self, painter, c, w, h, bounding_rect):
        """
        :param painter: painter from paint event
        :param c: NodeInstance's theme color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        """

        # main rect
        background_color = QColor('#212224')
        painter.setBrush(background_color)
        pen = QPen(c)
        pen.setWidth(2)
        painter.setPen(pen)
        body_path = self.get_extended_body_path_TRON_DESIGN(10, w, h)
        painter.drawPath(body_path)

        header_gradient = QLinearGradient(self.get_header_rect(w, h).topRight(),
                                          self.get_header_rect(w, h).bottomLeft())
        header_gradient.setColorAt(0, QColor(c.red(), c.green(), c.blue(), 255))
        header_gradient.setColorAt(0.5, QColor(c.red(), c.green(), c.blue(), 100))
        header_gradient.setColorAt(1, QColor(c.red(), c.green(), c.blue(), 0))
        painter.setBrush(header_gradient)
        header_path = self.get_extended_header_path_TRON_DESIGN(10, w, h)
        painter.drawPath(header_path)


    def draw_ghostly_extended_background(self, painter, c, w, h, bounding_rect):
        """
        :param painter: painter from paint event
        :param c: NodeInstance's theme color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        """

        # main rect
        background_color = QColor(31, 31, 36, 150)

        body_gradient = QRadialGradient(QPointF(bounding_rect.topLeft().x()+w,
                                                bounding_rect.topLeft().y()-h),
                                        pythagoras(2*h, 2*w))
        body_gradient.setColorAt(0, QColor(c.red() / 10 + 100, c.green() / 10 + 100, c.blue() / 10 + 100, 100))
        body_gradient.setColorAt(0.7, background_color)
        body_gradient.setColorAt(1, background_color)

        painter.setBrush(body_gradient)
        painter.setBrush(QColor(28, 28, 28, 170))
        pen = QPen(c.darker())
        pen.setWidth(1)
        painter.setPen(pen)
        body_path = self.get_extended_body_path_GHOSTLY_DESIGN(5, w, h)
        painter.drawPath(body_path)


    def draw_blender_extended_background(self, painter, c, w, h, bounding_rect):
        """
        :param painter: painter from paint event
        :param c: NodeInstance's theme color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        """
        background_color = QColor(100, 100, 100, 150)
        header_color = QColor(c.red(), c.green(), c.blue(), 180)

        rel_header_height = self.get_header_rect(w, h).height()/h
        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, header_color)
        gradient.setColorAt(rel_header_height, header_color)
        gradient.setColorAt(rel_header_height+0.0001, background_color)
        gradient.setColorAt(1, background_color)

        painter.setBrush(gradient)
        painter.setPen(QPen(c.darker()))
        painter.drawRoundedRect(bounding_rect, 7, 7)


    def get_extended_body_path_TRON_DESIGN(self, c_s, w, h):
        """
        :param c_s: corner size/corner radius
        :param w: width
        :param h: height
        """

        path = QPainterPath()
        path.moveTo(+w / 2, -h / 2 + c_s)
        path.lineTo(+w / 2 - c_s, -h / 2)
        path.lineTo(-w / 2 + c_s, -h / 2)
        path.lineTo(-w / 2, -h / 2 + c_s)
        path.lineTo(-w / 2, +h / 2 - c_s)
        path.lineTo(-w / 2 + c_s, +h / 2)
        path.lineTo(+w / 2 - c_s, +h / 2)
        path.lineTo(+w / 2, +h / 2 - c_s)
        path.closeSubpath()
        return path

    def get_extended_body_path_GHOSTLY_DESIGN(self, c_s, w, h):
        """
        Very similar to 'extended tron'
        :param c_s: corner size/corner radius
        :param w: width
        :param h: height
        """

        path = QPainterPath()
        path.moveTo(+w / 2, -h / 2 + c_s)
        path.lineTo(+w / 2 - c_s, -h / 2)
        path.lineTo(-w / 2 + c_s, -h / 2)
        path.lineTo(-w / 2, -h / 2 + c_s)
        path.lineTo(-w / 2, +h / 2 - c_s)
        path.lineTo(-w / 2 + c_s, +h / 2)
        path.lineTo(+w / 2 - c_s, +h / 2)
        path.lineTo(+w / 2, +h / 2 - c_s)
        path.closeSubpath()
        return path

    def get_extended_header_path_TRON_DESIGN(self, c_s, w, h):
        """
        :param c_s: corner size/corner radius
        :param w: width
        :param h: height
        """

        # header_height = 35 * (self.ni.parent_node.title.count('\n') + 1)
        header_height = self.get_header_rect(w, h).height()
        header_bottom = -h / 2 + header_height
        path = QPainterPath()
        path.moveTo(+w / 2, -h / 2 + c_s)
        path.lineTo(+w / 2 - c_s, -h / 2)
        path.lineTo(-w / 2 + c_s, -h / 2)
        path.lineTo(-w / 2, -h / 2 + c_s)
        path.lineTo(-w / 2, header_bottom - c_s)
        path.lineTo(-w / 2 + c_s, header_bottom)
        path.lineTo(+w / 2 - c_s, header_bottom)
        path.lineTo(+w / 2, header_bottom - c_s)
        path.closeSubpath()
        return path

    def draw_dark_minimalistic(self, painter, c, w, h, bounding_rect):
        """
        :param painter: painter from paint event
        :param c: color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        """

        path = QPainterPath()
        path.moveTo(-w / 2, 0)

        path.cubicTo(-w / 2, -h / 2,
                     -w / 2, -h / 2,
                     0, -h / 2)
        path.cubicTo(+w / 2, -h / 2,
                     +w / 2, -h / 2,
                     +w / 2, 0)
        path.cubicTo(+w / 2, +h / 2,
                     +w / 2, +h / 2,
                     0, +h / 2)
        path.cubicTo(-w / 2, +h / 2,
                     -w / 2, +h / 2,
                     -w / 2, 0)
        path.closeSubpath()

        body_gradient = QLinearGradient(bounding_rect.bottomLeft(),
                                        bounding_rect.topRight())
        body_gradient.setColorAt(0, QColor(c.red(), c.green(), c.blue(), 150))
        body_gradient.setColorAt(1, QColor(c.red(), c.green(), c.blue(), 80))

        painter.setBrush(body_gradient)
        painter.setPen(QPen(QColor(30, 43, 48)))

        painter.drawPath(path)

    def draw_tron_minimalistic(self, painter, c_s, c, w, h, background_color=QColor('#36383B')):
        """
        :param painter: painter from paint event
        :param c_s: corner size/corner radius
        :param c: color
        :param w: width
        :param h: height
        :param background_color: (default) background color
        """

        path = QPainterPath()
        path.moveTo(-w / 2, 0)

        path.lineTo(-w / 2 + c_s / 2, -h / 2 + c_s / 2)
        path.lineTo(0, -h / 2)
        path.lineTo(+w / 2 - c_s / 2, -h / 2 + c_s / 2)
        path.lineTo(+w / 2, 0)
        path.lineTo(+w / 2 - c_s / 2, +h / 2 - c_s / 2)
        path.lineTo(0, +h / 2)
        path.lineTo(-w / 2 + c_s / 2, +h / 2 - c_s / 2)
        path.closeSubpath()

        painter.setBrush(background_color)
        pen = QPen(c)
        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawPath(path)

    def draw_ghostly_minimalistic(self, painter, c_s, c, w, h, background_color=QColor(30, 30, 30, 170)):
        """
        :param painter: painter from paint event
        :param c_s: corner size/corner radius
        :param c: color
        :param w: width
        :param h: height
        :param background_color: std background color
        """

        path = self.get_extended_body_path_GHOSTLY_DESIGN(c_s, w, h)  # equals the minimalistic in this case

        painter.setBrush(background_color)
        # pen = QPen(QColor('#333333'))  # QPen(c)
        # pen.setWidth(1)
        # painter.setPen(pen)
        painter.setPen(Qt.NoPen)

        painter.drawPath(path)


    def draw_blender_minimalistic(self, painter, c_s, c, w, h, bounding_rect, background_color=QColor(30, 30, 30, 150)):
        """
        :param painter: painter from paint event
        :param c_s: corner size/corner radius
        :param c: color
        :param w: width
        :param h: height
        :param background_color: std background color
        """

        painter.setBrush(self.interpolate_color(c, background_color, 0.97))
        painter.setPen(QPen(c))
        painter.drawRoundedRect(bounding_rect, c_s, c_s)


    def get_header_rect(self, w, h):
        """
        :param w: width
        :param h: height
        """

        header_height = 1.4 * self.ni.title_label.boundingRect().height()  # 35 * (self.parent_node.title.count('\n')+1)

        header_rect = QRectF()
        header_rect.setTopLeft(QPointF(-w / 2, -h / 2))
        header_rect.setWidth(w)
        header_rect.setHeight(header_height)
        return header_rect


    def interpolate_color(self, c1, c2, val):
        r1 = c1.red()
        g1 = c1.green()
        b1 = c2.blue()
        a1 = c1.alpha()

        r2 = c2.red()
        g2 = c2.green()
        b2 = c2.blue()
        a2 = c2.alpha()

        r = (r2 - r1) * val + r1
        g = (g2 - g1) * val + g1
        b = (b2 - b1) * val + b1
        a = (a2 - a1) * val + a1

        return QColor(r, g, b, a)