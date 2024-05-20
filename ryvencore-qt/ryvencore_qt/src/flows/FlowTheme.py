from typing import Optional, Tuple, List

from qtpy.QtCore import Qt, QPointF, QPoint, QRectF, QMargins, QMarginsF
from qtpy.QtGui import QColor, QPainter, QBrush, QRadialGradient, QLinearGradient, QPen, QPainterPath, QFont, QPolygon
from qtpy.QtWidgets import QStyle, QStyleOption

from ..utils import pythagoras


#
#   notice: available themes are hardcoded in Ryven for CLI; make sure to update those
#   in case of changes affecting it
#


class FlowTheme:

    name = ''
    type_ = 'dark'

    node_selection_stylesheet__base = '''
QScrollArea {
    border: 0px solid grey;
    border-radius: 0px;
}
NodeWidget {

}
'''
    node_selection_stylesheet = ''

    header_padding = (10, 2, 10, 2)  # (left, top, right, botton)

    exec_conn_color = QColor('#ffffff')
    exec_conn_width = 1.5
    exec_conn_pen_style = Qt.SolidLine

    data_conn_color = QColor('#ffffff')
    data_conn_width = 1.5
    data_conn_pen_style = Qt.DashLine

    flow_background_brush = QBrush(QColor('#333333'))
    flow_background_grid: Optional[Tuple[str, QColor, int, int, int]] = None
    flow_highlight_pen_color = QColor('#245d75')

    node_item_shadow_color = QColor('#2b2b2b')

    EXPORT: List[str] = []

    def __init__(self):
        pass

    def load(self, data: dict):
        if data and self.name in data.keys():
            imported = {}
            for k, v in data[self.name].items():
                if v != 'default':
                    imported[k] = v
            self._load(imported)

    def _load(self, imported: dict):
        for k, v in imported.items():

            if k == 'exec connection color':
                self.exec_conn_color = self.hex_to_col(v)
            elif k == 'exec connection width':
                self.exec_conn_width = v
            elif k == 'exec connection pen style':
                self.exec_conn_pen_style = self._parse_pen_style(v)

            elif k == 'data connection color':
                self.data_conn_color = self.hex_to_col(v)
            elif k == 'data connection width':
                self.data_conn_width = v
            elif k == 'data connection pen style':
                self.data_conn_pen_style = self._parse_pen_style(v)

            elif k == 'flow background color':
                self.flow_background_brush.setColor(self.hex_to_col(v))

    def build_node_selection_stylesheet(self):
        return self.node_selection_stylesheet__base + '\n' + self.node_selection_stylesheet

    def paint_NI_title_label(self, node_gui, selected: bool, hovering: bool, painter: QPainter, option: QStyleOption,
                             node_style: str, node_title: str, node_color: QColor, node_item_bounding_rect):
        pass

    def paint_PI_label(self, node_gui, painter: QPainter, option: QStyleOption, type_: str, connected: bool, label_str: str,
                       node_color: QColor, bounding_rect: QRectF):
        pass

    def paint_PI(self, node_gui, painter: QPainter, option: QStyleOption, node_color: QColor, type_: str, connected: bool,
                 rect: QRectF):  # padding, w, h):
        pass

    def paint_NI(self, node_gui,
                 selected: bool, hovered: bool, node_style: str,
                 painter: QPainter, option: QStyleOption,
                 color: QColor, w, h, bounding_rect, title_rect):

        painter.setRenderHint(QPainter.Antialiasing)

        if node_style == 'normal':
            self.draw_NI_normal(node_gui, selected, hovered, painter, color, w, h, bounding_rect, title_rect)
        elif node_style == 'small':
            self.draw_NI_small(node_gui, selected, hovered, painter, color, w, h, bounding_rect)

    def draw_NI_normal(self, node_gui, selected: bool, hovered: bool,
                       painter: QPainter, c: QColor, w, h, bounding_rect, title_rect):
        pass

    def draw_NI_small(self, node_gui, selected: bool, hovered: bool,
                      painter: QPainter, c: QColor, w, h, bounding_rect, background_color=None):
        pass

    def paint_NI_selection_border(self, ni, painter: QPainter, color: QColor, w, h, bounding_rect):
        pen = QPen(self.flow_highlight_pen_color)
        pen.setWidth(3)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)

        size_factor = 1.2

        rect = QRectF(bounding_rect)
        rect.setWidth(w*size_factor)
        rect.setHeight(h*size_factor)
        rect.setX(rect.x() - w*size_factor/2)
        rect.setY(rect.y() - h*size_factor/2)

        painter.drawRoundedRect(rect, 10, 10)

    @staticmethod
    def paint_NI_title_label_default(painter: QPainter, node_style: str, title: str, color: QColor, pen_w: float,
                                     font: QFont, node_item_bounding_rect):
        pen = QPen(color)
        pen.setWidth(pen_w)  # type: ignore

        painter.setPen(pen)
        painter.setFont(font)

        text_rect = node_item_bounding_rect
        text_rect.setTop(text_rect.top())

        if node_style == 'normal':
            painter.drawText(text_rect, Qt.AlignLeft | Qt.AlignVCenter, title)
        elif node_style == 'small':
            painter.drawText(text_rect, Qt.AlignTop | Qt.AlignHCenter, title)

    @staticmethod
    def paint_PI_label_default(painter: QPainter, label_str: str, color: QColor, font: QFont, bounding_rect: QRectF):
        painter.setBrush(Qt.NoBrush)
        pen = QPen(color)
        painter.setPen(pen)
        painter.setFont(font)
        painter.drawText(bounding_rect, Qt.AlignCenter, label_str)

    @staticmethod
    def get_header_rect(node_width, node_height, title_rect):
        header_height = 1.0 * title_rect.height()  # 35 * (self.parent_node.title.count('\n')+1)

        header_rect = QRectF()
        header_rect.setTopLeft(QPointF(-node_width / 2, -node_height / 2))
        header_rect.setWidth(node_width)
        header_rect.setHeight(header_height)
        return header_rect

    @staticmethod
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

    @staticmethod
    def hex_to_col(hex_str: str) -> QColor:
        """Converts a hex value in format '#xxxxxx[xx]' to QColor using alpha value if [xx] is used."""

        h = hex_str.lstrip('#')

        if len(h) == 6:
            r, g, b = tuple(
                int(h[i:i + 2], 16) for i in (0, 2, 4)
            )
            return QColor(r, g, b)
        elif len(h) == 8:
            r, g, b, a = tuple(
                int(h[i:i + 2], 16) for i in (0, 2, 4, 6)
            )
            return QColor(r, g, b, a)

        raise ValueError(f'Invalid hex color string: {hex_str}')

    @staticmethod
    def col(c: QColor, alpha=255):
        return QColor(c.red(), c.green(), c.blue(), alpha)

    @staticmethod
    def _parse_pen_style(s: str):
        if s == 'solid line':
            return Qt.SolidLine
        elif s == 'dash line':
            return Qt.DashLine
        elif s == 'dash dot line':
            return Qt.DashDotLine
        elif s == 'dash dot dot line':
            return Qt.DashDotDotLine
        elif s == 'dot line':
            return Qt.DotLine


