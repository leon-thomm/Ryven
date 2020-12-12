from PySide2.QtCore import Qt, QPointF, QRectF
from PySide2.QtGui import QColor, QPainter, QBrush, QRadialGradient, QLinearGradient, QPen, QPainterPath, QFont
from PySide2.QtWidgets import QStyle

from custom_src.global_tools.math import pythagoras


class NIPainter:

    def paint_NI_title_label(painter, option, hovering, design_style, title_str, node_color, bounding_rect):
        pass

    def paint_NI_title_label_default(painter, design_style, title_str, c, pen_w, font, bounding_rect):
        pen = QPen(c)
        pen.setWidth(pen_w)

        painter.setPen(pen)
        painter.setFont(font)

        text_rect = bounding_rect
        text_rect.setTop(text_rect.top()-7)

        if design_style == 'extended':
            painter.drawText(text_rect, Qt.AlignLeft | Qt.AlignVCenter, title_str)
        elif design_style == 'minimalistic':
            painter.drawText(text_rect, Qt.AlignTop | Qt.AlignHCenter, title_str)

    def paint_PI_label(painter, option, exec_type, connected, label_str, node_color, bounding_rect):
        pass

    def paint_PI_label_default(painter, label_str, c, font, bounding_rect):
        painter.setBrush(Qt.NoBrush)
        pen = QPen(c)
        painter.setPen(pen)
        painter.setFont(font)
        painter.drawText(bounding_rect, Qt.AlignCenter, label_str)


    def paint_PI(painter, option, node_color, exec_type, connected, padding, w, h):
        pass

    def paint_NI(design_style,
                 painter, option,
                 c: QColor, w: int, h: int, bounding_rect, title_rect):
        pass

    def get_header_rect(w, h, title_rect):
        """
        :param w: width
        :param h: height
        """

        header_height = 1.4 * title_rect.height()  # 35 * (self.parent_node.title.count('\n')+1)

        header_rect = QRectF()
        header_rect.setTopLeft(QPointF(-w / 2, -h / 2))
        header_rect.setWidth(w)
        header_rect.setHeight(header_height)
        return header_rect

    def interpolate_color(c1, c2, val):
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


