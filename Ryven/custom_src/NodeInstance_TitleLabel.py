from PySide2.QtCore import QRectF, QPointF, QSizeF, Qt, Property
from PySide2.QtGui import QFont, QFontMetricsF, QColor, QPen
from PySide2.QtWidgets import QGraphicsWidget, QGraphicsLayoutItem, QGraphicsItem

from custom_src.Design import Design
from custom_src.global_tools.strings import get_longest_line


class TitleLabel(QGraphicsWidget):
    def __init__(self, parent_node_instance):
        super(TitleLabel, self).__init__(parent_node_instance)

        self.setGraphicsItem(self)

        self.parent_node_instance = parent_node_instance
        self.title_str = self.parent_node_instance.parent_node.title
        self.font = QFont('Poppins', 15) if self.parent_node_instance.parent_node.design_style == 'extended' else \
            QFont('K2D', 20, QFont.Bold, True)
        self.fm = QFontMetricsF(self.font)

        self.width = self.fm.width(get_longest_line(self.title_str)+'___')
        self.height = self.fm.height() * 0.7 * (self.title_str.count('\n') + 1)

        self.color = QColor(30, 43, 48)
        self.pen_width = 1.5
        self.hovering = False  # whether the mouse is hovering over the parent NI (!)

        Design.flow_theme_changed.connect(self.theme_changed)
        self.update_design()

    def boundingRect(self):
        return QRectF(QPointF(0, 0), self.geometry().size())

    def setGeometry(self, rect):
        self.prepareGeometryChange()
        QGraphicsLayoutItem.setGeometry(self, rect)
        self.setPos(rect.topLeft())

    def sizeHint(self, which, constraint=...):
        return QSizeF(self.width, self.height)

    def paint(self, painter, option, widget=None):
        pen = QPen(self.color)
        pen.setWidth(self.pen_width)

        painter.setPen(pen)
        painter.setFont(self.font)

        text_rect = self.boundingRect()
        text_rect.setTop(text_rect.top()-7)

        if self.design_style() == 'extended':
            painter.drawText(text_rect, Qt.AlignTop, self.title_str)
        elif self.design_style() == 'minimalistic':
            painter.drawText(text_rect, Qt.AlignTop | Qt.AlignHCenter, self.title_str)

    def design_style(self):
        return self.parent_node_instance.parent_node.design_style

    def set_NI_hover_state(self, hovering: bool):
        self.hovering = hovering
        self.update_design()
    
    def theme_changed(self, new_theme):
        self.update_design()

    def update_design(self):
        theme = Design.flow_theme

        if self.design_style() == 'extended':
            if theme == 'dark std':
                if self.hovering:
                    self.color = self.parent_node_instance.color.lighter()
                    self.pen_width = 2
                else:
                    self.color = QColor(30, 43, 48)
                    self.pen_width = 1.5
            elif theme == 'dark tron' or theme == 'ghostly':
                if self.hovering:
                    self.color = self.parent_node_instance.color.lighter()
                else:
                    self.color = self.parent_node_instance.color
                self.pen_width = 2
            elif theme == 'blender':
                self.color = QColor('#ffffff')
        elif self.design_style() == 'minimalistic':
            if theme == 'dark std':
                if self.hovering:
                    self.color = self.parent_node_instance.color.lighter()
                    self.pen_width = 1.5
                else:
                    self.color = QColor(30, 43, 48)
                    self.pen_width = 1.5
            elif theme == 'dark tron' or theme == 'ghostly' or theme == 'blender':
                self.color = self.parent_node_instance.color
                self.pen_width = 2

        self.update()


    # ANIMATION STUFF
    def get_color(self):
        return self.color

    def set_color(self, val):
        self.color = val
        QGraphicsItem.update(self)

    p_color = Property(QColor, get_color, set_color)