class FlowTheme_Toy(FlowTheme):
    name = 'Toy'

    node_selection_stylesheet = ''

    header_padding = (12, 5, 10, 2)

    exec_conn_color = QColor(188, 187, 242)
    exec_conn_width = 5
    exec_conn_pen_style = Qt.SolidLine

    data_conn_color = QColor(188, 187, 242)
    data_conn_width = 5
    data_conn_pen_style = Qt.DashLine

    flow_background_brush = QBrush(QColor('#333333'))

    def paint_NI_title_label(self, node_gui, selected, hovering, painter, option, node_style, node_title, node_color,
                             node_item_bounding_rect):

        if node_style == 'normal':
            self.paint_NI_title_label_default(
                painter=painter,
                node_style=node_style,
                title=node_title,
                color=QColor(30, 43, 48) if not hovering else node_color.lighter(),
                pen_w=2 if hovering else 1.5,
                font=QFont('Poppins', 15),
                node_item_bounding_rect=node_item_bounding_rect
            )
        else:
            self.paint_NI_title_label_default(
                painter=painter,
                node_style=node_style,
                title=node_title,
                color=QColor(30, 43, 48) if not hovering else node_color.lighter(),
                pen_w=1.5,
                font=QFont('K2D', 20, QFont.Bold, True),
                node_item_bounding_rect=node_item_bounding_rect
            )

    def paint_PI_label(self, node_gui, painter, option, type_, connected, label_str, node_color, bounding_rect):
        c = QColor('#FFFFFF')
        self.paint_PI_label_default(painter, label_str, c, QFont("Source Code Pro", 10, QFont.Bold), bounding_rect)

    def paint_PI(self, node_gui, painter, option, node_color, type_, connected, rect):

        color = QColor('#2E688C') if type_ == 'data' else QColor('#3880ad')
        if option.state & QStyle.State_MouseOver:
            color = color.lighter()

        brush = QBrush(QColor(color))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(rect)

    def draw_NI_normal(self, node_gui, selected: bool, hovered: bool,
                       painter: QPainter, c: QColor, w, h, bounding_rect, title_rect):

        # main rect
        header_color = QColor(
            int(c.red() / 10 + 100),
            int(c.green() / 10 + 100),
            int(c.blue() / 10 + 100),
        )
        if selected:
            header_color = header_color.lighter()
        body_gradient = QRadialGradient(bounding_rect.topLeft(), pythagoras(h, w))
        body_gradient.setColorAt(0, self.col(header_color, alpha=200))
        body_gradient.setColorAt(1, self.col(header_color, alpha=0))

        painter.setBrush(body_gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, 12, 12)

        header_gradient = QLinearGradient(FlowTheme_Toy.get_header_rect(w, h, title_rect).topRight(),
                                          FlowTheme_Toy.get_header_rect(w, h, title_rect).bottomLeft())
        header_gradient.setColorAt(0, QColor(c.red(), c.green(), c.blue(), 255))
        header_gradient.setColorAt(1, QColor(c.red(), c.green(), c.blue(), 0))
        painter.setBrush(header_gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(FlowTheme_Toy.get_header_rect(w, h, title_rect), 12, 12)

    def draw_NI_small(self, node_gui, selected: bool, hovered: bool,
                      painter: QPainter, c: QColor, w, h, bounding_rect, background_color=None):

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


class FlowTheme_DarkTron(FlowTheme):
    name = 'Tron'

    node_selection_stylesheet = ''

    header_padding = (12, 5, 10, 2)

    exec_conn_color = QColor(0, 120, 180)
    exec_conn_width = 4
    exec_conn_pen_style = Qt.SolidLine

    data_conn_color = QColor(0, 120, 180)
    data_conn_width = 4
    data_conn_pen_style = Qt.DashLine

    flow_background_brush = QBrush(QColor('#333333'))

    def paint_NI_title_label(self, node_gui, selected, hovering, painter, option, node_style, node_title, node_color,
                             node_item_bounding_rect):
        if node_style == 'normal':
            self.paint_NI_title_label_default(
                painter=painter,
                node_style=node_style,
                title=node_title,
                color=node_color if not (hovering or selected) else node_color.lighter().lighter(),
                pen_w=2,
                font=QFont('Poppins', 15),
                node_item_bounding_rect=node_item_bounding_rect
            )
        else:
            self.paint_NI_title_label_default(
                painter=painter,
                node_style=node_style,
                title=node_title,
                color=node_color,
                pen_w=2,
                font=QFont('K2D', 20, QFont.Bold, True),
                node_item_bounding_rect=node_item_bounding_rect
            )

    def paint_PI_label(self, node_gui, painter, option, type_, connected, label_str, node_color, bounding_rect):
        if type_ == 'exec':
            c = QColor('#FFFFFF')
        else:
            c = node_color

        self.paint_PI_label_default(painter, label_str, c, QFont("Source Code Pro", 10, QFont.Bold), bounding_rect)

    def paint_PI(self, node_gui, painter, option, node_color, type_, connected, rect):

        color = QColor('#FFFFFF') if type_ == 'exec' else QColor(node_color)
        pen = QPen(color)
        pen.setWidth(2)
        painter.setPen(pen)
        if connected or \
                option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
            r = color.red()
            g = color.green()
            b = color.blue()
            brush = QBrush(QColor(r, g, b, 100))
            painter.setBrush(brush)
        else:
            painter.setBrush(Qt.NoBrush)

        painter.drawEllipse(rect)

    # def paint_NI(self, node, node_style,
    #              painter, option,
    #              color: QColor, w: int, h: int, bounding_rect, title_rect):
    #
    #     painter.setRenderHint(QPainter.Antialiasing)
    #
    #     if node_style == 'normal':
    #         self.draw_NI_normal(node, painter, color, w, h, bounding_rect, title_rect)
    #     elif node_style == 'small':
    #         if option.state & QStyle.State_MouseOver:  # use special dark background color when mouse hovers
    #             self.draw_NI_small(node, painter, color, w, h, bounding_rect, color.darker())
    #         else:
    #             self.draw_NI_small(node, painter, color, w, h, bounding_rect, QColor('#212429'))

    def draw_NI_normal(self, node_gui, selected: bool, hovered: bool,
                       painter, c: QColor, w: int, h: int, bounding_rect, title_rect):

        background_color = QColor('#212224')
        painter.setBrush(background_color)
        pen = QPen(c if not selected else c.lighter())
        pen.setWidth(2)
        painter.setPen(pen)
        body_path = self.get_extended_body_path(w, h)
        painter.drawPath(body_path)

        header_gradient = QLinearGradient(self.get_header_rect(w, h, title_rect).topRight(),
                                          self.get_header_rect(w, h, title_rect).bottomLeft())
        header_gradient.setColorAt(0, QColor(c.red(), c.green(), c.blue(), 255))
        header_gradient.setColorAt(0.5, QColor(c.red(), c.green(), c.blue(), 100))
        header_gradient.setColorAt(1, QColor(c.red(), c.green(), c.blue(), 0))
        painter.setBrush(header_gradient)
        header_path = self.get_extended_header_path(w, h, title_rect)
        painter.drawPath(header_path)

    @staticmethod
    def get_extended_body_path(w, h):

        c_s = 10  # corner size

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

    def get_extended_header_path(self, w, h, title_rect):

        c_s = 10  # corner size

        # header_height = 35 * (NIPainter_DarkTron.ni.parent_node.title.count('\n') + 1)
        header_height = self.get_header_rect(w, h, title_rect).height()
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

    def draw_NI_small(self, node_gui, selected: bool, hovered: bool,
                      painter: QPainter, c: QColor, w, h, bounding_rect, background_color=None):

        if hovered:
            background_color = c.darker()
        else:
            background_color = QColor('#212429')

        c_s = 10  # corner size

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


class FlowTheme_Ghost(FlowTheme):
    name = 'Ghost'
    type_ = 'dark'

    node_selection_stylesheet = ''

    header_padding = (12, 6, 10, 2)

    exec_conn_color = QColor(0, 17, 25)
    exec_conn_width = 2
    exec_conn_pen_style = Qt.SolidLine

    data_conn_color = QColor(0, 17, 25)
    data_conn_width = 2
    data_conn_pen_style = Qt.DashLine

    flow_background_color = QColor('#333333')
    flow_background_brush = QBrush(flow_background_color)

    node_color = QColor(28, 28, 28, 170)
    node_small_color = QColor('#212429')

    EXPORT = [
        'nodes color',
        'small nodes color',
        'flow background color'
    ]

    def _load(self, imported: dict):
        super()._load(imported)

        for k, v in imported.items():
            if k == 'nodes color':
                self.node_color = self.hex_to_col(v)
            elif k == 'small nodes color':
                self.node_small_color = self.hex_to_col(v)
            elif k == 'flow background color':
                self.flow_background_color = self.hex_to_col(v)
                self.flow_background_brush = QBrush(self.flow_background_color)

    def paint_NI_title_label(self, node_gui, selected, hovering, painter, option, node_style, node_title, node_color,
                             node_item_bounding_rect):

        if node_style == 'normal':
            self.paint_NI_title_label_default(
                painter=painter,
                node_style=node_style,
                title=node_title,
                color=node_color if not hovering else node_color.lighter(),
                pen_w=2,
                font=QFont('Poppins', 15),
                node_item_bounding_rect=node_item_bounding_rect
            )
        else:
            self.paint_NI_title_label_default(
                painter=painter,
                node_style=node_style,
                title=node_title,
                color=node_color,
                pen_w=2,
                font=QFont('K2D', 20, QFont.Bold, True),
                node_item_bounding_rect=node_item_bounding_rect
            )

    def paint_PI_label(self, node_gui, painter, option, type_, connected, label_str, node_color, bounding_rect):
        if type_ == 'exec':
            c = QColor('#FFFFFF')
        else:
            c = node_color

        self.paint_PI_label_default(painter, label_str, c, QFont("Source Code Pro", 10, QFont.Bold), bounding_rect)

    def paint_PI(self, node_gui, painter, option, node_color, type_, connected, rect):

        color = QColor('#FFFFFF') if type_ == 'exec' else QColor(node_color)

        if type_ == 'exec':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                brush = QBrush(QColor(255, 255, 255, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)
        elif type_ == 'data':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                r = color.red()
                g = color.green()
                b = color.blue()
                brush = QBrush(QColor(r, g, b, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)

        pen = QPen(color)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawEllipse(rect.marginsRemoved(QMarginsF(3, 3, 3, 3)))

    # def paint_NI(self, node, node_style,
    #              painter, option,
    #              color: QColor, w: int, h: int, bounding_rect, title_rect):
    #
    #     painter.setRenderHint(QPainter.Antialiasing)
    #
    #     if node_style == 'normal':
    #         self.draw_NI_normal(node, painter, color, w, h, bounding_rect, title_rect)
    #     elif node_style == 'small':
    #         if option.state & QStyle.State_MouseOver:  # use special dark background color when mouse hovers
    #             self.draw_NI_small(node, painter, color, w, h, bounding_rect, background_color=color.darker())
    #         else:
    #             self.draw_NI_small(node, painter, color, w, h, bounding_rect)

    def draw_NI_normal(self, node_gui, selected: bool, hovered: bool,
                       painter, c, w, h, bounding_rect, title_rect):

        background_color = self.node_color

        # body_gradient = QRadialGradient(QPointF(bounding_rect.topLeft().x() + w,
        #                                         bounding_rect.topLeft().y() - h),
        #                                 pythagoras(2 * h, 2 * w))
        # body_gradient.setColorAt(0, QColor(c.red() / 10 + 100, c.green() / 10 + 100, c.blue() / 10 + 100, 100))
        # body_gradient.setColorAt(0.7, background_color)
        # body_gradient.setColorAt(1, background_color)
        #
        # painter.setBrush(body_gradient)

        painter.setBrush(background_color)
        pen = QPen(c.darker())
        pen.setWidth(1 if not selected else 5)
        painter.setPen(pen)
        body_path = self.get_extended_body_path(5, w, h)
        painter.drawPath(body_path)

    @staticmethod
    def get_extended_body_path(c_s, w, h):

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

    def draw_NI_small(self, node_gui, selected: bool, hovered: bool,
                      painter, c, w, h, bounding_rect, background_color=None):

        background_color = self.node_small_color
        c_s = 10  # corner size

        path = self.get_extended_body_path(c_s, w, h)  # equals the small in this case

        painter.setBrush(background_color)
        # pen = QPen(QColor('#333333'))  # QPen(c)
        # pen.setWidth(1)
        # painter.setPen(pen)
        painter.setPen(Qt.NoPen)

        painter.drawPath(path)


class FlowTheme_Blender(FlowTheme):
    name = 'Blender'

    node_selection_stylesheet = ''

    header_padding = (5, 0, 0, 0)

    exec_conn_color = QColor(0, 17, 25)
    exec_conn_width = 3
    exec_conn_pen_style = Qt.SolidLine

    data_conn_color = QColor(200, 200, 200)
    data_conn_width = 2.5
    data_conn_pen_style = Qt.SolidLine

    flow_background_color = QColor('#232323')
    flow_background_brush = QBrush(flow_background_color)

    node_color = QColor('#3f3f3f')
    corner_radius_normal = 5
    corner_radius_small = 10

    EXPORT = [
        'nodes color',
        'flow background color'
    ]

    def _load(self, imported: dict):
        super()._load(imported)

        for k, v in imported.items():
            if k == 'nodes color':
                self.node_color = self.hex_to_col(v)
            elif k == 'flow background color':
                self.flow_background_color = self.hex_to_col(v)
                self.flow_background_brush = QBrush(self.flow_background_color)

    def paint_NI_title_label(self, node_gui, selected, hovering, painter, option, node_style, node_title, node_color,
                             node_item_bounding_rect):
        if node_style == 'normal':
            self.paint_NI_title_label_default(
                painter=painter,
                node_style=node_style,
                title=node_title,
                color=QColor('#FFFFFF'),
                pen_w=2,
                font=QFont('Segoe UI', 11),
                node_item_bounding_rect=node_item_bounding_rect
            )
        else:
            self.paint_NI_title_label_default(
                painter=painter,
                node_style=node_style,
                title=node_title,
                color=node_color,
                pen_w=2,
                font=QFont('Segoe UI', 15, QFont.Bold, True),
                node_item_bounding_rect=node_item_bounding_rect
            )

    def paint_PI_label(self, node_gui, painter, option, type_, connected, label_str, node_color, bounding_rect):
        if type_ == 'exec':
            c = QColor('#FFFFFF')
        else:
            c = node_color

        self.paint_PI_label_default(painter, label_str, c, QFont("Source Code Pro", 10, QFont.Bold), bounding_rect)

    def paint_PI(self, node_gui, painter, option, node_color, type_, connected, rect):

        color = QColor('#FFFFFF') if type_ == 'exec' else node_color

        painter.setBrush(QBrush(color))

        # if type_ == 'exec':
        #     if connected or \
        #             option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
        #         brush = QBrush(QColor(255, 255, 255, 100))
        #         painter.setBrush(brush)
        #     else:
        #         painter.setBrush(Qt.NoBrush)
        # elif type_ == 'data':
        #     if connected or \
        #             option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
        #         r = node_color.red()
        #         g = node_color.green()
        #         b = node_color.blue()
        #         brush = QBrush(QColor(r, g, b, 100))
        #         painter.setBrush(brush)
        #     else:
        #         painter.setBrush(Qt.NoBrush)

        pen = QPen(color)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawEllipse(rect.marginsRemoved(QMarginsF(2, 2, 2, 2)))

    def draw_NI_normal(self, node_gui, selected: bool, hovered: bool,
                       painter, c, w, h, bounding_rect, title_rect):

        background_color = self.node_color
        header_color = QColor(c.red(), c.green(), c.blue(), 180)
        if selected:
            header_color = header_color.lighter()


        rel_header_height = self.get_header_rect(w, h, title_rect).height() / h
        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, header_color)
        gradient.setColorAt(rel_header_height, header_color)
        gradient.setColorAt(rel_header_height + 0.0001, background_color)
        gradient.setColorAt(1, background_color)

        painter.setBrush(gradient)
        painter.setPen(
            Qt.NoPen
            if not selected else
            QPen(QColor(200, 200, 200))
        )
        painter.drawRoundedRect(bounding_rect, self.corner_radius_normal, self.corner_radius_normal)

    def draw_NI_small(self, node_gui, selected: bool, hovered: bool,
                      painter, c, w, h, bounding_rect, background_color=None):

        background_color = QColor('#212429')
        painter.setBrush(self.interpolate_color(c, background_color, 0.97))
        painter.setPen(
            QPen(c)
            if not selected else
            QPen(QColor(200, 200, 200))
        )
        painter.drawRoundedRect(bounding_rect, self.corner_radius_small, self.corner_radius_small)


class FlowTheme_Simple(FlowTheme):
    name = 'Simple'
    type_ = 'dark'

    node_selection_stylesheet = ''

    header_padding = (10, 2, 10, 2)

    exec_conn_color = QColor('#989c9f')
    exec_conn_width = 2
    exec_conn_pen_style = Qt.SolidLine

    data_conn_color = QColor('#989c9f')
    data_conn_width = 2
    data_conn_pen_style = Qt.DashLine

    flow_background_color = QColor('#3f4044')
    flow_background_brush = QBrush(flow_background_color)

    node_background_color = QColor('#212429')
    node_small_background_color = QColor('#212429')

    EXPORT = [
        'nodes background color',
        'small nodes background color',
        'flow background color'
    ]

    def _load(self, imported: dict):
        super()._load(imported)

        for k, v in imported.items():
            if k == 'nodes background color':
                self.node_background_color = self.hex_to_col(v)
            elif k == 'small nodes background color':
                self.node_small_background_color = self.hex_to_col(v)
            elif k == 'flow background color':
                self.flow_background_color = self.hex_to_col(v)
                self.flow_background_brush = QBrush(self.flow_background_color)

    def paint_NI_title_label(self, node_gui, selected, hovering, painter, option, node_style, node_title, node_color,
                             node_item_bounding_rect):
        if node_style == 'normal':
            self.paint_NI_title_label_default(
                painter=painter,
                node_style=node_style,
                title=node_title,
                color=QColor('#312b29'),
                pen_w=2,
                font=QFont('ASAP', 13, QFont.Bold),
                node_item_bounding_rect=node_item_bounding_rect
            )
        else:
            self.paint_NI_title_label_default(
                painter=painter,
                node_style=node_style,
                title=node_title,
                color=node_color,
                pen_w=2,
                font=QFont('Poppins', 15, QFont.Thin),
                node_item_bounding_rect=node_item_bounding_rect
            )

    def paint_PI_label(self, node_gui, painter, option, type_, connected, label_str, node_color, bounding_rect):
        c = None
        if not connected:
            c = QColor('#53585c')
        else:
            if type_ == 'exec':
                c = QColor('#cccccc')
            else:
                c = node_color

        self.paint_PI_label_default(painter, label_str, c, QFont("Courier New", 10, QFont.Bold), bounding_rect)

    def paint_PI(self, node_gui, painter, option, node_color, type_, connected, rect):

        color = None
        if not connected:
            color = QColor('#53585c')
        else:
            if type_ == 'exec':
                color = QColor('#dddddd')
            else:
                color = QColor(node_color)

        if type_ == 'exec':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                brush = QBrush(QColor(255, 255, 255, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)
        elif type_ == 'data':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                r = color.red()
                g = color.green()
                b = color.blue()
                brush = QBrush(QColor(r, g, b, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)

        brush = QBrush(color)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(rect.marginsRemoved(QMarginsF(2, 2, 2, 2)))
        # painter.drawEllipse(QRectF(padding+w/8, padding+h/8, 3*w/4, 3*h/4))

    def draw_NI_normal(self, node_gui, selected: bool, hovered: bool,
                       painter, c, w, h, bounding_rect, title_rect):

        background_color = self.node_background_color

        if selected:
            header_color = c.lighter()
        else:
            header_color = c

        rel_header_height = self.get_header_rect(w, h, title_rect).height() / h
        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, header_color)
        gradient.setColorAt(rel_header_height, header_color)
        gradient.setColorAt(rel_header_height + 0.0001, background_color)
        gradient.setColorAt(1, background_color)

        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)  # QPen(c.darker()))
        painter.drawRoundedRect(bounding_rect, 9, 9)

    def draw_NI_small(self, node_gui, selected: bool, hovered: bool,
                      painter, c, w, h, bounding_rect, background_color=None):

        background_color = self.node_small_background_color
        c_s = 10
        painter.setBrush(self.interpolate_color(c, background_color, 0.97))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, c_s, c_s)


class FlowTheme_Ueli(FlowTheme):
    name = 'Ueli'

    node_selection_stylesheet = ''

    header_padding = (5, 2, 10, 0)

    exec_conn_color = QColor('#989c9f')
    exec_conn_width = 2
    exec_conn_pen_style = Qt.SolidLine

    data_conn_color = QColor('#989c9f')
    data_conn_width = 2
    data_conn_pen_style = Qt.DashLine

    flow_background_color = QColor('#3f4044')
    flow_background_brush = QBrush(flow_background_color)

    nodes_background_color = QColor('#212429')
    small_nodes_background_color = nodes_background_color

    EXPORT = [
        'nodes background color',
        'small nodes background color',
        'flow background color'
    ]

    def _load(self, imported: dict):
        super()._load(imported)

        for k, v in imported.items():
            if k == 'nodes background color':
                c = self.hex_to_col(v)
                self.nodes_background_color = c
            elif k == 'small nodes background color':
                self.small_nodes_background_color = self.hex_to_col(v)
            elif k == 'flow background color':
                self.flow_background_color = self.hex_to_col(v)
                self.flow_background_brush = QBrush(self.flow_background_color)

    def paint_NI_title_label(self, node_gui, selected, hovering, painter, option, node_style, node_title, node_color,
                             node_item_bounding_rect):
        if node_style == 'normal':
            painter.setPen(QPen(QColor(node_color.name())))
            painter.setFont(QFont('Poppins', 13))
            painter.drawText(node_item_bounding_rect, Qt.AlignLeft | Qt.AlignVCenter, node_title)
        else:
            self.paint_NI_title_label_default(
                painter=painter,
                node_style=node_style,
                title=node_title,
                color=node_color,
                pen_w=2,
                font=QFont('Poppins', 15, QFont.Thin),
                node_item_bounding_rect=node_item_bounding_rect
            )

    def paint_PI_label(self, node_gui, painter, option, type_, connected, label_str, node_color, bounding_rect):

        c = None
        if not connected:
            c = '#53585c'
        else:
            if type_ == 'exec':
                c = '#cccccc'
            else:
                c = node_color
        color = QColor(c)

        self.paint_PI_label_default(painter, label_str, color, QFont("Courier New", 10, QFont.Bold), bounding_rect)

    def paint_PI(self, node_gui, painter, option, node_color, type_, connected, rect):

        color_str = None
        if not connected:
            color_str = '#53585c'
        else:
            if type_ == 'exec':
                color_str = '#dddddd'
            else:
                color_str = node_color

        color = QColor(color_str)
        if type_ == 'exec':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                brush = QBrush(QColor(255, 255, 255, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)
        elif type_ == 'data':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                r = color.red()
                g = color.green()
                b = color.blue()
                brush = QBrush(QColor(r, g, b, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)

        brush = QBrush(color)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(rect.marginsRemoved(QMarginsF(2, 2, 2, 2)))
        # painter.drawEllipse(QRectF(padding+w/8, padding+h/8, 3*w/4, 3*h/4))

    def draw_NI_normal(self, node_gui, selected: bool, hovered: bool,
                       painter, c, w, h, bounding_rect: QRectF, title_rect):

        if selected:
            background_color = self.interpolate_color(self.nodes_background_color, c.darker(), 0.18)
        else:
            background_color = self.nodes_background_color

        header_color = c

        header_height = self.get_header_rect(w, h, title_rect).height()
        rel_header_height = header_height / h
        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, header_color)
        gradient.setColorAt(rel_header_height, header_color)
        gradient.setColorAt(rel_header_height + 0.0001, background_color)
        gradient.setColorAt(1, background_color)

        painter.setBrush(QBrush(background_color))
        painter.setPen(Qt.NoPen)  # QPen(c.darker()))
        painter.drawRoundedRect(QRectF(
            QPointF(bounding_rect.left(), bounding_rect.top() + header_height),
            bounding_rect.bottomRight()
        ), 6, 6)

    def draw_NI_small(self, node_gui, selected: bool, hovered: bool,
                      painter, c, w, h, bounding_rect, background_color=None):
        background_color = self.small_nodes_background_color
        c_s = 10  # corner size
        painter.setBrush(self.interpolate_color(c, background_color, 0.97))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, c_s, c_s)


class FlowTheme_PureDark(FlowTheme):
    name = 'pure dark'

    node_selection_stylesheet = ''

    header_padding = (4, 2, 2, 2)

    exec_conn_color = QColor('#ffffff')
    exec_conn_width = 1.5
    exec_conn_pen_style = Qt.SolidLine

    data_conn_color = QColor('#ffffff')
    data_conn_width = 1.5
    data_conn_pen_style = Qt.DashLine

    flow_background_brush = QBrush(QColor('#1E242A'))
    flow_background_grid = ('points', flow_background_brush.color().lighter(), 2, 50, 50)

    node_item_shadow_color = QColor('#101010')

    node_normal_bg_col = QColor('#0C1116')
    node_small_bg_col = QColor('#363c41')
    node_title_color = QColor('#ffffff')
    port_pin_pen_color = QColor('#ffffff')

    EXPORT = [
        'extended node background color',
        'small node background color',
        'node title color',
        'port pin pen color'
    ]

    def _load(self, imported: dict):
        super()._load(imported)

        for k, v in imported.items():
            if k == 'extended node background color':
                self.node_normal_bg_col = self.hex_to_col(v)
            elif k == 'small node background color':
                self.node_small_bg_col = self.hex_to_col(v)
            elif k == 'node title color':
                self.node_title_color = self.hex_to_col(v)
            elif k == 'port pin pen color':
                self.port_pin_pen_color = self.hex_to_col(v)

    def paint_NI_title_label(self, node_gui, selected, hovering, painter, option, node_style, node_title, node_color,
                             node_item_bounding_rect):

        painter.setPen(QPen(self.node_title_color))

        if node_style == 'normal':
            painter.setFont(QFont('Segoe UI', 11))
            align = Qt.AlignLeft | Qt.AlignVCenter
        else:
            painter.setFont(QFont('Segoe UI', 15))
            align = Qt.AlignCenter

        painter.drawText(node_item_bounding_rect, align, node_title)

    def paint_PI_label(self, node_gui, painter, option, type_, connected, label_str, node_color, bounding_rect):
        c = None
        if not connected:
            c = QColor('#53585c')
        else:
            if type_ == 'exec':
                c = QColor('#cccccc')
            else:
                c = node_color

        self.paint_PI_label_default(painter, label_str, c, QFont("Segoe UI", 10), bounding_rect)

    def paint_PI(self, node_gui, painter, option, node_color, type_, connected, rect):

        if connected:
            painter.setBrush(QColor('#508AD8'))
            painter.setPen(Qt.NoPen)
        else:
            painter.setBrush(Qt.NoBrush)
            p = QPen(self.port_pin_pen_color)
            p.setWidthF(1.1)
            painter.setPen(p)

        # rect = QRectF(padding + w / 8, padding + h / 8, 3 * w / 4, 3 * h / 4)
        if type_ == 'exec':
            painter.setBrush(QBrush(QColor('white')))
        # painter.drawEllipse(rect)
        painter.drawEllipse(rect.marginsRemoved(QMarginsF(2, 2, 2, 2)))

    def draw_NI_normal(self, node_gui, selected: bool, hovered: bool,
                       painter, c, w, h, bounding_rect: QRectF, title_rect):

        if selected:
            background_color = self.interpolate_color(self.node_normal_bg_col, c.darker(), 0.18)
        else:
            background_color = self.node_normal_bg_col

        header_height = self.get_header_rect(w, h, title_rect).height()

        painter.setBrush(QBrush(background_color))
        painter.setPen(Qt.NoPen)  # QPen(c.darker()))
        painter.drawRoundedRect(QRectF(
            QPointF(bounding_rect.left(), bounding_rect.top() + header_height),
            bounding_rect.bottomRight()
        ), 3, 3)

        p = QPen(c)
        p.setWidthF(2.3)
        painter.setPen(p)
        painter.drawLine(
            QPointF(bounding_rect.left(), bounding_rect.top() + header_height),
            QPointF(bounding_rect.right(), bounding_rect.top() + header_height)
        )

    def draw_NI_small(self, node_gui, selected: bool, hovered: bool,
                      painter, c, w, h, bounding_rect, background_color=None):

        painter.setBrush(QBrush(self.node_small_bg_col))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, 4, 4)