class NIPainter_DarkStd(NIPainter):

    def paint_NI_title_label(painter, option, hovering, design_style, title_str, node_color, bounding_rect):
        if design_style == 'extended':
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, QColor(30, 43, 48) if not hovering else node_color.lighter(),
                2 if hovering else 1.5,
                QFont('Poppins', 15),
                bounding_rect
            )
        else:
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, QColor(30, 43, 48) if not hovering else node_color.lighter(),
                1.5,
                QFont('K2D', 20, QFont.Bold, True),
                bounding_rect
            )

    def paint_PI_label(painter, option, exec_type, connected, label_str, node_color, bounding_rect):
        c = QColor('#FFFFFF')
        NIPainter.paint_PI_label_default(painter, label_str, c, QFont("Source Code Pro", 10, QFont.Bold), bounding_rect)

    def paint_PI(painter, option, node_color, exec_type, connected, padding, w, h):

        color = QColor('#2E688C') if exec_type == 'data' else QColor('#3880ad')
        if option.state & QStyle.State_MouseOver:
            color = color.lighter()

        brush = QBrush(QColor(color))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(QRectF(padding, padding, w, h))

    def paint_NI(design_style,
                 painter, option,
                 c: QColor, w: int, h: int, bounding_rect, title_rect):

        painter.setRenderHint(QPainter.Antialiasing)

        if design_style == 'extended':
            NIPainter_DarkStd.draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect)
        elif design_style == 'minimalistic':
            NIPainter_DarkStd.draw_NI_minimalistic(painter, c, w, h, bounding_rect)

    def draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect):
        """
        :param painter: painter from paint event
        :param c: NodeInstance's theme color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        :param title_rect: NI's title label's bounding rect
        """

        # main rect
        body_gradient = QRadialGradient(bounding_rect.topLeft(), pythagoras(h, w))
        body_gradient.setColorAt(0, QColor(c.red() / 10 + 100, c.green() / 10 + 100, c.blue() / 10 + 100, 200))
        body_gradient.setColorAt(1, QColor(c.red() / 10 + 100, c.green() / 10 + 100, c.blue() / 10 + 100, 0))

        painter.setBrush(body_gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, 12, 12)

        header_gradient = QLinearGradient(NIPainter_DarkStd.get_header_rect(w, h, title_rect).topRight(),
                                          NIPainter_DarkStd.get_header_rect(w, h, title_rect).bottomLeft())
        header_gradient.setColorAt(0, QColor(c.red(), c.green(), c.blue(), 255))
        header_gradient.setColorAt(1, QColor(c.red(), c.green(), c.blue(), 0))
        painter.setBrush(header_gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(NIPainter_DarkStd.get_header_rect(w, h, title_rect), 12, 12)

    def draw_NI_minimalistic(painter, c, w, h, bounding_rect):
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


class NIPainter_DarkTron(NIPainter):

    def paint_NI_title_label(painter, option, hovering, design_style, title_str, node_color, bounding_rect):
        if design_style == 'extended':
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, node_color if not hovering else node_color.lighter(),
                2,
                QFont('Poppins', 15),
                bounding_rect
            )
        else:
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, node_color,
                2,
                QFont('K2D', 20, QFont.Bold, True),
                bounding_rect
            )

    def paint_PI_label(painter, option, exec_type, connected, label_str, node_color, bounding_rect):
        if exec_type == 'exec':
            c = QColor('#FFFFFF')
        else:
            c = node_color
        NIPainter.paint_PI_label_default(painter, label_str, c, QFont("Source Code Pro", 10, QFont.Bold), bounding_rect)

    def paint_PI(painter, option, node_color, exec_type, connected, padding, w, h):

        color = QColor('#FFFFFF') if exec_type == 'exec' else node_color
        pen = QPen(color)
        pen.setWidth(2)
        painter.setPen(pen)
        if connected or \
                option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
            r = node_color.red()
            g = node_color.green()
            b = node_color.blue()
            brush = QBrush(QColor(r, g, b, 100))
            painter.setBrush(brush)
        else:
            painter.setBrush(Qt.NoBrush)

        painter.drawEllipse(QRectF(padding, padding, w, h))

    def paint_NI(design_style,
                 painter, option,
                 c: QColor, w: int, h: int, bounding_rect, title_rect):

        painter.setRenderHint(QPainter.Antialiasing)

        if design_style == 'extended':
            NIPainter_DarkTron.draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect)
        elif design_style == 'minimalistic':
            if option.state & QStyle.State_MouseOver:  # use special dark background color when mouse hovers
                NIPainter_DarkTron.draw_NI_minimalistic(painter, c, w, h, background_color=c.darker())
            else:
                NIPainter_DarkTron.draw_NI_minimalistic(painter, c, w, h)

    def draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect):
        """
        :param painter: painter from paint event
        :param c: NodeInstance's theme color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        :param title_rect: NI's title label's bounding rect
        """

        background_color = QColor('#212224')
        painter.setBrush(background_color)
        pen = QPen(c)
        pen.setWidth(2)
        painter.setPen(pen)
        body_path = NIPainter_DarkTron.get_extended_body_path(w, h)
        painter.drawPath(body_path)

        header_gradient = QLinearGradient(NIPainter_DarkTron.get_header_rect(w, h, title_rect).topRight(),
                                          NIPainter_DarkTron.get_header_rect(w, h, title_rect).bottomLeft())
        header_gradient.setColorAt(0, QColor(c.red(), c.green(), c.blue(), 255))
        header_gradient.setColorAt(0.5, QColor(c.red(), c.green(), c.blue(), 100))
        header_gradient.setColorAt(1, QColor(c.red(), c.green(), c.blue(), 0))
        painter.setBrush(header_gradient)
        header_path = NIPainter_DarkTron.get_extended_header_path(w, h, title_rect)
        painter.drawPath(header_path)

    def get_extended_body_path(w, h):
        """
        :param c_s: corner size/corner radius
        :param w: width
        :param h: height
        """
        c_s = 10

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

    def get_extended_header_path(w, h, title_rect):
        """
        :param w: width
        :param h: height
        :param title_rect: NI's title label's bounding rect
        """
        c_s = 10

        # header_height = 35 * (NIPainter_DarkTron.ni.parent_node.title.count('\n') + 1)
        header_height = NIPainter_DarkTron.get_header_rect(w, h, title_rect).height()
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

    def draw_NI_minimalistic(painter, c, w, h, background_color=QColor('#36383B')):
        """
        :param painter: painter from paint event
        :param c_s: corner size/corner radius
        :param c: color
        :param w: width
        :param h: height
        :param background_color: (default) background color
        """

        c_s = 10

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