class FlowTheme_PureLight(FlowTheme_PureDark):
    name = 'pure light'
    type_ = 'light'

    header_padding = (2, 2, 2, 2)

    node_selection_stylesheet = '''
NodeSelectionWidget {
    background-color: white;
}
NodeWidget {
    background-color: white;
}
    '''

    exec_conn_color = QColor('#1f1f1f')

    data_conn_color = QColor('#1f1f1f')

    flow_background_brush = QBrush(QColor('#ffffff'))
    flow_background_grid = ('points', QColor('#dddddd'), 2, 20, 20)

    node_normal_bg_col = QColor('#cdcfd1')
    node_small_bg_col = QColor('#bebfc1')
    node_title_color = QColor('#1f1f1f')
    port_pin_pen_color = QColor('#1f1f1f')

    node_item_shadow_color = QColor('#cccccc')


class FlowTheme_Colorful(FlowTheme):
    name = 'colorful dark'

    header_padding = (12, 0, 2, 2)

    exec_conn_color = QColor('#ffffff')
    exec_conn_width = 1.5
    exec_conn_pen_style = Qt.SolidLine

    data_conn_color = QColor('#ffffff')
    data_conn_width = 1.5
    data_conn_pen_style = Qt.DashLine

    flow_background_brush = QBrush(QColor('#1E242A'))
    flow_background_grid = ('points', flow_background_brush.color().lighter(), 2, 50, 50)

    node_ext_background_color = QColor('#0C1116')
    node_small_background_color = QColor('#363c41')
    node_title_color = QColor('#ffffff')
    port_pin_pen_color = QColor('#ffffff')

    EXPORT = [
        'node title color',
        'port pin pen color'
    ]

    def _load(self, imported: dict):
        super()._load(imported)

        for k, v in imported.items():
            if k == 'node title color':
                self.node_title_color = self.hex_to_col(v)
            elif k == 'port pin pen color':
                self.port_pin_pen_color = self.hex_to_col(v)

    def paint_NI_title_label(self, node_gui, selected, hovering, painter, option, node_style, node_title, node_color,
                             node_item_bounding_rect):

        painter.setPen(QPen(self.node_title_color))

        if node_style == 'normal':
            painter.setFont(QFont('Segoe UI', 11))
            align = Qt.AlignLeft | Qt.AlignVCenter
        else:
            painter.setFont(QFont('Segoe UI', 15))
            align = Qt.AlignCenter

        painter.drawText(node_item_bounding_rect, align, node_title)

    def paint_PI_label(self, node_gui, painter, option, type_, connected, label_str, node_color, bounding_rect):
        c = None
        if not connected:
            c = QColor('#dddddd')
        else:
            if type_ == 'exec':
                c = QColor('#cccccc')
            else:
                c = node_color

        self.paint_PI_label_default(painter, label_str, c, QFont("Segoe UI", 10), bounding_rect)

    def paint_PI(self, node_gui, painter, option, node_color, type_, connected, rect):

        if connected:
            painter.setBrush(QColor('#508AD8'))
            painter.setPen(Qt.NoPen)
        else:
            painter.setBrush(Qt.NoBrush)
            p = QPen(self.port_pin_pen_color)
            p.setWidthF(1.1)
            painter.setPen(p)

        painter.drawEllipse(rect.marginsRemoved(QMarginsF(2, 2, 2, 2)))
        # painter.drawEllipse(QRectF(padding + w / 8, padding + h / 8, 3 * w / 4, 3 * h / 4))

    def draw_NI_normal(self, node_gui, selected: bool, hovered: bool,
                       painter, c, w, h, bounding_rect: QRectF, title_rect):

        background_color = c
        background_color.setAlpha(150)

        if selected:
            header_color = QColor(c.red(), c.green(), c.blue(), 130)
        else:
            header_color = QColor(c.red(), c.green(), c.blue(), 130).darker()

        rel_header_height = self.get_header_rect(w, h, title_rect).height() / h
        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, header_color)
        gradient.setColorAt(rel_header_height, header_color)
        gradient.setColorAt(rel_header_height + 0.0001, background_color)
        gradient.setColorAt(1, background_color)

        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, 7, 7)

    def draw_NI_small(self, node_gui, selected: bool, hovered: bool,
                      painter, c, w, h, bounding_rect, background_color=None):

        painter.setBrush(QBrush(QColor(c.red(), c.green(), c.blue(), 150)))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, 8, 8)


class FlowTheme_ColorfulLight(FlowTheme_Colorful):
    name = 'colorful light'
    type_ = 'light'

    header_padding = (12, 0, 2, 2)

    exec_conn_color = QColor('#1f1f1f')

    data_conn_color = QColor('#1f1f1f')

    flow_background_brush = QBrush(QColor('#ffffff'))
    flow_background_grid = ('points', QColor('#dddddd'), 2, 20, 20)

    node_title_color = QColor('#1f1f1f')
    port_pin_pen_color = QColor('#1f1f1f')

    node_item_shadow_color = QColor('#cccccc')

    def paint_PI_label(self, node_gui, painter, option, type_, connected, label_str, node_color, bounding_rect):
        c = None
        if not connected:
            c = QColor('#1f1f1f')
        else:
            if type_ == 'exec':
                c = QColor('#cccccc')
            else:
                c = node_color

        self.paint_PI_label_default(painter, label_str, c, QFont("Segoe UI", 10), bounding_rect)

    def draw_NI_normal(self, node_gui, selected: bool, hovered: bool, painter, c, w, h, bounding_rect: QRectF, title_rect):

        background_color = c.lighter()
        background_color.setAlpha(150)

        header_color = QColor(c.red(), c.green(), c.blue(), 130).darker()

        rel_header_height = self.get_header_rect(w, h, title_rect).height() / h
        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, header_color)
        gradient.setColorAt(rel_header_height, header_color)
        gradient.setColorAt(rel_header_height + 0.0001, background_color)
        gradient.setColorAt(1, background_color)

        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, 7, 7)

    def draw_NI_small(self, node_gui, selected: bool, hovered: bool,
                      painter, c, w, h, bounding_rect, background_color=None):

        painter.setBrush(QBrush(QColor(c.red(), c.green(), c.blue(), 150)))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, 8, 8)