class NIPainter_Ghostly(NIPainter):

    def paint_NI_title_label(painter, option, hovering, design_style, title_str, node_color, bounding_rect):
        if design_style == 'extended':
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, node_color if not hovering else node_color.lighter(),
                2,
                QFont('Poppins', 15),
                bounding_rect
            )
        else:
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, node_color,
                2,
                QFont('K2D', 20, QFont.Bold, True),
                bounding_rect
            )

    def paint_PI_label(painter, option, exec_type, connected, label_str, node_color, bounding_rect):
        if exec_type == 'exec':
            c = QColor('#FFFFFF')
        else:
            c = node_color
        NIPainter.paint_PI_label_default(painter, label_str, c, QFont("Source Code Pro", 10, QFont.Bold), bounding_rect)

    def paint_PI(painter, option, node_color, exec_type, connected, padding, w, h):

        color = QColor('#FFFFFF') if exec_type == 'exec' else node_color

        if exec_type == 'exec':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                brush = QBrush(QColor(255, 255, 255, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)
        elif exec_type == 'data':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                r = node_color.red()
                g = node_color.green()
                b = node_color.blue()
                brush = QBrush(QColor(r, g, b, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)

        pen = QPen(color)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawEllipse(QRectF(padding+w/4, padding+h/4, w/2, h/2))

    def paint_NI(design_style,
                 painter, option,
                 c: QColor, w: int, h: int, bounding_rect, title_rect):

        painter.setRenderHint(QPainter.Antialiasing)

        if design_style == 'extended':
            NIPainter_Ghostly.draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect)
        elif design_style == 'minimalistic':
            if option.state & QStyle.State_MouseOver:  # use special dark background color when mouse hovers
                NIPainter_Ghostly.draw_NI_minimalistic(painter, c, w, h, background_color=c.darker())
            else:
                NIPainter_Ghostly.draw_NI_minimalistic(painter, c, w, h)

    def draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect):
        """
        :param painter: painter from paint event
        :param c: NodeInstance's theme color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        :param title_rect: NI's title label's bounding rect
        """

        background_color = QColor(31, 31, 36, 150)

        body_gradient = QRadialGradient(QPointF(bounding_rect.topLeft().x() + w,
                                                bounding_rect.topLeft().y() - h),
                                        pythagoras(2 * h, 2 * w))
        body_gradient.setColorAt(0, QColor(c.red() / 10 + 100, c.green() / 10 + 100, c.blue() / 10 + 100, 100))
        body_gradient.setColorAt(0.7, background_color)
        body_gradient.setColorAt(1, background_color)

        painter.setBrush(body_gradient)
        painter.setBrush(QColor(28, 28, 28, 170))
        pen = QPen(c.darker())
        pen.setWidth(1)
        painter.setPen(pen)
        body_path = NIPainter_Ghostly.get_extended_body_path(5, w, h)
        painter.drawPath(body_path)

    def get_extended_body_path(c_s, w, h):
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

    def draw_NI_minimalistic(painter, c, w, h, background_color=QColor(30, 30, 30, 170)):
        """
        :param painter: painter from paint event
        :param c_s: corner size/corner radius
        :param c: color
        :param w: width
        :param h: height
        :param background_color: std background color
        """
        c_s = 10
        path = NIPainter_Ghostly.get_extended_body_path(c_s, w, h)  # equals the minimalistic in this case

        painter.setBrush(background_color)
        # pen = QPen(QColor('#333333'))  # QPen(c)
        # pen.setWidth(1)
        # painter.setPen(pen)
        painter.setPen(Qt.NoPen)

        painter.drawPath(path)