class FlowTheme_Industrial(FlowTheme):
    name = 'Industrial'

    header_padding = (8, 0, 8, 0)  # (8, 6, 10, 2)

    exec_conn_color = QColor(255, 255, 255)
    exec_conn_width = 2
    exec_conn_pen_style = Qt.SolidLine

    data_conn_color = QColor(255, 194, 45)
    data_conn_width = 2
    data_conn_pen_style = Qt.DashLine

    flow_background_brush = QBrush(QColor(19, 19, 19))
    flow_background_grid = ('points', QColor(80, 80, 80), 2, 30, 30)

    node_color = QColor(10, 10, 10, 250)
    node_item_shadow_color = QColor(0, 0, 0)

    def paint_NI_title_label(self, node_gui, selected, hovering, painter, option, node_style, node_title, node_color,
                             node_item_bounding_rect):
        if node_style == 'normal':
            self.paint_NI_title_label_default(
                painter=painter,
                node_style=node_style,
                title=node_title,
                color=QColor(200, 200, 200),
                pen_w=1,
                font=QFont('Segoe UI', 11, QFont.Normal if not (hovering or selected) else QFont.Bold),
                node_item_bounding_rect=node_item_bounding_rect
            )
        else:
            self.paint_NI_title_label_default(
                painter=painter,
                node_style=node_style,
                title=node_title,
                color=node_color,
                pen_w=2,
                font=QFont('Segoe UI', 15, QFont.Bold),
                node_item_bounding_rect=node_item_bounding_rect
            )

    def paint_PI_label(self, node_gui, painter, option, type_, connected, label_str, node_color, bounding_rect):
        c = QColor('#FFFFFF')
        self.paint_PI_label_default(painter, label_str, c, QFont("Segoe UI", 8, QFont.Normal), bounding_rect)

    def paint_PI(self, node_gui, painter, option, node_color, type_, connected, rect):

        color = QColor('#FFFFFF') if type_ == 'exec' else QColor(node_color)

        # add = 2
        # padd = padding + add
        outer_ellipse_rect = rect.marginsRemoved(QMarginsF(2, 2, 2, 2))  # QRectF(padd, padd, w - 2*padd, h - 2*padd)
        # add = 4
        # padd = padding + add
        inner_ellipse_rect = rect.marginsRemoved(QMarginsF(4, 4, 4, 4))  # QRectF(padd, padd, w - 2*padd, h - 2*padd)

        if type_ == 'exec':

            if connected:
                brush = QBrush(QColor(255, 255, 255, 200))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)

            rect_ = rect.marginsRemoved(QMarginsF(2, 2, 2, 2))

            painter.setPen(QPen(QColor(255, 255, 255)))

            painter.drawPolygon(QPolygon([
                rect_.topLeft().toPoint(),
                QPoint(rect_.right(), rect_.center().toPoint().y()),
                rect_.bottomLeft().toPoint(),
            ]))

        elif type_ == 'data':

            pen = QPen(color)
            pen.setWidth(1)
            painter.setPen(pen)

            if connected:
                # draw inner ellipse
                brush = QBrush(QColor(color.red(), color.green(), color.blue(), 200))
                painter.setBrush(brush)
                painter.drawEllipse(inner_ellipse_rect)

            # draw outer ellipse
            painter.setBrush(Qt.NoBrush)
            painter.drawEllipse(outer_ellipse_rect)

    def draw_NI_normal(self, node_gui, selected: bool, hovered: bool,
                       painter, c, w, h, bounding_rect, title_rect):

        background_color = QColor(14, 14, 14)
        header_color = QColor(105, 105, 105, 150)

        rel_header_height = self.get_header_rect(w, h, title_rect).height() / h
        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, header_color)
        gradient.setColorAt(rel_header_height, header_color)
        gradient.setColorAt(rel_header_height + 0.0001, background_color)
        gradient.setColorAt(1, background_color)

        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)  # QPen(c.darker())
        painter.drawRoundedRect(bounding_rect, 2, 2)

    def draw_NI_small(self, node_gui, selected: bool, hovered: bool,
                      painter, c, w, h, bounding_rect, background_color=None):

        background_color = QColor(217, 217, 217, 50)
        c_s = 2
        painter.setBrush(self.interpolate_color(c, background_color, 0.97))
        pen = QPen(QColor(130, 130, 130))
        painter.setPen(pen)
        painter.drawRoundedRect(bounding_rect, c_s, c_s)