class NIPainter_Blender(NIPainter):

    def paint_NI_title_label(painter, option, hovering, design_style, title_str, node_color, bounding_rect):
        if design_style == 'extended':
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, QColor('#FFFFFF'),
                2,
                QFont('Poppins', 15),
                bounding_rect
            )
        else:
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, node_color,
                2,
                QFont('K2D', 20, QFont.Bold, True),
                bounding_rect
            )

    def paint_PI_label(painter, option, exec_type, connected, label_str, node_color, bounding_rect):
        if exec_type == 'exec':
            c = QColor('#FFFFFF')
        else:
            c = node_color
        NIPainter.paint_PI_label_default(painter, label_str, c, QFont("Source Code Pro", 10, QFont.Bold), bounding_rect)

    def paint_PI(painter, option, node_color, exec_type, connected, padding, w, h):

        color = QColor('#FFFFFF') if exec_type == 'exec' else node_color

        if exec_type == 'exec':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                brush = QBrush(QColor(255, 255, 255, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)
        elif exec_type == 'data':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                r = node_color.red()
                g = node_color.green()
                b = node_color.blue()
                brush = QBrush(QColor(r, g, b, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)

        pen = QPen(color)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawEllipse(QRectF(padding + w / 4, padding + h / 4, w / 2, h / 2))

    def paint_NI(design_style,
                 painter, option,
                 c: QColor, w: int, h: int, bounding_rect, title_rect):

        painter.setRenderHint(QPainter.Antialiasing)

        if design_style == 'extended':
            NIPainter_Blender.draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect)
        elif design_style == 'minimalistic':
            NIPainter_Blender.draw_NI_minimalistic(painter, c, w, h, bounding_rect)

    def draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect):
        """
        :param painter: painter from paint event
        :param c: NodeInstance's theme color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        :param title_rect: NI's title label's bounding rect
        """

        background_color = QColor(100, 100, 100, 150)
        header_color = QColor(c.red(), c.green(), c.blue(), 180)

        rel_header_height = NIPainter.get_header_rect(w, h, title_rect).height()/h
        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, header_color)
        gradient.setColorAt(rel_header_height, header_color)
        gradient.setColorAt(rel_header_height+0.0001, background_color)
        gradient.setColorAt(1, background_color)

        painter.setBrush(gradient)
        painter.setPen(QPen(c.darker()))
        painter.drawRoundedRect(bounding_rect, 7, 7)

    def draw_NI_minimalistic(painter, c, w, h, bounding_rect, background_color=QColor(30, 30, 30, 150)):
        """
        :param painter: painter from paint event
        :param c_s: corner size/corner radius
        :param c: color
        :param w: width
        :param h: height
        :param background_color: std background color
        """
        c_s = 15
        painter.setBrush(NIPainter.interpolate_color(c, background_color, 0.97))
        painter.setPen(QPen(c))
        painter.drawRoundedRect(bounding_rect, c_s, c_s)


class NIPainter_Easy(NIPainter):

    def paint_NI_title_label(painter, option, hovering, design_style, title_str, node_color, bounding_rect):
        if design_style == 'extended':
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, QColor('#312b29'),
                2,
                QFont('ASAP', 13, QFont.Bold),
                bounding_rect
            )
        else:
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, node_color,
                2,
                QFont('Poppins', 15, QFont.Thin),
                bounding_rect
            )

    def paint_PI_label(painter, option, exec_type, connected, label_str, node_color, bounding_rect):
        c = None
        if not connected:
            c = QColor('#53585c')
        else:
            if exec_type == 'exec':
                c = QColor('#cccccc')
            else:
                c = node_color
        NIPainter.paint_PI_label_default(painter, label_str, c, QFont("Courier New", 10, QFont.Bold), bounding_rect)

    def paint_PI(painter, option, node_color, exec_type, connected, padding, w, h):
        color = None
        if not connected:
            color = QColor('#53585c')
        else:
            if exec_type == 'exec':
                color = QColor('#dddddd')
            else:
                color = node_color

        if exec_type == 'exec':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                brush = QBrush(QColor(255, 255, 255, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)
        elif exec_type == 'data':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                r = node_color.red()
                g = node_color.green()
                b = node_color.blue()
                brush = QBrush(QColor(r, g, b, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)

        brush = QBrush(QColor(color))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(QRectF(padding+w/8, padding+h/8, 3*w/4, 3*h/4))

    def paint_NI(design_style,
                 painter, option,
                 c: QColor, w: int, h: int, bounding_rect, title_rect):

        painter.setRenderHint(QPainter.Antialiasing)

        if design_style == 'extended':
            NIPainter_Easy.draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect)
        elif design_style == 'minimalistic':
            NIPainter_Easy.draw_NI_minimalistic(painter, c, w, h, bounding_rect)

    def draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect):
        """
        :param painter: painter from paint event
        :param c: NodeInstance's theme color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        :param title_rect: NI's title label's bounding rect
        """

        background_color = QColor('#2b2e33')
        header_color = c

        rel_header_height = NIPainter.get_header_rect(w, h, title_rect).height()/h
        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, header_color)
        gradient.setColorAt(rel_header_height, header_color)
        gradient.setColorAt(rel_header_height+0.0001, background_color)
        gradient.setColorAt(1, background_color)

        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen) #QPen(c.darker()))
        painter.drawRoundedRect(bounding_rect, 9, 9)

    def draw_NI_minimalistic(painter, c, w, h, bounding_rect, background_color=QColor('#2b2e33')):
        """
        :param painter: painter from paint event
        :param c_s: corner size/corner radius
        :param c: color
        :param w: width
        :param h: height
        :param background_color: std background color
        """
        c_s = 10
        painter.setBrush(NIPainter.interpolate_color(c, background_color, 0.97))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, c_s, c_s)


class NIPainter_Peasy(NIPainter):

    def paint_NI_title_label(painter, option, hovering, design_style, title_str, node_color, bounding_rect):
        if design_style == 'extended':
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, QColor('#312b29'),
                2,
                QFont('ASAP', 13, QFont.Bold),
                bounding_rect
            )
        else:
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, node_color,
                2,
                QFont('Poppins', 15, QFont.Thin),
                bounding_rect
            )

    def paint_PI_label(painter, option, exec_type, connected, label_str, node_color, bounding_rect):
        c = None
        if not connected:
            c = QColor('#53585c')
        else:
            if exec_type == 'exec':
                c = QColor('#cccccc')
            else:
                c = node_color
        NIPainter.paint_PI_label_default(painter, label_str, c, QFont("Courier New", 10, QFont.Bold), bounding_rect)

    def paint_PI(painter, option, node_color, exec_type, connected, padding, w, h):
        color = None
        if not connected:
            color = QColor('#53585c')
        else:
            if exec_type == 'exec':
                color = QColor('#dddddd')
            else:
                color = node_color

        if exec_type == 'exec':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                brush = QBrush(QColor(255, 255, 255, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)
        elif exec_type == 'data':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                r = node_color.red()
                g = node_color.green()
                b = node_color.blue()
                brush = QBrush(QColor(r, g, b, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)

        brush = QBrush(QColor(color))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(QRectF(padding+w/8, padding+h/8, 3*w/4, 3*h/4))

    def paint_NI(design_style,
                 painter, option,
                 c: QColor, w: int, h: int, bounding_rect, title_rect):

        painter.setRenderHint(QPainter.Antialiasing)

        if design_style == 'extended':
            NIPainter_Peasy.draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect)
        elif design_style == 'minimalistic':
            NIPainter_Peasy.draw_NI_minimalistic(painter, c, w, h, bounding_rect)

    def draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect):
        """
        :param painter: painter from paint event
        :param c: NodeInstance's theme color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        :param title_rect: NI's title label's bounding rect
        """

        background_color = QColor('#212429')
        header_color = c

        rel_header_height = NIPainter.get_header_rect(w, h, title_rect).height()/h
        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, header_color)
        gradient.setColorAt(rel_header_height, header_color)
        gradient.setColorAt(rel_header_height+0.0001, background_color)
        gradient.setColorAt(1, background_color)

        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen) #QPen(c.darker()))
        painter.drawRoundedRect(bounding_rect, 9, 9)

    def draw_NI_minimalistic(painter, c, w, h, bounding_rect, background_color=QColor('#212429')):
        """
        :param painter: painter from paint event
        :param c_s: corner size/corner radius
        :param c: color
        :param w: width
        :param h: height
        :param background_color: std background color
        """
        c_s = 10
        painter.setBrush(NIPainter.interpolate_color(c, background_color, 0.97))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, c_s, c_s)