class FlowTheme_Fusion(FlowTheme):
    name = 'Fusion'
    type_ = 'light'

    node_selection_stylesheet = '''
    NodeSelectionWidget {
        background-color: white;
    }
    NodeWidget {
        background-color: white;
    }
        '''

    exec_conn_color = QColor('#1f1f1f')
    exec_conn_width = 2

    data_conn_color = QColor('#1f1f1f')
    data_conn_width = 2

    flow_background_brush = QBrush(QColor('#ffffff'))

    node_normal_bg_col = QColor('#ebeced')
    node_small_bg_col = QColor('#cccdcf')
    node_title_color = QColor('#1f1f1f')
    port_pin_pen_color = QColor('#1f1f1f')

    node_item_shadow_color = QColor('#cccccc')


    def paint_NI_title_label(self, node_gui, selected, hovering, painter, option, node_style, node_title, node_color,
                             node_item_bounding_rect):

        painter.setPen(QPen(self.node_title_color))

        if node_style == 'normal':
            painter.setFont(QFont('Segoe UI', 10))
            align = Qt.AlignLeft | Qt.AlignVCenter
        else:
            painter.setFont(QFont('Segoe UI', 12))
            align = Qt.AlignCenter

        painter.drawText(node_item_bounding_rect, align, node_title)


    def paint_PI_label(self, node_gui, painter, option, type_, connected, label_str, node_color, bounding_rect):
        pen = QPen(QColor('#000000'))
        pen.setWidthF(1.2)
        painter.setPen(pen)

        self.paint_PI_label_default(painter, label_str, QColor(0, 0, 0), QFont("Segoe UI", 8), bounding_rect)


    def paint_PI(self, node_gui, painter, option, node_color, type_, connected, rect):

        painter.setBrush(QColor('#000000'))
        painter.setPen(Qt.NoPen)

        if type_ == 'data':
            painter.drawEllipse(rect.marginsRemoved(QMarginsF(3, 3, 3, 3)))
        else:
            draw_rect = rect.marginsRemoved(QMarginsF(3, 3, 3, 3))
            path = QPainterPath(draw_rect.topLeft())
            path.lineTo(QPointF(draw_rect.right(), draw_rect.center().y()))
            path.lineTo(draw_rect.bottomLeft())
            path.closeSubpath()

            painter.drawPath(path)


    def draw_NI_normal(self, node_gui, selected: bool, hovered: bool,
                       painter, c, w, h, bounding_rect: QRectF, title_rect):

        pen = QPen(c)
        col_top = self.node_normal_bg_col.lighter(105)
        col_bottom = self.node_normal_bg_col

        if not selected:
            pen.setWidthF(1)
        else:
            pen.setWidthF(2.5)
            col_bottom = QColor(255, 255, 255)

        header_height = self.get_header_rect(w, h, title_rect).height()
        header_fraction = header_height / bounding_rect.height()

        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, col_top)
        gradient.setColorAt(header_fraction, self.interpolate_color(col_top, col_bottom, 0.7))
        gradient.setColorAt(1, col_bottom)

        painter.setBrush(QBrush(gradient))
        painter.setPen(pen)
        painter.drawRoundedRect(bounding_rect, 3, 3)


    def draw_NI_small(self, node_gui, selected: bool, hovered: bool,
                      painter, c, w, h, bounding_rect, background_color=None):

        painter.setBrush(QBrush(self.node_small_bg_col))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, 4, 4)


flow_themes: List[FlowTheme] = [
    FlowTheme_Toy(),
    FlowTheme_DarkTron(),
    FlowTheme_Ghost(),
    FlowTheme_Blender(),
    FlowTheme_Simple(),
    FlowTheme_Ueli(),
    FlowTheme_PureDark(),
    FlowTheme_Colorful(),
    FlowTheme_PureLight(),
    FlowTheme_ColorfulLight(),
    FlowTheme_Industrial(),
    FlowTheme_Fusion(),
]