class NIPainter_Ueli(NIPainter):

    def paint_NI_title_label(painter, option, hovering, design_style, title_str, node_color, bounding_rect):
        if design_style == 'extended':
            painter.setPen(QPen(QColor(node_color.name())))
            painter.setFont(QFont('Poppins', 13))
            painter.drawText(bounding_rect, Qt.AlignLeft | Qt.AlignVCenter, title_str)
        else:
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, node_color,
                2,
                QFont('Poppins', 15, QFont.Thin),
                bounding_rect
            )

    def paint_PI_label(painter, option, exec_type, connected, label_str, node_color, bounding_rect):
        c = None
        if not connected:
            c = QColor('#53585c')
        else:
            if exec_type == 'exec':
                c = QColor('#cccccc')
            else:
                c = node_color
        NIPainter.paint_PI_label_default(painter, label_str, c, QFont("Courier New", 10, QFont.Bold), bounding_rect)

    def paint_PI(painter, option, node_color, exec_type, connected, padding, w, h):
        color = None
        if not connected:
            color = QColor('#53585c')
        else:
            if exec_type == 'exec':
                color = QColor('#dddddd')
            else:
                color = node_color

        if exec_type == 'exec':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                brush = QBrush(QColor(255, 255, 255, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)
        elif exec_type == 'data':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                r = node_color.red()
                g = node_color.green()
                b = node_color.blue()
                brush = QBrush(QColor(r, g, b, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)

        brush = QBrush(QColor(color))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(QRectF(padding+w/8, padding+h/8, 3*w/4, 3*h/4))

    def paint_NI(design_style,
                 painter, option,
                 c: QColor, w: int, h: int, bounding_rect, title_rect):

        painter.setRenderHint(QPainter.Antialiasing)

        if design_style == 'extended':
            NIPainter_Ueli.draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect)
        elif design_style == 'minimalistic':
            NIPainter_Ueli.draw_NI_minimalistic(painter, c, w, h, bounding_rect)

    def draw_NI_extended_background(painter, c, w, h, bounding_rect: QRectF, title_rect):
        """
        :param painter: painter from paint event
        :param c: NodeInstance's theme color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        :param title_rect: NI's title label's bounding rect
        """

        background_color = QColor('#212429')
        header_color = c

        header_height = NIPainter.get_header_rect(w, h, title_rect).height()
        rel_header_height = header_height/h
        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, header_color)
        gradient.setColorAt(rel_header_height, header_color)
        gradient.setColorAt(rel_header_height+0.0001, background_color)
        gradient.setColorAt(1, background_color)

        painter.setBrush(QBrush(background_color))
        painter.setPen(Qt.NoPen)  # QPen(c.darker()))
        painter.drawRoundedRect(QRectF(
            QPointF(bounding_rect.left(), bounding_rect.top()+header_height),
            bounding_rect.bottomRight()
        ), 6, 6)

    def draw_NI_minimalistic(painter, c, w, h, bounding_rect, background_color=QColor('#212429')):
        """
        :param painter: painter from paint event
        :param c_s: corner size/corner radius
        :param c: color
        :param w: width
        :param h: height
        :param background_color: std background color
        """
        c_s = 10
        painter.setBrush(NIPainter.interpolate_color(c, background_color, 0.97))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, c_s, c_s)
